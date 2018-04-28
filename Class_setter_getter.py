
class Student:
    def name_setter(self, name, st_id=10):
        self.name = name
        self.st_id = st_id

    def name_getter(self):
        print("Name = ", self.name, "\n", "ID = ", self.st_id)


student = Student()
student.name_setter("Dinesh", 9)
student.name_getter()