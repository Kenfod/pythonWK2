def main():
    # Accept user input to create a list of integers
    num_list = []
    while True:
        try:
            num = input("Enter an integer (or 'q' to Quit): ")
            if num.lower() == 'q':
                break
            num_list.append(int(num))
        except ValueError:
            print("Invalid input. Please enter an integer or 'q'.")

    # Compute the sum of all integers in the list
    list_sum = sum(num_list)
    print("Integer list entered is ",num_list)
    # Print the sum
    print("Sum of the integers is ", list_sum)

if __name__ == "__main__":
    main()
