for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
Question a: count in 10s from 0 to 100
"""
for i in range(0,101,10):
    print(i, end=" ")
print()

"""
Question b: count down from 20 to 1
"""
for i in range(20,0,-1):
    print(i, end=" ")
print()

"""
Question c: print a number of stars.
"""
number_of_stars=int(input("Number of stars: "))
print("*"*number_of_stars)

"""
Question d: print lines of increasing stars.
"""
number_of_stars=int(input("Number of stars: "))
for i in range(1,number_of_stars+1):
    print("*"* i)