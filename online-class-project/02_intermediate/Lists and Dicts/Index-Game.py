def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Element at index {index} modified to: {new_value}"
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    if 0 <= start <= end <= len(lst):
        return lst[start:end]
    else:
        return "Invalid slice range."

def main():
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Welcome to the Index Game!")
    print("Your list is:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            try:
                idx = int(input("Enter the index to access: "))
                print(access_element(my_list, idx))
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '2':
            try:
                idx = int(input("Enter the index to modify: "))
                new_val = input("Enter the new value: ")
                print(modify_element(my_list, idx, new_val))
                print("Updated list:", my_list)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '3':
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print("Sliced list:", result)
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
