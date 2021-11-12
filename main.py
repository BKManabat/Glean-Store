from flask import Flask, request, jsonify, redirect, render_template, session, url_for
from API.api_users import API_Users
from API.api_products import API_Products
from API.api_admin import API_Admin
from database.tables import Tables
import admin
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/gleandb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'OurSecretKey'
app.register_blueprint(admin.app)
tables = Tables(app)


API_Users.register_route(app, tables)
API_Products.register_route(app, tables)
API_Admin.register_route(app, tables)


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/login')
def login():
  if 'username' in session:
    return redirect(url_for('home'))
  return render_template("login.html")

@app.route('/store')
def home():
  response = requests.get('https://Glean-Store.marcovisaya.repl.co/get_products')
  if response:
    products = response.json()
    print(session)
    if 'username' not in session:
      return render_template("home.html", username = None, products = products)
    else:
      return render_template("home.html", username = session['username'], products = products)
  else:
    return "No products"

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))

@app.after_request
def after_request(response):
   response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
   return response

if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)