from abc import abstractmethod

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def happyBday(self):
        # fazer anaiversário
        self.setAge(self.__age + 1)
        print(f'{self.getName()} tem {self.getAge()} anos.')

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

    def setName(self, nome):
        self.__name = nome

    def setAge(self, idade):
        self.__age = idade

    def setGender(self, sexo):
        self.__gender = sexo
    
    @abstractmethod
    def profile(self):
        pass

# classe pessoa 