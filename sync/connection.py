from abc import ABC, abstractmethod


class AbstractConnection(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def cursor(self):
        pass