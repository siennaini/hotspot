# HOTSPOT - Nested Restaurant Finder
# Unit 7: Nested Data

print("HOTSPOT RESTAURANT FINDER")
print("-------------------------")

restaurants = [
    {
        "name": "Sushigo Yaxchilan",
        "cuisine": "Japanese",
        "rating": 4.9,
        "features": ["Sushi", "Delivery", "Good Reviews"]
    },
    {
        "name": "Nicoletta",
        "cuisine": "Italian",
        "rating": 4.8,
        "features": ["Pasta", "Desserts", "Good Reviews"]
    },
    {
        "name": "The BurgerOn",
        "cuisine": "Burgers",
        "rating": 4.8,
        "features": ["Burgers", "Fries", "Takeout"]
    }
]

# First loop: goes through every restaurant
for restaurant in restaurants:

    print("\nRestaurant:", restaurant["name"])
    print("Cuisine:", restaurant["cuisine"])
    print("Rating:", restaurant["rating"])

    print("Features:")

    # Second loop: goes through the features
    # inside each restaurant
    for feature in restaurant["features"]:
        print("-", feature)

    # Conditional inside the loop
    if restaurant["rating"] >= 4.8:
        print("HOTSPOT Status: Highly Recommended")
    else:
        print("HOTSPOT Status: Recommended")

print("\nRestaurant search complete.")