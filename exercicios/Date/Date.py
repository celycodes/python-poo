# Class Date
# Atributos - day - month - year
# methods
# exbir a data formatada (aaaa/mm/dd)

class Date:
  def __init__(self, day, month, year):
      self.__day = day
      self.__month = month
      self.__year = year

  def getDay(self):
    return self.__day

  def getMonth(self):
    return self.__month

  def getYear(self):
    return self.__year

  def setDay(self, newDay):
    self.__day = newDay

  def setMonth(self, newMonth):
    self.__month = newMonth

  def setYear(self, newYear):
    self.__year = newYear

  def formatDate(self):
    print(f'{self.getYear()}/{self.getMonth()}/{self.getDay()}')