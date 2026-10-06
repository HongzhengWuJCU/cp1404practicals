import random

print("Welcome to the Gopher Population Simulator!")
population=1000
print(f"Starting population: {population}")
year =1
while year!=10 and population>0:
    born_population=int(random.uniform(10,20)*population*0.01)
    died_population=int(random.uniform(5,25)*population*0.01)
    population=population+born_population-died_population
    year+=1
    print(f"{born_population} gophers were born. {died_population} died.")
    print(f"Population: {population}")
    print(f"Year {year}")