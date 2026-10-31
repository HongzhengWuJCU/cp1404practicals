usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
get_user_name=input("please input your name: ")
if get_user_name in usernames:
    print("Access granted")
else:
    print("Access denied")


number=int(input("Input what you want number: "))
while number >0:
    numbers=[]
    for i in range(number):
        get_number=int(input(f"Number {i+1}: "))
        numbers.append(get_number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)/number}")
    number = int(input("Input what you want number: "))