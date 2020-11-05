from time import sleep

def password():
    pin = int(input("PLEASE ENTER YOUR ACCOUNT PIN"))
    if pin == 1234:
      print("Correct pin please wait we are fetching the data")
      sleep(4)
return True

    else:
         print("wrong pin")
     return False


def atm_start():
  print("hello welcome to edvr atm")
  if password():
    while True:
    print("press '1' for checking balance")
    print("press '2' for withdrawl of cash ")
    print("press '3' for depositing money ")
    print("press '4' for exiting ")

choose = int(input("\nchoose which money transcation fits your day:"))

if choose == 1:
   print("please wait we are fetching your data")
         sleep(4)   
    print("your account balance is: " , balance)

  elif choice == 2:
    withdrawl = int(input("how much money do you want to withdraw from your account:"))
           balance = balance - withdrawl
          print(f"you have successfully taken {withdrawl} money from your account")

  elif choose == 3:
    deposit = int(input("how much money do you want to add to your account:"))
            balance = balance + deposit
          print(f"you hve successfully added {deposit} money to your account")

  elif choose == 4:
    print("THANKS FOR USING EDVR ATM HOPE YOU HAVE A GOOD DAY")
            break


    atm_start()
