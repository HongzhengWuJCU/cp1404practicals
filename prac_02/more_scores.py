import random

def main():
    # Generate the file that include the score and result
    number_of_score = int(input("Enter the number of score: "))
    for i in range(number_of_score):
        score=random.randint(0,100)
        result=get_result(score)
        with open("results.txt","a") as out_file:
            out_file.write(f"{score} is {result}\n")

def get_result(score: float):
    # determine what result you get
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()