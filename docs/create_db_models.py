# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    """description: Stores details of customers"""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class Product(Base):
    """description: Stores details of men's golf shoes"""
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock_quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    brand_id = Column(Integer, ForeignKey('brands.id'))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class Order(Base):
    """description: Represents an order placed by a customer"""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    total_amount = Column(Float)
    status = Column(String)
    payment_id = Column(Integer, ForeignKey('payments.id'))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class OrderDetail(Base):
    """description: Details of products ordered in an order"""
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    unit_price = Column(Float)
    amount = Column(Float)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class Category(Base):
    """description: Product categories"""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class Brand(Base):
    """description: Brands of products"""
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class Cart(Base):
    """description: Shopping cart details for customers"""
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class CartItem(Base):
    """description: Items within a shopping cart"""
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class Payment(Base):
    """description: Payment records for orders"""
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    amount_paid = Column(Float)
    payment_date = Column(DateTime)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class Address(Base):
    """description: Addresses used by customers for orders"""
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    street = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class Review(Base):
    """description: Customer reviews and ratings for products"""
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    rating = Column(Integer)
    comment = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

class Promotion(Base):
    """description: Promotional offers on products"""
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    discount_percentage = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(String)
    updated_date = Column(DateTime, onupdate=datetime.datetime.utcnow)

Base.metadata.create_all(engine)

# Initialize some data
customer = Customer(name="John Doe", email="john.doe@example.com", created_by="system")
category = Category(name="Sports", created_by="admin")
brand = Brand(name="Nike", created_by="admin")
product = Product(name="Nike Air Max", price=199.99, stock_quantity=50, category_id=1, brand_id=1, created_by="admin")
order = Order(customer_id=1, total_amount=199.99, status="Pending", created_by="john.doe@example.com")
order_detail = OrderDetail(order_id=1, product_id=1, quantity=1, unit_price=199.99, amount=199.99, created_by="john.doe@example.com")
cart = Cart(customer_id=1, created_by="john.doe@example.com")
cart_item = CartItem(cart_id=1, product_id=1, quantity=2, created_by="john.doe@example.com")
payment = Payment(order_id=1, amount_paid=199.99, payment_date=datetime.datetime.utcnow(), created_by="john.doe@example.com")
address = Address(customer_id=1, street="123 Golf Way", city="Golftown", state="GT", postal_code="12345", created_by="john.doe@example.com")
review = Review(product_id=1, customer_id=1, rating=5, comment="Great shoes!", created_by="john.doe@example.com")
promotion = Promotion(product_id=1, discount_percentage=10.0, start_date=datetime.datetime.utcnow(),
                      end_date=datetime.datetime.utcnow() + datetime.timedelta(days=30), created_by="admin")

# add instances to the session
session.add_all([customer, category, brand, product, order, order_detail, cart, cart_item,
                 payment, address, review, promotion])

# commit the session
session.commit()
