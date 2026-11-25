from datetime import datetime
from html import escape

import streamlit as st

import main as hotspot
from models import HotspotDatabase


st.set_page_config(page_title="HOTSPOT", page_icon="📍", layout="wide")



def apply_mobile_styles():
    """Make Streamlit columns and controls comfortable on phones and tablets."""
    st.markdown(
        """
        <style>
        /* Keep long restaurant names and messages inside the screen. */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
            max-width: 100%;
            overflow-x: hidden;
        }
        [data-testid="stMainBlockContainer"] {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }
        [data-testid="stAppViewContainer"] {
            transition: background 180ms ease, color 180ms ease;
        }
        [data-testid="stSidebar"] {
            box-shadow: 8px 0 32px rgba(15, 23, 42, 0.06);
        }
        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li,
        [data-testid="stCaptionContainer"] {
            overflow-wrap: anywhere;
            word-break: normal;
        }
        h1, h2, h3 {
            letter-spacing: -0.035em;
            font-weight: 750;
        }
        h1 {
            padding-bottom: 0.35rem;
        }

        /* Tablet: two columns where possible. Phone: columns naturally wrap. */
        [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
            align-items: stretch;
            gap: 0.75rem;
        }
        [data-testid="column"] {
            min-width: min(100%, 245px) !important;
            flex: 1 1 245px !important;
            width: auto !important;
        }

        /* Make buttons and form controls easier to tap. */
        .stButton button, .stFormSubmitButton button {
            min-height: 2.75rem;
            width: 100%;
            white-space: normal;
            border-radius: 0.75rem;
            transition: transform 120ms ease, box-shadow 120ms ease;
        }
        .stButton button:hover, .stFormSubmitButton button:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 14px rgba(30, 40, 70, 0.12);
        }
        .stButton button[kind="primary"],
        .stFormSubmitButton button[kind="primary"] {
            font-weight: 700;
            box-shadow: 0 5px 16px rgba(229, 9, 20, 0.16);
        }
        [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 1rem;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.045);
        }
        [data-testid="stAlert"] {
            border-radius: 0.9rem;
        }
        input, textarea, [data-baseweb="select"] {
            max-width: 100%;
            border-radius: 0.7rem;
        }
        input:focus, textarea:focus {
            box-shadow: 0 0 0 2px rgba(229, 9, 20, 0.22);
        }
        [data-testid="stMetricValue"] {
            font-size: clamp(1.25rem, 4vw, 2rem);
            overflow-wrap: anywhere;
        }
        [data-testid="stMetricLabel"] {
            white-space: normal;
            overflow-wrap: anywhere;
        }
        [data-testid="stProgressBar"] {
            width: 100%;
        }
        [data-testid="stTabs"] [role="tablist"] {
            gap: 0.25rem;
            overflow-x: auto;
            flex-wrap: nowrap;
        }
        [data-testid="stTabs"] button[role="tab"] {
            white-space: nowrap;
            min-height: 2.75rem;
            font-weight: 650;
        }

        @media (max-width: 640px) {
            [data-testid="stMainBlockContainer"] {
                padding-top: 1rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
            h1 { font-size: 1.7rem !important; }
            h2 { font-size: 1.4rem !important; }
            h3 { font-size: 1.15rem !important; }
            [data-testid="stMetric"] {
                padding: 0.5rem 0.25rem;
            }
            [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
            }
            [data-testid="column"] {
                min-width: 100% !important;
                width: 100% !important;
                flex: 1 1 100% !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def apply_visual_theme(theme):
    palettes = {
        "Light": {
            "background": "#ffffff",
            "surface": "#ffffff",
            "text": "#202536",
            "accent": "#df4355",
            "border": "#e4e8f0",
        },
        "Dark": {
            "background": "#000000",
            "surface": "#111111",
            "text": "#ffffff",
            "accent": "#e50914",
            "border": "#333333",
        },
        "Colorful": {
            "background": "#f7f1ff",
            "surface": "#ffffff",
            "text": "#291c3a",
            "accent": "#8c43d6",
            "border": "#e4d7f4",
        },
    }
    palette = palettes.get(theme, palettes["Light"])
    background = (
        "linear-gradient(135deg, #fff2d8 0%, #fce4f2 45%, #e8e2ff 100%)"
        if theme == "Colorful"
        else palette["background"]
    )
    control_background = "#000000" if theme == "Dark" else "#ffffff"
    control_text = "#ffffff" if theme == "Dark" else "#000000"
    control_border = "#555555" if theme == "Dark" else "#cccccc"
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: {background};
            color: {palette["text"]};
            color-scheme: {"dark" if theme == "Dark" else "light"};
        }}
        [data-testid="stHeader"],
        [data-testid="stToolbar"] {{
            background: {background} !important;
            color: {palette["text"]} !important;
        }}
        [data-testid="stHeader"] *,
        [data-testid="stToolbar"] * {{
            color: {palette["text"]} !important;
        }}
        [data-testid="stMain"] {{
            color: {palette["text"]};
        }}
        [data-testid="stAppViewContainer"] * {{
            color: {palette["text"]} !important;
        }}
        [data-testid="stSidebar"] {{
            background: {palette["surface"]};
            border-right: 1px solid {palette["border"]};
        }}
        [data-testid="stVerticalBlockBorderWrapper"] {{
            background: {palette["surface"]};
            border-color: {palette["border"]};
        }}
        [data-testid="stVerticalBlockBorderWrapper"] > div,
        [data-testid="stExpander"],
        [data-testid="stMetric"],
        [data-testid="stAlert"],
        [data-testid="stNotification"],
        [data-testid="stStatusWidget"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"],
        [data-testid="stCode"],
        [data-testid="stTooltipContent"] {{
            background: {palette["surface"]} !important;
            color: {palette["text"]} !important;
            border-color: {palette["border"]} !important;
        }}
        [data-testid="stExpander"] *,
        [data-testid="stMetric"] *,
        [data-testid="stDataFrame"] *,
        [data-testid="stTable"] *,
        [data-testid="stCode"] *,
        [data-testid="stTooltipContent"] * {{
            color: {palette["text"]} !important;
        }}
        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li,
        [data-testid="stMetricLabel"],
        [data-testid="stCaptionContainer"] {{
            color: {palette["text"]};
        }}
        h1, h2, h3 {{
            color: {palette["text"]};
        }}
        h1::after {{
            content: "";
            display: block;
            width: 3rem;
            height: 0.22rem;
            margin-top: 0.45rem;
            border-radius: 1rem;
            background: {palette["accent"]};
        }}
        .stButton button[kind="primary"],
        .stFormSubmitButton button[kind="primary"] {{
            background: {palette["accent"]} !important;
            border-color: {palette["accent"]} !important;
            color: #ffffff !important;
        }}
        .stButton button[kind="primary"] *,
        .stFormSubmitButton button[kind="primary"] * {{
            color: #ffffff !important;
        }}
        .stButton button,
        .stFormSubmitButton button,
        [data-testid="stSidebar"] button {{
            background-color: {control_background} !important;
            color: {control_text} !important;
            border-color: {control_border} !important;
        }}
        .stButton button *,
        .stFormSubmitButton button *,
        [data-testid="stSidebar"] button * {{
            color: {control_text} !important;
        }}
        .stButton button:hover,
        .stFormSubmitButton button:hover,
        [data-testid="stSidebar"] button:hover {{
            filter: brightness(0.92);
        }}
        input, textarea, select, option,
        [data-baseweb="input"],
        [data-baseweb="textarea"],
        [data-baseweb="select"] > div {{
            background-color: {control_background} !important;
            color: {control_text} !important;
            border-color: {control_border} !important;
            -webkit-text-fill-color: {control_text} !important;
        }}
        input, textarea, [data-baseweb="select"] input,
        [role="combobox"] {{
            background-color: {control_background} !important;
            color: {control_text} !important;
            -webkit-text-fill-color: {control_text} !important;
            caret-color: {palette["accent"]};
        }}
        input::placeholder, textarea::placeholder,
        [data-baseweb="select"] input::placeholder {{
            color: {palette.get("muted", palette["text"])} !important;
            opacity: 0.75;
        }}
        [data-baseweb="popover"],
        [data-baseweb="popover"] > div,
        [data-baseweb="menu"],
        [role="listbox"],
        [role="option"] {{
            background-color: {control_background} !important;
            color: {control_text} !important;
        }}
        [role="option"]:hover,
        [role="option"][aria-selected="true"],
        [data-baseweb="menu"] [aria-selected="true"] {{
            background-color: {control_border} !important;
            color: {control_text} !important;
        }}
        [data-baseweb="select"] [data-baseweb="tag"] {{
            background-color: {control_border} !important;
            color: {control_text} !important;
        }}
        [data-baseweb="select"] svg {{
            fill: {palette["text"]};
        }}
        [data-testid="stAlert"] {{
            background: {palette["surface"]} !important;
            border: 1px solid {palette["border"]};
            color: {palette["text"]} !important;
        }}
        [data-testid="stAlert"] * {{
            color: {palette["text"]} !important;
        }}
        [data-testid="stFileUploader"],
        [data-testid="stFileUploader"] section,
        [data-testid="stFileUploader"] small,
        [data-testid="stFileUploader"] button {{
            background: {palette["surface"]} !important;
            color: {palette["text"]} !important;
            border-color: {palette["border"]} !important;
        }}
        [data-testid="stFileUploader"] * {{
            color: {palette["text"]} !important;
        }}
        [data-testid="stRadio"] [data-baseweb="radio"] > div:first-child {{
            background: {palette["surface"]} !important;
            border-color: {palette["border"]} !important;
        }}
        [data-testid="stRadio"] [data-baseweb="radio"] > div:first-child > div {{
            background: {palette["accent"]} !important;
        }}
        [data-testid="stRadio"] input[type="radio"] {{
            accent-color: {palette["accent"]} !important;
        }}
        [data-testid="stTooltipContent"] {{
            background: {palette["surface"]} !important;
            color: {palette["text"]} !important;
        }}
        [data-testid="stTabs"] button[role="tab"][aria-selected="true"] {{
            color: {palette["accent"]};
        }}
        .hotspot-warning,
        .hotspot-warning * {{
            background: #c62828 !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }}
        .hotspot-info,
        .hotspot-info * {{
            background: #c62828 !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_warning(message):
    st.markdown(
        "<div class='hotspot-warning' style='background:#c62828;color:#fff;"
        "padding:.85rem 1rem;border-radius:.75rem;font-weight:600'>"
        f"{escape(message)}</div>",
        unsafe_allow_html=True,
    )


def show_info(message):
    st.markdown(
        "<div class='hotspot-info' style='background:#c62828;color:#fff;"
        "padding:.85rem 1rem;border-radius:.75rem;font-weight:600'>"
        f"{escape(message)}</div>",
        unsafe_allow_html=True,
    )


def show_success(message):
    st.markdown(
        "<div class='hotspot-info' style='background:#c62828;color:#fff;"
        "padding:.85rem 1rem;border-radius:.75rem;font-weight:600'>"
        f"{escape(message)}</div>",
        unsafe_allow_html=True,
    )


def toggle_display_mode(account_type, username):
    accounts = st.session_state.database.data[
        "users" if account_type == "user" else "businesses"
    ]
    account = accounts.get(username)
    if account is None:
        st.session_state.theme_switch_error = "Could not update display mode."
        return

    next_theme = "Light" if account.get("visual_theme") == "Dark" else "Dark"
    if not st.session_state.database.set_visual_theme(
        account_type, username, next_theme
    ):
        st.session_state.theme_switch_error = "Could not update display mode."
        return
    st.session_state.pop("theme_switch_error", None)
    save_and_refresh()


def render_display_mode_button(account_type, username, theme):
    next_theme = "Light" if theme == "Dark" else "Dark"
    st.sidebar.button(
        f"Switch to {next_theme} mode",
        key=f"display_mode_toggle_{account_type}_{username}",
        on_click=toggle_display_mode,
        args=(account_type, username),
    )
    if error := st.session_state.pop("theme_switch_error", None):
        st.sidebar.error(error)


def initialize_state():
    # The JSON database is the permanent source of truth.
    if "database" not in st.session_state:
        st.session_state.database = HotspotDatabase()
        users, posts = st.session_state.database.load_data()
        st.session_state.users = users
        st.session_state.posts = posts
    st.session_state.database.ensure_social_fields()
    st.session_state.users = st.session_state.database.get_users()
    if "username" not in st.session_state:
        st.session_state.username = None
    if "business_username" not in st.session_state:
        st.session_state.business_username = None


def save_and_refresh():
    """Save changes immediately and refresh the in-memory Streamlit data."""
    database = st.session_state.database
    database.save_data()
    st.session_state.users = database.get_users()
    st.session_state.posts = database.get_posts()


def show_authentication():
    st.title("HOTSPOT")
    st.caption("Find your next favorite restaurant.")
    customer_tab, business_tab = st.tabs(["Customer", "Business owner"])

    with customer_tab:
        sign_in_tab, sign_up_tab = st.tabs(["Sign in", "Create account"])

        with sign_in_tab:
            with st.form("sign_in_form"):
                username = st.text_input("Username").strip()
                password = st.text_input("Password", type="password").strip()
                submitted = st.form_submit_button("Sign in", type="primary")
            if submitted:
                if not st.session_state.database.authenticate_user(username, password):
                    st.error("Account not found or password is incorrect.")
                else:
                    st.session_state.username = username
                    st.session_state.business_username = None
                    st.rerun()

        with sign_up_tab:
            signup_restaurants = hotspot.get_restaurants_in_city("Cancun")
            restaurant_names = [restaurant.name for restaurant in signup_restaurants]
            with st.form("sign_up_form"):
                new_username = st.text_input(
                    "Choose a username",
                    help="Usernames must be unique across customer and business accounts.",
                ).strip()
                new_password = st.text_input(
                    "Choose a password",
                    type="password",
                    help="Use at least 5 characters.",
                ).strip()
                favorites = st.multiselect(
                    "Choose exactly five Cancun favorites",
                    restaurant_names,
                )
                privacy = st.radio(
                    "Account privacy",
                    ["Public", "Private"],
                    horizontal=True,
                    help="Public accounts accept follow requests immediately. Private accounts require your approval.",
                )
                submitted = st.form_submit_button("Create account", type="primary")
            if submitted:
                if len(favorites) != 5:
                    st.error("Choose exactly five favorite restaurants.")
                else:
                    created, message = st.session_state.database.create_user(
                        new_username, new_password, favorites, privacy
                    )
                    if not created:
                        st.error(message)
                    else:
                        save_and_refresh()
                        st.session_state.username = new_username
                        st.session_state.business_username = None
                        st.success(f"Welcome to HOTSPOT, {new_username}!")
                        st.rerun()

    with business_tab:
        st.caption("Manage your restaurant's HOTSPOT business profile.")
        business_sign_in, business_sign_up = st.tabs(
            ["Business sign in", "Create business account"]
        )
        with business_sign_in:
            with st.form("business_sign_in_form"):
                business_username = st.text_input("Business username")
                business_password = st.text_input(
                    "Password", type="password", key="business_sign_in_password"
                )
                submitted = st.form_submit_button("Sign in as business", type="primary")
            if submitted:
                if not st.session_state.database.authenticate_business(
                    business_username, business_password
                ):
                    st.error("Business account not found or password is incorrect.")
                else:
                    st.session_state.business_username = business_username.strip()
                    st.session_state.username = None
                    st.rerun()

        with business_sign_up:
            city_options = hotspot.get_available_cities()
            with st.form("business_sign_up_form"):
                business_username = st.text_input(
                    "Choose a business username",
                    help="Usernames must be unique across customer and business accounts.",
                )
                business_password = st.text_input(
                    "Choose a password", type="password",
                    key="business_sign_up_password",
                    help="Use at least 5 characters.",
                )
                restaurant_name = st.text_input("Restaurant name")
                cuisine = st.text_input("Cuisine served")
                city = st.selectbox("City", city_options)
                address = st.text_input("Restaurant address")
                description = st.text_area("About your restaurant")
                phone = st.text_input("Phone number (optional)")
                email = st.text_input("Business email (optional)")
                website = st.text_input("Website (optional)")
                submitted = st.form_submit_button(
                    "Create business account", type="primary"
                )
            if submitted:
                created, message = st.session_state.database.create_business(
                    business_username,
                    business_password,
                    restaurant_name,
                    cuisine,
                    city,
                    address,
                    description,
                    phone,
                    email,
                    website,
                )
                if not created:
                    st.error(message)
                else:
                    st.session_state.business_username = business_username.strip()
                    st.session_state.username = None
                    st.success(f"Welcome to HOTSPOT, {restaurant_name}!")
                    st.rerun()

def restaurant_card(restaurant, username):
    with st.container(border=True):
        st.subheader(restaurant.name)
        st.caption(f"{restaurant.cuisine} - {restaurant.rating:.1f}/5")
        business_match = st.session_state.database.find_business(
            restaurant.name, hotspot.restaurant_cities.get(restaurant.name)
        )
        if business_match:
            business_username, _ = business_match
            with st.expander("Restaurant profile & posts"):
                show_business_profile(business_username, username)
        else:
            st.caption("Restaurant owner profile coming soon.")


def restaurant_names_in_city(city):
    names = {
        restaurant.name for restaurant in hotspot.get_restaurants_in_city(city)
    }
    names.update(
        business["restaurant_name"]
        for business in st.session_state.database.data["businesses"].values()
        if business["city"].casefold() == city.casefold()
    )
    return sorted(names, key=str.casefold)


def show_business_profile(business_username, viewer):
    business = st.session_state.database.data["businesses"][business_username]
    st.markdown(f"### {business['restaurant_name']}")
    st.caption(f"{business['cuisine']} · {business['city']}")
    if business["address"]:
        st.write(business["address"])
    if business["description"]:
        st.write(business["description"])
    user = st.session_state.users[viewer]
    follow_label = (
        "Following"
        if business_username in user["following_businesses"]
        else "Follow restaurant"
    )
    if st.button(follow_label, key=f"follow_business_{business_username}_{viewer}"):
        changed, message = st.session_state.database.toggle_business_follow(
            viewer, business_username
        )
        save_and_refresh()
        st.success(message) if changed else st.error(message)
        st.rerun()
    st.caption(f"{len(business['followers'])} followers")

    owned_posts = [
        post for post in st.session_state.posts
        if post.get("author_type") == "business"
        and post.get("business_username") == business_username
    ]
    community_posts = [
        post for post in st.session_state.posts
        if post.get("author_type") != "business"
        and post.get("restaurant", "").casefold()
        == business["restaurant_name"].casefold()
        and post.get("city", "").casefold() == business["city"].casefold()
    ]
    owner_tab, community_tab = st.tabs(["From the restaurant", "Community posts"])
    with owner_tab:
        if owned_posts:
            for post in reversed(owned_posts):
                render_post(post, viewer, "business_profile_owner")
        else:
            show_info("The restaurant hasn't posted yet.")
    with community_tab:
        if community_posts:
            for post in reversed(community_posts):
                render_post(post, viewer, "business_profile_community")
        else:
            show_info("No community posts about this restaurant yet.")


def show_aha_moment(recommendation):
    """Show the public-rating versus personalized-score comparison."""
    restaurant, scores, result, warnings, hotspot_score = recommendation

    st.subheader("The Aha! Moment")
    st.write(
        "A restaurant can have a great public rating, but that does not automatically "
        "make it the best choice for you. HOTSPOT combines your preferences, trust, "
        "and decision friction to create a personalized score."
    )

    public_score = restaurant.rating / 5
    personal_score = hotspot_score / 100

    public_column, hotspot_column = st.columns(2)
    with public_column:
        st.markdown("#### Public opinion")
        st.metric("Restaurant rating", f"{restaurant.rating:.1f}/5")
        st.progress(public_score)
        st.caption("Based on the restaurant's rating in the HOTSPOT database.")

    with hotspot_column:
        st.markdown("#### Your HOTSPOT result")
        st.metric("Personalized HOTSPOT Score", f"{hotspot_score:.1f}/100")
        st.progress(personal_score)
        st.caption("Calculated using trust, taste match, and decision friction.")

    if result == "Recommended":
        show_success(
            f"HOTSPOT recommends {restaurant.name}: it has a rating of "
            f"{restaurant.rating:.1f}/5 and matches the preference rule."
        )
    else:
        show_warning(
            f"{restaurant.name} is not marked as recommended by the basic rule. "
            "A high public rating alone is not enough."
        )

    st.markdown("#### What is behind your score?")
    trust_col, taste_col, friction_col = st.columns(3)
    trust_col.metric("Trust Score", scores["Trust Score"])
    taste_col.metric("Taste Match", scores["Taste Match"])
    friction_col.metric("Decision Friction", scores["Decision Friction"])

    st.progress(scores["Trust Score"] / 100, text="Trust")
    st.progress(scores["Taste Match"] / 100, text="Taste match")
    st.progress(scores["Decision Friction"] / 100, text="Decision friction (lower is better)")

    with st.container(border=True):
        st.markdown("### Hidden Truth")
        st.write(
            "The highest-rated restaurant is not always the restaurant that fits you "
            "best. HOTSPOT looks beyond the public rating: it checks whether the cuisine "
            "matches your favorites, learns from your previous ratings, considers "
            "recommendation sources, and can add trust when your friends have rated "
            "the same restaurant positively. It also considers how difficult the "
            "decision may be."
        )
        friend_bonus = scores["Friend Trust Bonus"]
        if scores["Trusted Friends"]:
            friend_names = ", ".join(
                f"{friend} ({rating:g}/5)"
                for friend, rating in scores["Trusted Friends"]
            )
            show_info(
                f"Your trusted friends add +{friend_bonus} trust points: {friend_names}."
            )
        elif friend_bonus:
            show_info(f"Your trusted-friend bonus is +{friend_bonus} trust points.")
        else:
            st.caption(
                "No trusted-friend bonus was added for this restaurant. Connect with "
                "friends and rate restaurants to make this part of the system useful."
            )
        st.caption(
            "The HOTSPOT Score is calculated as the average of Trust Score, Taste "
            "Match, and 100 minus Decision Friction."
        )

    for warning in warnings:
        show_warning(warning.removeprefix("WARNING: "))


def show_discover(username):
    st.title("Personalized recommendations")
    cities = hotspot.get_available_cities()
    city = st.selectbox("Choose a city", cities, key="discover_city")
    recommendations = hotspot.generate_city_recommendations(
        username, city, st.session_state.users
    )
    if not recommendations:
        show_info("There are no new recommendations in this city.")
        return

    # The highest HOTSPOT-scoring restaurant is the featured Aha! example.
    show_aha_moment(recommendations[0])

    st.divider()
    st.subheader("Your top recommendations")
    for restaurant, scores, result, warnings, hotspot_score in recommendations[:5]:
        with st.container(border=True):
            st.subheader(restaurant.name)
            st.caption(
                f"{restaurant.cuisine} - Restaurant rating "
                f"{restaurant.rating:.1f}/5 - {result}"
            )
            trust, taste, friction, overall = st.columns(4)
            trust.metric("Trust Score", scores["Trust Score"], help="Score out of 100")
            taste.metric("Taste Match", scores["Taste Match"], help="Score out of 100")
            friction.metric(
                "Decision Friction",
                scores["Decision Friction"],
                help="Score out of 100; lower is better",
            )
            overall.metric("HOTSPOT Score", f"{hotspot_score:.1f}", help="Score out of 100")
            if scores["Trusted Friends"]:
                friend_names = ", ".join(
                    f"{friend} ({rating:g}/5)"
                    for friend, rating in scores["Trusted Friends"]
                )
                st.write(
                    f"Friend trust bonus: +{scores['Friend Trust Bonus']} "
                    f"from {friend_names}"
                )
            for warning in warnings:
                show_warning(warning.removeprefix("WARNING: "))


def show_browse():
    st.title("Browse restaurants")
    city = st.selectbox("City", hotspot.get_available_cities(), key="browse_city")
    city_restaurants = hotspot.get_restaurants_in_city(city)
    cuisines = ["All cuisines"] + sorted(
        {restaurant.cuisine for restaurant in city_restaurants}
        | {
            business["cuisine"]
            for business in st.session_state.database.data["businesses"].values()
            if business["city"].casefold() == city.casefold()
        }
    )
    selected_cuisine = st.selectbox("Cuisine", cuisines)
    query = st.text_input("Search by restaurant name").strip().casefold()
    filtered = [
        restaurant
        for restaurant in city_restaurants
        if (selected_cuisine == "All cuisines" or restaurant.cuisine == selected_cuisine)
        and query in restaurant.name.casefold()
    ]
    st.caption(f"{len(filtered)} restaurants")
    for restaurant in filtered:
        with st.container(border=True):
            restaurant_card(restaurant, st.session_state.username)
    known_names = {restaurant.name.casefold() for restaurant in city_restaurants}
    additional_businesses = [
        (business_username, business)
        for business_username, business
        in st.session_state.database.data["businesses"].items()
        if business["city"].casefold() == city.casefold()
        and business["restaurant_name"].casefold() not in known_names
        and query in business["restaurant_name"].casefold()
        and (
            selected_cuisine == "All cuisines"
            or business["cuisine"] == selected_cuisine
        )
    ]
    if additional_businesses:
        st.subheader("HOTSPOT business profiles")
        for business_username, business in additional_businesses:
            with st.container(border=True):
                with st.expander(
                    f"{business['restaurant_name']} · {business['cuisine']}"
                ):
                    show_business_profile(
                        business_username, st.session_state.username
                    )


def show_ratings(username):
    st.title("Rate a restaurant")
    city = st.selectbox("City", hotspot.get_available_cities(), key="rating_city")
    restaurants = restaurant_names_in_city(city)
    with st.form("rating_form"):
        restaurant_name = st.selectbox(
            "Restaurant", restaurants
        )
        rating = st.select_slider(
            "Your rating",
            options=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
            value=4,
        )
        submitted = st.form_submit_button("Save rating", type="primary")
    if submitted:
        saved = st.session_state.database.save_rating(
            username, restaurant_name, rating
        )
        if saved:
            save_and_refresh()
            show_success(f"Saved {rating:g}/5 for {restaurant_name}.")
        else:
            show_warning("Could not save this rating. Please sign in again.")
        if rating >= 3.5:
            show_info("This rating qualifies as a trusted rating.")

    st.subheader("My ratings")
    ratings = st.session_state.users[username]["ratings"]
    if ratings:
        for name, value in ratings.items():
            st.write(f"**{name}** - {value:g}/5")
    else:
        show_info("You haven't rated any restaurants yet.")


def render_post(post, viewer, placement):
    with st.container(border=True):
        if post.get("author_type") == "business":
            business = st.session_state.database.data["businesses"].get(
                post.get("business_username", post["username"]), {}
            )
            st.markdown(
                "<p style='color:#d32f2f;font-size:.75rem;font-weight:700;"
                "margin-bottom:.2rem'>BY OWNER</p>",
                unsafe_allow_html=True,
            )
            author = business.get("restaurant_name", post["username"])
        else:
            author = f"@{post['username']}"
        st.markdown(f"**{author}** | {post['restaurant']} ({post['city']})")
        st.write(post["caption"])
        if post["media_type"] == "Photo":
            st.image(post["media"], caption=post["media_name"])
        else:
            st.video(post["media"])
        likes = post.get("likes", [])
        if viewer is not None:
            if st.button(
                f"{'♥' if viewer in likes else '♡'}  {len(likes)}",
                key=f"like_post_{placement}_{post['id']}_{viewer}",
            ):
                changed, message = st.session_state.database.like_post(
                    viewer, post["id"]
                )
                if changed:
                    save_and_refresh()
                    st.rerun()
                st.error(message)
        else:
            st.caption(f"♥ {len(likes)}")


def show_searched_profile(viewer, profile_username):
    profile = st.session_state.users[profile_username]
    with st.container(border=True):
        st.subheader(f"@{profile_username}'s profile")
        viewer_user = st.session_state.users[viewer]
        if profile_username in viewer_user["following"]:
            if st.button("Unfollow", key=f"unfollow_profile_{profile_username}"):
                changed, message = st.session_state.database.unfollow_user(
                    viewer, profile_username
                )
                save_and_refresh()
                st.session_state.notice = message
                st.rerun()
        elif profile_username in viewer_user["outgoing_follow_requests"]:
            if st.button("Cancel follow request", key=f"cancel_profile_follow_{profile_username}"):
                st.session_state.database.cancel_follow_request(viewer, profile_username)
                save_and_refresh()
                st.rerun()
        else:
            follow_label = (
                "Request to follow"
                if profile.get("privacy", "Public") == "Private"
                else "Follow"
            )
            if st.button(follow_label, key=f"follow_profile_{profile_username}"):
                changed, message = st.session_state.database.follow_user(
                    viewer, profile_username
                )
                if changed:
                    st.session_state.notice = message
                else:
                    st.error(message)
                save_and_refresh()
                st.rerun()

        is_private = profile.get("privacy", "Public") == "Private"
        if is_private and profile_username not in viewer_user["following"]:
            show_info("This account is private. Follow them to see their full profile.")
            return

        friends_col, followers_col, following_col = st.columns(3)
        friends_col.metric("Friends", len(profile["friends"]))
        followers_col.metric("Followers", len(profile["followers"]))
        following_col.metric("Following", len(profile["following"]))

        st.markdown("#### Top five restaurants")
        if profile["top_restaurants"]:
            for position, restaurant_name in enumerate(
                profile["top_restaurants"], start=1
            ):
                restaurant = hotspot.get_restaurant_by_name(restaurant_name)
                if restaurant is not None:
                    st.write(
                        f"{position}. **{restaurant.name}** - "
                        f"{restaurant.cuisine}, {restaurant.rating:.1f}/5"
                    )
        else:
            st.write("No favorite restaurants yet.")

        st.markdown("#### Ratings")
        if profile["ratings"]:
            for restaurant_name, rating in profile["ratings"].items():
                st.write(f"**{restaurant_name}** - {rating:g}/5")
        else:
            st.write("No ratings yet.")

        posts = [
            post for post in st.session_state.posts
            if post.get("username") == profile_username
        ]
        st.markdown("#### Posts")
        if posts:
            for post in reversed(posts):
                render_post(post, viewer, "searched_profile")
        else:
            st.write("No posts yet.")


def latest_friend_activities(username):
    users = st.session_state.users
    posts = st.session_state.posts
    activities = []

    for friend in users[username]["friends"]:
        friend_user = users.get(friend)
        if friend_user is None:
            continue

        candidates = [
            (event, index)
            for index, event in enumerate(friend_user.get("activity", []))
        ]
        logged_ratings = {
            event.get("entity")
            for event, _ in candidates
            if event.get("type") == "rating"
        }
        for index, (restaurant, rating) in enumerate(
            friend_user.get("ratings", {}).items()
        ):
            if restaurant not in logged_ratings:
                candidates.append(
                    (
                        {
                            "description": f"Rated {restaurant} {rating:g}/5",
                            "created_at": None,
                        },
                        len(candidates) + index,
                    )
                )

        for index, post in enumerate(posts):
            if post.get("username") == friend and not post.get("created_at"):
                candidates.append(
                    (
                        {
                            "description": (
                                f"Shared a post about {post.get('restaurant', 'a restaurant')}"
                            ),
                            "created_at": None,
                        },
                        index,
                    )
                )

        if not candidates:
            continue
        latest, order = max(
            candidates,
            key=lambda item: (
                bool(item[0].get("created_at")),
                item[0].get("created_at") or "",
                item[1],
            ),
        )
        activities.append((friend, latest, order))

    return sorted(
        activities,
        key=lambda item: (
            bool(item[1].get("created_at")),
            item[1].get("created_at") or "",
            item[2],
        ),
        reverse=True,
    )


def show_social(username):
    st.title("HOTSPOT Social")
    feed_tab, restaurant_tab, my_posts_tab, create_tab = st.tabs(
        ["Feed", "Restaurant feed", "My posts", "Create a post"]
    )
    posts = st.session_state.posts

    with feed_tab:
        if posts:
            for post in reversed(posts):
                render_post(post, username, "social_feed")
        else:
            show_info("There are no posts yet.")

    with restaurant_tab:
        city = st.selectbox("City", hotspot.get_available_cities(), key="feed_city")
        restaurant_name = st.selectbox(
            "Restaurant",
            restaurant_names_in_city(city),
            key="feed_restaurant",
        )
        business_match = st.session_state.database.find_business(restaurant_name, city)
        if business_match:
            business_username, _ = business_match
            with st.container(border=True):
                show_business_profile(business_username, username)
        matching_posts = [
            post for post in reversed(posts)
            if post["restaurant"].casefold() == restaurant_name.casefold()
            and post["city"].casefold() == city.casefold()
        ]
        if matching_posts:
            for post in matching_posts:
                render_post(post, username, "restaurant_feed")
        else:
            show_info("No posts for this restaurant yet.")

    with my_posts_tab:
        own_posts = [post for post in reversed(posts) if post["username"] == username]
        if own_posts:
            for post in own_posts:
                render_post(post, username, "my_posts")
        else:
            show_info("You haven't created any posts yet.")

    with create_tab:
        cities = hotspot.get_available_cities()
        city = st.selectbox("City", cities, key="post_city")
        media_type = st.radio("Media type", ["Photo", "Video"], horizontal=True)
        with st.form("create_post_form"):
            restaurant_name = st.selectbox(
                "Restaurant",
                restaurant_names_in_city(city),
                key="post_restaurant",
            )
            media_file = st.file_uploader(
                "Choose a photo or video",
                type=["jpg", "jpeg", "png"] if media_type == "Photo" else ["mp4", "mov"],
            )
            caption = st.text_area("Caption")
            submitted = st.form_submit_button("Publish post", type="primary")
        if submitted:
            if media_file is None:
                st.error("Choose a photo or video before publishing.")
            else:
                post = {
                    "username": username,
                    "restaurant": restaurant_name,
                    "city": city,
                    "media_type": media_type,
                    "media_name": media_file.name,
                    "media": media_file.getvalue(),
                    "caption": caption.strip() or "No caption.",
                }
                st.session_state.database.create_post(post)
                save_and_refresh()
                st.success("Your post is live and saved to the JSON database.")


def show_activity(username):
    st.title("Activity")
    notifications = st.session_state.users[username].get("notifications", [])
    if not notifications:
        show_info("You're all caught up!")
        return

    if any(not notification.get("read", False) for notification in notifications):
        if st.button("Mark all as read"):
            st.session_state.database.mark_notifications_read(username)
            save_and_refresh()
            st.rerun()

    for index, notification in reversed(list(enumerate(notifications))):
        with st.container(border=True):
            actor = notification.get("actor")
            description = notification.get("description", "New activity.")
            if (
                isinstance(actor, str)
                and actor in st.session_state.users
                and actor != username
            ):
                st.button(
                    f"@{actor}",
                    key=f"activity_actor_{notification.get('id', index)}",
                    on_click=open_activity_profile,
                    args=(actor,),
                )
                remainder = description.replace(f"@{actor}", "", 1).strip()
                if remainder:
                    if notification.get("read", False):
                        st.write(remainder)
                    else:
                        st.markdown(f"**{remainder}**")
            else:
                if notification.get("read", False):
                    st.write(description)
                else:
                    st.markdown(f"**{description}**")
            try:
                created_at = datetime.fromisoformat(
                    notification["created_at"]
                ).astimezone()
            except (KeyError, ValueError):
                st.caption("Recent activity")
            else:
                st.caption(created_at.strftime("%b %d, %I:%M %p"))


def open_activity_profile(username):
    st.session_state.activity_profile_to_view = username
    st.session_state.main_navigation = "Profile"


def show_friends(username):
    st.title("Friends & connections")
    user = st.session_state.users[username]
    friends_count, followers_count, following_count = st.columns(3)
    friends_count.metric("Friends", len(user["friends"]))
    followers_count.metric("Followers", len(user["followers"]))
    following_count.metric("Following", len(user["following"]))

    st.subheader("Latest activity")
    latest_activities = latest_friend_activities(username)
    if not user["friends"] or not latest_activities:
        show_info("Looks like you're all caught up!")
    else:
        for friend, activity, _ in latest_activities[:10]:
            with st.container(border=True):
                st.markdown(f"**@{friend}**")
                st.write(activity["description"])
                if activity.get("created_at"):
                    try:
                        activity_time = datetime.fromisoformat(
                            activity["created_at"]
                        ).astimezone()
                    except ValueError:
                        st.caption("Recent activity")
                    else:
                        st.caption(activity_time.strftime("%b %d, %I:%M %p"))
                else:
                    st.caption("Earlier activity")

    search_tab, requests_tab = st.tabs(["Find people", "Follow requests"])

    with search_tab:
        search_query = st.text_input("Search by username", key="friend_username_search_mobile")
        matches = (
            st.session_state.database.search_users(search_query, username)
            if search_query.strip()
            else []
        )
        selected_profile = st.session_state.get("friend_profile_to_view")
        if selected_profile and selected_profile not in matches:
            st.session_state.pop("friend_profile_to_view", None)
        if search_query.strip():
            if not matches:
                show_info("No matching usernames found.")
            else:
                with st.container(border=True):
                    for match in matches[:8]:
                        if st.button(
                            f"@{match}",
                            key=f"username_suggestion_mobile_{match}",
                            use_container_width=True,
                        ):
                            st.session_state.friend_profile_to_view = match
                            st.rerun()

        profile_to_view = st.session_state.get("friend_profile_to_view")
        if profile_to_view in st.session_state.users and profile_to_view != username:
            show_searched_profile(username, profile_to_view)
            if st.button("Close profile", key="close_searched_profile_mobile"):
                del st.session_state["friend_profile_to_view"]
                st.rerun()

    with requests_tab:
        incoming = user["incoming_follow_requests"]
        if incoming:
            for requester in incoming:
                col1, col2, col3 = st.columns([3, 1, 1])
                col1.write(f"**@{requester}** requested to follow you")
                if col2.button("Accept", key=f"accept_follow_mobile_{requester}"):
                    st.session_state.database.accept_follow_request(username, requester)
                    save_and_refresh()
                    st.rerun()
                if col3.button("Decline", key=f"decline_follow_mobile_{requester}"):
                    st.session_state.database.decline_follow_request(username, requester)
                    save_and_refresh()
                    st.rerun()
        else:
            show_info("You have no follow requests.")

    if "notice" in st.session_state:
        st.success(st.session_state.pop("notice"))

    if user["friends"]:
        st.subheader("Trusted friend ratings")
        for friend in user["friends"]:
            trusted_ratings = {
                name: rating
                for name, rating in st.session_state.users[friend]["ratings"].items()
                if rating >= 3.5
            }
            with st.expander(f"{friend} - {len(trusted_ratings)} trusted ratings"):
                if trusted_ratings:
                    for name, rating in trusted_ratings.items():
                        st.write(f"{name}: {rating:g}/5")
                else:
                    st.write("No trusted ratings yet.")

def show_profile(username):
    profile_to_view = st.session_state.get("activity_profile_to_view")
    if profile_to_view in st.session_state.users and profile_to_view != username:
        show_searched_profile(username, profile_to_view)
        if st.button("Back to my profile", key="back_from_activity_profile_mobile"):
            st.session_state.pop("activity_profile_to_view", None)
            st.rerun()
        return

    st.title("My profile")
    user = st.session_state.users[username]
    st.subheader("App appearance")
    visual_theme = st.selectbox(
        "Choose your visuals",
        ["Light", "Dark", "Colorful"],
        index=["Light", "Dark", "Colorful"].index(
            user.get("visual_theme", "Light")
        ),
        key="customer_visual_theme",
    )
    if visual_theme != user.get("visual_theme", "Light"):
        if st.session_state.database.set_visual_theme(
            "user", username, visual_theme
        ):
            save_and_refresh()
            st.rerun()

    st.subheader("Privacy")
    privacy = st.radio(
        "Account privacy",
        ["Public", "Private"],
        index=0 if user.get("privacy", "Public") == "Public" else 1,
        horizontal=True,
        key="profile_privacy_mobile",
        help="Private accounts require you to approve friend requests.",
    )
    if privacy != user.get("privacy", "Public"):
        if st.session_state.database.set_privacy(username, privacy):
            save_and_refresh()
            st.success(f"Your account is now {privacy.lower()}.")
            st.rerun()
    first, second, third = st.columns(3)
    first.metric("Friends", len(user["friends"]))
    second.metric("Ratings", len(user["ratings"]))
    third.metric("Favorite restaurants", len(user["top_restaurants"]))
    st.subheader("Your top five")
    for position, restaurant_name in enumerate(user["top_restaurants"], start=1):
        restaurant = hotspot.get_restaurant_by_name(restaurant_name)
        if restaurant is not None:
            st.write(
                f"{position}. **{restaurant.name}** - "
                f"{restaurant.cuisine}, {restaurant.rating:.1f}/5"
            )


def show_business_dashboard(username):
    business = st.session_state.database.data["businesses"][username]
    st.title(business["restaurant_name"])
    st.caption("Business dashboard")
    overview_tab, posts_tab, community_tab, activity_tab = st.tabs(
        ["Restaurant profile", "Your posts", "Community posts", "Activity"]
    )
    with overview_tab:
        st.subheader("Restaurant profile")
        st.write(f"**Cuisine:** {business['cuisine']}")
        st.write(f"**City:** {business['city']}")
        if business["address"]:
            st.write(f"**Address:** {business['address']}")
        if business["description"]:
            st.write(business["description"])
        if business["phone"]:
            st.write(f"**Phone:** {business['phone']}")
        if business["email"]:
            st.write(f"**Email:** {business['email']}")
        if business["website"]:
            st.write(f"**Website:** {business['website']}")
        st.metric("Followers", len(business["followers"]))
        st.subheader("App appearance")
        visual_theme = st.selectbox(
            "Choose your visuals",
            ["Light", "Dark", "Colorful"],
            index=["Light", "Dark", "Colorful"].index(
                business.get("visual_theme", "Light")
            ),
            key="business_visual_theme",
        )
        if visual_theme != business.get("visual_theme", "Light"):
            if st.session_state.database.set_visual_theme(
                "business", username, visual_theme
            ):
                save_and_refresh()
                st.rerun()

    owned_posts = [
        post for post in st.session_state.posts
        if post.get("author_type") == "business"
        and post.get("business_username") == username
    ]
    with posts_tab:
        with st.form("business_post_form"):
            media_type = st.radio(
                "Media type", ["Photo", "Video"], horizontal=True,
                key="business_post_media_type",
            )
            media_file = st.file_uploader(
                "Choose a photo or video",
                type=["jpg", "jpeg", "png"]
                if media_type == "Photo"
                else ["mp4", "mov"],
                key="business_post_media",
            )
            caption = st.text_area("Caption", key="business_post_caption")
            submitted = st.form_submit_button("Publish restaurant post", type="primary")
        if submitted:
            if media_file is None:
                st.error("Choose a photo or video before publishing.")
            else:
                created = st.session_state.database.create_business_post(
                    username,
                    {
                        "media_type": media_type,
                        "media_name": media_file.name,
                        "media": media_file.getvalue(),
                        "caption": caption.strip() or "No caption.",
                    },
                )
                if created:
                    save_and_refresh()
                    st.success("Your restaurant post is live.")
                    st.rerun()
                else:
                    st.error("Business account not found.")
        if owned_posts:
            st.subheader("Published by your restaurant")
            for post in reversed(owned_posts):
                render_post(post, None, "business_dashboard_owner")
        else:
            show_info("Your restaurant hasn't posted yet.")

    with community_tab:
        community_posts = [
            post for post in st.session_state.posts
            if post.get("author_type") != "business"
            and post.get("restaurant", "").casefold()
            == business["restaurant_name"].casefold()
            and post.get("city", "").casefold() == business["city"].casefold()
        ]
        if community_posts:
            for post in reversed(community_posts):
                render_post(post, None, "business_dashboard_community")
        else:
            show_info("No customer posts about your restaurant yet.")

    with activity_tab:
        notifications = business.get("notifications", [])
        if notifications:
            for notification in reversed(notifications):
                st.write(notification["description"])
        else:
            show_info("No activity yet.")


def main():
    apply_mobile_styles()
    initialize_state()
    business_username = st.session_state.business_username
    if business_username is not None:
        business = st.session_state.database.data["businesses"][business_username]
        theme = business.get("visual_theme", "Light")
        apply_visual_theme(theme)
        st.sidebar.title("HOTSPOT Business")
        st.sidebar.caption(f"Signed in as **{business_username}**")
        render_display_mode_button("business", business_username, theme)
        if st.sidebar.button("Log out"):
            st.session_state.business_username = None
            st.rerun()
        show_business_dashboard(business_username)
        return

    username = st.session_state.username
    if username is None:
        apply_visual_theme("Dark")
        show_authentication()
        return
    theme = st.session_state.users[username].get("visual_theme", "Light")
    apply_visual_theme(theme)

    st.sidebar.title("HOTSPOT")
    st.sidebar.caption(f"Signed in as **{username}**")
    st.sidebar.caption("Data storage: local JSON file")
    render_display_mode_button("user", username, theme)
    notifications = st.session_state.users[username].get("notifications", [])
    unread_count = sum(not notification.get("read", False) for notification in notifications)
    activity_label = "Activity" if unread_count == 0 else f"Activity 🔔 {unread_count}"
    navigation_options = [
        "Social",
        "Discover",
        "Browse restaurants",
        "Rate a restaurant",
        activity_label,
        "Friends",
        "Profile",
    ]
    current_page = st.session_state.get("main_navigation", "Social")
    if current_page.startswith("Activity"):
        st.session_state.main_navigation = activity_label
    elif current_page not in navigation_options:
        st.session_state.main_navigation = "Social"
    page = st.sidebar.radio(
        "Navigate",
        navigation_options,
        key="main_navigation",
    )
    if st.sidebar.button("Log out"):
        st.session_state.username = None
        st.rerun()

    if page == "Discover":
        show_discover(username)
    elif page == "Browse restaurants":
        show_browse()
    elif page == "Rate a restaurant":
        show_ratings(username)
    elif page == "Social":
        show_social(username)
    elif page.startswith("Activity"):
        show_activity(username)
    elif page == "Friends":
        show_friends(username)
    else:
        show_profile(username)


if __name__ == "__main__":
    main()
