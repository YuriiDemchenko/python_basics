import pytest
from calc import calculator


@pytest.mark.parametrize(
    "num1, num2, operator, expected_result",
    [(2, 2, "+", 4), (2, 2, "*", 4), (4, 2, "/", 2), (10, 5, "-", 5)],
)
def test_calc(num1, num2, operator, expected_result):
    result = calculator(num1, num2, operator)
    assert result == expected_result


@pytest.mark.parametrize(
    "num1, num2, operator, expected_exception",
    [(2, 0, "/", ZeroDivisionError), (2, "1", "/", TypeError)],
)
def test_calc_with_error(num1, num2, operator, expected_exception):
    with pytest.raises(expected_exception):
        calculator(num1, num2, operator)
