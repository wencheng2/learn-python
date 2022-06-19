#https://www.codecademy.com/courses/learn-python-3/lessons/data-types/exercises/review
#need to complete bonus steps
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
  def get_average(self):
    return sum(score)/len(score)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  def is_passing(self, grade):
    if grade >= minimum_passing:
      return "passing"

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
