from Doctor import Doctor
class Hospital:
    def __init__(self):
        self.doctor=Doctor()
    def provide_care(self):
        self.doctor.treat()