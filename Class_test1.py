students = []


class Student:
    def __init__(self, name, id = 3):
        self.name = name
        print("Name = ",name," ID = ",id)

    def name_capitalize(self):
        print(self.name.capitalize())



student = Student("dinesh")
student.name_capitalize()