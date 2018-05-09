students = []
read_students = []



def write_file():
    try:
        f = open("students.txt","a")
        for i in students:
            f.write(str(i)+"\n")
        f.close()
    except Exception as e:
        print("Error writing to file: "+e)



def read_file():
    try:
        f = open("students.txt","r")
        for i in f.readlines():
            read_students.append(i)
        f.close()
    except Exception as e:
        print("Error reading from file: "+e)


def add_students(name,st_id=121):
    st_temp = {"name": name, "id":st_id}
    students.append(st_temp)


def print_readDetails():
    print("Details from file: ")
    for i in read_students:
        print(i)



print("Enter y to write and n to exit: ")
while True:
    n = input("--> ")
    if n == "n":
        write_file()
        read_file()
        print_readDetails()
        break;
    else:
        name = input("Enter name of student: ")
        stid = input("Enter student id: ")
        add_students(name,stid)

