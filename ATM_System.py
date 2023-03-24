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


def check(card_num):
	if card_num in data:
		pin_num = int(input('Enter the pin:'))
		if data[card_num]['pin'] == pin_num:
			return True
		else:
			return False
	else:
		return False


def check_balance(card_num):
	if check(card_num):
		print('Available Balance:', data[card_num]['amount'])
	else:
		print('record not found')


def withdraw(card_num,total,bank,atm):
	print(bank)
	bank1 = int(input('Please select bank name from which you want to withdraw:'))
	x = bank[bank1]
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
						# 	print('Out of cash')
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


def deposit(card_num,total):
	if check(card_num):
		amt = int(input('Enter the amount to Deposit:'))
		new_amt = int(data[card_num]['amount'])+amt
		data[card_num]['amount']=new_amt
		print('Deposit Successful')
		print('Available Balance:',data[card_num]['amount'])
		return total
	else:
		print('Record not found')


def user_detail(card_num):
	if check(card_num):
		print('\nCard Number:',data[card_num]['card_num'])
		print('Name:',data[card_num]['name'])
		print('Available Balance',data[card_num]['amount'])
		print('Bank:',data[card_num]['bank name'])
		print('mobile:',data[card_num]['mobile'])
		print('----------------------------------------------------------------')
	else:
		print('No User Found')


def change_pin():
	if check(card_num):
		new_pin=int(input('Enter new pin number:'))
		data[card_num]['pin'] = new_pin
		print('Pin number successfully updated')
	else:
		print('Wrong Card Number')

#--------------------------------admin side----------------------------------------------------------------

def admin():
	while True:
		admin_id =int(input('Enter your ID:'))
		if admin_id == 12345:
			admin_pin= int(input('Enter the pin:'))
			if admin_pin == 111:
				return True
			else:
				print('Wrong pin')
		else:
			admin_id =int(input('Enter your ID:'))


def new_acc():
	print(bank)
	bank1 = int(input('Enter the bank on which you want to create account:'))
	if bank1 in bank:
		while True:
			card_num = str(random.randint(1000000000000000,9999999999999999))
			card_num = int(card_num)
			if card_num in data:
				continue
			else:
				print('Your card number is:',card_num)
				pin = str(random.randint(1000,9999))
				pin = int(pin)
				print('Your Pin number is:',pin)
				name = input('Enter your name:')
				no = int(input('Enter your mobile number:'))
				amount = int(input('Enter the amount:'))
				x = bank[bank1]
				data[card_num]={'card_num':card_num , 'pin': pin, 'amount': amount,'bank name':x, 'mobile':no, 'name':name}
				print('account added')
				print(data)
				print(user)
			return data
	else:
		print('bank not exist')
	return bank


def delete_acc(data):
	card_num=int(input('Enter the card number that you want to delete:'))
	if card_num in data:
		if data[card_num]['amount'] == 0:
			del(data[card_num])
			print('Account deleted')
		else:
			print('you can not delete account ...there is some balance in the account')
	else:
		print('Account not found')


def update_acc():
	card_num = int(input('Enter the card number in which you want to update:'))
	if card_num in data:
		print('what you want to update?')
		choice = int(input('1.mobile  2.name\nEnter your choice:'))
		if choice == 1:
			update = int(input('Enter new mobile number that you want to update:'))
			data[card_num]['mobile']= update
			print('mobile number updated')
			print(data)
		elif choice == 2:
			update = int(input('Enter new name that you want to update:'))
			data[card_num]['name']= update
			print('name updated')
			print(data)
	else:
	 	print('Account not found')


def add_balance(atm):
	print(bank)
	bank_name = int(input('Enter bank id:'))
	x = bank[bank_name]
	if x in atm:
		branch = input('Enter the branch name:')
		if branch in atm[x]:
			add = int(input('Enter the amount:'))
			new = atm[x][branch]['atm_bal']
			new = int(atm[x][branch]['atm_bal']) + add
			#new = atm[bank_name][branch]['atm_bal']
			atm[x][branch]['atm_bal'] = atm[x][branch]['atm_bal']+add
			print('balance added successfully')
			print(atm)
			return atm
		else:
			print('Branch already exist')
		print(atm)
	else:
		print('Bank not found')


def add_bank():
	print(bank)
	while True:
		bank1 = input('Enter the bank name:')
		if bank1.isupper()== False:
			continue
		else:
			if bank1 in bank.values():
				print('bank already exist')
			else:	
				x = list(bank.keys())[-1]
			x = x+1
			bank[x]=bank1
			atm[bank1]={}
		print(bank)
		print(atm)
		return bank
		return atm


def del_bank():
	print({1:'ICICI', 2:'HDFC', 3:'SBI', 4:'Axis'})
	bank_name = int(input('Enter the bank id that you want to delete:'))
	s = bank[bank_name]
	x= user.keys()
	if s in x:
		if len(user[s])==0:
			del(user[s])
			del(atm[s])
			print('bank delete successfully')
		else:
			print('You can not delete bank...Because there are some users in the bank')
	else:
		print('Bank not found')


def add_atm(bank,atm):
	print(bank)
	bank_name = int(input('Enter the bank id:'))
	x = bank[bank_name]
	if x in atm:
		branch = input('Enter the ATM branch name that you want to add:')
		if branch in atm[x]:
			print('branch is already exist')
		else:
			amount = int(input("Enter the amount:"))
			atm[x].update({branch:{'atm_bal':amount}})
			print('atm added successfully')
			print(atm)
	else:
		print('Bank is not found')
	return bank
	return atm


def delete_atm():
	print(bank)
	bank_name = int(input('Enter the bank id that you want to delete:'))
	s = bank[bank_name]
	if s in atm:
		x = input('Enter the branch that you want to delete:')
		if x in atm[s]:
			y=atm[s].pop(x)
			print(y,'Branch deleted successfully')
			print(atm)
		else:
			print('Branch not found')
	else:
		print('Bank not found')


def update_atm():
	print(bank)
	bank_name = int(input('Enter the bank id:'))
	s = bank[bank_name]
	if s in atm:
		old = input('Enter the old branch that you want to update:')
		if old in atm[s]:
			update = input('Enter the new branch:')
			atm[s][update] = atm[s].pop(old)
			print('updated')
			print(atm)
		else:
			print('Branch not found')
	else:
		print('bank not found')


def update_bank():
	print(bank)
	bank_name=int(input('Enter the bank id that you want to update:'))
	s = bank[bank_name]
	if s in bank.values():
		x =(list(bank.keys())[list(bank.values()).index(s)])
		newname = input("Enter new bank name:")
		if newname.isupper() == True:
			if newname in bank.values():
				print('bank already exist ')
			else:
				print(x)
				bank[x] = newname
				print(atm)
				print(bank)
		else:
			print('Please enter the name in uppercase')
	else:
		print('Bank not found')



start = int(input('Enter 0 for admin and 1 for user:'))
while True:
	if start == 0:
		choice = int(input('1.Create Account\n2.Delete Account\n3.Update Account\n4.Add Money\n5.Add Bank\n6.Delete Bank\n7.Update ATM\n8.Add ATM\n9.Delete ATM\n10.Update Bank\n11.Exit\n12.GO BACK TO MAIN MENU\nEnter Choice:'))
		if choice == 1:
			admin()
			data = new_acc()
		elif choice == 2:
			admin()
			data = delete_acc(data)
		elif choice == 3:
			admin()
			update_acc()
		elif choice == 4:
			admin()
			atm = add_balance(atm)
		elif choice == 5:
			admin()
			bank = add_bank() 
		elif choice == 6:
			admin()
			del_bank()
		elif choice == 7:
			admin()
			update_atm()
		elif choice == 8:
			admin()
			bank = add_atm(bank,atm)
		elif choice == 9:
			admin()
			delete_atm()
		elif choice ==10:
			admin()
			update_bank()
		elif choice == 11:
			break
		elif choice == 12:
			start = int(input('Enter 0 for admin and 1 for user:'))
		else:
			print('Please Select valid choice')

	elif start == 1:
		ch = int(input('1.Check Balance\n2.Withdraw\n3.Deposite\n4.User Detail\n5.Change Pin\n8.Exit\n9.GO BACK TO MAIN MENU\nEnter Choice:'))
		if ch == 1:
			card_num = int(input('Enter the Card Number:'))
			check_balance(card_num)
		elif ch == 2:
			card_num = int(input('Enter the Card Number:'))
			withdraw(card_num,total,bank,atm)
		elif ch == 3:
			card_num = int(input('Enter the Card Number:'))
			deposit(card_num,total)
		elif ch == 4:
			card_num = int(input('Enter the Card Number:'))
			user_detail(card_num)
		elif ch == 5:
			card_num = int(input('Enter the Card Number:'))
			change_pin()
		elif ch == 8:
			break
		elif ch == 9:
			start = int(input('Enter 0 for admin and 1 for user:'))
		else:
			print('Please select valid choice')
	else:
		print('Please select from 0 and 1')
		start = int(input('Enter 0 for admin and 1 for user:'))
