import os


# set configuration 
class Config():
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_password_key'