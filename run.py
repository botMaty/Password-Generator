from pass_generator import *
from temp_file_manager import *

def get_number_by_range(a: int, b: int):
	while True:
		num = input().strip()
		if not len(num):
			continue
		if not all(i in string.digits for i in num):
			print('Enter digits!')
		elif int(num) < a and int(num) > b:
			print('Enter a number in definded range.')
		else: break
	return int(num)

digit = 0
lower = 0
upper = 0
symbl = 0
pass_session = []
temp_file_name = 'passwords_temporary_file.txt'

print('Do you want to upload your last passwords?\n1. Yes\n0. No')
inp = get_number_by_range(0, 1)
if inp:
	pass_session = read_temp_file(temp_file_name).split()

while(True):
	print(f"Select your operation:\n1. Num of digits = {digit}\n2. Num of lower cases = {str(lower)}\n3. Num of upper cases = {str(upper)}\n4. Num of symbols = {str(symbl)}\n5. Generate password\n6. Show your passwords\n7. Rejix\n0. Exit")
	inp = get_number_by_range(0, 7)

	if inp == 0:
		print('Do you want to save your passwords?\n1. Yes\n0. No')
		inp = get_number_by_range(0, 1)
		if inp:
			save_to_temp_file(temp_file_name, pass_session)
		break

	if inp == 5:
		password = password_generator(digit, lower, upper, symbl)
		if len(password):
			pass_session.append(password)
		print(password)

	elif inp == 6:
		for i in range(len(pass_session)):
			print(f'{i+1}. {pass_session[i]}')

	elif inp == 7:
		password = input('Enter your password: ').strip()
		if len(password) and rigix_check(password, digit, lower, upper, symbl):
			print('Accept ;)')
		else: print('Not true.')

	else:
		print('Enter the number:')
		num = get_number_by_range(0, float('inf'))

		if inp == 1:
			digit = num
		elif inp == 2:
			lower = num
		elif inp == 3:
			upper = num
		elif inp == 4:
			symbl = num


