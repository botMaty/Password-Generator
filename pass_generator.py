import random
import string

def password_generator(digit: int, lower: int, upper: int, symbl: int):
	"""Generate a Password by given arguments.

	Args:
		digit (int): number of digits
		lower (int): number of lower cases
		upper (int): number of upper cases
		symbl (int): number of symbols

	Returns:
		str: the generated password.
	"""	
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

def rigix_check(password: str, digit: int, lower: int, upper: int, symbl: int):
	"""Rigix your given password by given arguments.

	Args:
		password (str): the given password
		digit (int): number of digits
		lower (int): number of lower cases
		upper (int): number of upper cases
		symbl (int): number of symbols

	Returns:
		bool: Return **True** if rigix was true else **False**
	"""	
	if len(password) != digit + lower + upper + symbl:
		return False

	d, l, u, s = 0, 0, 0, 0
	for p in password:
		if p in string.digits:
			d += 1
		elif p in string.ascii_lowercase:
			l += 1
		elif p in string.ascii_uppercase:
			u += 1
		else : s += 1
	if d == digit and l == lower and u == upper and s == symbl:
		return True
	return False

