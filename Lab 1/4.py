class Student:
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
        self.school_record=SchoolRecord()
    def display_name(self):
        print("Name: "+self.name)
    def display_grade(self):
        print("Grade: " + str(self.grade))
    

class SchoolRecord:
    def __init__(self):
        self.grades=[]
    def record_grade(self, grade):
        if 0<=grade<=100:
            self.grades.append(grade)
        else:
            print("Please enter a value between 0 and 100")
    def calculate_gpa(self):
        return sum(self.grades) / len(self.grades)
student=Student("Jake Mecca", 12)
student.school_record.record_grade(86)
student.school_record.record_grade(90)
student.school_record.record_grade(75)
student.school_record.record_grade(99)
print(student.school_record.calculate_gpa())
student.display_name()
student.display_grade()
'''Creating these classes was pretty simple. 
In the first class, I included basic information such as your name
and grade level. The second class includes your grades. Through this
class you could input grades and calculate your GPA.
'''