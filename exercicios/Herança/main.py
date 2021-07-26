from Person import Person
from Student import Student
from Employee import Employee
from Teacher import Teacher

p1 = Person('Maria Nonata', 71, 'Femninino')
s1 = Student('Celenny Cristhyne', 19, 'Feminino', 123456, 'Ciencia da Computação')
s2 = Student('Isabeli Tâmara', 22, 'Feminino', 125670, 'Fisioterapia')
e1 = Employee('Antonio Joaquim', 39, 'Masculino', 'Tecnologia da informação', True)
t1 = Teacher('Maria das graças', 44, 'Feminino', 'Pedagogia', 1000 )

t1.profile()
s2.cancelMatri()
s2.profile()