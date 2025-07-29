import psycopg2
from psycopg2 import sql

class DB:

	def __init__(self):
		self.table_name = "password_table"
		self.user_column_name = "username"
		self.passwords_column_name = "passwords"
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
		if self._conn and self.table_name and self.user_column_name and self.passwords_column_name:
			return True
		else:
			return False
			print("Can not connect to database")

	def add_data(self, username:str, data: list):
		if self.check_is_connected():
			if not self.user_exist(username):
				print("Username does not exist.")
				return
			curs = self._conn.cursor()
			query = f"SELECT {self.passwords_column_name} FROM {self.table_name} WHERE {self.user_column_name}=%s;"
			curs.execute(query, (username,))
			pre_data = curs.fetchone()
			if pre_data[0]:
				data += pre_data[0]
			query = f"UPDATE {self.table_name} SET {self.passwords_column_name} = %s WHERE {self.user_column_name} = %s;"
			curs.execute(query, (data, username))
			self._conn.commit()
			curs.close()
			print(f"Data added to {username}.")


	def get_data(self, username: str):
		if self.check_is_connected():
			if not self.user_exist(username):
				print("Username does not exist.")
				return None
			curs = self._conn.cursor()
			query = f"SELECT {self.passwords_column_name} FROM {self.table_name} WHERE {self.user_column_name} = %s"
			curs.execute(query, (username,))
			data = curs.fetchone()
			curs.close()
			return data[0]
		return None

	def user_exist(self, username: str):
		if self.check_is_connected():
			curs = self._conn.cursor()
			query = f"SELECT {self.user_column_name} FROM {self.table_name} WHERE {self.user_column_name}=%s;"
			curs.execute(query, (username,))
			exist = curs.fetchone()
			if exist:
				return True
		return False

	def add_user(self, username: str):
		if self.check_is_connected():
			if self.user_exist(username):
				print("Username already exist!")
				return
			curs = self._conn.cursor()
			query =  f"INSERT INTO {self.table_name} ({self.user_column_name}) VALUES (%s);"
			curs.execute(query, (username,))
			self._conn.commit()
			curs.close()
			print("Username added.")

	def close_db(self):
		if self.check_is_connected():
			self._conn.close()
