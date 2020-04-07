from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_cors import CORS
import sys
import os


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Init app
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


#* Models

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username,
        self.password = password


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(150))
    invoices = db.relationship('Invoice', backref='customers')

    def __init__(self, name, address):   
        self.name = name
        self.address = address


class Invoice(db.Model):
    __tablename__ = 'invoices'
    date_created = db.Column(db.Date, nullable = False)
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    items = db.relationship('Item', backref='invoices')

    def __init__(self, date_created):
        self.date_created = date_created

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, unique = False)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    product = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

    def __init__(self, quantity,):
        self.name = name


class Product(db.Model):
    __tablename__ = 'products'
    item = db.relationship('Item', backref='products')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique = True)
    description = db.Column(db.String(200))
    price = db.Column(db.Numeric(10,2), unique = False)
    
    def __init__(self, name, description):
        self.name = name
        self.description = description


#* API methods ###################


#* Create Customer
@app.route('/customer', methods=['POST'])
def add_Customer():
  name = request.json['name']
  address = request.json['address']

  customer = Customer(name, address)
  db.session.add(customer)
  db.session.commit()

  return jsonify({'message': 'New Customer Created'})


#* Get All Customers
@app.route('/customer', methods=['GET'])
def get_products():
  customers = Customer.query.all()
  output = []

  for customer in customers:
      customer_data = {}
      customer_data['id'] = customer.id
      customer_data['name'] = customer.name
      customer_data['address'] = customer.address
      output.append(customer_data)
    
  return jsonify({'customers' : output})


#* Get Customer
@app.route('/customer/<id>', methods=['GET'])
def get_Customer(id):
  customer = Customer.query.get(id)

  customer_data ={}

  customer_data['id'] = customer.id
  customer_data['name'] = customer.name
  customer_data['address'] = customer.address

  return jsonify({'customer': customer_data})


#* Update a Customer
@app.route('/product/<id>', methods=['PUT'])
def update_Customer(id):
  customer = Customer.query.get(id)

  name = request.json['name']
  description = request.json['address']

  customer.name = name
  customer.address = address
  
  customer_data ={}
  customer_data['id'] = customer.id
  customer_data['name'] = customer.name
  customer_data['address'] = customer.address

  db.session.commit()

  return jsonify({'customer': 'Updated'})


#* Delete Customer
@app.route('/customer/<id>', methods=['DELETE'])
def delete_customer(id):
  customer = Customer.query.get(id)
  db.session.delete(customer)
  db.session.commit()

  return jsonify({'message': 'Deleted Customer'})

#* Products ************************

#* Create Product
@app.route('/product', methods=['POST'])
def add_Product():
  name = request.json['name']
  description = request.json['description']

  product = Product(name, description)
  db.session.add(product)
  db.session.commit()

  return jsonify({'product': 'New Product Created'})




#* Get All Products
@app.route('/product', methods=['GET'])
def get_Products():
  products = Product.query.all()
  output = []

  for product in products:
      product_data = {}
      product_data['id'] = product.id
      product_data['name'] = product.name
      product_data['description'] = product.description
      product_data['price'] = product.price
      output.append(product_data)
    
  return jsonify({'products' : output})

  #* Get Product
@app.route('/product/<id>', methods=['GET'])
def get_Product(id):
  product = Product.query.get(id)

  product_data ={}

  product_data['id'] = product.id
  product_data['name'] = product.name
  product_data['description'] = product.description
  product_data['price'] = product.price

  return jsonify({'customer':  product_data})


#* Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_Product(id):
  product = Product.query.get(id)

  name = request.json['name']
  description = request.json['description']

  product.name = name
  product.description = description
  
  product_data ={}
  product_data['id'] = product.id
  product_data['name'] = product.name
  product_data['price'] = product.address

  db.session.commit()

  return jsonify({'customer': 'Updated'})


#* Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_Product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return jsonify({'message': 'Deleted Customer'})





#*END OF API****************
  #* Run Server
if __name__ == '__main__':
  app.run(debug=True)