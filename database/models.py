# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 31, 2024 18:40:08
# Database: sqlite:////tmp/tmp.G9Pge8XdEz/GolfShoes/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Brand(SAFRSBaseX, Base):
    """
    description: Brands of products
    """
    __tablename__ = 'brands'
    _s_collection_name = 'Brand'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="brand")



class Category(SAFRSBaseX, Base):
    """
    description: Product categories
    """
    __tablename__ = 'categories'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="category")



class Customer(SAFRSBaseX, Base):
    """
    description: Stores details of customers
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    AddressList : Mapped[List["Address"]] = relationship(back_populates="customer")
    CartList : Mapped[List["Cart"]] = relationship(back_populates="customer")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="customer")



class Order(SAFRSBaseX, Base):
    """
    description: Represents an order placed by a customer
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'))
    total_amount = Column(Float)
    status = Column(String)
    payment_id = Column(ForeignKey('payments.id'))
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))
    payment : Mapped["Payment"] = relationship(foreign_keys='[Order.payment_id]', back_populates=("OrderList"))

    # child relationships (access children)
    PaymentList : Mapped[List["Payment"]] = relationship(foreign_keys='[Payment.order_id]', back_populates="order")
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="order")



class Payment(SAFRSBaseX, Base):
    """
    description: Payment records for orders
    """
    __tablename__ = 'payments'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'))
    amount_paid = Column(Float)
    payment_date = Column(DateTime)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(foreign_keys='[Payment.order_id]', back_populates=("PaymentList"))

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(foreign_keys='[Order.payment_id]', back_populates="payment")



class Address(SAFRSBaseX, Base):
    """
    description: Addresses used by customers for orders
    """
    __tablename__ = 'addresses'
    _s_collection_name = 'Address'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'))
    street = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("AddressList"))

    # child relationships (access children)



class Cart(SAFRSBaseX, Base):
    """
    description: Shopping cart details for customers
    """
    __tablename__ = 'carts'
    _s_collection_name = 'Cart'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'))
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("CartList"))

    # child relationships (access children)
    CartItemList : Mapped[List["CartItem"]] = relationship(back_populates="cart")



class Product(SAFRSBaseX, Base):
    """
    description: Stores details of men's golf shoes
    """
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock_quantity = Column(Integer)
    category_id = Column(ForeignKey('categories.id'))
    brand_id = Column(ForeignKey('brands.id'))
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    brand : Mapped["Brand"] = relationship(back_populates=("ProductList"))
    category : Mapped["Category"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)
    CartItemList : Mapped[List["CartItem"]] = relationship(back_populates="product")
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="product")
    PromotionList : Mapped[List["Promotion"]] = relationship(back_populates="product")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="product")



class CartItem(SAFRSBaseX, Base):
    """
    description: Items within a shopping cart
    """
    __tablename__ = 'cart_items'
    _s_collection_name = 'CartItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    cart_id = Column(ForeignKey('carts.id'))
    product_id = Column(ForeignKey('products.id'))
    quantity = Column(Integer)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    cart : Mapped["Cart"] = relationship(back_populates=("CartItemList"))
    product : Mapped["Product"] = relationship(back_populates=("CartItemList"))

    # child relationships (access children)



class OrderDetail(SAFRSBaseX, Base):
    """
    description: Details of products ordered in an order
    """
    __tablename__ = 'order_details'
    _s_collection_name = 'OrderDetail'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'))
    product_id = Column(ForeignKey('products.id'))
    quantity = Column(Integer)
    unit_price = Column(Float)
    amount = Column(Float)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderDetailList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderDetailList"))

    # child relationships (access children)



class Promotion(SAFRSBaseX, Base):
    """
    description: Promotional offers on products
    """
    __tablename__ = 'promotions'
    _s_collection_name = 'Promotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    discount_percentage = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("PromotionList"))

    # child relationships (access children)



class Review(SAFRSBaseX, Base):
    """
    description: Customer reviews and ratings for products
    """
    __tablename__ = 'reviews'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    customer_id = Column(ForeignKey('customers.id'))
    rating = Column(Integer)
    comment = Column(String)
    created_date = Column(DateTime)
    created_by = Column(String)
    updated_date = Column(DateTime)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReviewList"))
    product : Mapped["Product"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)
