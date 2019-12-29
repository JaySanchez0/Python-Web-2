from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.routes import routes
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']="postgres://xygkswomtxuojo:17ab83f42e9c703d07559a2657fcdac334aae047552aae2c126db65f3066357e@ec2-107-22-234-204.compute-1.amazonaws.com:5432/d8mga7c8qf7b3k"
routes(app)
app.run(host="localhost",port=80)