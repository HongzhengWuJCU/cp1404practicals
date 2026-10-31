strings=input(">>> (Input indefinite set of strings) ")
while strings !="":
    print(strings)
    lists=[item.strip() for item in strings.split(",") ]
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

