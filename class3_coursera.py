class test2:
    x = 0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name, "constructed")
    def val(self):
        self.x += 1
        print(self.name,'x = ',self.x)


s = test2('Dinesh')
s.val()

p = test2('Kumar')
s.val()
p.val()
p.val()
s.val()

