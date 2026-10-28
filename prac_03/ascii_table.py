LOWER = 33
UPPER = 127

def valid_ascii(prompt):
    value = int(input(prompt))
    while value < LOWER or value > UPPER:
        print("The input is wrong, please input again")
        value = int(input(prompt))
    return value

for i in range(LOWER, UPPER + 1):
    print(f"{i} {chr(i)}")

character = input("Enter a character: ")
while len(character) != 1 or not LOWER <= ord(character) <= UPPER:
    print("Please enter one character within the ASCII range.")
    character = input("Enter a character: ")

print(f"The ASCII code for {character} is {ord(character)}")

number = valid_ascii("Enter a number between 33 and 127: ")
print(f"The character for {number} is {chr(number)}")