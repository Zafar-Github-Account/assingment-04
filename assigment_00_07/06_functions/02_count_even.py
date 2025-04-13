def count_even(lst):
    """ Returns the number of even numbers in the list. """
    count = 0  # Initialize a counter to keep track of even numbers
    for num in lst:  # Iterate over each number in the list
        if num % 2 == 0:  # Check if the number is even
            count += 1  # If it's even, increment the count
    print(count)  # Print the count of even numbers

def get_list_of_ints():
    """ Reads in integers until the user presses enter and returns the resulting list. """
    lst = []  # Initialize an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")  # Prompt for input
    
    while user_input != "":  # Keep going as long as user input is not empty
        lst.append(int(user_input))  # Convert input to integer and append to the list
        user_input = input("Enter an integer or press enter to stop: ")  # Ask for next input
    
    return lst  # Return the populated list of integers

def main():
    lst = get_list_of_ints()  # Get the list of integers from user
    count_even(lst)  # Call count_even to print the number of even integers

if __name__ == '__main__':
    main()
