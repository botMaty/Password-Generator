import bcrypt

def get_hashed_password(password: str):
	return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

def check_hashed_password(password: str, hashed_password: str):
	return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
