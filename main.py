from search_engine import search_restaurant
from structures import Restaurant
from automation_engine import (
    calculate_trust_score,
    calculate_taste_match,
    calculate_decision_friction,
    check_restaurant,
    check_warning
)

import os


# ============================================================
# RESTAURANT DATABASE
# ============================================================

restaurants = [

    # ========================================================
    # CANCUN
    # ========================================================

    Restaurant(
        name="Sushigo Yaxchilan",
        cuisine="Japanese",
        rating=4.9,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="Nicoletta",
        cuisine="Italian",
        rating=4.8,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="The BurgerOn",
        cuisine="Burgers",
        rating=4.8,
        recommendation_source="unknown",
        matches_preferences=False
    ),

    Restaurant(
        name="Sushi Central",
        cuisine="Japanese",
        rating=4.7,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="NODO BRGRS",
        cuisine="Burgers",
        rating=4.7,
        recommendation_source="verified_review",
        matches_preferences=False
    ),

    Restaurant(
        name="Icaza",
        cuisine="Mexican",
        rating=4.6,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="EGO",
        cuisine="International",
        rating=4.6,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Prima Donna",
        cuisine="Italian",
        rating=4.7,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="Kai",
        cuisine="Japanese",
        rating=4.8,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Marbella",
        cuisine="Mediterranean",
        rating=4.5,
        recommendation_source="friend",
        matches_preferences=False
    ),

    Restaurant(
        name="Puerto Santo",
        cuisine="Mexican",
        rating=4.5,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Harry's",
        cuisine="Steakhouse",
        rating=4.7,
        recommendation_source="verified_review",
        matches_preferences=False
    ),

    Restaurant(
        name="RosaNegra",
        cuisine="Latin",
        rating=4.6,
        recommendation_source="friend",
        matches_preferences=False
    ),

    Restaurant(
        name="Porfirio's",
        cuisine="Mexican",
        rating=4.5,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="La Habichuela",
        cuisine="Mexican",
        rating=4.5,
        recommendation_source="friend",
        matches_preferences=False
    ),

    Restaurant(
        name="Bovino's",
        cuisine="Steakhouse",
        rating=4.6,
        recommendation_source="verified_review",
        matches_preferences=False
    ),

    Restaurant(
        name="Ryoshi",
        cuisine="Japanese",
        rating=4.7,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="Elefanta",
        cuisine="Greek",
        rating=4.6,
        recommendation_source="verified_review",
        matches_preferences=False
    ),

    Restaurant(
        name="Bovino's Churrascaría",
        cuisine="Brazilian",
        rating=4.5,
        recommendation_source="friend",
        matches_preferences=False
    ),

    Restaurant(
        name="Mextreme",
        cuisine="Mexican",
        rating=4.4,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Casa Rolandi",
        cuisine="Seafood",
        rating=4.6,
        recommendation_source="friend",
        matches_preferences=False
    ),

    Restaurant(
        name="Cambalache",
        cuisine="Argentinian",
        rating=4.6,
        recommendation_source="verified_review",
        matches_preferences=False
    ),

    Restaurant(
        name="Puerto Madero",
        cuisine="Argentinian",
        rating=4.7,
        recommendation_source="friend",
        matches_preferences=False
    ),

    Restaurant(
        name="El Fish Fritanga",
        cuisine="Seafood",
        rating=4.5,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="Tacun",
        cuisine="Mexican",
        rating=4.4,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="La Parrilla",
        cuisine="Mexican",
        rating=4.5,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="Basta Pasta",
        cuisine="Italian",
        rating=4.4,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Umami",
        cuisine="Asian",
        rating=4.5,
        recommendation_source="friend",
        matches_preferences=False
    ),

    Restaurant(
        name="El Galeon del Caribe",
        cuisine="Seafood",
        rating=4.3,
        recommendation_source="verified_review",
        matches_preferences=False
    ),

    Restaurant(
        name="Casa Jaguar",
        cuisine="Mexican",
        rating=4.5,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="Mora",
        cuisine="International",
        rating=4.4,
        recommendation_source="verified_review",
        matches_preferences=False
    ),

    Restaurant(
        name="Olive Garden",
        cuisine="Italian",
        rating=4.3,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    # ========================================================
    # MIAMI
    # ========================================================

    Restaurant(
        name="Sunny's",
        cuisine="Steakhouse",
        rating=4.8,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Boia De",
        cuisine="Italian",
        rating=4.8,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="The Surf Club Restaurant",
        cuisine="American",
        rating=4.6,
        recommendation_source="verified_review",
        matches_preferences=False
    ),

    Restaurant(
        name="Joe's Stone Crab",
        cuisine="Seafood",
        rating=4.7,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="Cote Miami",
        cuisine="Korean",
        rating=4.6,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Mandolin Aegean Bistro",
        cuisine="Greek",
        rating=4.7,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="Ariete",
        cuisine="Cuban",
        rating=4.6,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Shingo",
        cuisine="Japanese",
        rating=4.8,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Hiyakawa",
        cuisine="Japanese",
        rating=4.7,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Naoe",
        cuisine="Japanese",
        rating=4.8,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Stubborn Seed",
        cuisine="New American",
        rating=4.5,
        recommendation_source="verified_review",
        matches_preferences=False
    ),

    Restaurant(
        name="Los Félix",
        cuisine="Mexican",
        rating=4.6,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Krüs Kitchen",
        cuisine="International",
        rating=4.7,
        recommendation_source="friend",
        matches_preferences=True
    ),

    Restaurant(
        name="Bachour",
        cuisine="Bakery",
        rating=4.6,
        recommendation_source="verified_review",
        matches_preferences=True
    ),

    Restaurant(
        name="Barra Callao",
        cuisine="Peruvian",
        rating=4.9,
        recommendation_source="verified_review",
        matches_preferences=True
    )
]


# ============================================================
# CITY INFORMATION
# ============================================================

restaurant_cities = {}


# Put all original restaurants in Cancun.

for restaurant in restaurants:

    restaurant_cities[
        restaurant.name
    ] = "Cancun"


# Move Miami restaurants into Miami.

miami_restaurants = [

    "Sunny's",
    "Boia De",
    "The Surf Club Restaurant",
    "Joe's Stone Crab",
    "Cote Miami",
    "Mandolin Aegean Bistro",
    "Ariete",
    "Shingo",
    "Hiyakawa",
    "Naoe",
    "Stubborn Seed",
    "Los Félix",
    "Krüs Kitchen",
    "Bachour",
    "Barra Callao"

]


for restaurant_name in miami_restaurants:

    restaurant_cities[
        restaurant_name
    ] = "Miami"


# ============================================================
# USERS
# ============================================================

users = {}


# ============================================================
# SOCIAL POSTS
# ============================================================

posts = []


# ============================================================
# GET RESTAURANT
# ============================================================

def get_restaurant_by_name(name):

    for restaurant in restaurants:

        if restaurant.name.lower() == name.lower():

            return restaurant

    return None


# ============================================================
# GET RESTAURANTS IN CITY
# ============================================================

def get_restaurants_in_city(city):

    city_restaurants = []

    for restaurant in restaurants:

        restaurant_city = restaurant_cities[
            restaurant.name
        ]

        if restaurant_city.lower() == city.lower():

            city_restaurants.append(
                restaurant
            )

    return city_restaurants


# ============================================================
# GET AVAILABLE CITIES
# ============================================================

def get_available_cities():

    cities = []

    for restaurant in restaurants:

        city = restaurant_cities[
            restaurant.name
        ]

        if city not in cities:

            cities.append(city)

    return cities


# ============================================================
# SIGN UP
# ============================================================

def sign_up():

    print("\n========================================")
    print("              HOTSPOT SIGN UP")
    print("========================================")

    username = input(
        "Create a username: "
    ).strip()

    if username == "":

        print(
            "Warning: Username cannot be empty."
        )

        return None

    if username in users:

        print(
            "Warning: That username already exists."
        )

        return None

    password = input(
        "Create a password: "
    ).strip()

    if password == "":

        print(
            "Warning: Password cannot be empty."
        )

        return None

    # --------------------------------------------------------
    # TOP 5
    # --------------------------------------------------------

    print("\n========================================")
    print("           BUILD YOUR PROFILE")
    print("========================================")

    print(
        "\nChoose your TOP 5 favorite restaurants."
    )

    print(
        "These choices help HOTSPOT learn "
        "your taste."
    )

    # We only show Cancun restaurants during
    # the initial profile setup.

    signup_restaurants = get_restaurants_in_city(
        "Cancun"
    )

    for index, restaurant in enumerate(
        signup_restaurants,
        start=1
    ):

        print(
            f"{index}. {restaurant.name} "
            f"| {restaurant.cuisine} "
            f"| {restaurant.rating}/5"
        )

    selected_restaurants = []

    while len(selected_restaurants) < 5:

        try:

            choice = int(
                input(
                    f"\nChoose favorite "
                    f"#{len(selected_restaurants) + 1}: "
                )
            )

            if (
                choice < 1
                or choice > len(signup_restaurants)
            ):

                print(
                    "Warning: Invalid choice."
                )

                continue

            selected = signup_restaurants[
                choice - 1
            ]

            if selected.name in selected_restaurants:

                print(
                    "Warning: You already selected "
                    "that restaurant."
                )

                continue

            selected_restaurants.append(
                selected.name
            )

            print(
                f"Added: {selected.name}"
            )

        except ValueError:

            print(
                "Warning: Please enter a number."
            )

    # --------------------------------------------------------
    # CREATE ACCOUNT
    # --------------------------------------------------------

    users[username] = {

        "password": password,

        "top_restaurants":
            selected_restaurants,

        "ratings": {},

        "friends": []

    }

    print("\n========================================")
    print("          PROFILE CREATED!")
    print("========================================")

    print(
        f"\nWelcome to HOTSPOT, {username}!"
    )

    print("\nYour Top 5:")

    for restaurant in selected_restaurants:

        print(
            f"- {restaurant}"
        )

    return username


# ============================================================
# SIGN IN
# ============================================================

def sign_in():

    print("\n========================================")
    print("             HOTSPOT SIGN IN")
    print("========================================")

    username = input(
        "Username: "
    ).strip()

    password = input(
        "Password: "
    ).strip()

    if username not in users:

        print(
            "Warning: Account not found."
        )

        return None

    if users[username]["password"] != password:

        print(
            "Warning: Incorrect password."
        )

        return None

    print(
        f"\nWelcome back, {username}!"
    )

    return username


# ============================================================
# PERSONAL PREFERENCE SCORE
# ============================================================

def calculate_preference_score(
    restaurant,
    username,
    user_store=None
):

    if user_store is None:
        user_store = users

    top_restaurants = user_store[username][
        "top_restaurants"
    ]

    user_ratings = user_store[username][
        "ratings"
    ]

    score = 0

    favorite_cuisines = []

    # --------------------------------------------------------
    # LEARN CUISINES FROM TOP 5
    # --------------------------------------------------------

    for favorite_name in top_restaurants:

        favorite = get_restaurant_by_name(
            favorite_name
        )

        if favorite is not None:

            favorite_cuisines.append(
                favorite.cuisine
            )

    # --------------------------------------------------------
    # CUISINE MATCH
    # --------------------------------------------------------

    for cuisine in favorite_cuisines:

        if restaurant.cuisine == cuisine:

            score += 15

    # --------------------------------------------------------
    # LEARN FROM PREVIOUS RATINGS
    # --------------------------------------------------------

    total = 0

    count = 0

    for restaurant_name, rating in (
        user_ratings.items()
    ):

        rated_restaurant = get_restaurant_by_name(
            restaurant_name
        )

        if rated_restaurant is not None:

            if (
                rated_restaurant.cuisine
                == restaurant.cuisine
            ):

                total += rating

                count += 1

    if count > 0:

        average = total / count

        score += average * 8

    # --------------------------------------------------------
    # RESTAURANT QUALITY
    # --------------------------------------------------------

    if restaurant.rating >= 4.8:

        score += 10

    elif restaurant.rating >= 4.6:

        score += 7

    elif restaurant.rating >= 4.4:

        score += 4

    return score


# ============================================================
# FRIEND TRUST BONUS
# ============================================================

def calculate_friend_trust_bonus(
    restaurant,
    username,
    user_store=None
):

    if user_store is None:
        user_store = users

    friends = user_store[username][
        "friends"
    ]

    bonus = 0

    trusted_friends = []

    for friend in friends:

        friend_ratings = user_store[friend][
            "ratings"
        ]

        if restaurant.name in friend_ratings:

            rating = friend_ratings[
                restaurant.name
            ]

            if rating >= 3.5:

                bonus += 10

                trusted_friends.append(
                    (
                        friend,
                        rating
                    )
                )

    bonus = min(
        bonus,
        30
    )

    return bonus, trusted_friends


# ============================================================
# PERSONALIZED SCORE
# ============================================================

def calculate_personalized_scores(
    restaurant,
    username,
    user_store=None
):

    if user_store is None:
        user_store = users

    user_ratings = user_store[username][
        "ratings"
    ]

    trust_score = calculate_trust_score(
        50,
        restaurant.recommendation_source
    )

    taste_match = calculate_taste_match(
        50,
        restaurant.matches_preferences
    )

    preference_score = calculate_preference_score(
        restaurant,
        username,
        user_store
    )

    taste_match += preference_score

    decision_friction = calculate_decision_friction(
        50,
        restaurant.matches_preferences
    )

    decision_friction -= (
        preference_score / 2
    )

    # --------------------------------------------------------
    # FRIEND TRUST
    # --------------------------------------------------------

    friend_bonus, trusted_friends = (
        calculate_friend_trust_bonus(
            restaurant,
            username,
            user_store
        )
    )

    trust_score += friend_bonus

    # --------------------------------------------------------
    # USER'S OWN RATING
    # --------------------------------------------------------

    if restaurant.name in user_ratings:

        rating = user_ratings[
            restaurant.name
        ]

        if rating >= 4:

            trust_score += 10

        elif rating <= 2:

            trust_score -= 10

    # --------------------------------------------------------
    # KEEP SCORES BETWEEN 0 AND 100
    # --------------------------------------------------------

    trust_score = max(
        0,
        min(100, round(trust_score))
    )

    taste_match = max(
        0,
        min(100, round(taste_match))
    )

    decision_friction = max(
        0,
        min(100, round(decision_friction))
    )

    return {

        "Trust Score": trust_score,

        "Taste Match": taste_match,

        "Decision Friction":
            decision_friction,

        "Friend Trust Bonus":
            friend_bonus,

        "Trusted Friends":
            trusted_friends

    }


# ============================================================
# CITY-SPECIFIC RECOMMENDATIONS
# ============================================================

def generate_city_recommendations(
    username,
    city,
    user_store=None
):

    if user_store is None:
        user_store = users

    city_restaurants = get_restaurants_in_city(
        city
    )

    top_restaurants = user_store[username][
        "top_restaurants"
    ]

    results = []

    for restaurant in city_restaurants:

        # ----------------------------------------------------
        # DON'T RECOMMEND TOP 5 AGAIN
        # ----------------------------------------------------

        if restaurant.name in top_restaurants:

            continue

        scores = calculate_personalized_scores(
            restaurant,
            username,
            user_store
        )

        result = check_restaurant(
            restaurant.rating,
            restaurant.matches_preferences
        )

        warnings = check_warning(
            scores
        )

        # ----------------------------------------------------
        # HOTSPOT SCORE
        # ----------------------------------------------------

        hotspot_score = (

            scores["Trust Score"]

            + scores["Taste Match"]

            + (
                100
                - scores["Decision Friction"]
            )

        ) / 3

        results.append(
            (
                restaurant,
                scores,
                result,
                warnings,
                hotspot_score
            )
        )

    results.sort(
        key=lambda item: item[4],
        reverse=True
    )

    return results


# ============================================================
# FIND RESTAURANTS BY CITY
# ============================================================

def find_restaurants(username):

    print("\n========================================")
    print("          FIND RESTAURANTS")
    print("========================================")

    print(
        "\nFirst, choose the city you want "
        "to explore."
    )

    print(
        "\nAvailable cities:"
    )

    cities = get_available_cities()

    for index, city in enumerate(
        cities,
        start=1
    ):

        restaurant_count = len(
            get_restaurants_in_city(city)
        )

        print(
            f"{index}. {city} "
            f"({restaurant_count} restaurants)"
        )

    try:

        city_choice = int(
            input(
                "\nChoose a city: "
            )
        )

        if (
            city_choice < 1
            or city_choice > len(cities)
        ):

            print(
                "Warning: Invalid city."
            )

            return

        city = cities[
            city_choice - 1
        ]

        # ----------------------------------------------------
        # CITY SELECTED
        # ----------------------------------------------------

        print("\n========================================")
        print(
            f"          {city.upper()}"
        )
        print("========================================")

        print(
            f"\nHOTSPOT is finding the best "
            f"new restaurants in {city} "
            f"for you..."
        )

        recommendations = (
            generate_city_recommendations(
                username,
                city
            )
        )

        if len(recommendations) == 0:

            print(
                "\nThere are no new recommendations "
                "available in this city."
            )

            return

        # ----------------------------------------------------
        # RECOMMENDATIONS
        # ----------------------------------------------------

        print("\n========================================")
        print(
            f"      YOUR {city.upper()} PICKS"
        )
        print("========================================")

        for position, item in enumerate(
            recommendations[:5],
            start=1
        ):

            restaurant = item[0]

            scores = item[1]

            result = item[2]

            warnings = item[3]

            hotspot_score = item[4]

            print(
                f"\n#{position} "
                f"{restaurant.name}"
            )

            print(
                f"Cuisine: "
                f"{restaurant.cuisine}"
            )

            print(
                f"Restaurant Rating: "
                f"{restaurant.rating}/5"
            )

            print(
                f"HOTSPOT Score: "
                f"{round(hotspot_score, 1)}/100"
            )

            print(
                f"HOTSPOT Result: "
                f"{result}"
            )

            # ------------------------------------------------
            # FRIEND TRUST
            # ------------------------------------------------

            print(
                "\nFRIEND TRUST BONUS"
            )

            print(
                "------------------"
            )

            if scores[
                "Friend Trust Bonus"
            ] > 0:

                print(
                    f"Friend Trust Bonus: "
                    f"+{scores['Friend Trust Bonus']}"
                )

                for friend, rating in (
                    scores[
                        "Trusted Friends"
                    ]
                ):

                    print(
                        f"- {friend} rated "
                        f"{restaurant.name} "
                        f"{rating}/5"
                    )

            else:

                print(
                    "No friend trust bonus yet."
                )

            # ------------------------------------------------
            # PERSONALIZED SCORES
            # ------------------------------------------------

            print(
                "\nPersonalized Scores:"
            )

            print(
                f"Trust Score: "
                f"{scores['Trust Score']}"
            )

            print(
                f"Taste Match: "
                f"{scores['Taste Match']}"
            )

            print(
                f"Decision Friction: "
                f"{scores['Decision Friction']}"
            )

            for warning in warnings:

                print(
                    warning
                )

        # ----------------------------------------------------
        # CITY BROWSING OPTION
        # ----------------------------------------------------

        print("\n========================================")

        print(
            f"Want to browse all "
            f"{city} restaurants?"
        )

        print("1. Yes")

        print("2. No")

        try:

            browse_choice = int(
                input(
                    "\nChoose: "
                )
            )

            if browse_choice == 1:

                browse_city(
                    city
                )

        except ValueError:

            print(
                "Returning to menu."
            )

    except ValueError:

        print(
            "Warning: Please enter a number."
        )


# ============================================================
# BROWSE CITY
# ============================================================

def browse_city(city):

    city_restaurants = get_restaurants_in_city(
        city
    )

    print("\n========================================")

    print(
        f"       ALL RESTAURANTS IN {city.upper()}"
    )

    print("========================================")

    for index, restaurant in enumerate(
        city_restaurants,
        start=1
    ):

        print(
            f"\n{index}. "
            f"{restaurant.name}"
        )

        print(
            f"   Cuisine: "
            f"{restaurant.cuisine}"
        )

        print(
            f"   Rating: "
            f"{restaurant.rating}/5"
        )


# ============================================================
# RATE RESTAURANT
# ============================================================

def rate_restaurant(username):

    print("\n========================================")
    print("          RATE A RESTAURANT")
    print("========================================")

    # Instead of showing every restaurant,
    # first ask for a city.

    cities = get_available_cities()

    print(
        "\nChoose the city of the restaurant:"
    )

    for index, city in enumerate(
        cities,
        start=1
    ):

        print(
            f"{index}. {city}"
        )

    try:

        city_choice = int(
            input(
                "\nChoose city: "
            )
        )

        if (
            city_choice < 1
            or city_choice > len(cities)
        ):

            print(
                "Warning: Invalid city."
            )

            return

        city = cities[
            city_choice - 1
        ]

        city_restaurants = (
            get_restaurants_in_city(
                city
            )
        )

        print(
            f"\nRestaurants in {city}:"
        )

        for index, restaurant in enumerate(
            city_restaurants,
            start=1
        ):

            print(
                f"{index}. "
                f"{restaurant.name}"
            )

        restaurant_choice = int(
            input(
                "\nChoose restaurant: "
            )
        )

        if (
            restaurant_choice < 1
            or restaurant_choice
            > len(city_restaurants)
        ):

            print(
                "Warning: Invalid restaurant."
            )

            return

        restaurant = city_restaurants[
            restaurant_choice - 1
        ]

        print(
            f"\nYou selected: "
            f"{restaurant.name}"
        )

        print(
            "\nRating from 1 to 5."
        )

        print(
            "Half-star ratings are allowed."
        )

        rating = float(
            input(
                "Your rating: "
            )
        )

        if rating < 1 or rating > 5:

            print(
                "Warning: Rating must be "
                "between 1 and 5."
            )

            return

        if (rating * 2) % 1 != 0:

            print(
                "Warning: Use whole or "
                "half-star ratings."
            )

            return

        users[username]["ratings"][
            restaurant.name
        ] = rating

        print(
            f"\nSaved: "
            f"{restaurant.name} = {rating}/5"
        )

        if rating >= 3.5:

            print(
                "\nThis rating qualifies "
                "as a trusted rating."
            )

    except ValueError:

        print(
            "Warning: Please enter a valid number."
        )


# ============================================================
# VIEW RATINGS
# ============================================================

def view_ratings(username):

    print("\n========================================")
    print("             MY RATINGS")
    print("========================================")

    ratings = users[username][
        "ratings"
    ]

    if len(ratings) == 0:

        print(
            "\nYou have not rated "
            "any restaurants yet."
        )

        return

    for restaurant, rating in (
        ratings.items()
    ):

        print(
            f"{restaurant}: "
            f"{rating}/5"
        )


# ============================================================
# FIND FRIENDS
# ============================================================

def search_users(username):

    print("\n========================================")
    print("             FIND FRIENDS")
    print("========================================")

    search_name = input(
        "\nEnter username: "
    ).strip()

    if search_name == username:

        print(
            "Warning: You cannot add yourself."
        )

        return

    if search_name not in users:

        print(
            "No user found."
        )

        return

    if search_name in users[username][
        "friends"
    ]:

        print(
            "You are already friends."
        )

        return

    users[username]["friends"].append(
        search_name
    )

    users[search_name]["friends"].append(
        username
    )

    print(
        f"\n{search_name} was added "
        "to your friend connections!"
    )


# ============================================================
# VIEW FRIENDS
# ============================================================

def view_friends(username):

    friends = users[username][
        "friends"
    ]

    print("\n========================================")
    print("          FRIEND CONNECTIONS")
    print("========================================")

    if len(friends) == 0:

        print(
            "\nYou don't have any friends yet."
        )

        return

    for friend in friends:

        print(
            f"\nFriend: {friend}"
        )

        ratings = users[friend][
            "ratings"
        ]

        trusted = 0

        for restaurant, rating in (
            ratings.items()
        ):

            if rating >= 3.5:

                trusted += 1

                print(
                    f"  {restaurant}: "
                    f"{rating}/5"
                )

        print(
            f"Trusted ratings: {trusted}"
        )


# ============================================================
# REMOVE FRIEND
# ============================================================

def remove_friend(username):

    friends = users[username][
        "friends"
    ]

    if len(friends) == 0:

        print(
            "\nYou don't have any friends."
        )

        return

    for index, friend in enumerate(
        friends,
        start=1
    ):

        print(
            f"{index}. {friend}"
        )

    try:

        choice = int(
            input(
                "\nChoose friend to remove: "
            )
        )

        if (
            choice < 1
            or choice > len(friends)
        ):

            print(
                "Warning: Invalid choice."
            )

            return

        friend = friends[
            choice - 1
        ]

        users[username]["friends"].remove(
            friend
        )

        if username in users[friend][
            "friends"
        ]:

            users[friend]["friends"].remove(
                username
            )

        print(
            f"\nRemoved {friend}."
        )

    except ValueError:

        print(
            "Warning: Please enter a number."
        )


# ============================================================
# FRIENDS PAGE
# ============================================================

def friends_page(username):

    while True:

        print("\n========================================")
        print("          FRIENDS & CONNECTIONS")
        print("========================================")

        print(
            f"Connected friends: "
            f"{len(users[username]['friends'])}"
        )

        print("\n1. Find and add friend")
        print("2. View friends")
        print("3. Remove friend")
        print("4. Back")

        try:

            choice = int(
                input(
                    "\nChoose: "
                )
            )

            if choice == 1:

                search_users(
                    username
                )

            elif choice == 2:

                view_friends(
                    username
                )

            elif choice == 3:

                remove_friend(
                    username
                )

            elif choice == 4:

                break

            else:

                print(
                    "Warning: Invalid choice."
                )

        except ValueError:

            print(
                "Warning: Enter a number."
            )


# ============================================================
# CREATE SOCIAL POST
# ============================================================

def create_post(username):

    print("\n========================================")
    print("             CREATE A POST")
    print("========================================")

    # --------------------------------------------------------
    # CITY FIRST
    # --------------------------------------------------------

    cities = get_available_cities()

    print(
        "\nFirst choose the city:"
    )

    for index, city in enumerate(
        cities,
        start=1
    ):

        print(
            f"{index}. {city}"
        )

    try:

        city_choice = int(
            input(
                "\nChoose city: "
            )
        )

        if (
            city_choice < 1
            or city_choice > len(cities)
        ):

            print(
                "Warning: Invalid city."
            )

            return

        city = cities[
            city_choice - 1
        ]

        # ----------------------------------------------------
        # RESTAURANTS IN THAT CITY
        # ----------------------------------------------------

        city_restaurants = (
            get_restaurants_in_city(
                city
            )
        )

        print(
            f"\nRestaurants in {city}:"
        )

        for index, restaurant in enumerate(
            city_restaurants,
            start=1
        ):

            print(
                f"{index}. "
                f"{restaurant.name}"
            )

        restaurant_choice = int(
            input(
                "\nChoose restaurant: "
            )
        )

        if (
            restaurant_choice < 1
            or restaurant_choice
            > len(city_restaurants)
        ):

            print(
                "Warning: Invalid restaurant."
            )

            return

        restaurant = city_restaurants[
            restaurant_choice - 1
        ]

        # ----------------------------------------------------
        # MEDIA TYPE
        # ----------------------------------------------------

        print("\nMedia type:")

        print("1. Photo")
        print("2. Video")

        media_choice = int(
            input(
                "\nChoose: "
            )
        )

        if media_choice == 1:

            media_type = "Photo"

        elif media_choice == 2:

            media_type = "Video"

        else:

            print(
                "Warning: Invalid media type."
            )

            return

        # ----------------------------------------------------
        # MEDIA PATH
        # ----------------------------------------------------

        media_path = input(
            "\nEnter photo/video file path: "
        ).strip()

        if media_path == "":

            print(
                "Warning: File path cannot "
                "be empty."
            )

            return

        if os.path.exists(media_path):

            print(
                "Media file found!"
            )

        else:

            print(
                "Note: The file path was saved, "
                "but the file was not found."
            )

        # ----------------------------------------------------
        # CAPTION
        # ----------------------------------------------------

        caption = input(
            "\nWrite a caption: "
        ).strip()

        if caption == "":

            caption = "No caption."

        # ----------------------------------------------------
        # SAVE POST
        # ----------------------------------------------------

        post = {

            "username": username,

            "restaurant":
                restaurant.name,

            "city": city,

            "media_type":
                media_type,

            "media_path":
                media_path,

            "caption":
                caption

        }

        posts.append(
            post
        )

        print("\n========================================")
        print("             POST CREATED!")
        print("========================================")

        print(
            f"\n{restaurant.name}"
        )

        print(
            f"{media_type}"
        )

        print(
            caption
        )

    except ValueError:

        print(
            "Warning: Please enter a valid number."
        )


# ============================================================
# HOTSPOT FEED
# ============================================================

def show_feed(username):

    print("\n========================================")
    print("             HOTSPOT FEED")
    print("========================================")

    if len(posts) == 0:

        print(
            "\nThere are no posts yet."
        )

        return

    for number, post in enumerate(
        reversed(posts),
        start=1
    ):

        print("\n----------------------------------------")

        print(
            f"POST #{number}"
        )

        print(
            f"@{post['username']}"
        )

        print(
            f"Restaurant: "
            f"{post['restaurant']}"
        )

        print(
            f"City: "
            f"{post['city']}"
        )

        print(
            f"Media: "
            f"{post['media_type']}"
        )

        print(
            f"File: "
            f"{post['media_path']}"
        )

        print(
            f"Caption: "
            f"{post['caption']}"
        )


# ============================================================
# RESTAURANT FEED
# ============================================================

def restaurant_feed(username):

    print("\n========================================")
    print("         RESTAURANT FEED")
    print("========================================")

    # --------------------------------------------------------
    # CITY FIRST
    # --------------------------------------------------------

    cities = get_available_cities()

    print(
        "\nChoose a city first:"
    )

    for index, city in enumerate(
        cities,
        start=1
    ):

        print(
            f"{index}. {city}"
        )

    try:

        city_choice = int(
            input(
                "\nChoose city: "
            )
        )

        if (
            city_choice < 1
            or city_choice > len(cities)
        ):

            print(
                "Warning: Invalid city."
            )

            return

        city = cities[
            city_choice - 1
        ]

        # ----------------------------------------------------
        # RESTAURANTS IN CITY
        # ----------------------------------------------------

        city_restaurants = (
            get_restaurants_in_city(
                city
            )
        )

        print(
            f"\nRestaurants in {city}:"
        )

        for index, restaurant in enumerate(
            city_restaurants,
            start=1
        ):

            print(
                f"{index}. "
                f"{restaurant.name}"
            )

        restaurant_choice = int(
            input(
                "\nChoose restaurant: "
            )
        )

        if (
            restaurant_choice < 1
            or restaurant_choice
            > len(city_restaurants)
        ):

            print(
                "Warning: Invalid restaurant."
            )

            return

        restaurant = city_restaurants[
            restaurant_choice - 1
        ]

        # ----------------------------------------------------
        # SHOW POSTS
        # ----------------------------------------------------

        matching_posts = []

        for post in posts:

            if (
                post["restaurant"]
                == restaurant.name
            ):

                matching_posts.append(
                    post
                )

        print("\n========================================")

        print(
            f"POSTS FOR "
            f"{restaurant.name.upper()}"
        )

        print("========================================")

        if len(matching_posts) == 0:

            print(
                "\nNo posts yet."
            )

            return

        for number, post in enumerate(
            reversed(matching_posts),
            start=1
        ):

            print(
                f"\nPost #{number}"
            )

            print(
                f"@{post['username']}"
            )

            print(
                f"{post['media_type']}: "
                f"{post['media_path']}"
            )

            print(
                f"Caption: "
                f"{post['caption']}"
            )

    except ValueError:

        print(
            "Warning: Please enter a valid number."
        )


# ============================================================
# MY POSTS
# ============================================================

def my_posts(username):

    print("\n========================================")
    print("              MY POSTS")
    print("========================================")

    user_posts = []

    for post in posts:

        if post["username"] == username:

            user_posts.append(
                post
            )

    if len(user_posts) == 0:

        print(
            "\nYou haven't created "
            "any posts yet."
        )

        return

    for post in user_posts:

        print("\n----------------------------------------")

        print(
            f"Restaurant: "
            f"{post['restaurant']}"
        )

        print(
            f"City: "
            f"{post['city']}"
        )

        print(
            f"Media: "
            f"{post['media_type']}"
        )

        print(
            f"File: "
            f"{post['media_path']}"
        )

        print(
            f"Caption: "
            f"{post['caption']}"
        )


# ============================================================
# SOCIAL PAGE
# ============================================================

def social_page(username):

    while True:

        print("\n========================================")
        print("           HOTSPOT SOCIAL")
        print("========================================")

        print("\n1. Create a post")
        print("2. View HOTSPOT feed")
        print("3. View restaurant feed")
        print("4. View my posts")
        print("5. Back")

        try:

            choice = int(
                input(
                    "\nChoose: "
                )
            )

            if choice == 1:

                create_post(
                    username
                )

            elif choice == 2:

                show_feed(
                    username
                )

            elif choice == 3:

                restaurant_feed(
                    username
                )

            elif choice == 4:

                my_posts(
                    username
                )

            elif choice == 5:

                break

            else:

                print(
                    "Warning: Invalid choice."
                )

        except ValueError:

            print(
                "Warning: Please enter a number."
            )


# ============================================================
# PROFILE PAGE
# ============================================================

def profile_page(username):

    while True:

        print("\n========================================")
        print("              MY PROFILE")
        print("========================================")

        print(
            f"\nUsername: {username}"
        )

        print("\nTop 5:")

        for position, restaurant in enumerate(
            users[username][
                "top_restaurants"
            ],
            start=1
        ):

            print(
                f"{position}. "
                f"{restaurant}"
            )

        print(
            f"\nFriends: "
            f"{len(users[username]['friends'])}"
        )

        print(
            f"Ratings: "
            f"{len(users[username]['ratings'])}"
        )

        print("\n1. Rate a restaurant")
        print("2. View my ratings")
        print("3. Friends & Connections")
        print("4. Back")

        try:

            choice = int(
                input(
                    "\nChoose: "
                )
            )

            if choice == 1:

                rate_restaurant(
                    username
                )

            elif choice == 2:

                view_ratings(
                    username
                )

            elif choice == 3:

                friends_page(
                    username
                )

            elif choice == 4:

                break

            else:

                print(
                    "Warning: Invalid choice."
                )

        except ValueError:

            print(
                "Warning: Please enter a number."
            )


# ============================================================
# MAIN USER MENU
# ============================================================

def user_menu(username):

    while True:

        print("\n========================================")
        print("             HOTSPOT MENU")
        print("========================================")

        print(
            f"Logged in as: {username}"
        )

        print("\n1. Find Restaurants")

        print(
            "2. My Personalized Recommendations"
        )

        print(
            "3. My Profile"
        )

        print(
            "4. Friends & Connections"
        )

        print(
            "5. HOTSPOT Social"
        )

        print(
            "6. Log out"
        )

        try:

            choice = int(
                input(
                    "\nChoose an option: "
                )
            )

            # ------------------------------------------------
            # CITY-FIRST RESTAURANT DISCOVERY
            # ------------------------------------------------

            if choice == 1:

                find_restaurants(
                    username
                )

            # ------------------------------------------------
            # PERSONALIZED RECOMMENDATIONS
            #
            # This still exists as a general recommendation
            # system, but restaurant discovery is city-first.
            # ------------------------------------------------

            elif choice == 2:

                print(
                    "\nFor personalized recommendations, "
                    "choose a city first."
                )

                find_restaurants(
                    username
                )

            # ------------------------------------------------
            # PROFILE
            # ------------------------------------------------

            elif choice == 3:

                profile_page(
                    username
                )

            # ------------------------------------------------
            # FRIENDS
            # ------------------------------------------------

            elif choice == 4:

                friends_page(
                    username
                )

            # ------------------------------------------------
            # SOCIAL
            # ------------------------------------------------

            elif choice == 5:

                social_page(
                    username
                )

            # ------------------------------------------------
            # LOG OUT
            # ------------------------------------------------

            elif choice == 6:

                print(
                    f"\nGoodbye, {username}!"
                )

                break

            else:

                print(
                    "Warning: Please choose "
                    "1-6."
                )

        except ValueError:

            print(
                "Warning: Please enter a number."
            )

        except Exception:

            print(
                "Warning: Something went wrong. "
                "Please try again."
            )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    while True:

        print("\n========================================")
        print("                HOTSPOT")
        print("       Restaurant Decision Engine")
        print("========================================")

        print("\n1. Sign In")
        print("2. Sign Up")
        print("3. Exit")

        try:

            choice = int(
                input(
                    "\nChoose an option: "
                )
            )

            if choice == 1:

                username = sign_in()

                if username is not None:

                    user_menu(
                        username
                    )

            elif choice == 2:

                username = sign_up()

                if username is not None:

                    user_menu(
                        username
                    )

            elif choice == 3:

                print(
                    "\nThank you for using HOTSPOT!"
                )

                break

            else:

                print(
                    "Warning: Please choose "
                    "1, 2, or 3."
                )

        except ValueError:

            print(
                "Warning: Please enter a number."
            )

        except Exception:

            print(
                "Warning: Something went wrong. "
                "Please try again."
            )


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":

    main()