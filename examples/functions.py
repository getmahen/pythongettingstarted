students = []

def addStudent(firstName, lastName, id=123):
    students.append({"id": id, "firstName": firstName, "lastName": lastName})


def printStudent(student, *args):
    print("Student firstName is: {0} and LastName is: {1} and Id: {2}".format(
        student["firstName"], student["lastName"], student["id"]))
    print(args)


def save_file(student):
    try:
        f = open("student.txt", "a")
        f.write(student["firstName"] + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("student.txt", "r")
        for studentFirstName in f.readlines():
          addStudent(firstName=studentFirstName, lastName="Rek", id=123)
        f.close()
    except Exception:
        print("Could not read file")

# addStudent(firstName="mahi", lastName="Rek", id=123)
# printStudent(students[0], "loves Python", None, True)

id = raw_input("Enter Student Id: ")
firstName = raw_input("Enter First Name: ")
lastName = raw_input("Enter Last Name: ")

save_file({"firstName" : firstName, "lastName" : lastName})
read_file()
#addStudent(firstName=firstName, lastName=lastName, id=id)

for student in students:
  printStudent(student, "loves Python", None, True)