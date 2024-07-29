# loan_calculator.py
def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = years * 12
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    return round(monthly_payment, 2)  # Change to round the monthly payment to 2 decimal

def get_loan_details():
    while True:
        try:
            principal = float(input("Enter the loan amount: "))
            annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
            years = int(input("Enter the loan term (in years): "))
            return principal, annual_interest_rate, years
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    while True:
        print("Loan Calculator")
        principal, annual_interest_rate, years = get_loan_details()
        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
        print(f"Monthly Payment: ${monthly_payment:.2f}")

        choice = input("Do you want to calculate another loan? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the loan calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
