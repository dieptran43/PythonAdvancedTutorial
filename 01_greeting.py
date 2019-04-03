class Greeting:
    count = 0
    def __init__(self, name):
        self.name = name
        Greeting.count += 1
    
    def say_hi(self):
        print("Hi....", self.name)
    
    def say_bye(self):
        return "Bye..." + self.name

if __name__ == "__main__":
    object_01 = Greeting("Python Advanced Tutorial By IPMan DiepVan")
    object_01.say_hi()
    #we must to declare it by Print
    print("Call say bye function: "+ object_01.say_bye()) 
    print("Count instance of class Greeting 1: ", Greeting.count)

    object_02 = Greeting("Mrs Kim")
    object_02.say_hi()
    #we must to declare it by Print
    print("Call say bye function: "+ object_02.say_bye()) 
    print("Count instance of class Greeting 2: ", Greeting.count)