# class Dog:
#     species = "Canis familiaris"
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f"{self.name} is {self.age} years old"
#
#
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
# buddy = Dog("Buddy", 9)
# miles = Dog("Miles", 4)
# print(buddy.description())
# print(buddy.speak("Woof Woof"))
#
# miles.species="Felis silvestris"
# print(miles.species)


class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

        # print our string object

    def __repr__(self):
        return f"object : {self.string}"
        #return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other


# Driver Code
if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # concatenate String object and a string
    print(string1+' malk')
    print('foo\'bar')
