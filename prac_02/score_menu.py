def main():
    # Control the whole thing
    score = float(input("Enter your score: "))
    print("(G)et a valid score (must be 0-100 inclusive)\n"
    "(P)rint result (copy or import your function to determine the result from score.py)\n"
    "(S)how stars (this should print as many stars as the score)\n"
    "(Q)uit")
    choice=input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(score)
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print(get_start(score))
        else:
            print("Invalid choice and input error message")
        print("(G)et a valid score (must be 0-100 inclusive)\n"
              "(P)rint result (copy or import your function to determine the result from score.py)\n"
              "(S)how stars (this should print as many stars as the score)\n"
              "(Q)uit")
        choice = input(">>> ").upper()
    print("farewell")


def get_start(score: float):
    # create as many stars as the score
    return "*" * int(score)


def get_valid_score(score: float) -> float:
    # get valid score
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter your score: "))
    return score


def get_result(score: float) -> str:
    # get final result
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()