import pytest

from src.functions.integer_to_roman import int_to_roman


@pytest.mark.parametrize("input_number, expected_result", [(4, "IV"),
                                                           (8, "VIII"),
                                                           (15, "XV"),
                                                           (16, "XVI"),
                                                           (23, "XXIII"),
                                                           (42, "XLII")])
def test_integer_to_roman(input_number, expected_result):
    assert int_to_roman(input_number) == expected_result
