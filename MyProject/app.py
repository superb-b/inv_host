from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
""" app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) """

""" class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False) """

@app.route('/')
def index():
    return render_template('index.html')

""" @app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    item = InventoryItem.query.filter_by(name=data['name']).first()
    if item:
        item.quantity += int(data['quantity'])
    else:
        new_item = InventoryItem(name=data['name'], quantity=int(data['quantity']))
        db.session.add(new_item)
    db.session.commit()
    return jsonify(message="Item added or updated successfully") """

""" @app.route('/items', methods=['GET'])
def get_items():
    items = InventoryItem.query.all()
    return jsonify([{'name': item.name, 'quantity': item.quantity} for item in items]) """

""" @app.route('/book', methods=['POST'])
def book_item():
    data = request.get_json()
    item = InventoryItem.query.filter_by(name=data['name']).first()
    if item and item.quantity >= int(data['quantity']):
        item.quantity -= int(data['quantity'])
        db.session.commit()
        return jsonify(message="Item booked successfully")
    return jsonify(message="Item not available or insufficient quantity"), 400 """

if __name__ == '__main__':
    """ db.create_all() """
    app.run(debug=True )
