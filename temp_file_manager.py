import tempfile
import os

def create_and_get_temp_file_path(temp_file_name: str):
	temp_dir = os.getenv('TEMP') or os.getenv('TMP') or '/tmp'
	file_path = os.path.join(temp_dir, temp_file_name)

	if not os.path.exists(file_path):
		with tempfile.NamedTemporaryFile() as temp_file:
			os.rename(temp_file.name, file_path)
	return file_path

def save_to_temp_file(temp_file_name: str, array):
	with open(create_and_get_temp_file_path(temp_file_name), 'w') as f:
		for i in array:
			f.write(i+'\n')

def read_temp_file(temp_file_name: str):
	with open(create_and_get_temp_file_path(temp_file_name), 'r') as f:
		content = f.read()
	return content
