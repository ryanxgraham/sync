import logging
import sys
from collections import OrderedDict

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format='%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(msg)s'
)    

logger = logging.getLogger(__name__)

class Schema:
    """
    Class defining table schema field names, data types, primary keys, and references.

    Attributes:

    fields -- An ordered dictioary of field names and associated data types
    primary_keys -- a list of primary keys
    references -- a dictionary of references

    Methods:
    add_field(field_name, data_type)
    edit_field(field_name, new_field_name)
    edit_data_type(field_name, data_type)
    remove_field(field_name)

    """
    def __init__(self, fields: dict, primary_keys: list, references: dict):
        self.fields = OrderedDict(fields.items())
        self.primary_keys = primary_keys
        self.references = references

    def add_field(self, field_name: str, data_type: DataType):
        """
        Add a field_name and data_type to the fields dictionary
        
        Arguments:

        field_name,
        data_type
        """
        if field_name in fields:
            logger.error('Failed to add %s', field_name)
            raise KeyError(f'{field_name} already exists in the schema. To change the field name, use the edit_field method. To change the data type, use the edit_data_type method.', field_name)
        fields[field_name] = data_type
        logger.info('%s with type %s added to fields', field_name, data_type)
        logger.debug('%s', fields)

    def edit_field(self, field_name: str, new_field_name:str):
        """
        Edit the name of a field in the fields dictionary

        Arguments:

        field_name,
        new_field_name
        """
        if field_name not in fields:
            logger.error('Failed to edit %s', field_name)
            raise KeyError(f'{field_name} does not exist in fields.', field_name)
        for _ in range(len(fields)):
            k,v = fields.popitem(False)
            fields[new_field_name if field_name == k else k] = v
        logger.info('%s changed to %s', field_name, new_field_name)
        logger.debug('%s', fields)

    def edit_data_type(self, field_name: str, data_type: DataType):
        """
        Edit the data_type of a field in the fields dictionary.
        
        Arguments:

        field_name,
        data_type
        """
        if field_name not in fields:
            logger.error('Failed to change data_type of field: %s', field_name)            
            raise KeyError(f'{field_name} does not exist in fields', field_name)
        fields[field_name] = data_type
        logger.info(f'{field_name} set to {data_type}', field_name, data_type)

    def remove_field(self, field_name: str):
        """
        Removes a field from the fields dictionary
        
        Arguments:

        field_name
        """
        if field_name not in fields:
            logger.error('Failed to remove %s from fields', field_name)
            raise KeyError(f'{field_name} does not exist in fields', field_name)
        del fields[field_name]
        logger.info(f'Field {field_name} removed', field_name)
        logger.debug(f'{fields}', fields)
