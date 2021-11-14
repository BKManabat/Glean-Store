from flask import Flask, request, jsonify, redirect, render_template, session
from utilities.utilities_date import time_now

class API_Orders:
  @staticmethod
  def register_route(app, tables):

    db = tables.get_db()
    OrderModel = tables.OrderModel

    @app.route('/admin/get_orders', methods=['GET'])
    def get_orders():
      orders = OrderModel.query.all()
      return jsonify(orders)

    @app.route('/add_order', methods=['PUT'])
    def add_order():
      order = OrderModel(
        assigned_user = request.form['assigned_user'],
        assigned_courier = request.form['assigned_courier'],
        package_type = request.form['package_type'],
        packages = request.form['packages'],
        date_ordered = time_now(),
        destination = request.form['destination'],
        status = 'waiting'
      )

      db.session.add(order)
      db.session.commit()

      return jsonify(order)

    @app.route('/admin/delete_order', methods=['DELETE'])
    def delete_order():
      order = OrderModel.query.filter_by(id=request.form['id']).first()
      if order:
        db.session.delete(order)
        db.session.commit()
        return '',200
      else:
        return '',400

    @app.route('/admin/update_order', methods=['PUT'])
    def update_order_status():
      order = OrderModel.query.filter_by(id=request.form['id']).first()
      if order:
        if order.status == 'waiting':
          order.status = 'in transit'
        elif order.status == 'in transit':
          order.status = 'delivered'
        db.session.merge(order)
        db.session.commit()
        return '',200
      else:
        return '',400