from flask import Flask, request, redirect, url_for, session, render_template_string

app = Flask(__name__)
app.secret_key = 'secret'

# Sample product data
products = [
    {"name": "Mobile", "price": 10000},
    {"name": "TV", "price": 20000},
    {"name": "Laptop", "price": 50000},
    {"name": "Fridge", "price":25000},
    {"name": "bueaty products", "price": 5000},
    {"name": "watches", "price":3000}
]

# Inline HTML templates
login_html = """
<!DOCTYPE html>
<html>
<body style="background-color: lightblue;">
<h1 color='black'>SHOPPING IN your daily items <h1>
  <h2>Login Page</h2>
  <form method="post" action="/login">
    Username: <input type="text" name="username" required><br>
    <button type="submit">Login</button>
  </form>
</body>
</html>
"""

home_html = """
<!DOCTYPE html>
<html>
<body style="background-color: lightgreen;">
  <h2>Welcome, {{ user }}</h2>
  <a href="/shop">Go to Shopping</a><br>
  <a href="/cart">View Cart</a>
</body>
</html>
"""

shop_html = """
<!DOCTYPE html>
<html>
<body style="background-color: #f0e68c;">
  <h2>Shopping Items</h2>
  <ul>
    {% for item in products %}
      <li>{{ item.name }} - ₹{{ item.price }}
        <a href="/add_to_cart/{{ item.name }}">Add to Cart</a>
      </li>
    {% endfor %}
  </ul>
  <a href="/cart">Go to Cart</a>
</body>
</html>
"""

cart_html = """
<!DOCTYPE html>
<html>
<body style="background-color: #ffa07a;">
  <h2>Your Cart</h2>
  {% if cart %}
    <ul>
      {% for item in cart %}
        <li>{{ item }}</li>
      {% endfor %}
    </ul>
  {% else %}
    <p>No items in cart</p>
  {% endif %}
  <a href="/shop">Back to Shop</a>
</body>
</html>
"""

# Routes

@app.route('/')
def login():
    return render_template_string(login_html)

@app.route('/login', methods=['POST'])
def do_login():
    session['user'] = request.form['username']
    session['cart'] = []
    return redirect(url_for('home'))

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template_string(home_html, user=session['user'])

@app.route('/shop')
def shop():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template_string(shop_html, products=products)

@app.route('/add_to_cart/<product_name>')
def add_to_cart(product_name):
    if 'user' not in session:
        return redirect(url_for('login'))
    cart = session.get('cart', [])
    cart.append(product_name)
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template_string(cart_html, cart=session.get('cart', []))

if __name__ == '__main__':
    app.run(debug=True)




import webbrowser
from threading import Timer

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)