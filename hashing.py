import bcrypt

def get_hashed_password(password: str):
	"""Send the password to hashed it in str type

	Args:
		password (str): your password

	Returns:
		str: hashed password
	"""	
	return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

def check_hashed_password(password: str, hashed_password: str):
	"""To compare **password** with **hashed_password**

	Args:
		password (str): your password to compare
		hashed_password (str): your hashed password to compare

	Returns:
		bool:
	"""	
	return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
