import random
import string
import tempfile
import os

def get_number_by_range(a: int, b: int):
	while True:
		num = input().strip()
		if num not in string.digits:
			print('Enter digits!')
		elif int(num) < a and int(num) > b:
			print('Enter a number in definded range.')
		else: break
	return int(num)

def password_generator(digit: int, lower: int, upper: int, symbl: int):
	password = ''
	arr = [0, 1, 2, 3]
	i, j, k, l = 0, 0, 0, 0
	while(i + j + k + l < digit + lower + upper + symbl):
		if 0 in arr and i == digit:
			arr.remove(0)
		if 1 in arr and j == lower:
			arr.remove(1)
		if 2 in arr and k == upper:
			arr.remove(2)
		if 3 in arr and l == symbl:
			arr.remove(3)
		num = random.choice(arr)
		if num == 0:
			password += random.choice(string.digits)
			i += 1
		elif num == 1:
			password += random.choice(string.ascii_lowercase)
			j += 1
		elif num == 2:
			password += random.choice(string.ascii_uppercase)
			k += 1
		elif num == 3:
			password += random.choice(string.punctuation)
			l += 1
	return password

def get_temp_file(temp_file_name):
	temp_dir = os.getenv('TEMP') or os.getenv('TMP') or '/tmp'
	file_path = os.path.join(temp_dir, temp_file_name)

	if not os.path.exists(file_path):
		with tempfile.NamedTemporaryFile() as temp_file:
			os.rename(temp_file.name, file_path)
	return file_path

def save_to_temp(temp_file_name, pass_session):
	with open(get_temp_file(temp_file_name), 'w') as f:
		for p in pass_session:
			f.write(p+'\n')

def get_passwords(temp_file_name):
	with open(get_temp_file(temp_file_name), 'r') as f:
		passwords = f.read().split()
	return passwords

digit = 0
lower = 0
upper = 0
symbl = 0
pass_session = []
temp_file_name = 'passwords_temporary_file.txt'

print('Do you want to upload your last passwords?\n1. Yes\n0. No')
inp = get_number_by_range(0, 1)
if inp:
	pass_session = get_passwords(temp_file_name)

while(True):
	print(f"Select your operation:\n1. Num of digits = {digit}\n2. Num of lower cases = {str(lower)}\n3. Num of upper cases = {str(upper)}\n4. Num of symbols = {str(symbl)}\n5. Generate password\n6. Show your passwords\n0. Exit")
	inp = get_number_by_range(0, 6)

	if inp == 0:
		print('Do you want to save your passwords?\n1. Yes\n0. No')
		inp = get_number_by_range(0, 1)
		if inp:
			save_to_temp(temp_file_name, pass_session)
		break

	if inp == 5:
		password = password_generator(digit, lower, upper, symbl)
		if len(password):
			pass_session.append(password)
		print(password)
		continue
	elif inp == 6:
		for i in range(len(pass_session)):
			print(f'{i+1}. {pass_session[i]}')
		continue

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
