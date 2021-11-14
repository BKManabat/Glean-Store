from flask import Flask, request, jsonify, redirect, render_template, session, url_for, Blueprint
import requests

app = Blueprint('admin', __name__, url_prefix='/admin')

@app.route('/')
def index():
  if 'admin' in session:
    return render_template('admin/dashboard.html')
  else:
    return redirect(url_for('admin.login'))

@app.route('/login')
def login():
  if 'admin' in session:
    return redirect(url_for('admin.index'))
  else:
    return render_template('admin/login.html')

@app.route('/logout')
def logout():
  session.pop('admin', None)
  return redirect(url_for('admin.index'))

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

@app.route('/manage_orders')
def manage_orders():
  response = requests.get('https://Glean-Store.marcovisaya.repl.co/admin/get_orders')
  orders = []

  if response:
    orders = response.json()
  return render_template('admin/manage_orders.html', orders=orders)

