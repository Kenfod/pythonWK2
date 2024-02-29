def main():
    # Create an empty dictionary to store person's information
    person_info = {}

    # Ask the user for input and store the information in the dictionary
    person_info['name'] = input("Enter your name: ")
    person_info['age'] = input("Enter your age: ")
    person_info['favorite_color'] = input("Enter your favorite color: ")

    # Print the dictionary containing person's information
    print("\nPerson's Information:")
    for key, value in person_info.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
