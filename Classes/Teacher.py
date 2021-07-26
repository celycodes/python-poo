from Person import Person

class Teacher(Person):
    def __init__(self, name, age, gender, specialty, salary):
        super().__init__(name, age, gender)
        self.__specialty = specialty
        self.__salary = salary

    def getSpecialty(self):
        return self.__specialty

    def getSalary(self):
        return self.__salary

    def setSpecialty(self, materia):
        self.__specialty = materia

    def setSalary(self, salario):
        self.__salary = salario

    def profile(self):
        print(f'<<<<<<< PROFILE >>>>>>>\nName: {self.getName()}\nAge: {self.getAge()}\nGender: {self.getGender()}\nEspecialidade: {self.getSpecialty()}\nSalário: {self.getSalary()}\n')

    def increaseSalary(self, au):
        # receber salario
        self.setSalary(self.__salary + au)

# professor