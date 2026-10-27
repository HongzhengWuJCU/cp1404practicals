def main():
    file_name=input("Input the file name: ")
    while file_name!="":
        if not is_valid_file(file_name):
            print("The file is exist")
        else:
            print(f"{file_name} has {read_line(file_name)} lines")
        file_name = input("Input the file name: ")

def is_valid_file(prompt):
    try:
        with open(f"{prompt}.txt", "r"):
         return True
    except FileNotFoundError:
        return False

def read_line(prompt):
    lines=0
    with open(f"{prompt}.txt", "r") as in_file:
        for line in in_file:
            lines+=1
        return lines

main()