import psycopg2

try:
	conn = psycopg2.connect(
		host="localhost",
		database="pass_generator_db",
		user="botMaty",
		password="1234",
		port=5432
	)
	print("Successfully connected to database.")

except Exception as e:
	print(f"Error connecting to database: {e}")
