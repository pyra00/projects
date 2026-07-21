from Battery import Battery

class Phone:
    def __init__(self):
        self.battery=Battery()
    def power_on(self):
        self.battery.charge()
        print('Phone is on.')