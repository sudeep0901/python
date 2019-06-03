from .abs_auto import AbsAuto

class NullCar(AbsAuto):
    def __init__(self, car):
        self._carname = car

    def start(self):
        print('unknown car "%s"' % self._carname)        

    def end(self):
        print("Unknowncar ended")