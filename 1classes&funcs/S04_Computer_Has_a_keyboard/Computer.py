from Keyboard import Keyboard
class Computer:
    def __init__(self):
        self.keyboard = Keyboard()
    def work(self):
        self.keyboard.type()
        print('Working on the computer.')
        