def get_lst():
    """
    Prompts the user to enter one element of the list at a time
    and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def get_last_element(lst):
    """
    Prints the last element of the list.
    """
    # Using index method
    print(lst[len(lst) - 1])

    # Or more pythonic way:
    # print(lst[-1])

def main():
    lst = get_lst()
    if lst:  # Make sure the list isn't empty
        get_last_element(lst)
    else:
        print("The list is empty.")

if __name__ == '__main__':
    main()
