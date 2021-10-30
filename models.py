from sqlalchemy import Column, Integer, String, Boolean, Float 
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Item(Base):
	__tablename__ = 'item'
	id = Column(Integer, primary_key=True) 
	name = Column(String)
	price = Column(Float) 
	pre_price = Column(Float) 
	category = Column(String)
	image = Column(String)
	description = Column(String)
	brand = Column(String)
