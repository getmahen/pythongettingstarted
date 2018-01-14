from student import Student

# This is how to derive or inherit from a base/parent class (In this case base/parent class is Student)
class HighSchoolStudent(Student):
  
  school_name = "SpringField High school"

  def get_school_name(self):
    return "This is a High School " + self.school_name

  #def get_name_capitalized(self):
    # original_value = super().get_name_capitalized()
    # return original_value + "-HS"