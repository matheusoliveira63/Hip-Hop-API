from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# Create Database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hiphop.db' 

db = SQLAlchemy(app) 

# Define a Model
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    records = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'records': self.records
        }   


with app.app_context(): 
    db.create_all()  # Create the database tables     

# Create Routes 
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Hip-Hop API!'})

# URI: /artists
@app.route('/artists', methods=['GET'])
def get_artists(): 
    artists = Artist.query.all()
    return jsonify([artist.to_dict() for artist in artists])

# URI : /artists/2
@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    if artist:
        return jsonify(artist.to_dict())
    else:
        return jsonify({'message': 'Artist not found!'}), 404
    

# POST: /artist
@app.route('/artists', methods=['POST'])
def create_artist():
    data = request.get_json()
    new_artist = Artist(name=data['name'], 
                        records=data['records'])
    db.session.add(new_artist)
    db.session.commit()
    
    return jsonify(new_artist.to_dict()), 201


# PUT: /artist/2
@app.route('/artists/<int:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    data = request.get_json()
    
    artist = Artist.query.get(artist_id)
    if artist: 
        artist.name = data.get('name', artist.name)
        artist.records = data.get('records', artist.records)

        db.session.commit()
        
        return jsonify(artist.to_dict())
    else:
        return jsonify({'message': 'Artist not found!'}), 404


# DELETE: /artist/2
@app.route('/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id): 
    artist = Artist.query.get(artist_id)
    if artist:
        db.session.delete(artist)
        db.session.commit()
        return jsonify({'message': 'Artist deleted successfully!'})
    else:
        return jsonify({'message': 'Artist not found!'}), 404
         


    
    
   











if __name__ == '__main__':
    app.run(debug=True)
