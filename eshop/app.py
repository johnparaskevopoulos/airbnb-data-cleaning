from flask import Flask, render_template, redirect, url_for, session
import json
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load products from JSON file
PRODUCTS_PATH = Path(__file__).parent / 'products.json'
with PRODUCTS_PATH.open() as f:
    PRODUCTS = json.load(f)

def get_cart():
    return session.setdefault('cart', [])

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    cart = get_cart()
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart_ids = get_cart()
    cart_items = [p for p in PRODUCTS if p['id'] in cart_ids]
    total = sum(item['price'] for item in cart_items)
    return render_template('cart.html', items=cart_items, total=total)

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
