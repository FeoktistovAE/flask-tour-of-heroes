from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

from dotenv import load_dotenv
import os


load_dotenv()

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
ma = Marshmallow(app)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = ''.join((
    f"{os.getenv('DATABASE')}",
    f"://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}",
    f"@{os.getenv('HOST')}/{os.getenv('DATABASE_NAME')}",
))


# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
)

app.register_blueprint(swaggerui_blueprint)

db.init_app(app)
