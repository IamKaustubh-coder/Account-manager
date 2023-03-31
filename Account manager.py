#Oops not oops! haha
#Bank
import datetime
timea=datetime.datetime.now()
accounts={}
getstat=[]
time=timea.strftime('%H:%M:%S')


class BankAccount():
	
	def __init__(self, name):
		self.name=name
		self.balance=0
		self.transaction=[]
	
	def deposit(self, amount):
		self.balance+=amount
		print(f'{amount} succesfully deposited\n')
		x='Deppsited : '+ str(amount)+'  '+'Time : '+time
		self.transaction.append(x)
	
	def withdraw(self, amount):
		if self.balance<amount:
			print('Insufficient balance\n')
			
		else:
			self.balance-=amount
			print(f'succesfully withdrew {amount} rupees\n')
			x='withdrawn : '+ str(amount)+'  '+'Time : '+time
			self.transaction.append(x)
			

		
	def transfer(self, amount, other_ac_name):
	       if amount > self.balance:
	       	print('Insufficient Balance')
	       elif other_ac_name not in accounts:
	       	print('no such account')
	       else:
	       	other_ac = accounts[other_ac_name]
	       	self.balance-=amount
	       	other_ac.balance+=amount
	       	print(f'{amount} rupees successfully transferred to account {other_ac_name}')

			
	def status(self):
		print(f'Balance : {self.balance}')
		print('ACTIONS : ')
		for i in range(len(self.transaction)):
			print(f'{self.transaction[i]}')
		print()
	
	def getstatus(self):
		getstat=[]
		getstat.append(self.name)
		getstat.append(self.balance)
		return getstat
		
	
		


print('Welcome to this account manager')
print('ACTIONS')
print('1.Create accounts(c)')
print('2.select an account to perform action(s)')
print('3.Deposit money(d)')
print('4Withdraw money(w)')
print('5.Transfer money between accounts(t)')
print('6.Display status(s)')
print('7.Exit account manager(exit)')
print('8. SAVE YOUR ACCOUNTS AS TEXT ON YOUR DEVICE(save)')

ifcreate=False
while True:
	inp=input('What do you want to do (c, d, w, t, s, e, st, save) -  ')	
	inp=inp.lower()

	
	#create
	if inp=='c':	
		name=input('Please Enter account/owner name -  ')
		accounts[name]=BankAccount(name)
		print(f'Account {name} succesfully created\n')
		acselect=False
		ifcreate=True
		
	elif inp!='c':
		if not ifcreate:
			print('Create an account first')
			
		#select	
		elif inp=='s':
			name=input('Please enter account/owner name -  ')
			if name in accounts:
				account=accounts[name]
				print(f'Selected account : {name}\n')
				acselect=True
			else:
				print(f'{name} not found')
			
				
		#check
		elif acselect==False:
				print('No account selected\n')
				
		#deposit		
		elif inp=='d':
			try:
				amount=int(input('Please Enter Amount -  '))
			except ValueError:
				print('Incorrect input')
			account.deposit(amount)
			
		#withdraw		
		elif inp=='w':
			try:
				amount=int(input('Please Enter Amount -  '))
			except ValueError:
				print('Incorrect input')
				
			account.withdraw(amount)
			
		#transfer
		elif inp=='t':
			other_ac=input('Please Enter Account/owner name you want to transfer money - ')
			try:
				amount=int(input('Please Enter Amount -  '))
			except ValueError:
				print('incorrect input')
				
			account.transfer(amount, other_ac)
			
	
		
		#status	
		elif inp=='st':
				account.status()
				
		#save as text
		elif inp=='save':
				
			try:
				acc=[]
				for account in accounts.values():
					x=account.getstatus()
					acc.append(x)
					
				name=input('Please enter file name -  ')
				name=str(name)
				file=open(f'/storage/emulated/0/{name}.txt', 'w')
				file.write(str([x for x in acc]))
				file.close()
				print('Succesfully created')
			except Exception as e:
				print('An error occured')
				print(e)
			finally:
				if 'file' in locals():
					file.close()
			
		#exit
		elif inp=='exit':
				print('Warning This will reset all acount')
				choice=input('Are you sure!(y, n) -  ')
				choice=choice.lower()
				if choice in ['y', 'n']:
					if choice=='y':
						break
					if choice=='n':
						print('Action cancelled')
						continue
			
			
			
		



