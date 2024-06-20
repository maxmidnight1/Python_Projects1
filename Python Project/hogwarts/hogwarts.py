
# Dict = Dictionary

# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slitherin", "patronus": None}
]

# print(students["Hermione"])

for student in students:
    print(student["name"], student["house"], student["patronus"],  sep=", ")

"""
print(students[0])
print(students[1])
print(students[2])
"""

# for student in students:
#    print(student)

# for i in range(len(students)):
#    print(i + 1, students[i])