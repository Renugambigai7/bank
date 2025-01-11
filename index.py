
balance = 1000.0
has_account = True  
to_Apply  = ['deposit', 'withdraw', 'check balance', 'apply for loan', 'exit']
loan_types = {
    'home loan': {'limit': 500000.0, 'interest_rate': 3.5},
    'auto loan': {'limit': 50000.0, 'interest_rate': 4.0},
    'personal loan': {'limit': 20000.0, 'interest_rate': 5.0}
}
print("Welcome to the ABC Bank!")
print(f"Available Choice : {to_Apply }")
if has_account:
    user_choice = input("Please choose an operation: ").lower()
    if user_choice in to_Apply :
        if user_choice == 'deposit':
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"You have successfully deposited ${amount:.2f}. Your new balance is ${balance:.2f}.")
            else:
                print("Deposit amount must be greater than zero.")
        elif user_choice == 'withdraw':
            amount = float(input("Enter the amount to withdraw: "))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print(f"You have successfully withdrawn ${amount:.2f}. Your new balance is ${balance:.2f}.")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be greater than zero.")
        elif user_choice == 'check balance':
            print(f"Your current balance is ${balance:.2f}.")
        elif user_choice == 'apply for loan':
            if has_account:
                print("Available loan types: home loan, auto loan, personal loan")
                loan_type = input("Enter the loan type you wish to apply for: ").lower()
                
                if loan_type in loan_types:
                    loan_amount = int(input("Enter the loan amoapply for loanunt: "))
                    loan_limit = loan_types[loan_type]['limit']
                    interest_rate = loan_types[loan_type]['interest_rate']
                    
                    if loan_amount > 0:
                        if loan_amount <= loan_limit:
                            interest = loan_amount * (interest_rate / 100)
                            total_repayment = loan_amount + interest
                            print(f"{loan_type.capitalize()} approved for ${loan_amount:.2f}.")
                            print(f"Interest: ${interest:.2f}, Total repayment: ${total_repayment:.2f}.")
                        else:
                            print(f"Loan amount exceeds the limit of ${loan_limit:.2f} for {loan_type}.")
                    else:
                        print("Loan amount must be greater than zero.")
                else:
                    print("Invalid loan type. Please choose a valid loan type.")
            else:
                print("You need to have an account with our bank to apply for a loan.")
        elif user_choice == 'exit':
            print("Thank you for banking with us. Goodbye!")      
    else:
        print("Invalid operation. Please choose from the available operations.")
    if balance > 1000:
        print("You have a healthy balance!")
    if balance < 500:
        print("Consider saving more to increase your balance.")
    print("-" * 30)
