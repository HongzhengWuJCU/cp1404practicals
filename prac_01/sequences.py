def is_even(number):
# This function is decide whether the number is even or add
    return number % 2 == 0

x=int(input("Enter the number for x but x must lower than y: "))
y=int(input("Enter the number for y but y must higher than x: "))
print("(1): Show the even numbers from x to y\n"
"(2): Show the odd numbers from x to y\n"
"(3): Show the squares of the numbers from x to y\n"
"(4): Exit the program")
choice=input(">>> ")
while choice!="4":
    if choice =="1":
        print("Show the even number from x to y")
        for i in range(x,y+1):
            if is_even(i):
                print(i, end=" ")
    elif choice =="2":
        print("Show the odd numbers from x to y")
        for i in range(x,y+1):
            if not is_even(i):
                print(i, end=" ")
    elif choice =="3":
        print("Show the squares of the numbers from x to y")
        for i in range(x,y+1):
            print(i*i, end=" ")
    else:
        print("Invalid Choice")
    print("\n(1): Show the even numbers from x to y\n"
"(2): Show the odd numbers from x to y\n"
"(3): Show the squares of the numbers from x to y\n"
"(4): Exit the program")
    choice = input(">>> ")
print("Finished")
