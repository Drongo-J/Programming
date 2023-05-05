file=open("database.txt","r")
file.close

import datetime

def line():
	print("===============================================")

def s():
	print()

def welcome():
    print("Welcome to the program!")

input1=""

def again():
	s()
	line()
	s()
	input1=input("If you want try again, press 1, else press any button : ")
	if input1=="1": 
		s()
		line()
		signIn()
	else:
		s()
		line()
		s()
		print("Program ended.")
		s()
		line()
		s()

def home(option=None):
	s()
	print("Please select an option . . .")
	s()
	def home2():
		option=input("Sign In (1) | Sign Up (2) : ")
		s()
		line()
		if option.strip()=="1":
			signIn()
		elif option.strip()=="2":
			signUp()
		else:
			s()
			print("Enter \"Sign In\" or \"Sign up\", not other things! ")
			home2()
	home2()
	
def signIn(Username=None, Password=None):
	Username = input("\nEnter your username : ").title().strip()
	Password = input("Enter your password : ").strip()
	if len(Username or Password)>1:
		if True:
			db=open("database.txt", "r")
			usernames=[]
			passwords=[]
			for i in db:
				a=i.split(",")
				a[1]=a[1].strip()
				usernames.append(a[0])
				passwords.append(a[1])
			data = dict(zip(usernames, passwords))
			try:
				if data[Username]:
					try:
						if Password == data[Username]:
							s()
							line()
							print("\nLogin was successful!")
							s()
							line()
						else:
							s()
							line()
							print("\nIncorrect password or username.")
							again()						
					except:
						s()
						line()
						print("\nIncorrect password or username.")
						again()
				else:
					s()
					line()
					print("\nUsername doesn't exist.")
					again()
			except:
				s()
				line()
				print("\nUsername doesn't exist.")
				again()
		else:
			s()
			line()
			print("\nPlease attempt login again.")
			signIn()		


def signUp(Username=None, Password=None, PasswordConfirmation=None, age=None, mail=None, city=None,registerTime=None):
	Username=input("\nCreate a username : ").title().strip()
	Password=input("Create a password : ").strip()
	PasswordConfirmation=input("Please, confirm your password : ").strip()
	age=input("Enter your age : ").strip()
	mail=input("Enter your mail : ").strip()
	city=input("Enter your city : ").title().strip()
	registerTime= datetime.datetime.now()
	db = open("database.txt", "r")
	usernames=[]
	for i in db:
		a=i.split(",")
		c=a[0]
		usernames.append(c)
	if Password!=PasswordConfirmation:
		print("Passwords don't match, please sign up again.")
		signUp()
	else:
		if 1<len(PasswordConfirmation)<=6:
			print("Password is too short.")
			print("Please, enter one that is longer than 8 letters.")
			signUp()
		if len(PasswordConfirmation)==0:
			print("\nPlease, enter something.")
			signUp()
		elif Username in usernames:
			print("\nUsername has already taken.")
			print("Please, choose another username.")
			signUp()
		else:
			db=open("database.txt","a")
			db.write(Username+", "+Password+", "+age+", "+mail+", "+city+", "+str(registerTime)+"\n")
			print("\nYou have successfully registered!")

welcome()
home()
