from flask import Flask, render_template, request
from flask import redirect, url_for, jsonify 
from database import *
from models import *
from Pythonblob import *

import random 

app = Flask(# Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'        # Name of directory for static files
)

s_item_id = 0
num_selected_items = 0

## Your code goes here!  ##
@app.route('/') 
def home():
	return render_template('home.html', items=get_8_random_items())
		
@app.route('/shopitem/<int:id>', methods=['GET', 'POST']) 
def shopitem(id):
	global s_item_id
	global num_selected_items
	s_item_id = id 
	#change code to all other button (REM not onclick -its href)
	#in the brackets- find the ccategory of the item that u got the idd of(PRESSED
	#on), and thats what u put there
	itemsInCategory = get_items_by_category(id, get_item_category_by_id(id))
	if request.method == 'POST': 
		num_selected_items = request.form.get('num_items')
		print(num_selected_items)
	# Pass to the html:
	return render_template("shopitem.html", ItemIdx=id-1, items=query_all(), itemsInCategory=itemsInCategory)

@app.route('/cart') 
def cart():
	global s_item_id
	global num_selected_items
	s_item_idx = s_item_id - 1 
	s_item_id = 0 
	num_items = num_selected_items
	num_selected_items = 0 
	# print("s_item_id:", s_item_idx, "num_items:", num_items) 
	return render_template('cart.html', items=query_all(), s_item_idx=s_item_idx, num_items=num_items, bloblist=bloblist,users=users, x=x)

## And doesn't go after this line.  ##
if __name__ == "__main__":  # Makes sure this is the main process
	app.run(# Starts the site
		host='0.0.0.0',     # EStablishes the host, required for repl to detect the site
		port=8080,          # Randomly select the port the machine hosts on.
        debug=True)
