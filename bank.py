from account_operarion import *
while True:
    print("1. Admin")
    print("2. User")
    choice = int(input("Enter your option: "))

    if choice == 1:
        user_admin = input("Enter username: ")

        if user_admin == "admin@123":
            password = input("Enter password: ")

            if password == "admin_login":
                print("1. View accounts")
                a_choice = int(input("Enter your option: "))

                if a_choice == 1:
                    view_accounts()

            else:
                print("Incorrect password")

        else:
            print("Incorrect username")
            
    else:
        print("1.  Create account")
        print("2.  Deposit money")
        print("3.  Withdrawl money")
        print("4.  Check balance")
        print("5.  statement")
        print("6.  Exit")
        u_choice=int(input("Enter your choice"))
        if u_choice==1:
            create_account()
        elif u_choice==2:
            deposit_money()
        elif u_choice==3:
            withdrawl_money()
        elif u_choice==4:
            check_balance()
        else:
            print("Thank you")
            break