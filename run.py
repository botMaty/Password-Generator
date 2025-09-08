from pass_generator import *
from temp_file_manager import *
from db_connecting import DB

digit = 0
lower = 0
upper = 0
symbl = 0
session = {}
db = DB()
db_connected = db.check_is_connected()
temp_file_name = 'passwords_temporary_file.txt'

def option_0():
	global temp_file_name, session
	print("Do you want to save your passwords?")
	print("1. Yes")
	print("0. No")
	inp = get_number_by_range(0, 1)
	if inp == 1:
		save_to_temp_file(temp_file_name, session['pass'])
	db.close_db()

def option_1():
	global digit, lower, upper, symbl
	while True:
		print("Select the characters type you want to change the num of it:")
		print(f"1. Num of digits = {digit}")
		print(f"2. Num of lower cases = {str(lower)}")
		print(f"3. Num of upper cases = {str(upper)}")
		print(f"4. Num of symbols = {str(symbl)}")
		print("0. Back")

		inp = get_number_by_range(0, 4)

		if inp == 0:
			break

		print("Enter the number:")
		num = get_number_by_range(0, float('inf'))
		if inp == 1:
			digit = num
		elif inp == 2:
			lower = num
		elif inp == 3:
			upper = num
		elif inp == 4:
			symbl = num

		clear_screen()
	clear_screen()

def option_2():
	global session
	password = password_generator(digit, lower, upper, symbl)

	if len(password) and password not in session['pass']:
		session['pass'].append(password)

	print("Your password: " + password)
	wait_for_enter()
	clear_screen()

def option_3():
	global session
	for i in range(len(session['pass'])):
		print(f'{i+1}. {session['pass'][i]}')
	wait_for_enter()
	clear_screen()

def option_4():
	global digit, lower, upper, symbl
	print(f"Digits = {digit}")
	print(f"Lower cases = {str(lower)}")
	print(f"Upper cases = {str(upper)}")
	print(f"Symbols = {str(symbl)}")

	password = input('Enter your password: ').strip()
	if len(password) and rigix_check(password, digit, lower, upper, symbl):
		print('Accept ;)')
	else: print('Not true.')
	wait_for_enter()
	clear_screen()

def option_5():
	global db, db_connected, temp_file_name, session

	if db_connected:
		while True:
			if session['user']:
				print("Select your db operation:")
				print("1. Add your passwords")
				print("2. Get your passwords")
				print("3. Logout")
				print("0. Back")

				inp = inp = get_number_by_range(0,3)
				if inp == 0:
					break
				
				clear_screen()

				if inp == 1:
					db.add_data(session['user'], session['pass'])
					print("data added to your db.")
				elif inp == 2:
					passwords = db.get_data(session['user'])
					if passwords:
						session['pass'] += passwords
					print("Data added to you session")
				elif inp == 3:
					session['user'] = None
					break

				wait_for_enter()

			else:

				print("Login/Register")
				print("1. You already have username")
				print("2. Add your username")
				print("0. Back")

				inp = inp = get_number_by_range(0,2)
				if inp == 0:
					break

				clear_screen()

				username = input("Enter your username: ").strip()
				lr_pass = input("Enter your password: ").strip()
				lr_check = False
				if inp == 1:
					lr_check = db.check_password(username, lr_pass)
					if lr_check:
						print("Login successfully :D")

				elif inp == 2:
					lr_check = db.add_user(username, lr_pass)
					if lr_check:
						print("Username added")

				if lr_check:
					session['user'] = username

				wait_for_enter()

			clear_screen()

	else: 
		db = DB()
		db_connected = db.check_is_connected()
		if db_connected:
			option_5()
		else:
			wait_for_enter()
	clear_screen()


def menu():
	while(True):
		print("Select your operation:")
		print("1. Passwords characters")
		print("2. Generate password")
		print("3. Show your passwords")
		print("4. Rigix")
		print("5. DB manager")
		print("0. Exit")

		inp = get_number_by_range(0, 5)

		clear_screen()

		if inp == 0:
			option_0()
			break
		elif inp == 1:
			option_1()
		elif inp == 2:
			option_2()
		elif inp == 3:
			option_3()
		elif inp == 4:
			option_4()
		elif inp == 5:
			option_5()
		

def get_number_by_range(a: int, b: int):
	while True:
		num = input().strip()
		if not len(num):
			continue
		if not all(i in string.digits for i in num):
			print('Enter digits!')
		elif int(num) < a or int(num) > b:
			print('Enter a number in definded range.')
		else: break
	return int(num)

def wait_for_enter():
	input("Press enter to continue")

def clear_screen():
	"""Clears the terminal screen."""
    # For Windows
	if os.name == 'nt':
		_ = os.system('cls')
	# For macOS and Linux (posix)
	else:
		_ = os.system('clear')

if __name__ == "__main__":
	session['pass'] = []
	session['user'] = None
	print("Do you want to upload your last passwords?")
	print("1. Yes")
	print("0. No")
	inp = get_number_by_range(0, 1)
	if inp:
		session['pass'] = read_temp_file(temp_file_name).split()
	clear_screen()
	menu()