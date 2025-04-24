from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{environ.get('MYSQL_USER')}:{environ.get('MYSQL_PASSWORD')}@"
    f"{environ.get('MYSQL_HOST')}/{environ.get('MYSQL_DATABASE')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Toode model matching the actual database structure
class Toode(db.Model):
    __tablename__ = 'toode'
    toode_id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(255))
    hind = db.Column(db.Float)
    kategooria = db.Column(db.String(255))
    
    def to_dict(self):
        return {
            'toode_id': self.toode_id,
            'nimi': self.nimi,
            'hind': self.hind,
            'kategooria': self.kategooria
        }

# GET - Kõik tooted
@app.route('/api/tooted', methods=['GET'])
def get_tooted():
    tooted = Toode.query.all()
    return jsonify([toode.to_dict() for toode in tooted])

# GET - Üks toode
@app.route('/api/tooted/<int:toode_id>', methods=['GET'])
def get_toode(toode_id):
    toode = Toode.query.get_or_404(toode_id)
    return jsonify(toode.to_dict())

# GET - Tooted kategooria järgi
@app.route('/api/tooted/kategooria/<kategooria>', methods=['GET'])
def get_tooted_by_kategooria(kategooria):
    tooted = Toode.query.filter_by(kategooria=kategooria).all()
    return jsonify([toode.to_dict() for toode in tooted])

# POST - Lisa uus toode
@app.route('/api/tooted', methods=['POST'])
def create_toode():
    data = request.get_json()
    
    if not all(key in data for key in ['nimi', 'hind', 'kategooria']):
        return jsonify({'error': 'Puuduvad vajalikud väljad (nimi, hind, kategooria)'}), 400
    
    new_toode = Toode(
        nimi=data['nimi'],
        hind=data['hind'],
        kategooria=data['kategooria']
    )
    
    try:
        db.session.add(new_toode)
        db.session.commit()
        return jsonify(new_toode.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# PUT - Muuda toodet
@app.route('/api/tooted/<int:toode_id>', methods=['PUT'])
def update_toode(toode_id):
    toode = Toode.query.get_or_404(toode_id)
    data = request.get_json()
    
    if 'nimi' in data:
        toode.nimi = data['nimi']
    if 'hind' in data:
        toode.hind = data['hind']
    if 'kategooria' in data:
        toode.kategooria = data['kategooria']
    
    try:
        db.session.commit()
        return jsonify(toode.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# DELETE - Kustuta toode
@app.route('/api/tooted/<int:toode_id>', methods=['DELETE'])
def delete_toode(toode_id):
    toode = Toode.query.get_or_404(toode_id)
    
    try:
        db.session.delete(toode)
        db.session.commit()
        return jsonify({'message': 'Toode kustutatud'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 