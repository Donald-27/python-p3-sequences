#!/usr/bin/env python3

def print_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]

    # Generate the Fibonacci sequence until it reaches the desired length
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Sum of the last two numbers
        fibonacci_sequence.append(next_number)

    # Print the Fibonacci sequence up to the nth length
    print(fibonacci_sequence[:n])

# Example usage
print_fibonacci(10)
