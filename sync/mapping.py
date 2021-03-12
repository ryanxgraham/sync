from sync.data_type import DataType, StrType, IntType, FloatType, BoolType
from abc import ABC, abstractmethod
import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format='%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(msg)s'
)    

logger = logging.getLogger(__name__)

class Mapping(ABC):
    """
    Abstract base class for mapping database data types to internal data types for easy conversion
    """
    @abstractmethod
    def to_flavor(self, data_type: DataType) -> str:
        """
        Abstract method for converting internal data types to a specific databases data types
        """
        pass

    @abstractmethod
    def to_internal(self, s: str) -> DataType:
        """
        Abstract method for converting a specific database data type to internal data types.
        """
        pass
        
class PostgresMapping(Mapping):
    """
    Mapping of internal data types to postgres data types
    """
    TO_DB_MAP = {
        StrType: 'text',
        IntType: 'bigint',
        FloatType: 'numeric',
        BoolType: 'boolean'}

    FROM_DB_MAP = {
        'text': StrType,
        'smallint': IntType,
        'integer': IntType,
        'bigint': IntType,
        'decimal': FloatType,
        'double': FloatType,
        'numeric': FloatType,
        'boolean': BoolType
    }
    
    def to_flavor(self, data_type: DataType) -> str:
        """
        Convert from internal data type to postgres data types
        """
        if data_type not in self.TO_DB_MAP:
            logger.error('%s does not exist in TO_DB_MAP', data_type)
            raise TypeError(f'Invalid data type {data_type}.')
        return self.TO_DB_MAP[data_type]

    def to_internal(self, s: str) -> DataType:
        """
        Convert from postgres data type to internal data type
        """
        if s not in self.FROM_DB_MAP:
            logger.error('%s does not exist in FROM_DB_MAP', s)
            raise TypeError(f'Invalid data type {s}.')            
        return self.FROM_DB_MAP[s]