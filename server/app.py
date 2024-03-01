#!/usr/bin/env python3

# library imports
from flask import request

# local imports
from config import create_app, db, api

# Add your model imports

# instantiate app
app = create_app()

# routes go here

@app.route('/')
def index():
    return '<h1>121123 Phase 4 Project/Product</h1>'

# Users Routes
@app.get('/users')
def get_users():
    all_users = User.query.all()
    return [ user.to_dict() for user in all_users], 200

@app.get('/users/<int:id>')
def get_users_by_id(id):
    found_users = User.query.where(User.id ==id).first()
    if found_users:
        return found_users.to_dict(), 200
    else:
        return{'error': 'User not found'}

@app.post('/users')
def add_users():
    data = request.json

    try:
        new_user = User(
            username=data.get('username'), password=data.get('password'), date_of_birth=data.get('date_of_birth'), favorite_platform=data.get('favorite_platform'), profile_picture=data.get('profile_picture'))
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201
    
    except ValueError as error:
        return {'error': f'{error}'}, 406
    except:
        return {'error': 'Invalid data'}
# Games Routes
        
@app.get('/games')
def get_games():
    all_games = Game.query.all()
    return [ game.to_dict() for game in all_games], 200

@app.get('/games/<int:id>')
def get_game_by_id(id):
    found_games = Game.query.where(Game.id ==id).first()
    if found_games:
        return found_games.to_dict(), 200
    else:
        return {'error': 'Game not found'}
    
@app.post('/games')
def post_games():
    data = request.json

    try:
        new_games = Game(name=data.get('name'), release_date=data.get('release_date'), image_url=data.get('image_url'), description=data.get('description'))
        db.session.add(new_games)
        db.session.commit()
        return new_games.to_dict(), 200
    
    except ValueError as error:
        return{'error': f'{error}'}, 400
    
@app.patch('/games/<int:id>')
def update_games(id):
    data = request.json
    found_games = Game.query.where(Game.id ==id).first()
    
    if found_games:
        try:
            for key in data:
                setattr(found_games, key, data[key])
            db.session.commit()

            return found_games.to_dict(), 202
        
        except ValueError as error:
            return {'error': f'{error}'}, 406
    else:
        return {'error': "Game not found"}
    
#Rating Routes   
@app.get('/ratings')
def get_ratings():
    all_ratings = Rating.query.all()
    return [ rating.to_dict() for rating in all_ratings], 200

@app.get('/ratings/<int:id>')

@app.post('/ratings')
def add_ratings():
    data = request.json

    try:
        new_rating = Rating(rating=data.get('rating'), comment=data.get('comment'))
        db.session.add(new_rating)
        db.session.commit()
        return new_rating.to_dict(), 201
    
    except ValueError as error:
        return {'error': f'{error}'}, 406
    except:
        return {'error': "Invalid Data"}
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)

