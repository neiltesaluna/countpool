from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os

dbname = os.environ.get('MYSQL_DATABASE')
dbhost = os.environ.get('MYSQL_HOST')
dbport = os.environ.get('MYSQL_PORT')
dbusername = os.environ.get('MYSQL_USER')
dbpassword = os.environ.get('MYSQL_PASSWORD')

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{dbusername}:{dbpassword}@{dbhost}:{dbport}/{dbname}?charset=utf8mb4'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from countpool import routes
from countpool.models import Timer

db.create_all()
