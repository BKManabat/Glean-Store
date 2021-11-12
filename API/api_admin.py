from flask import Flask, request, jsonify, redirect, render_template, session

class API_Admin:
  @staticmethod
  def register_route(app, tables):
    db = tables.get_db()
    UserModel = tables.UserModel
    AdminModel = tables.AdminModel
    # admin = AdminModel(username="admin", password='123', phone='6969',email='sam.bot@gmail.com')
    # db.session.add(admin)
    # db.session.commit()

    @app.route('/admin/verify', methods=['POST'])
    def verify_admin():
      # print(AdminModel.query.all())
      admin = AdminModel.query.filter_by(username=request.form['username'], password=request.form['password']).first()
      if admin:
        session['admin'] = request.form['username']
        return '',200
      else:
        return '',401

    @app.route('/admin/get_users', methods=['GET'])
    def get_users():
      users = UserModel.query.all()
      if users:
        return jsonify(users), 200
      else:
        return '',400

    @app.route('/admin/delete_user', methods=['DELETE'])
    def delete_user():
      user = UserModel.query.filter_by(id=request.form['id']).first()
      if user:
        db.session.delete(user)
        db.session.commit()
        return '',200
      else:
        return '',400