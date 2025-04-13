def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Calculate the weight on Mars (37.8% of Earth's weight)
    mars_weight = earth_weight * 0.378
    
    # Round the result to two decimal places
    mars_weight = round(mars_weight, 2)
    
    # Output the result
    print(f"The equivalent on Mars: {mars_weight}")

if __name__ == "__main__":
    main()
