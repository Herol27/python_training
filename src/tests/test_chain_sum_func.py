import pytest

from src.functions.chain_sum import chain_sum


@pytest.mark.parametrize("x, y, z, expected_result", [(1, 2, 1, 4),
                                                       (2, 2, 4, 8),
                                                       (9, 3, 3, 15),
                                                       (0, 1, 15, 16),
                                                       (-12, 22, 13, 23),
                                                       (0, -27, 69, 42)])
def test_chain_sum(x, y, z, expected_result):
    assert chain_sum(x)(y)(z)() == expected_result
