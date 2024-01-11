from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Replace 'your_connection_string' with your actual Azure SQL Database connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_connection_string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    availability = db.Column(db.Boolean, default=False)

@app.route('/api/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        name=data['name'],
        author=data['author'],
        date=data['date'],
        availability=data['availability']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
