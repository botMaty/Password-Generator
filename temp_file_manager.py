import tempfile
import os

def create_and_get_temp_file_path(temp_file_name: str):
	"""This function used to create the temp file and send it path. if the file exists, it only sends the path.

	Args:
		temp_file_name (str): name of the temp file you want to create

	Returns:
		str: the path of temp file in **str** type.
	"""	
	temp_dir = os.getenv('TEMP') or os.getenv('TMP') or '/tmp'
	file_path = os.path.join(temp_dir, temp_file_name)

	if not os.path.exists(file_path):
		with tempfile.NamedTemporaryFile() as temp_file:
			os.rename(temp_file.name, file_path)
	return file_path

def save_to_temp_file(temp_file_name: str, data: list):
	"""Save your given data in the temp file

	Args:
		temp_file_name (str): name of the temp file
		data (list): your data in list type
	"""	
	with open(create_and_get_temp_file_path(temp_file_name), 'w') as f:
		for i in list:
			f.write(i+'\n')

def read_temp_file(temp_file_name: str):
	"""Read and return the data of your temp file in list type.

	Args:
		temp_file_name (str): name of the temp file

	Returns:
		list: a list of the data
	"""	
	with open(create_and_get_temp_file_path(temp_file_name), 'r') as f:
		content = f.read()
	return content
