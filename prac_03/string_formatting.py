number=int(input(">>> "))
for i in range(number+1):
    print(f"2 ^ {i:2} is {2**i:>{len(str(2**number))}}")