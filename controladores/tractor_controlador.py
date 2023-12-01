from app import *
from flask import jsonify,request

from modelos.tractor_modelo import *

@app.route('/tractores',methods=['GET'])
def get_Tractores():
    all_tractores=Tractor.query.all()         
    result=tractores_schema.dump(all_tractores)                                                   
    return jsonify(result)       
               
@app.route('/tractores/<id_tractores>',methods=['GET'])
def get_tractor(id_tractores):
    tractor=Tractor.query.get(id_tractores)
    return tractor_schema.jsonify(tractor)  

@app.route('/tractores', methods=['POST']) # crea ruta o endpoint
def create_tractor():
    #print(request.json)  # request.json contiene el json que envio el cliente
    modelo_tractor=request.json['modelo_tractor']
    motor_tractor=request.json['motor_tractor']
    potencia_tractor=request.json['potencia_tractor']
    transmision_tractor=request.json['transmision_tractor']
    toma_tractor=request.json['toma_tractor']
    sistema_tractor=request.json['sistema_tractor']
    levante_tractor=request.json['levante_tractor']
    imagen_tractor=request.json['imagen_tractor']
    stock_tractor=request.json['stock_tractor']
    new_tractor=Tractor(modelo_tractor,motor_tractor,potencia_tractor,transmision_tractor,toma_tractor,sistema_tractor,levante_tractor,imagen_tractor,stock_tractor)
    db.session.add(new_tractor)
    db.session.commit() # confirma el alta
    return tractor_schema.jsonify(new_tractor)

@app.route('/tractores/<id_tractores>' ,methods=['PUT'])
def update_tractor(id_tractores):
    tractor=Tractor.query.get(id_tractores)
    modelo_tractor=request.json['modelo_tractor']
    motor_tractor=request.json['motor_tractor']
    potencia_tractor=request.json['potencia_tractor']
    transmision_tractor=request.json['transmision_tractor']
    toma_tractor=request.json['toma_tractor']
    sistema_tractor=request.json['sistema_tractor']
    levante_tractor=request.json['levante_tractor']
    imagen_tractor=request.json['imagen_tractor']
    stock_tractor=request.json['stock_tractor']
    
    tractor.modelo_tractor=modelo_tractor
    tractor.motor_tractor=motor_tractor
    tractor.potencia_tractor=potencia_tractor
    tractor.transmision_tractor=transmision_tractor
    tractor.toma_tractor=toma_tractor
    tractor.sistema_tractor=sistema_tractor
    tractor.levante_tractor=levante_tractor
    tractor.imagen_tractor=imagen_tractor
    tractor.stock_tractor=stock_tractor

    db.session.commit()  
    return tractor_schema.jsonify(tractor)    

@app.route('/tractores/<id_tractores>',methods=['DELETE'])
def delete_tractor(id_tractores):
    tractor=Tractor.query.get(id_tractores)
    db.session.delete(tractor)
    db.session.commit()                     
    return tractor_schema.jsonify(tractor) 
