def rightmost_set_bit(n):
    if n == 0:
        return None  # No set bits in 0
    return n & -n  # Isolates the rightmost set bit

# Main program
try:
    number = int(input("Enter a number: "))  # Take input from the user
    result = rightmost_set_bit(number)

    if result:
        print(f"The rightmost set bit of {number} is: {result} (binary: {bin(result)})")
    else:
        print("The number has no set bits.")
except ValueError:
    print("Please enter a valid integer.")
