from pass_generator import *
from temp_file_manager import *
from db_connecting import DB
import os

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
	print('Do you want to save your passwords?\n1. Yes\n0. No')
	inp = get_number_by_range(0, 1)
	if inp:
		save_to_temp_file(temp_file_name, session['pass'])
	db.close_db()

def option_1():
	global digit, lower, upper, symbl
	while True:
		print(f"Select the characters type you want to change the num of it:\n1. Num of digits = {digit}\n2. Num of lower cases = {str(lower)}\n3. Num of upper cases = {str(upper)}\n4. Num of symbols = {str(symbl)}\n0. Back")
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
	if len(password):
		session['pass'].append(password)
	print("Your password: " + password)
	clear_screen(with_press=True)

def option_3():
	global session
	for i in range(len(session['pass'])):
		print(f'{i+1}. {session['pass'][i]}')
	clear_screen(with_press=True)

def option_4():
	global digit, lower, upper, symbl
	print(f"Digits = {digit}\nLower cases = {str(lower)}\nUpper cases = {str(upper)}\nSymbols = {str(symbl)}")
	password = input('Enter your password: ').strip()
	if len(password) and rigix_check(password, digit, lower, upper, symbl):
		print('Accept ;)')
	else: print('Not true.')
	clear_screen(with_press=True)

def option_5():
	global db, db_connected, temp_file_name, session

	if db_connected:
		while True:
			if session['user']:
				print("Select your db operation:\n1. Add your passwords.\n2. Get your passwords.\n3. Logout\n0. Back")
				inp = inp = get_number_by_range(0,3)
				if inp == 0:
					break
				
				if inp == 1:
					db.add_data(session['user'], session['pass'])
					print("data added to your db.")
				elif inp == 2:
					passwords = db.get_data(session['user'])
					if passwords:
						session['pass'] += passwords
					print("Data added to you session.")
				elif inp == 3:
					session['user'] = None
					break

			else:

				print("Login/Register\n1. You already have username\n2. Add your username\n0. Back")
				inp = inp = get_number_by_range(0,2)
				if inp == 0:
					break
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
						print("Username added.")

				if lr_check:
					session['user'] = username

			clear_screen(with_press=True)

	else: print('Can not connect to DB.')
	clear_screen()


def menu():
	while(True):
		print(f"Select your operation:\n1. Passwords characters\n2. Generate password\n3. Show your passwords\n4. Rigix\n5. DB manager\n0. Exit")
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

def clear_screen(with_press=False):
	"""Clears the terminal screen."""
	if with_press:
		input("Press enter to continue")

    # For Windows
	if os.name == 'nt':
		_ = os.system('cls')
	# For macOS and Linux (posix)
	else:
		_ = os.system('clear')

if __name__ == "__main__":
	session['pass'] = []
	session['user'] = None
	print('Do you want to upload your last passwords?\n1. Yes\n0. No')
	inp = get_number_by_range(0, 1)
	if inp:
		session['pass'] = read_temp_file(temp_file_name).split()
	clear_screen()
	menu()