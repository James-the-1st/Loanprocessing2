# Get user input
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))
loan_amount = float(input("Enter the loan amount you're requesting: "))

# Define the loan qualification criteria
min_credit_score = 3124
min_annual_income = 25000
max_loan_amount = 100000

# Check if the user qualifies for the loan
if credit_score >= min_credit_score:
    if annual_income >= min_annual_income:
        if loan_amount <= max_loan_amount:
            print("Congratulations! You qualify for the loan.")
        else:
            print("Sorry, your loan amount exceeds the maximum allowed.")
    else:
        print("Sorry, your annual income is below the minimum required.")
else:
    print("Sorry, your credit score is below the minimum required.")
