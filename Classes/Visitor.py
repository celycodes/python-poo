from Person import Person
class Visitor(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
'''
Vemos a representação de uma herança pobre
ou Herança para Implmentação em que uma classe
filha apenas herda os métodos e atributos porém 
não implementa nada.
* classe Visitor herda de Person 
'''