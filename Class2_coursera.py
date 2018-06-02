class test:
    x = 0
    def __init__(self):
        print("I am a constructor")
    def val(self):
        self.x += 1
        print("X = ",self.x)
    def __del__(self):
        print("I am desctructor")


a = test()
a.val()
a.val()
a = 42
print('Value a has: ',a)