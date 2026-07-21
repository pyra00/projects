from Teacher import Teacher 
class Classroom:
    def __init__(self):
        self.teacher =Teacher()
    def start_lesson(self):
        self.teacher.teach()
 