import re

def letters_and_num_only(value):
	if re.match("^[A-Za-z0-9_-]*$", value):
		return True
	return False

def letters_only(value):
	if re.match("^[A-Za-z]*$", value):
		return True
	return False
