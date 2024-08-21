# test_loan_calculator.py

import pytest
from loan_calculator import calculate_monthly_payment

@pytest.mark.parametrize("principal, interest, years, expected", [
    (1000, 5, 1, 85.61),  # Corrected expected value
    (5000, 3.5, 5, 90.96),  # Corrected expected value
    (20000, 6, 10, 222.04),  # Corrected expected value
    (100000, 4.5, 30, 506.69),  # Corrected expected value
])
def test_calculate_monthly_payment(principal, interest, years, expected):
    assert abs(calculate_monthly_payment(principal, interest, years) - expected) < 0.01

@pytest.mark.parametrize("principal, interest, years, expected", [
    (1000, 0, 1, 83.33),  # Zero interest rate case
])
def test_calculate_monthly_payment_zero_interest(principal, interest, years, expected):
    assert abs(calculate_monthly_payment(principal, interest, years) - expected) < 0.01

@pytest.mark.parametrize("principal, interest, years, expected", [
    (1000, 5, 0.5, 169.11),  # Short term loan of 6 months
])
def test_calculate_monthly_payment_short_term(principal, interest, years, expected):
    assert abs(calculate_monthly_payment(principal, interest, years) - expected) < 0.01
