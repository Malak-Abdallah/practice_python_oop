# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width


rec1=rectangle(10,15)
print("first rectangle area= {}".format(rec1.area()))
rec2=rectangle(82,14).area()
print("second rectangle area= {}".format(rec2))

