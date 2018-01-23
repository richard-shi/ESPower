import machine

class Controller:

    def __init__(self, power=False):
        print("Controller startup")

        # By default off
        self.pin = machine.Pin(2, machine.Pin.OUT)

    def status(self):
        return self.pin.value()

    def change(self, new_status):
        self.pin.value(new_status)



