class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #__str__ to define output
    def __str__(self):
        return str(self.a) + "/" + str(self.b)

    def __add__(self, other):
        tmpAbove = (self.a * other.b) + (other.b * self.b)
        tmpBelow = self.b * other.b
        return str(tmpAbove) +"/" + str(tmpBelow)


# it have not to of class Fraction
if __name__ == "__main__":
    obj1 = Fraction(2,3)
    #use __str__
    print("Fraction 1: ", obj1)

    obj2 = Fraction(5,4)
    #use __str__
    print("Fraction 2: ", obj2)

    #use __add__
    print("Case 1: ", obj1.__add__(obj2))
    print("Case 2: ", obj1 + obj2)