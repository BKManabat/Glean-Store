from flask import Flask, request, jsonify, redirect, render_template, session, url_for, Blueprint
import requests

app = Blueprint('admin', __name__, url_prefix='/admin')

@app.route('/')
def index():
  return render_template('admin/index.html')

@app.route('/dashboard')
def admin_dashboard():
  # if 'admin' in session:
    return render_template('admin/dashboard.html')
  # else:
  #   return redirect(url_for('/'))

@app.route('/manage_users')
def manage_users():
  response = requests.get('https://Glean-Store.marcovisaya.repl.co/admin/get_users')
  if response:
    users = response.json()
    return render_template('admin/manage_users.html', users=users)
  else:
    return "No Users"

@app.route('/manage_products')
def manage_products():
  response = requests.get('https://Glean-Store.marcovisaya.repl.co/get_products')
  products = []

  if response:
    products = response.json()
  return render_template('admin/manage_products.html', products=products)
