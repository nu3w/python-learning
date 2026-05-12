# abstraction: data hiding: complex events hide from users

# example: ATM, car/ bike start process how the engine work, login/ authenticayion SystemError

class Bike:
    key = False
    clutch = False
    acc = False
    
    def start(self):
        self.key = True
        self.clutch = True
        self.acc = True
        print("bike start")
        