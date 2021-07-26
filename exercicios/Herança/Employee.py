from Person import Person

class Employee(Person):
    def __init__(self, name, age, gender, sector, working):
        super().__init__(name, age, gender)
        self.__sector = sector
        self.__working = working

    def getSector(self):
        return self.__sector

    def getWork(self):
        return self.__working

    def setSector(self, setor):
        self.__sector = setor

    def setWork(self, trabalhando):
        self.__working = trabalhando

    def profile(self):
        print(f'<<<<<<< PROFILE >>>>>>>\nName: {self.getName()}\nAge: {self.getAge()}\nGender: {self.getGender()}\nSector: {self.getSector()}\nWorking: {self.getWork()}\n')

    def changeWork(self):
        # mudar de emprego
        self.setWork(False)

# classe funcionário        