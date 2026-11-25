import time


def search_restaurant(restaurants, search_name):
    start_time = time.perf_counter()

    for restaurant in restaurants:
        if restaurant.name.lower() == search_name.lower():
            print("\nRestaurant found!")
            print("Name:", restaurant.name)
            print("Cuisine:", restaurant.cuisine)
            print("Rating:", restaurant.rating)

            end_time = time.perf_counter()
            print("Search completed in:", end_time - start_time, "seconds")
            return

    print("\nRestaurant not found.")