class Person:
    def __init__(self, name, by, address):
        self.__name = name
        self.__birth_year = by
        self.__address = address
        
    def get_age(self): # getter for the age attribute
        print(f"getting the current age of , {self.__name}")
        age = 2022 - self.__birth_year
        return self.__birth_year
    
    def set_age(self, value):# setter for the age attribute
        self.__birth_year = value
        
        
    def set_birthday(self,value):
        if isintance(value,int) and not (value < 2000):
            self.__birth_year = value
        else:
            raise ValueError("Please give an integer value")
    
        
    
    
p1 = Person("Isaac",45, "Abidjan")
    
print(p1.get_age())


