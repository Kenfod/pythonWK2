def main():
    # Accept user input to create the first set of integers
    set1 = create_set("first")

    # Accept user input to create the second set of integers
    set2 = create_set("second")

    # Create a new set containing only the elements that are common to both sets
    common_elements = set1.intersection(set2)

    # Print the common elements
    print("\nCommon Elements in Both Sets:", common_elements)

def create_set(name):
      #Function to create a set of integers based on user input.

    input_str = input(f"Enter space-separated integers for the {name} set: ")
    integers = map(int, input_str.split())
    return set(integers)

if __name__ == "__main__":
    main()
