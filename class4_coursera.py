class test2:
    x = 0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name, "constructed")
    def val(self):
        self.x += 1
        print(self.name,'x = ',self.x)



class test3(test2):
    points = 0
    def inhe(self):
        self.points += 7
        self.val()
        print("In Inher: ",self.name,"points",self.points)

t = test2("Kumar")
t.val()
te = test3("Dinesh")
te.val()
te.inhe()