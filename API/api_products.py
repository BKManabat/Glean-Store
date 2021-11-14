from flask import Flask, request, jsonify, redirect, render_template, session
from utilities.utilities_date import time_now

class API_Products:
  @staticmethod
  def register_route(app, tables):

    db = tables.get_db()
    ProductModel = tables.ProductModel

    @app.route('/get_products', methods=['GET'])
    def get_products():
      products = ProductModel.query.all()
      return jsonify(products)

    @app.route('/admin/add_product', methods=['PUT'])
    def add_product():
      product = ProductModel(name=request.form['name'],category=request.form['category'],description=request.form['description'], ingredients=request.form['ingredients'], price=request.form['price'], popularity=0, date_added = time_now(), stock=request.form['stock'], image=request.form['image'])

      db.session.add(product)
      db.session.commit()

      return jsonify(product)

    @app.route('/admin/delete_product', methods=['DELETE'])
    def delete_product():
      product = ProductModel.query.filter_by(id=request.form['id']).first()
      if product:
        db.session.delete(product)
        db.session.commit()
        return '',200
      else:
        return '',400

    @app.route('/admin/edit_product', methods=['POST'])
    def edit_product():
      product = ProductModel.query.filter_by(id=request.form['id']).first()
      if product:
        product.stock = request.form['stock']
        product.price = request.form['price']
        db.session.merge(product)
        db.session.commit()
        return '',200
      else:
        return '',400