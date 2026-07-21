from Engine import Engine 
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print('Car is moving.')