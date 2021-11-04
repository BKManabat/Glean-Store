from flask import Flask, request, jsonify, json, redirect
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gleandb.db'
db = SQLAlchemy(app)
test = 'test'
test2 = "test2"
test3 = "test3"

@dataclass
class UserModel(db.Model):
  id: int
  username: str
  password: str

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(50), nullable=False)

class User(Resource):
  def get(self):
    admin = UserModel(username='admin', password='123')
    guest = UserModel(username='guest', password='abc')
    db.session.add(admin)
    db.session.add(guest)
    user = UserModel.query.filter_by(username='admin', password='123').all()
    print(user)
    return jsonify(user)

api.add_resource(User, "/user")

@app.route('/')
def index():
  # return "he"
  return redirect("https://Glean-API.kyutifer.repl.co/user")

# @app.route("/user")
# def get_users():
#   return

if __name__ == "__main__":
	app.run(host="0.0.0.0")