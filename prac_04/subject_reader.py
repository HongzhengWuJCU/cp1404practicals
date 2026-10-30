"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data = load_data(FILENAME)
    max_name_length=max(len(i[1]) for i in data)
    max_people_length=max(len(str(i[2])) for i in data)
    for line in data:
        print(f"{line[0]} is taught by {line[1]:<{max_name_length}} and has {line[2]:<{max_people_length}} students")


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    lists=[]
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        data = [parts[0], parts[1], int(parts[2])]
        lists.append(data)# See if that worked
    input_file.close()
    return lists

main()