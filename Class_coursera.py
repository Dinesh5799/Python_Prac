class Party:
    x = 0
    def val(self):
        self.x = self.x+1
        print("X = ",self.x)


h = Party()
h.val()
print("Trying To Access: ",h.x)
h.val()
print("Trying To Access: ",h.x)