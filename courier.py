from flask import Flask, request, jsonify, redirect, render_template, session, url_for, Blueprint
import requests

app = Blueprint('courier', __name__, url_prefix='/courier')

@app.route('/')
def index():
  # if 'courier' in session:
  return render_template('courier/home.html')
  # else:
  #   return redirect(url_for('courier.login'))

@app.route('/login')
def login():
  if 'courier' in session:
    return redirect(url_for('courier.index'))
  else:
    return render_template('courier/login.html')

@app.route('/logout')
def logout():
  session.pop('courier', None)
  return redirect(url_for('courier.login'))
