# notes from lection
students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']

print(students)

item = 'Ivan'

if item in students:
    print(f"{item} is in the list!")
else:
    print(f"Sorry, {item} not found(")

# list comprehension

a = [0] * 5
b = [0 for i in range(5)]
c = [i * i for i in range(5)]
d = [int(i) for i in input().split()]