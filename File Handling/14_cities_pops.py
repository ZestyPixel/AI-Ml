import json

cities = {
    "Delhi": 19000000,
    "Mumbai": 20000000,
    "Chennai": 11000000
}

with open("File Handling/cities.json", "w") as file:
    json.dump(cities, file, indent=4)

with open("File Handling/cities.json", "r") as file:
    cities = json.load(file)

print("\nCities and populations:")
for city, population in cities.items():
    print(city, ":", population)

new_city = input("\nEnter new city name: ")
new_population = int(input("Enter population: "))

cities[new_city] = new_population

with open("File Handling/cities.json", "w") as file:
    json.dump(cities, file, indent=4) #Indent for better readability

print("City added successfully!")
