import random

def main():
    # Generate 15 random Fahrenheit values
    with open("temps_input.txt", "w") as out_file:
        for i in range(15):
            fahrenheit_value = random.randint(-200, 200)
            out_file.write(f"{fahrenheit_value}\n")
    with open("temps_input.txt", "r") as in_file:
        with open("temps_output.txt", "w") as out_file:
            for i in range(15):
                fahrenheit_value = float(in_file.readline())
                celsius_value = convert_celsius(fahrenheit_value)
                out_file.write(f"{celsius_value}\n")

def convert_celsius(value) -> float:
    # Convert Fahrenheit to Celsius
    celsius = 5 / 9 * (value - 32)
    return celsius

main()