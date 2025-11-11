# simple_interest.py
# Program to calculate Simple Interest

import sys

def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest given principal, rate, and time."""
    return (principal * rate * time) / 100

if __name__== "__main__":
    print("=== Simple Interest Calculator ===")

    try:
        # Case 1: Arguments passed through command line
        if len(sys.argv) == 4:
            p = float(sys.argv[1])
            r = float(sys.argv[2])
            t = float(sys.argv[3])

        # Case 2: No arguments passed, take input from user
        else:
            p = float(input("Enter the principal amount: "))
            r = float(input("Enter the rate of interest (%): "))
            t = float(input("Enter the time (in years): "))
        print("===Program parameters ===")
        print("princapal Amount:", p)
        print("rate of Interest:", r)
        print("Time in years:", t)
        # Calculate and display the result
        interest = calculate_simple_interest(p, r, t)
        print(f"\nThe Simple Interest = {  interest :.2f}")

    except ValueError:
        print("Error: Please enter valid numeric values.")
    except Exception as e:
        print("An error occurred:", e)