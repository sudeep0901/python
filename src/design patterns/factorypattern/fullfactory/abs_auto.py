import abc

class AbsAuto(metaclass=abc.ABCMeta):

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self,name):
        self._name = name

        
    @abc.abstractmethod
    def start(self):
        pass
    
    @abc.abstractmethod
    def end(self):
        pass