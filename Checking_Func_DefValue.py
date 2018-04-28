students = []


def add_student(name, st_id = 3):
    st_temp = {"name":name,"st_id":st_id}
    students.append(st_temp)


def print_student():
    print(students)


add_student("Dinesh",989)
add_student("Kumar")
add_student("Hogwarts",888)
print_student()
