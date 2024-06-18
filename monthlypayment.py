import pandas as pd

# Function to calculate monthly payment for a fixed-rate mortgage
def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    return monthly_payment

# Function to generate an amortization schedule
def amortization_schedule(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    
    schedule = []
    balance = principal
    
    for month in range(1, number_of_payments + 1):
        interest_payment = balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment
        schedule.append((month, monthly_payment, principal_payment, interest_payment, balance))
    
    return schedule

# Given data
house_price = 1_500_000  # $1.5 million
down_payment = 500_000  # $500,000
loan_amount = house_price - down_payment  # $1 million
interest_rate = 4  # 5% interest rate
loan_term_years = 30  # 20 years

# Generate amortization schedule
schedule = amortization_schedule(loan_amount, interest_rate, loan_term_years)

# Create a DataFrame from the schedule
columns = ['Month', 'Payment', 'Principal', 'Interest', 'Balance']
df_schedule = pd.DataFrame(schedule, columns=columns)

# Save the DataFrame to an Excel file

csv_file_path = 'amortization_schedule30yrs.csv'
df_schedule.to_csv(csv_file_path, index=False)


