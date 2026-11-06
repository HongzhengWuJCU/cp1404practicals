strings=input(">>> (Input indefinite set of strings) ")
while strings !="":
    print(strings)
    lists=[item.strip() for item in strings.split(",[") ]
    repeat_string=[]
    for line in lists:
        if lists.count(line)>=2:
            repeat_string.append(line)
            lists.remove(line)
    if len(repeat_string)!=0:
        print(f"Strings repeated: { ", ".join(repeat_string)}")
    else:
        print("No repeated strings entered")
    strings = input(">>> (Input indefinite set of strings) ")


def add_memberwise(numbers, other_ones):
    new_numbers=[]
    min_length=min(len(numbers), len(other_ones))
    for i in range(min_length):
        new_numbers.append(numbers[i]+other_ones[i])
    if min_length==len(numbers) and len(numbers) !=len(other_ones):
        new_numbers.append(other_ones[-1])
    elif min_length==len(other_ones) and len(numbers)!=len(other_ones):
        new_numbers.append(numbers[-1])
    return new_numbers

print(add_memberwise([1, 2, 3], [4, 5, 6]))
print(add_memberwise([1, 2, 3, 5], [1, 2, 3]))