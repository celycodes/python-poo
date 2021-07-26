from Student import Student

class Scholarshipstudent(Student):
    def __init__(self, name, age, gender, matriculation, course, scholarship):
        super().__init__(name,age, gender, matriculation, course)
        self.__scholarship = scholarship

    def getScholarship(self):
        return self.__scholarship

    def setScholarship(self, n):
        self.__scholarship = n

    def renewScholarship(self):
        # renovar bolsa de estudos
        return f'Renovando a bolsa de estudos de {self.getName()}'

    def payMatri(self):
        # pagar matrícula
        return f'{self.getName()} é bolsista! Pagamentto facilitado...'

    def profile(self):
         print(f'<<<<<<< PROFILE >>>>>>>\nName: {self.getName()}\nAge: {self.getAge()}\nGender: {self.getGender()}\nMatriculation: {self.getMatri()}\nCouse: {self.getCourse()}\nScholarshpip: {self.getScholarship()}')

b1 = Scholarshipstudent('Celenny', 19, 'F', 1123, 'Ciencia da computação', 100092)

b1.profile()