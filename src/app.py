"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Planets, People, Starship, Vehicle, Species, Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


## ENDPOINTS USUARIO
@app.route('/user', methods=['GET'])
def handle_hello():

    users_query = User.query.all()

    results= list(map(lambda item: item.serialize(), users_query ))

    if results == []:
        return jsonify({"msg":"no hay usuarios"}), 404

    response_body = {
        "msg": "Hello, estos son los usuarios ",
        "results": results
    }

    return jsonify(response_body), 200


#ENDPOINT PARA USUARIO
@app.route('/user/<int:user_id>', methods=['GET'])
def get_usuario(user_id):

    print(user_id)

    user_query= User.query.filter_by(id = user_id).first()
    

    if user_query is None:
       return jsonify({"msg": "no existe el usuario"}), 404
    

    response_body = {
        "msg": "Hello, este es el usuario ",
        "results" : user_query.serialize()
    }

    return jsonify(response_body), 200

#ENDPOINT PARA PLANETAS
@app.route('/planets', methods=['GET'])
def get_planets():
    
    planets_query = Planets.query.all()
    


    results =list(map(lambda item: item.serialize(), planets_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay planetas"}), 404
    

    response_body = {
        "msg": "Hello, estos son los planetas ",
        "results" : results
    }

    return jsonify(response_body), 200

#ENDPOINT PLANETA
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):

    print(planet_id)

    planet_query= Planets.query.filter_by(id = planet_id).first()
    

    if planet_query is None:
       return jsonify({"msg": "no existe el planeta"}), 404
    

    response_body = {
        "msg": "Hello, estos son los planetas ",
        "results" : planet_query.serialize()
    }

    return jsonify(response_body), 200

#NEDPOINT PARA PEOPLE
@app.route('/people', methods=['GET'])
def get_peoples():
    
    people_query = People.query.all()
    


    results =list(map(lambda item: item.serialize(), people_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay personas"}), 404
    

    response_body = {
        "msg": "Hello, estas son las personas ",
        "results" : results
    }

    return jsonify(response_body), 200

    #ENDPOINT PARA PERSONA
@app.route('/people/<int:people_id>', methods=['GET'])
def get_people(people_id):

    print(people_id)

    people_query= People.query.filter_by(id = people_id).first()
    

    if people_query is None:
       return jsonify({"msg": "no existe la persona"}), 404
    

    response_body = {
        "msg": "Hello, esta es la persona ",
        "results" : people_query.serialize()
    }

    return jsonify(response_body), 200

#ENDPOINT PARA STARSHIPS
@app.route('/starship', methods=['GET'])
def get_starships():
    
    starships_query = Starship.query.all()
    


    results =list(map(lambda item: item.serialize(), starships_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay starships"}), 404
    

    response_body = {
        "msg": "Hello, estas son las starships ",
        "results" : results
    }

    return jsonify(response_body), 200
#ENDPOINT PARA STARSHIP
@app.route('/starship/<int:starship_id>', methods=['GET'])
def get_starship(starship_id):

    print(starship_id)

    starship_query= Starship.query.filter_by(id = starship_id).first()
    

    if starship_query is None:
       return jsonify({"msg": "no existe el starship"}), 404
    

    response_body = {
        "msg": "Hello, este es el starship ",
        "results" : starship_query.serialize()
    }

    return jsonify(response_body), 200

    #ENDPOINT PARA VEHICLES
@app.route('/vehicle', methods=['GET'])
def get_vehicles():
    
    vehicles_query = Vehicle.query.all()
    


    results =list(map(lambda item: item.serialize(), vehicles_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay vehiculos"}), 404
    

    response_body = {
        "msg": "Hello, estos son los vehiculos ",
        "results" : results
    }

    return jsonify(response_body), 200

#ENDPOINT PARA VEHICULO
@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):

    print(vehicle_id)

    vehicle_query= Vehicle.query.filter_by(id = vehicle_id).first()
    

    if vehicle_query is None:
       return jsonify({"msg": "no existe el vehicle"}), 404
    

    response_body = {
        "msg": "Hello, este es el vehicle ",
        "results" : vehicle_query.serialize()
    }

    return jsonify(response_body), 200

    #ENDPOINT PARA SPECIES
@app.route('/species', methods=['GET'])
def get_species():
    
    species_query = Species.query.all()
    


    results =list(map(lambda item: item.serialize(), species_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay species"}), 404
    

    response_body = {
        "msg": "Hello, estas son las species ",
        "results" : results
    }

    return jsonify(response_body), 200

#ENDPOINT PARA SPECIE
@app.route('/species/<int:species_id>', methods=['GET'])
def get_specie(species_id):

    print(species_id)

    species_query= Species.query.filter_by(id = species_id).first()
    

    if species_query is None:
       return jsonify({"msg": "no existe la specie"}), 404
    

    response_body = {
        "msg": "Hello, esta es la specie ",
        "results" : species_query.serialize()
    }

    return jsonify(response_body), 200

    #ENPOINT PARA FAVORITOS 
@app.route('/favoritos', methods=['GET'])
def get_favoritos():
    
    favoritos_query = Favoritos.query.all()
    


    results =list(map(lambda item: item.serialize(), favoritos_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay favoritos"}), 404
    

    response_body = {
        "msg": "Hello, estos son los favoritos ",
        "results" : results
    }

    return jsonify(response_body), 200

    #ENDPOINT PARA FAVORITO
@app.route('/favoritos/<int:favoritos_id>', methods=['GET'])
def get_favorito(favoritos_id):

    print(favoritos_id)

    favoritos_query= Favoritos.query.filter_by(id = favoritos_id).first()
    

    if favoritos_query is None:
       return jsonify({"msg": "no existe el favorito"}), 404
    

    response_body = {
        "msg": "Hello, este es el favorito ",
        "results" : favoritos_query.serialize()
    }

    return jsonify(response_body), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
