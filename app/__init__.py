from flask import Flask
from config import Config

from logging_config import logging_config
import logging.config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,  db)

logging.config.dictConfig(logging_config)

from app import routes, models