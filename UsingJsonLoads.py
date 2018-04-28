import json
from pprint import pprint
students = []
show_students = []


def write_file():
    f = open("new1.txt", "a")
    for student in students:
        f.write(json.dumps(student) + "\n")
    f.close()


def read_file():
    fj = json.loads(open("new1.txt"))
    pprint(fj)


def add_student(name, st_id=333):
    students_temp = {"name": name, "id": st_id}
    students.append(students_temp)

while True:
    n = input("Enter Input: ")
    if n == "n":
        write_file()
        read_file()
        break
    else:
        name = input("Enter Name: ")
        stid = int(input("Enter Id: "))
        add_student(name,stid)
