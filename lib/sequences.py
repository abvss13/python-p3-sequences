# sequences.py

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    print(fibonacci_sequence[:length])

# Additional function to practice changing case in strings
def capitalize_string(input_string):
    return input_string.capitalize()

# Additional function to practice list manipulation
def reverse_and_sort_list(input_list):
    reversed_list = list(reversed(input_list))
    reversed_list.sort()
    return reversed_list
