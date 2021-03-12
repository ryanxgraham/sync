from abc import ABC, abstractmethod


class AbstractConnection(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def cursor(self):
        pass

    @abstractmethod
    def insert(self, row):
        pass

    @abstractmethod
    def delete(self, row):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def create_table(self, table_name):
        pass

    @abstractmethod
    def get_table(self, table_name):
        pass

    @abstractmethod
    def drop_table(self, table_name):
        pass

    @abstractmethod
    def export(self, table_name):
        pass
    