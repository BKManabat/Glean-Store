from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

def init_db(app):
  db = SQLAlchemy(app)

  @dataclass
  class UserModel(db.Model):
    id: int
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)

  db.create_all()

  return db, UserModel