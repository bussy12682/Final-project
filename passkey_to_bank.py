#create a simple password generator for checking people's bank balance and securing people's password and make it user friendly.
#which takes the input: a user name, bank password and output their balance. 
question_and_answer = str(input("Hello ade, how are you, have you paid your balace and submitted your project? 'yes' or 'no' "))
if question_and_answer == 'yes':
    print("ok, you will receive your certificate soon.")
    exit()
elif question_and_answer == 'no':
    print("i am sorry but you can't receive your certificate until you pay your balance and submit your project.")    
print()
print()
user_wanna_check_balance = str(input("Do you want to login to your bank 'yes' or 'no' : "))
if user_wanna_check_balance.upper() == "YES":
    print("Bank loading!!! " * 3)
elif user_wanna_check_balance.upper() == "NO":
    print("Exiting...")
    exit()
print("WE ARE BEYOND BANKING")
username = input("enter one of your name listed below")
user_bank_code = int(input("enter your bank four digit code"))

username == "ola","ade"
user_bank_code == 1234

if user_bank_code == 1234:
    print("Authenticating.....")
    print(f"Welcome {username}, you are successfully logged in.")
    print("Have a great banking session")

else:
    print("wrong bank details.")    
    print("Pls try again.")
    exit()
print()
balance_check = input("do you care to know your balance (yes or no)")
if balance_check == "yes":
    print("loading!!!.")
    print("your balance is 3,500")
elif balance_check == "no":
    print("ok.")
print()
balance_payment = input("Do you want to pay your balance now? 'yes' or 'no'")
if balance_payment == "yes":
    print("ok, make the payment into this bank:")
    print("opay: 7065432176: linar school of media and ict.")
    print("note project should be submitted before friday, thanks.")
if balance_payment == "no":
    print("ok, certificate will be receives immediately after you submit your project and py your balance")
    print()
    print()
screen_time_out = input("Screen time out, do you wanna log out (yes or no) ?")
if screen_time_out == "yes":
   print("ok, logging out....")
   exit()
elif screen_time_out == "no":
   print("OK.")

print("message loading!!!")
print(".........")
print(".........")
print(f" congratulatons {username} you have successfully won a 10% cashback.")    

#made by ENOCH OMONIYI