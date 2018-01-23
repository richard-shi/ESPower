
# TODO: Implement the GPIO reading

class Controller:

    def __init__(self, power=False):
        print("Controller startup")
        self.power = power

    def status(self):
        return self.power

    def change(self, new_status):
        self.power = new_status
        return self.power


