import psycopg2
from hashing import *

class DB:
	"""A class to manage your postgresql database.
	"""	

	def __init__(self):		
		self.table_name = "password_table"
		self.user_column_name = "username"
		self.user_pass_column_name = "user_login_hashed_password"
		self.data_column_name = "passwords"
		self._conn = None
		try:
			self._conn = psycopg2.connect(
				host="localhost",
				database="pass_generator_db",
				user="botMaty",
				password="1234",
				port=5432
			)
			print("Successfully connected to database.")

		except Exception as e:
			print(f"Can not connect to data base: {e}")

	def check_is_connected(self):
		"""Check the argumans in init and check database connection.

		Returns:
			bool: Return **True** if everything was right else **False**
		"""		
		if self._conn and self.table_name and self.user_column_name and self.data_column_name:
			return True
		else:
			return False

	def add_data(self, username:str, data: list):
		"""Add your given data to user data list

		Args:
			username (str):
			data (list):
		"""		
		if self.check_is_connected():
			if not self.user_exist(username):
				print("Username does not exist.")
				return
			curs = self._conn.cursor()
			query = f"SELECT {self.data_column_name} FROM {self.table_name} WHERE {self.user_column_name}=%s;"
			curs.execute(query, (username,))
			pre_data = curs.fetchone()
			if pre_data[0]:
				data += pre_data[0]
			query = f"UPDATE {self.table_name} SET {self.data_column_name} = %s WHERE {self.user_column_name} = %s;"
			curs.execute(query, (data, username))
			self._conn.commit()
			curs.close()
			print(f"Data added to {username}.")


	def get_data(self, username: str):
		"""Get the data of the given username

		Args:
			username (str):

		Returns:
			list: a list of data
		"""		
		if self.check_is_connected():
			if not self.user_exist(username):
				print("Username does not exist.")
				return None
			curs = self._conn.cursor()
			query = f"SELECT {self.data_column_name} FROM {self.table_name} WHERE {self.user_column_name} = %s"
			curs.execute(query, (username,))
			data = curs.fetchone()
			curs.close()
			return data[0]
		return None

	def user_exist(self, username: str):
		"""Check the given username in database

		Args:
			username (str):

		Returns:
			bool: Return **True** if user name exist else **False**
		"""		
		if self.check_is_connected():
			curs = self._conn.cursor()
			query = f"SELECT {self.user_column_name} FROM {self.table_name} WHERE {self.user_column_name}=%s;"
			curs.execute(query, (username,))
			exist = curs.fetchone()
			if exist:
				return True
		return False

	def add_user(self, username: str, password: str):
		"""Add the given username and password to data base.\n
		the password will **hashed** then saved.

		Args:
			username (str):
			password (str):

		Returns:
			bool: Return **True** if username can insert to database else **False**
		"""		
		if self.check_is_connected():
			if self.user_exist(username):
				print("Username already exist!")
				return False
			curs = self._conn.cursor()
			query =  f"INSERT INTO {self.table_name} ({self.user_column_name}, {self.user_pass_column_name}) VALUES (%s, %s);"
			curs.execute(query, (username, get_hashed_password(password)))
			self._conn.commit()
			curs.close()
			return True
		return False

	def check_password(self, username: str, password: str):
		"""Check the given password for username by saved password in database.\n
		the saved password is hashed password. so should use the **check_hashed_password** func.

		Args:
			username (str):
			password (str):
		Returns:
			bool: Return **True** if password was correct else **False**
		"""		
		if self.check_is_connected():
			if not self.user_exist(username):
				print("Username does not exist.")
				return False
			curs = self._conn.cursor()
			query = f"SELECT {self.user_pass_column_name} FROM {self.table_name} WHERE {self.user_column_name}=%s;"
			curs.execute(query, (username,))
			hashed_password = curs.fetchone()[0]
			cp = check_hashed_password(password, hashed_password)
			if not cp:
				print("Password is not True.")
			return cp
		return False
	
	def close_db(self):
		"""**Close The Database Connection**\n
		Used when there is no need to connect to the database.
		"""		
		if self.check_is_connected():
			self._conn.close()