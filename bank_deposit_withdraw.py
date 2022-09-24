def bank_deposit_withdraw():
    bank = 500
    deposit = ""
    withdraw = ""
    print("Welcome to the bank. Your balance is: ",bank)
    
    while bank >= 0:
        deposit = float(input("Deposit amount: "))
        bank += deposit
        print("Balance is ",bank)
        withdraw = float(input("Withdraw amount: "))
        if bank >= withdraw and bank -0.5 >= withdraw and withdraw %5 == 0:
            bank -= withdraw + 0.5
            print("Balance is: ",bank)
        else:
            print("Sorry, insufficient balance.")
            break
    print("Thanks for comming.")
     
bank_deposit_withdraw()