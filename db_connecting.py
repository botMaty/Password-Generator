import psycopg2
from psycopg2 import sql

class DB:

	def __init__(self):
		self.table_name = "password_table"
		self.column_name = "password"
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
		if self._conn and self.table_name and self.column_name:
			return True
		else:
			return False
			print("Can not connect to database")

	def add_data(self, data_to_insert: list):
		if self.check_is_connected():
			curs = self._conn.cursor()
			query = f"INSERT INTO {self.table_name} ({self.column_name}) VALUES (%s);"
			for d in data_to_insert:
				curs.execute(query, (d,))
			self._conn.commit()
			curs.close()
			print("Data added.")


	def get_data(self):
		if self.check_is_connected():
			curs = self._conn.cursor()
			query = f"SELECT {self.column_name} FROM {self.table_name}"
			curs.execute(query)
			data = curs.fetchall()
			curs.close()
			return [d[0] for d in data]
		return None

	def close_db(self):
		if self.check_is_connected():
			self._conn.close()
