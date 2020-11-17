from src.stringcalculator import calculator

def test_empty_string_zero():
    assert(calculator.add("")) == 0