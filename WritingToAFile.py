student = []


def write_file():
    try:
        f = open("records.txt", "a")
        for i in student:
            # print( str(i) )
            f.write(str(i)+"\n")
        f.close()
    except Exception as e:
        print(e)
        print("Failed to write to file")


def add_students(st_name, stu_id=111):
    st_temp = {"name": st_name, "stu_id": stu_id}
    student.append(st_temp)
    print(student)


while True:
    print("Press Yes to continue writing to file: ")
    print("Press No to exit: ")
    n = input("--> ")
    if n in ["No", "n"]:
        write_file()
    elif n in ["Yes", "y"]:
        print("Enter student name and id")
        name = input("name: ")
        st_id = input("id: ")
        add_students(name, st_id)
    else:
        print("Invalid Option chose")

