from sympy import Eq, solve
from symplyphysics import (
    units,
    Quantity,
    Symbol,
    print_expression,
    validate_input,
    validate_output,
)

# Description
## This inequality says that the efficiency of any heat machine must be less than the maximum value of 1 - Q1/Q2
## Efficiency according to Kelvin-Planck law: eta <= 1 - Q2/Q1
## Where:
## eta is machine efficiency
## Q1 is heat taken from the hot tank in Celsius(start)
## Q2 is heat given to the cold storage tank in Celsius(end)

eta = Symbol("efficiency", 1 - (units.temperature / units.temperature))
temperature_start = Symbol("temperature_start", units.temperature)
temperature_end = Symbol("temperature_end", units.temperature)

law = Eq(eta, 1 - (temperature_start / temperature_end))


def print_law() -> str:
    return print_expression(law)


@validate_input(temperature_start_=temperature_start, temperature_end_=temperature_end)
@validate_output(eta)
def calculate_eta(
    temperature_start_: Quantity,
    temperature_end_: Quantity,
) -> Quantity:
    solved = solve(law, eta, dict=True)[0][eta]
    result_expr = solved.subs(
        {temperature_start: temperature_start_, temperature_end: temperature_end_}
    )
    return Quantity(result_expr)
