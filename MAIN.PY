from utils import celsius_to_fahrenheit, greet, is_even, square


def main():
    name = input("Enter your name: ")
    print(greet(name))

    try:
        user_input = float(input("\nEnter a number: "))

        print(f"\n--- Results for {user_input} ---")
        print(f"Square: {square(user_input)}")
        print(f"Is Even: {is_even(int(user_input))}")
        print(f"Equivalent in Fahrenheit: {celsius_to_fahrenheit(user_input):.2f}°F")
    except ValueError:
        print("Error: Please enter a valid numerical value.")


if __name__ == "__main__":
    main()
