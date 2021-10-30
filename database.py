from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
import random

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_item(name, price, pre_price, category, image, description, brand):
    item = Item(name=name, price=price, pre_price=pre_price, category=category, image=image,
                description=description, brand=brand)
    session.add(item)
    session.commit()

def get_8_random_items(): 
    query = session.query(Item) 
    rowCount = int(query.count()) 
    items = []
    while(len(items)<8):
        # print("rowCount", rowCount, "Random:", random.random(), "rowCount*Random:", int(rowCount*random.random()))
        item = query.offset(int(rowCount*random.random())).first() 
        if not (item in items): 
            items.append(item) 
    return items 

def get_item_category_by_id(id):
    item = session.query(Item).filter_by(id=id)
    return item[0].category 

def get_items_by_category(ItemID, ItemCategory):
    items = session.query(Item).filter(Item.id!=ItemID, Item.category==ItemCategory).limit(4)
    #print("Item ID:", ItemID)
    #for item in items:
    #    print(item.id) 
    return items 

def query_all():
    return session.query(Item).all()
