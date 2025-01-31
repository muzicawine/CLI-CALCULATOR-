import math

def main():
    print("Welcome to the CLI Calculator!")
    print("Select an operation by entering the corresponding number:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (\u221a)")
    print("7. Logarithm (log)")
    print("8. Trigonometric Functions (sin, cos, tan)")
    print("9. Quit")

    while True:
        try:
            choice = input("\nEnter your choice: ")

            if choice == "9":
                print("Exiting the calculator. Goodbye!")
                break

            if choice in ["1", "2", "3", "4", "5"]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif choice == "2":
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif choice == "3":
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif choice == "4":
                    if num2 != 0:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
                elif choice == "5":
                    print(f"Result: {num1} ^ {num2} = {num1 ** num2}")

            elif choice == "6":
                num = float(input("Enter the number: "))
                if num >= 0:
                    print(f"Result: \u221a{num} = {math.sqrt(num)}")
                else:
                    print("Error: Square root of a negative number is not allowed.")

            elif choice == "7":
                num = float(input("Enter the number: "))
                base = input("Enter the base (default is e): ")
                if base == "":
                    print(f"Result: log({num}) = {math.log(num)}")
                else:
                    base = float(base)
                    print(f"Result: log base {base} of {num} = {math.log(num, base)}")

            elif choice == "8":
                print("Choose a trigonometric function:")
                print("1. Sine (sin)")
                print("2. Cosine (cos)")
                print("3. Tangent (tan)")

                trig_choice = input("Enter your choice: ")
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)

                if trig_choice == "1":
                    print(f"Result: sin({angle}) = {math.sin(radians)}")
                elif trig_choice == "2":
                    print(f"Result: cos({angle}) = {math.cos(radians)}")
                elif trig_choice == "3":
                    print(f"Result: tan({angle}) = {math.tan(radians)}")
                else:
                    print("Invalid trigonometric function choice.")

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Error: Invalid input. Please enter numerical values where required.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
