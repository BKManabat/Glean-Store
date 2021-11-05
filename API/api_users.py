from flask import Flask, request, jsonify, redirect, render_template, session
from database.tables import init_db

def register_route(app):
  db, UserModel = init_db(app)
  
  @app.route('/login', methods=['POST','PUT'])
  def login():
    if request.method == 'POST':
      user = UserModel.query.filter_by(username=request.form['username'], password=request.form['password']).first()
      users = UserModel.query.all()
      # print(users)
      if user:
        session['username'] = request.form['username']
        print("session_api:",session)
        return jsonify(request.form['username'])
      else:
        return '',401
    elif request.method == 'PUT':
      exist = UserModel.query.filter_by(username=request.form['username']).first()
      if(exist):
        return '',409
      user = UserModel(username=request.form['username'], password=request.form['password'])
      db.session.add(user)
      db.session.commit()
      return render_template("index.html")