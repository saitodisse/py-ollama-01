def main():
    import sys

    # Retrieve numbers from command line arguments
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except IndexError:
        num1 = 1
        num2 = 1
        print("No numbers provided. Using default values: 1 and 1.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Calculate the sum
    result = num1 + num2

    # Print the result
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()