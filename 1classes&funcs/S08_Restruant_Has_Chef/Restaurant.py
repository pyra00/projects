from chef import chef 
class Restaurant:
    def __init__(self):
        self.chef=chef()
    def serve_food(self):
        self.chef.cook()
        print('Food is served.')