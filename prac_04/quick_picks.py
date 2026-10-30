import random

quick_pick=int(input("How many quick picks you wish to generate: "))
MIN_NUMBER=1
MAX_NUMBER=45
QUICK_PICK_EACH_LINE=6
for i in range(quick_pick):
    numbers=[]
    for j in range(QUICK_PICK_EACH_LINE):
        numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
    numbers.sort()
    for j in range(QUICK_PICK_EACH_LINE):
        print(f"{numbers[j]:>{len(str(MAX_NUMBER))}}", end=" ")
    print()