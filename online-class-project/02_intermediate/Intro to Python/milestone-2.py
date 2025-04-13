def main():
    # Dictionary to store the gravity constants for each planet (as a percentage of Earth's gravity)
    planet_gravity = {
        "Mercury": 37.6,
        "Venus": 88.9,
        "Mars": 37.8,
        "Jupiter": 236.0,
        "Saturn": 108.1,
        "Uranus": 81.5,
        "Neptune": 114.0
    }

    # List of planets
    planets = list(planet_gravity.keys())

    # Display the list of planets with numbers
    print("Available planets:")
    for index, planet in enumerate(planets, 1):
        print(f"{index}. {planet}")

    # Get the weight on Earth from the user
    earth_weight = float(input("\nEnter a weight on Earth: "))

    # Ask the user to select a planet by number
    while True:
        try:
            planet_choice = int(input("\nEnter the number of the planet you want: "))
            if 1 <= planet_choice <= len(planets):
                planet_name = planets[planet_choice - 1]
                break
            else:
                print("Please enter a valid number corresponding to a planet.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get the gravity constant for the selected planet
    gravity = planet_gravity[planet_name]

    # Calculate the equivalent weight on the selected planet
    planet_weight = earth_weight * (gravity / 100)

    # Print the equivalent weight rounded to 2 decimal places
    print(f"\nThe equivalent weight on {planet_name}: {round(planet_weight, 2)}")

if __name__ == "__main__":
    main()
