from db_conn import connect
def create_account():
    name=input("Enter the your name:")
    email=input("Enter your email:")
    balance=float(input("Enter your initial balance:"))
    db=connect()
    curr=db.cursor()
    curr.execute("insert into accounts (name,email,balance) values (%s,%s,%s)",[name,email,balance])
    db.commit()
    print("Account created successfully")
    db.close()

def view_accounts():
    db=connect()
    curr=db.cursor()
    curr.execute("select * from accounts")
    account=curr.fetchall()
    print("Print accounts")
    for acc in account:
        print(f"ID: {acc[0]}, Name:  {acc[1]}, Email:  {acc[2]}, Balance:  {acc[3]}")
    db.close()

def deposit_money():
    acc_id=int(input("Enter your ID:"))
    money=float(input("Enter you deposit amount:"))
    db=connect()
    curr=db.cursor()
    curr.execute("update accounts set balance = balance+%s where id=%s",(money,acc_id))
    db.commit()
    print("Money deposit successfully")
    db.close()

def withdrawl_money():
    acc_id=int(input("Enter your ID:"))
    money=float(input("Enter amount to withdrawl"))
    db=connect()
    curr=db.cursor()
    curr.execute("select balance from accounts where id=%s",(acc_id,))
    result=curr.fetchone()
    if result and result[0]>=money:
        curr.execute("update accounts set balance = balance-%s where id=%s",(money,acc_id))
        db.commit()
        print("Withdrawl Successfully")
    else:
        print("Insuficient balance")
    db.close()

def check_balance():
    acc_id=int(input("Enter your ID:"))
    db=connect()
    curr=db.cursor()
    curr.execute("select name,balance from accounts where id=%s",(acc_id,))
    result=curr.fetchone()
    if result:
        print(f"Account holder:  {result[0]}, Balance:  {result[1]}")
    else:
        print("Account not found!")
    db.close()