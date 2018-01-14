students = []

class Student:
  #pass: is a keyword # this is just a way to indicate that this class does nothing. Just a placeholder
  #self: Is similar to "this" keyword in Javascript

  #This is a class level static variable
  school_name = "SpringField Elementary"

  # This is a Constructor
  def __init__(self, name, student_id=332):
    self.student_name = name
    self.student_id = student_id
    students.append(self)  

  # This is a method override of native str() function
  def __str__(self):
    return "Student Name: " + self.student_name

  def get_name_capitalized(self):
    return self.student_name.capitalize()

  # To access the class level static variable inside a method, we still need "self"
  def get_school_name(self):
    return self.school_name