def calculate_monthly_payment(principal, annual_interest_rate, years):
    """
    Calculate the monthly payment for a loan.

    :param principal: The loan amount
    :param annual_interest_rate: The annual interest rate as a percentage
    :param years: The term of the loan in years
    :return: The monthly payment amount
    """
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = years * 12
    
    if monthly_interest_rate == 0:
        return round(principal / number_of_payments, 2)

    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / \
                      ((1 + monthly_interest_rate) ** number_of_payments - 1)
    return round(monthly_payment, 2)

def get_loan_details():
    while True:
        try:
            principal = float(input("Enter the loan amount in dollars: "))
            if principal <= 0:
                print("The loan amount must be a positive number. Please try again.")
                continue

            annual_interest_rate = float(input("Enter the annual interest rate (percentage): "))
            if annual_interest_rate < 0:
                print("The annual interest rate cannot be negative. Please try again.")
                continue

            years = float(input("Enter the loan term (years): "))  # Changed from int to float
            if years <= 0:
                print("The loan term must be a positive number. Please try again.")
                continue

            return principal, annual_interest_rate, years
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    while True:
        print("\nLoan Calculator")
        principal, annual_interest_rate, years = get_loan_details()
        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
        print(f"Monthly Payment: ${monthly_payment:.2f}")

        choice = input("Do you want to calculate another loan? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the loan calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()