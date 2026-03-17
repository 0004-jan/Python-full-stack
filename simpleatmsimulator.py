pin = 1234
balance = 5000

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
else:
    print("Incorrect PIN")
