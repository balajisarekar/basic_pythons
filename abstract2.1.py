#case 2.1 /2 abstract method
from abc import*
class Vehicle(ABC):
    @abstractmethod
    def noofvechial(self):
        pass
class Bus(Vehicle):pass
b=Bus()  #2