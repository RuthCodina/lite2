from flask import Flask, request  #request, se encarga de extraer la información que viene del cliente.
from flask.json import jsonify 
from flask_pymongo import PyMongo, ObjectId #me permite convertir el id
from flask_cors import CORS

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost/lite2'
mongo = PyMongo(app)

CORS(app)

db = mongo.db.users #áca ya le estoy guardando la colección users en db

#áca establezco las rutas de la información que va a venir de react
@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert({
        'name': request.json['name'],
        'address': request.json['address'],
        'NIT': request.json['NIT'],
        'contact': request.json['contact']
    })
    return jsonify(str(ObjectId(id))) #el id que se va a mostrar áca es el ID generado por mongodb

@app.route('/users', methods=['GET'])
def getUsers():
    users = []   #el for lo que hará es llenar la lista de usarios con
    for doc in db.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'address': doc['address'],
            'NIT': doc['NIT'],
            'contact': doc['contact']
        })
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def getByUser(id):
    user =db.find_one({'_id': ObjectId(id)})
    print(user)
    return jsonify({
        'name': user['name'],
        'address': user['address'],
        'NIT': user['NIT'],
        'contact': user['contact']
    })

@app.route('/user/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'User deleted'})

@app.route('/user/<id>', methods=['PUT'])
def updateUser(id):
    db.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': request.json['name'],
        'address':request.json['address'],
        'NIT': request.json['NIT'],
        'contact': request.json['contact']
    }})
    return jsonify({'msg': 'User updated'})


if __name__=="__main__":
    app.run(debug = True)

