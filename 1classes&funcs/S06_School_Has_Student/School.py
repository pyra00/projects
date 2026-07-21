from Student import Student
class School:
    def __init__(self):
        self.student=Student()
    def begin_class(self):
        print('Class begins.')
        self.student.study()
        