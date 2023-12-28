import pytest
from sympy import Eq, symbols, solve
from symplyphysics import units, Quantity
from efficiency_from_quantity_of_heat import calculate_eta

def test_calculate_eta():
    temperature_start = Quantity(100, units.degC)
    temperature_end = Quantity(50, units.degC)
    expected_result = Quantity(0.5)
    
    result = calculate_eta(temperature_start, temperature_end)
    
    assert result == expected_result

def test_calculate_eta_invalid_input():
    temperature_start = Quantity(100, units.degC)
    temperature_end = Quantity(100, units.degC)
    
    with pytest.raises(ValueError):
        calculate_eta(temperature_start, temperature_end)