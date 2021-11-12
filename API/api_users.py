from flask import Flask, request, jsonify, redirect, render_template, session

class API_Users:
  @staticmethod
  def register_route(app, tables):

    db = tables.get_db()
    UserModel = tables.UserModel
    
    @app.route('/verify', methods=['POST','PUT'])
    def verify_user():
      if request.method == 'POST':
        user = UserModel.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        # print(users)
        if user:
          session['username'] = request.form['username']
          print("session_api:",session)
          return jsonify(user.username), 200
        else:
          return '',401
      elif request.method == 'PUT':
        exist = UserModel.query.filter_by(username=request.form['username']).first()
        if(exist):
          return '',409
        user = UserModel(username=request.form['username'], password=request.form['password'], phone=request.form['phone'], email=request.form['email'])
        db.session.add(user)
        db.session.commit()
        return render_template("index.html"), 200
    