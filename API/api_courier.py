from flask import Flask, request, jsonify, redirect, render_template, session

class API_Courier:
  @staticmethod
  def register_route(app, tables):

    db = tables.get_db()
    CourierModel = tables.CourierModel
    
    # courier = CourierModel(username="maru", password='123', phone='1234', status="Unavailable")
    # db.session.add(courier)
    # db.session.commit()

    @app.route('/courier/verify', methods=['POST'])
    def verify_courier():
      courier = CourierModel.query.filter_by(username=request.form['username'], password=request.form['password']).first()
      if courier:
        session['courier'] = request.form['username']
        return '',200
      else:
        return '',401