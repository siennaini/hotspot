# HOTSPOT - Sequence Logic
# Unit 6: Sequences, Strings, Indexes, and Files

print("HOTSPOT SEQUENCE ANALYZER")
print("------------------------")

# Restaurant data stored as a string sequence
restaurant_data = "Nicoletta-Italian-4.8"

# Use indexes
print("\nOriginal data:")
print(restaurant_data)

print("\nUsing indexes:")
print("First character:", restaurant_data[0])
print("Last character:", restaurant_data[-1])

# Split the string into parts
parts = restaurant_data.split("-")

restaurant_name = parts[0]
cuisine = parts[1]
rating = parts[2]

print("\nRestaurant Information:")
print("Name:", restaurant_name)
print("Cuisine:", cuisine)
print("Rating:", rating)


# String iteration
print("\nScanning restaurant name:")

for character in restaurant_name:
    print(character)


# Create a restaurant data file
with open("restaurant_data.txt", "w") as file:
    file.write("Sushigo Yaxchilan-Japanese-4.9\n")
    file.write("Nicoletta-Italian-4.8\n")
    file.write("The BurgerOn-Burgers-4.8\n")

print("\nRestaurant data saved.")


# Read and process the file
print("\nHOTSPOT RESTAURANTS:")

with open("restaurant_data.txt", "r") as file:

    for line in file:
        line = line.strip()

        restaurant = line.split("-")

        name = restaurant[0]
        cuisine = restaurant[1]
        rating = restaurant[2]

        print("\nName:", name)
        print("Cuisine:", cuisine)
        print("Rating:", rating)


print("\nSequence analysis complete.")