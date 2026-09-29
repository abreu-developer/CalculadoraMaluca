from abc import ABC, abstractmethod


class DriveHandlerInterface(ABC):
    
    @abstractmethod
    def standard_derivation(self, numbers: list[float]) -> float:
            pass
        
    @abstractmethod
    def variance(self, numbers: list[float]) -> float:
        pass