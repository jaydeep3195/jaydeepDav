import pytest
from loan_calculator import calculate_monthly_payment

def test_calculate_monthly_payment():
    assert abs(calculate_monthly_payment(1000, 5, 1) - 85.61) < 0.01
    assert abs(calculate_monthly_payment(5000, 3.5, 5) - 91.08) < 0.01
    assert abs(calculate_monthly_payment(20000, 6, 10) - 222.04) < 0.01
    assert abs(calculate_monthly_payment(100000, 4.5, 30) - 506.69) < 0.01

def test_calculate_monthly_payment_zero_interest():
    assert abs(calculate_monthly_payment(1000, 0, 1) - 83.33) < 0.01

def test_calculate_monthly_payment_short_term():
    assert abs(calculate_monthly_payment(1000, 5, 0.5) - 170.85) < 0.01