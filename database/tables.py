from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
import datetime

class Tables:
  def __init__(self,app):
    self.db = SQLAlchemy(app)
    self.UserModel = self.get_user_model()
    self.ProductModel = self.get_product_model()
    self.AdminModel = self.get_admin_model()

  def get_user_model(self):
    db = self.db

    @dataclass
    class UserModel(db.Model):
      id: int
      username: str
      password: str
      phone: str
      email: str
      sub_plan: str
      sub_packages: str
      sub_start: datetime
      sub_end: datetime

      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(100), nullable=False)
      password = db.Column(db.String(50), nullable=False)
      phone = db.Column(db.String(20), nullable=False)
      email = db.Column(db.String(50), nullable=False)
      sub_plan = db.Column(db.String(50), nullable=True)
      sub_packages = db.Column(db.String(100), nullable=True)
      sub_start = db.Column(db.DateTime, nullable=True)
      sub_end = db.Column(db.DateTime, nullable=True)
    
    self.db.create_all()
    return UserModel

  def get_product_model(self):
    db = self.db

    @dataclass
    class ProductModel(db.Model):
      id: int
      name: str
      category: str
      description: str
      ingredients: str
      price: float
      popularity: int
      date_added: datetime
      stock: int
      image: str

      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(100), nullable=False)
      category = db.Column(db.String(50), nullable=False)
      description = db.Column(db.String(100), nullable=False)
      ingredients = db.Column(db.String(200), nullable = False)
      price = db.Column(db.Float, nullable=False)
      popularity = db.Column(db.Integer, nullable=False)
      date_added = db.Column(db.DateTime, nullable=False)
      stock = db.Column(db.Integer, nullable=False)
      image = db.Column(db.String(100), nullable=False)
      
    self.db.create_all()
    return ProductModel

  def get_admin_model(self):
    db = self.db
    
    @dataclass
    class AdminModel(db.Model):
      id: int
      username: str
      password: str
      email: str
      phone: str

      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(100), nullable=False)
      password = db.Column(db.String(50), nullable=False)
      phone = db.Column(db.String(20), nullable=False)
      email = db.Column(db.String(50), nullable=False)
    
    self.db.create_all()
    return AdminModel

  def get_db(self):
    return self.db
