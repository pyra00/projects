from student import Student

class Classrom:
    def __init__(self):
        self.student = Student()
    def start_class(self):
        print("Class is starting...")
        self.student.say_hello()