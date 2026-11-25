import base64
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


class HotspotDatabase:
    """Reads and writes HOTSPOT users and social posts to a local JSON file."""

    def __init__(self, file_path="hotspot_data.json"):
        self.file_path = Path(file_path)
        if not self.file_path.is_absolute():
            self.file_path = Path(__file__).resolve().parent / self.file_path
        self.data = {"users": {}, "posts": [], "businesses": {}}
        self.load_data()

    def load_data(self):
        """Load saved information from JSON. Create the file if it does not exist."""
        if self.file_path.exists():
            try:
                with self.file_path.open("r", encoding="utf-8") as file:
                    loaded = json.load(file)
                self.data = {
                    "users": loaded.get("users", {}),
                    "posts": loaded.get("posts", []),
                    "businesses": loaded.get("businesses", {}),
                }
            except (json.JSONDecodeError, OSError):
                # Keep the original file untouched if it cannot be read.
                self.data = {"users": {}, "posts": [], "businesses": {}}
        else:
            self.save_data()
        self.data.setdefault("businesses", {})
        self.ensure_social_fields()
        return self.get_users(), self.get_posts()

    def ensure_social_fields(self):
        """Upgrade in-memory user records created before follow requests existed."""
        changed = False
        users = self.data["users"]
        list_fields = (
            "friends",
            "followers",
            "following",
            "incoming_friend_requests",
            "outgoing_friend_requests",
            "incoming_follow_requests",
            "outgoing_follow_requests",
            "activity",
            "following_businesses",
        )
        for user in users.values():
            if "privacy" not in user:
                user["privacy"] = "Public"
                changed = True
            for field in list_fields:
                if field not in user or not isinstance(user[field], list):
                    user[field] = []
                    changed = True

            for old_field, new_field in (
                ("outgoing_friend_requests", "outgoing_follow_requests"),
                ("incoming_friend_requests", "incoming_follow_requests"),
            ):
                for request in user[old_field]:
                    if request not in user[new_field]:
                        user[new_field].append(request)
                        changed = True
                if user[old_field]:
                    user[old_field].clear()
                    changed = True

        for username, user in users.items():
            for friend in user["friends"]:
                friend_user = users.get(friend)
                if friend_user is None:
                    continue
                if friend not in user["following"]:
                    user["following"].append(friend)
                    changed = True
                if username not in user["followers"]:
                    user["followers"].append(username)
                    changed = True
                if username not in friend_user["following"]:
                    friend_user["following"].append(username)
                    changed = True
                if friend not in friend_user["followers"]:
                    friend_user["followers"].append(friend)
                    changed = True

        for user in users.values():
            if "notifications" not in user or not isinstance(user["notifications"], list):
                user["notifications"] = []
                changed = True
            if user.get("visual_theme") not in ("Light", "Dark", "Colorful"):
                user["visual_theme"] = "Light"
                changed = True
        businesses = self.data.setdefault("businesses", {})
        for username, user in users.items():
            for business_username in user["following_businesses"]:
                business = businesses.get(business_username)
                if business is not None and username not in business.setdefault("followers", []):
                    business["followers"].append(username)
                    changed = True
        for business in businesses.values():
            if "followers" not in business or not isinstance(business["followers"], list):
                business["followers"] = []
                changed = True
            if "notifications" not in business or not isinstance(business["notifications"], list):
                business["notifications"] = []
                changed = True
            if business.get("visual_theme") not in ("Light", "Dark", "Colorful"):
                business["visual_theme"] = "Light"
                changed = True
            if "activity" not in business or not isinstance(business["activity"], list):
                business["activity"] = []
                changed = True
        for post in self.data["posts"]:
            if not post.get("id"):
                post["id"] = uuid4().hex
                changed = True
            if not isinstance(post.get("likes"), list):
                post["likes"] = []
                changed = True

        if changed:
            self.save_data()

    def save_data(self):
        """Write the current database to disk immediately."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_file = self.file_path.with_suffix(self.file_path.suffix + ".tmp")
        with temporary_file.open("w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
        temporary_file.replace(self.file_path)

    def get_users(self):
        return self.data["users"]

    def get_posts(self):
        posts = []
        for saved_post in self.data["posts"]:
            post = dict(saved_post)
            encoded_media = post.get("media", "")
            if encoded_media:
                post["media"] = base64.b64decode(encoded_media)
            posts.append(post)
        return posts

    def username_exists(self, username):
        normalized_username = username.strip().casefold()
        return any(
            existing_username.casefold() == normalized_username
            for account_type in ("users", "businesses")
            for existing_username in self.data.setdefault(account_type, {})
        )

    def create_user(self, username, password, favorites, privacy="Public"):
        username = username.strip()
        password = password.strip()
        if not username or not password:
            return False, "Username and password cannot be empty."
        if len(password) < 5:
            return False, "Password must be at least 5 characters."
        if self.username_exists(username):
            return False, "That username already exists."
        if privacy not in ("Public", "Private"):
            privacy = "Public"
        self.data["users"][username] = {
            "password": password,
            "top_restaurants": list(favorites),
            "ratings": {},
            "privacy": privacy,
            "friends": [],
            "followers": [],
            "following": [],
            "incoming_friend_requests": [],
            "outgoing_friend_requests": [],
            "incoming_follow_requests": [],
            "outgoing_follow_requests": [],
            "activity": [],
            "notifications": [],
            "following_businesses": [],
            "visual_theme": "Light",
        }
        self.save_data()
        return True, "Account created successfully."

    def create_business(
        self,
        username,
        password,
        restaurant_name,
        cuisine,
        city,
        address="",
        description="",
        phone="",
        email="",
        website="",
    ):
        username = username.strip()
        password = password.strip()
        restaurant_name = restaurant_name.strip()
        cuisine = cuisine.strip()
        city = city.strip()
        if not username or not password:
            return False, "Username and password cannot be empty."
        if len(password) < 5:
            return False, "Password must be at least 5 characters."
        if not restaurant_name or not cuisine or not city:
            return False, "Restaurant name, cuisine, and city are required."
        businesses = self.data.setdefault("businesses", {})
        if self.username_exists(username):
            return False, "That username is already in use."
        businesses[username] = {
            "password": password,
            "restaurant_name": restaurant_name,
            "cuisine": cuisine,
            "city": city,
            "address": address.strip(),
            "description": description.strip(),
            "phone": phone.strip(),
            "email": email.strip(),
            "website": website.strip(),
            "followers": [],
            "notifications": [],
            "visual_theme": "Light",
            "activity": [],
        }
        self.save_data()
        return True, "Business account created successfully."

    def authenticate_business(self, username, password):
        business = self.data.setdefault("businesses", {}).get(username.strip())
        return business is not None and business.get("password") == password

    def set_visual_theme(self, account_type, username, theme):
        if theme not in ("Light", "Dark", "Colorful"):
            return False
        accounts = (
            self.data["users"]
            if account_type == "user"
            else self.data.setdefault("businesses", {})
        )
        account = accounts.get(username)
        if account is None:
            return False
        account["visual_theme"] = theme
        self.save_data()
        return True

    def find_business(self, restaurant_name, city=None):
        for username, business in self.data.setdefault("businesses", {}).items():
            if business["restaurant_name"].casefold() != restaurant_name.casefold():
                continue
            if city and business["city"].casefold() != city.casefold():
                continue
            return username, business
        return None

    def toggle_business_follow(self, username, business_username):
        users = self.data["users"]
        businesses = self.data.setdefault("businesses", {})
        if username not in users or business_username not in businesses:
            return False, "Account not found."
        user = users[username]
        business = businesses[business_username]
        if business_username in user["following_businesses"]:
            user["following_businesses"].remove(business_username)
            if username in business["followers"]:
                business["followers"].remove(username)
            message = f"You unfollowed {business['restaurant_name']}."
        else:
            user["following_businesses"].append(business_username)
            if username not in business["followers"]:
                business["followers"].append(username)
            business.setdefault("notifications", []).append(
                {
                    "id": uuid4().hex,
                    "type": "follow",
                    "actor": username,
                    "description": f"@{username} followed your restaurant.",
                    "created_at": datetime.now(timezone.utc).isoformat(),
                    "read": False,
                }
            )
            message = f"You are now following {business['restaurant_name']}."
        self.save_data()
        return True, message

    def update_business_profile(self, username, restaurant_name, cuisine, city,
                                 address="", description="", phone="", email="",
                                 website=""):
        business = self.data.setdefault("businesses", {}).get(username)
        if business is None:
            return False, "Business account not found."
        restaurant_name = restaurant_name.strip()
        cuisine = cuisine.strip()
        city = city.strip()
        if not restaurant_name or not cuisine or not city:
            return False, "Restaurant name, cuisine, and city are required."
        business.update(
            {
                "restaurant_name": restaurant_name,
                "cuisine": cuisine,
                "city": city,
                "address": address.strip(),
                "description": description.strip(),
                "phone": phone.strip(),
                "email": email.strip(),
                "website": website.strip(),
            }
        )
        self.save_data()
        return True, "Restaurant profile updated."

    def authenticate_user(self, username, password):
        user = self.data["users"].get(username)
        return user is not None and user.get("password") == password

    def save_rating(self, username, restaurant_name, rating):
        if username not in self.data["users"]:
            return False
        rating = float(rating)
        self.data["users"][username]["ratings"][restaurant_name] = rating
        self.record_activity(
            username,
            "rating",
            f"Rated {restaurant_name} {rating:g}/5",
            entity=restaurant_name,
        )
        self.save_data()
        return True

    def record_activity(self, username, activity_type, description, entity=None):
        user = self.data["users"].get(username)
        if user is None:
            return False
        activity = {
            "type": activity_type,
            "description": description,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        if entity is not None:
            activity["entity"] = entity
        user.setdefault("activity", []).append(activity)
        return True

    def add_notification(self, recipient, actor, notification_type, description, post_id=None):
        user = self.data["users"].get(recipient)
        if user is None:
            return False
        notification = {
            "id": uuid4().hex,
            "type": notification_type,
            "actor": actor,
            "description": description,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "read": False,
        }
        if post_id is not None:
            notification["post_id"] = post_id
        user.setdefault("notifications", []).append(notification)
        return True

    def mark_notifications_read(self, username):
        user = self.data["users"].get(username)
        if user is None:
            return False
        for notification in user.setdefault("notifications", []):
            notification["read"] = True
        self.save_data()
        return True

    def set_privacy(self, username, privacy):
        if username not in self.data["users"] or privacy not in ("Public", "Private"):
            return False
        self.data["users"][username]["privacy"] = privacy
        self.save_data()
        return True

    def search_users(self, query, username):
        query = query.strip().lower().lstrip("@")
        if not query:
            return []
        matches = [
            name for name in sorted(self.data["users"])
            if name != username and query in name.lower()
        ]
        return sorted(
            matches,
            key=lambda name: (
                not name.lower().startswith(query),
                name.lower(),
            ),
        )

    def _sync_friendship(self, username, target_username):
        users = self.data["users"]
        sender = users[username]
        target = users[target_username]
        if (
            target_username in sender["following"]
            and username in target["following"]
        ):
            if target_username not in sender["friends"]:
                sender["friends"].append(target_username)
            if username not in target["friends"]:
                target["friends"].append(username)
        else:
            if target_username in sender["friends"]:
                sender["friends"].remove(target_username)
            if username in target["friends"]:
                target["friends"].remove(username)

    def _add_follow(self, username, target_username):
        users = self.data["users"]
        sender = users[username]
        target = users[target_username]
        if target_username not in sender["following"]:
            sender["following"].append(target_username)
        if username not in target["followers"]:
            target["followers"].append(username)
        self._sync_friendship(username, target_username)

    def follow_user(self, username, target_username):
        self.ensure_social_fields()
        users = self.data["users"]
        if username not in users or target_username not in users:
            return False, "User not found."
        if username == target_username:
            return False, "You cannot follow yourself."
        sender = users[username]
        target = users[target_username]
        if target_username in sender["following"]:
            return False, f"You already follow {target_username}."
        if target_username in sender["outgoing_follow_requests"]:
            return False, f"Your follow request to {target_username} is pending."
        if target.get("privacy", "Public") == "Private":
            sender["outgoing_follow_requests"].append(target_username)
            target["incoming_follow_requests"].append(username)
            self.add_notification(
                target_username,
                username,
                "follow_request",
                f"@{username} requested to follow you.",
            )
            self.save_data()
            return True, f"Follow request sent to {target_username}."
        self._add_follow(username, target_username)
        self.add_notification(
            target_username,
            username,
            "follow",
            f"@{username} started following you.",
        )
        self.save_data()
        if username in target["following"]:
            return True, f"You and {target_username} are now friends."
        return True, f"You are now following {target_username}."

    def accept_follow_request(self, username, requester):
        users = self.data["users"]
        if username not in users or requester not in users:
            return False
        target = users[username]
        sender = users[requester]
        if requester not in target["incoming_follow_requests"]:
            return False
        target["incoming_follow_requests"].remove(requester)
        if username in sender["outgoing_follow_requests"]:
            sender["outgoing_follow_requests"].remove(username)
        self._add_follow(requester, username)
        self.add_notification(
            requester,
            username,
            "follow_accepted",
            f"@{username} accepted your follow request.",
        )
        self.save_data()
        return True

    def decline_follow_request(self, username, requester):
        users = self.data["users"]
        if username not in users or requester not in users:
            return False
        target = users[username]
        sender = users[requester]
        if requester in target["incoming_follow_requests"]:
            target["incoming_follow_requests"].remove(requester)
        if username in sender["outgoing_follow_requests"]:
            sender["outgoing_follow_requests"].remove(username)
        self.save_data()
        return True

    def cancel_follow_request(self, username, target_username):
        users = self.data["users"]
        if username not in users or target_username not in users:
            return False
        sender = users[username]
        target = users[target_username]
        if target_username in sender["outgoing_follow_requests"]:
            sender["outgoing_follow_requests"].remove(target_username)
        if username in target["incoming_follow_requests"]:
            target["incoming_follow_requests"].remove(username)
        self.save_data()
        return True

    def unfollow_user(self, username, target_username):
        users = self.data["users"]
        if username not in users or target_username not in users:
            return False, "User not found."
        if username == target_username:
            return False, "You cannot follow yourself."
        sender = users[username]
        target = users[target_username]
        if target_username not in sender["following"]:
            return False, f"You do not follow {target_username}."
        sender["following"].remove(target_username)
        if username in target["followers"]:
            target["followers"].remove(username)
        self._sync_friendship(username, target_username)
        self.save_data()
        return True, f"You unfollowed {target_username}."

    def toggle_follow(self, username, target_username):
        users = self.data["users"]
        if username in users and target_username in users:
            if target_username in users[username]["following"]:
                return self.unfollow_user(username, target_username)
        return self.follow_user(username, target_username)

    def send_friend_request(self, username, target_username):
        return self.follow_user(username, target_username)

    def accept_friend_request(self, username, requester):
        return self.accept_follow_request(username, requester)

    def decline_friend_request(self, username, requester):
        return self.decline_follow_request(username, requester)

    def cancel_friend_request(self, username, target_username):
        return self.cancel_follow_request(username, target_username)

    def add_friend(self, username, friend_username):
        return self.follow_user(username, friend_username)[0]

    def remove_friend(self, username, friend_username):
        return self.unfollow_user(username, friend_username)[0]

    def create_post(self, post):
        saved_post = dict(post)
        saved_post["id"] = uuid4().hex
        saved_post["likes"] = []
        media = saved_post.get("media", b"")
        if isinstance(media, bytes):
            saved_post["media"] = base64.b64encode(media).decode("ascii")
        saved_post["created_at"] = datetime.now(timezone.utc).isoformat()
        self.record_activity(
            saved_post["username"],
            "post",
            f"Shared a post about {saved_post['restaurant']}",
        )
        self.data["posts"].append(saved_post)
        self.save_data()
        return True

    def create_business_post(self, business_username, post):
        business = self.data.setdefault("businesses", {}).get(business_username)
        if business is None:
            return False
        saved_post = dict(post)
        saved_post.update(
            {
                "id": uuid4().hex,
                "username": business_username,
                "author_type": "business",
                "business_username": business_username,
                "restaurant": business["restaurant_name"],
                "city": business["city"],
                "likes": [],
                "created_at": datetime.now(timezone.utc).isoformat(),
            }
        )
        media = saved_post.get("media", b"")
        if isinstance(media, bytes):
            saved_post["media"] = base64.b64encode(media).decode("ascii")
        business.setdefault("activity", []).append(
            {
                "type": "post",
                "description": f"Published a post for {business['restaurant_name']}.",
                "created_at": saved_post["created_at"],
            }
        )
        self.data["posts"].append(saved_post)
        self.save_data()
        return True

    def like_post(self, username, post_id):
        if username not in self.data["users"]:
            return False, "User not found."
        post = next(
            (saved for saved in self.data["posts"] if saved.get("id") == post_id),
            None,
        )
        if post is None:
            return False, "Post not found."
        post.setdefault("likes", [])
        if username in post["likes"]:
            post["likes"].remove(username)
            message = "Like removed."
        else:
            post["likes"].append(username)
            owner = post.get("username")
            if owner != username:
                if post.get("author_type") == "business":
                    business = self.data["businesses"].get(
                        post.get("business_username", owner)
                    )
                    if business is not None:
                        business.setdefault("notifications", []).append(
                            {
                                "id": uuid4().hex,
                                "type": "like",
                                "actor": username,
                                "description": f"@{username} liked your restaurant post.",
                                "post_id": post_id,
                                "created_at": datetime.now(timezone.utc).isoformat(),
                                "read": False,
                            }
                        )
                else:
                    self.add_notification(
                        owner,
                        username,
                        "like",
                        f"@{username} liked your post.",
                        post_id=post_id,
                    )
            message = "Post liked."
        self.save_data()
        return True, message
