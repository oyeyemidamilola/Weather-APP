from flask import Flask
from config import Config

# create instance of the application
app = Flask(__name__)
app.config.from_object(Config)
app.config["GEOIPIFY_API_KEY"] = 'at_e5iOhjDwvsfyYOvROlgnO4uMmJVm6'
from app import routes