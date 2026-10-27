file_name=input("Input your file name: ")

out_file=open(f"{file_name}.txt", "w")

out_file.close()

with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())   # 17
    second_number = int(in_file.readline())  # 42

print(first_number + second_number)  # 59


total=0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total+=int(line)

print(total)