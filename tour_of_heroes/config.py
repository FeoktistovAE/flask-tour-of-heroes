from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow

from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
ma = Marshmallow(app)

app.config["SQLALCHEMY_DATABASE_URI"] = ''.join((
    f"{os.getenv('DATABASE')}",
    f"://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}",
    f"@{os.getenv('HOST')}/{os.getenv('DATABASE_NAME')}",
))

db.init_app(app)
