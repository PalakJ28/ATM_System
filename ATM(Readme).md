# ATM

Python Project

### OBJECTIVE:
This project aims to develop a functional ATM using python. It mainly consists of developing and implementing a computer program that function follwing tasks:

-> Check Card Number
-> New Account 
-> Check Balance 
-> Add Balance 
-> Withdrawl
-> Deposit
-> User Detail
-> Change Pin
-> Add, Update, and Delete ATM

In order to understand what ATM functionality is and how it works, below is the description.

### ATM DESCRIPTION:
An ATM (Automated Teller Machine) is an electronic device that enables people to perform various banking transactions without the need for human interaction.

### FUNCTIONALITY

Card Authentication: When a customer inserts their ATM card into the machine, the card reader scans the magnetic stripe on the card and reads the information stored on it, such as the customer's account number and PIN.
Requesting Transaction: The customer then selects the desired transaction on the ATM's touchscreen or keypad, such as withdrawing cash, depositing a check, or checking their account balance.
Processing Transaction: The ATM communicates with the customer's bank through a secure network connection, verifying that the customer has sufficient funds in their account to complete the requested transaction.
Dispensing Cash: If the customer is withdrawing cash, the ATM will dispense the requested amount of money, usually in the form of banknotes.
Printing Receipt: The ATM will then print a receipt of the transaction, which shows the details of the transaction, such as the amount withdrawn, account balance, and any applicable fees.
Retrieving Card: Finally, the customer retrieves their ATM card from the machine, and the transaction is complete.

### IMPLEMENTATION PLAN:
The implementation workflow for this project is as follows:

import random

data = {1234:{'card_num':1234, 'pin':1234, 'amount': 10000, 'bank name':'ICICI', 'mobile':1234567890,'name':'Ayushi'},
        1174197420041234:{'card_num':1174197420041234, 'pin':5678, 'amount': 20000, 'bank name':'HDFC', 'mobile':9876543210,'name':'Vishwa'},
        7234567890111213:{'card_num':7234567890111213, 'pin':9011, 'amount': 30000, 'bank name':'Axis', 'mobile':9898989898,'name':'Riddhi'},
        }
total = 5000

k=0

user = {1:{1234},2:{1174197420041234},4:{7234567890111213},3:{}}

bank={1:'ICICI', 2:'HDFC', 3:'SBI', 4:'Axis'}

admin = {'id':12345,'pin':111}

atm = {'SBI':{'Naroda':{'atm_bal':6000},'Paladi':{'atm_bal':70000}},'ICICI':{'Nikol':{'atm_bal':60000},'Maninagar':{'atm_bal':90000}}, 
        'HDFC':{'Naranpura':{'atm_bal':40000}}, 'Axis':{'Iskon':{'atm_bal':100000}}}
        
        
Given code describe the following Bank Card and its respective ATM with user ID and other details such as Card Number, Bank, ATM.

In order to check the card is authenticated, the pin number required and checked as shown in given code.

def check(card_num):
    if card_num in data:
        pin_num = int(input('Enter the pin:'))
        if data[card_num]['pin'] == pin_num:
            return True
        else:
            return False
    else:
        return False

By entering the pin, pin get checked whether it is ture or false If pin is correct it shows the card details or else it reject the user and Show invalid pin message to user.

Then the program show the whole information about card owner 

Following options shown to user:

-> Check Balance 
-> Withdraw 

Withdraw let the user to withdrawl of money from their respective account with some if else conditions   

if bank1 in bank:
        print(['SBI=Naroda, Paladi','ICICI= Nikol,Maninagar', 'HDFC= Naranpura','Axis= Iskon'])
        branch = input('Enter the ATM branch name from you want to withdraw:')
        if branch in atm[x]:
            global k
            k=k+1
            if k<=5:
                if check(card_num):
                    amt = int(input('Enter the amount to withdraw:'))
                    d=atm[x][branch]['atm_bal']
                    if amt>d:
                        print('branch does not have that amount of money')
                    else:
                        # if amt>total:
                        #     print('Out of cash')
                        # else:
                        if amt>20000:
                            print('You can not withdraw more than 20000 per transaction')
                        else:
                            if amt>data[card_num]['amount']:
                                print("insufficient balance")
                            else:
                                # total = total-amt
                                d=d-amt
                                x = bank[bank1]
                                if x == data[card_num]['bank name']:
                                    # charges=0
                                    new_amt = int(data[card_num]['amount'])-amt
                                    data[card_num]['amount']=new_amt
                                    print('Withdraw Successful')
                                    print('Available Balance:',data[card_num]['amount'])
                                    
                                else:
                                    print('You choose another bank so charges are applied')
                                    charges = (amt*5)/100
                                    newamt = int(data[card_num]['amount'])-amt - charges
                                    if (amt+charges)>data[card_num]['amount']:
                                        print("insufficient balance")
                                    else:
                                        data[card_num]['amount']=newamt
                                        print('Withdraw Successful')
                                        print('Available Balance:',data[card_num]['amount'])
                                        print('Charges Deducted from your account is:',charges)
                                return total
                                return atm
                                return bank
                else:
                    print('record not found')
            else:
                print('Daily limit is 5')
        else:
            print('Branch does not exist')
    else:
        print('Bank Does not exist')
        
        
        
        
        
-> Deposit 
-> Add Balance 

### EXPLANATION

Program let user to explore more about their details by add, update, and delete their bank details. Similarly add, update and delete of ATM can be possible. Bank account have flexibiility to change the user name, add balance, delete bank, add atm, delete atm, and Update atm. Such that the user get upto date with their respective account. 
As per the program the following functioanlity processed as the code implies to.

### CONCLUSION

A program for basic appliction of ATM and Bank account using python to show how ATM works.
