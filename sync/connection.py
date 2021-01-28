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

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @abstractmethod
    @classmethod
    def from_config(cls, config):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def unload(self):
        pass

    
