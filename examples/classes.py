students = []

class Student:
  #pass: is a keyword # this is just a way to indicate that this class does nothing. Just a placeholder
  #self: Is similar to "this" keyword in Javascript

  #This is a class level static variable
  school_name = "SpringField Elementary"

  #This is a Constructor
  def __init__(self, name, student_id=332):
    self.student_name = name
    self.student_id = student_id
    students.append(self)  

  #This is a method override of native str() function
  def __str__(self):
    return "Student Name: " + self.student_name

  def get_name_capitalized(self):
    return self.student_name.capitalize()

  # To access the class level static variable inside a method, we still need "self"
  def get_school_name(self):
    return self.school_name


#This is how to derive or inherit from a base/parent class (In this case base/parent class is Student)
class HighSchoolStudent(Student):
  
  school_name = "SpringField High school"

  def get_school_name(self):
    return "This is a High School " + self.school_name

  def get_name_capitalized(self):
    original_value = super().get_name_capitalized()
    return original_value + "-HS"



james = HighSchoolStudent("james")
print(james.get_name_capitalized())
print(james.get_school_name())
print("High School name: {0}".format(HighSchoolStudent.school_name))


# mark = Student("Mark")
# print(mark)
# print(mark.get_name_capitalized())

# print("School name is: " + Student.school_name)

# for student in students:
#   print("Student Name in list is: {0} and Student Id is: {1} belongs to school: {2}".format(student.student_name, student.student_id, student.school_name))