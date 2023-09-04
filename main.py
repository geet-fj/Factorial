# main.py
from factorial_calculator import calculate_factorial

def main():
    num = int(input("Enter a number: "))
    result = calculate_factorial(num)
    print(f"The factorial of {num} is {result}")

if __name__ == "__main__":
    main()


# Sourcegraph Access Token
# sgp_08852bf5bb08477f9fdeff7371dddd6f493b06c9
