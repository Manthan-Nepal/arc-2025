
# # 1. solution

marks = [ 10, 20, 30, 40, 50, 65]

def average_marks(marks: list) -> float:
    return sum(marks) / len(marks)

print(average_marks(marks))

# # 2. solution

def table_multiplication(number: int) -> None:
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

table_multiplication(5)


# 3. solution

def is_palindrome(x: int) -> str:
    if x < 0:
        return f"Negative numbers, {x} are not palindromes."
    elif str(x) == str(x)[::-1]:
        return f"The number {x} is a palindrome."
    else:
        return f"The number {x} is not a palindrome."

print(is_palindrome(121))

# 4. solution

list_of_numbers = [10, 70, 30, 40, 50]

def greatest_number(list_of_numbers: list) -> int:
    return max(list_of_numbers)

print(greatest_number(list_of_numbers))


# 5. solution

x = [1, 2, 3, 1, 10, 8]

def find_peaks(x: list) -> list:
     peaks = []

     for i in range(1, len(x) - 1):
        if x[i] > x[i - 1] and x[i] > x[i + 1]:
            peaks.append(x[i])

     return peaks

print("Peaks:", find_peaks(x))


# 6. solution

def count_vowels(text:str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

input_data = input("Enter a string: ")
print("Number of vowels:", count_vowels(input_data))

# 7. solution

def sum_of_digits(number: int) -> int:
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum

input_number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(input_number))

# 8. solution

def roman_to_integer(s: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    for i in range(len(s)):
        # If this is not the last character and current is less than next, subtract it
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    return total

roman_numeral = "LVIII"
result = roman_to_integer(roman_numeral)
print(f"roman to integer of {roman_numeral} is {result}")

# 9. solution

def isValid(s: str) -> bool:
    # Map closing brackets to their matching opening brackets
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    stack = []
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            return False
    
    return len(stack) == 0

print(isValid("()[]{}"))   
      
# 10. solution

def character_frequency(s: str) -> dict:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage:
s = "hello"
result = character_frequency(s)
print(result)


# 11. solution 

grades_dict = {
        "Alice": {"Math": 90, "Science": 85, "Literature": 88},
        "Bob": {"Math": 78, "Science": 82, "Literature": 80},
        "Charlie": {"Math": 92, "Science": 91, "Literature": 94}
}

for student, subjects in grades_dict.items():
    total = sum(subjects.values())
    num_subjects = len(subjects)
    percentage = total / num_subjects
    print(f"{student}: {percentage:.2f}")






