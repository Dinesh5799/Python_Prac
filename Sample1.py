student = []


def print_students():
    for i in student:
        print(i.title())


def add_student(name):
    student.append(name)


while True:
    print("Enter Yes To Add A Student: ")
    print("Enter No To Quit: ")
    n = input("-->")
    if n=="No":
        print_students()
        break;
    elif n=="Yes":
        stu = input("Enter A Student Name: ")
        add_student(stu)
    else :
        print("Please Choose Between Given Options")
