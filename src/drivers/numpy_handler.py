import numpy

from .interfaces.driver_handler_interface import DriveHandlerInterface


#gerent numpy
class NumpyHandler(DriveHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy
        
    def standard_derivation(self, numbers: list[float]) -> float:
        return self.__np.std(numbers)