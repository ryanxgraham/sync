import pytest

from sync.data_type import BoolType, DataType, FloatType, IntType, StrType
from sync.mapping import PostgresMapping


def test_to_flavor():
    mapping = PostgresMapping()
    assert mapping.to_flavor(StrType) == 'text'
    assert mapping.to_flavor(IntType) == 'bigint'

def test_to_internal():
    mapping = PostgresMapping()
    assert mapping.to_internal('text') == StrType
    assert mapping.to_internal('boolean') == BoolType

def test_to_internal_fail_if_mapping_does_not_exist():
    mapping = PostgresMapping()
    with pytest.raises(TypeError):
        mapping.to_internal('real')
