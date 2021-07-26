from Person import Person

class Student(Person):
    def __init__(self, name, age, gender, matriculation, course):
        super().__init__(name, age, gender)
        self.__matriculation = matriculation
        self.__course = course

    def getMatri(self):
        return self.__matriculation

    def getCourse(self):
        return self.__course

    def setMatri(self, n):
        self.__matriculation = n

    def setCourse(self, curso):
        self.__course = curso

    def cancelMatri(self):
        # cancelar matrícula
        self.setMatri(False)
        self.setCourse(False)
        print(f'{self.getName()} sua matrícula foi cancelada com sucesso ...')

    def payMatri(self):
        # pagar matrícula
        print(f'A matricula de {self.getName()} está paga')

    def profile(self):
         print(f'<<<<<<< PROFILE >>>>>>>\nName: {self.getName()}\nAge: {self.getAge()}\nGender: {self.getGender()}\nMatriculation: {self.getMatri()}\nCouse: {self.getCourse()}\n')

# classe estudante