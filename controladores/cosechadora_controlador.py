from app import *
from flask import jsonify,request

from modelos.cosechadora_modelo import *

@app.route('/cosechadoras',methods=['GET'])
def get_Cosechadoras():
    all_cosechadoras=Cosechadora.query.all()         
    result=cosechadoras_schema.dump(all_cosechadoras)                                                   
    return jsonify(result)      
                 
@app.route('/cosechadoras/<id_cosechadoras>',methods=['GET'])
def get_cosechadora(id_cosechadoras):
    cosechadora=Cosechadora.query.get(id_cosechadoras)
    return cosechadora_schema.jsonify(cosechadora)   

@app.route('/cosechadoras', methods=['POST']) # crea ruta o endpoint
def create_cosechadora():
    #print(request.json)  # request.json contiene el json que envio el cliente
    modelo_cosechadora=request.json['modelo_cosechadora']
    motor_cosechadora=request.json['motor_cosechadora']
    potencia_cosechadora=request.json['potencia_cosechadora']
    plataforma_cosechadora=request.json['plataforma_cosechadora']
    capacidadTolva_cosechadora=request.json['capacidadTolva_cosechadora']
    CapacidadDescarga_cosechadora=request.json['CapacidadDescarga_cosechadora']
    PilotoAuto_cosechadora=request.json['PilotoAuto_cosechadora']
    jdlink_cosechadora=request.json['jdlink_cosechadora']
    combine_cosechadora=request.json['combine_cosechadora']
    activeyield_cosechadora=request.json['activeyield_cosechadora']
    imagen_cosechadora=request.json['imagen_cosechadora']
    stock_cosechadora=request.json['stock_cosechadora']
    new_cosechadora=Cosechadora(modelo_cosechadora,motor_cosechadora,potencia_cosechadora,plataforma_cosechadora,capacidadTolva_cosechadora,CapacidadDescarga_cosechadora,PilotoAuto_cosechadora,jdlink_cosechadora,combine_cosechadora,activeyield_cosechadora,imagen_cosechadora,stock_cosechadora)
    db.session.add(new_cosechadora)
    db.session.commit() # confirma el alta
    return cosechadora_schema.jsonify(new_cosechadora)

@app.route('/cosechadoras/<id_cosechadoras>' ,methods=['PUT'])
def update_cosechadora(id_cosechadoras):
    cosechadora=Cosechadora.query.get(id_cosechadoras)
    modelo_cosechadora=request.json['modelo_cosechadora']
    motor_cosechadora=request.json['motor_cosechadora']
    potencia_cosechadora=request.json['potencia_cosechadora']
    plataforma_cosechadora=request.json['plataforma_cosechadora']
    capacidadTolva_cosechadora=request.json['capacidadTolva_cosechadora']
    CapacidadDescarga_cosechadora=request.json['CapacidadDescarga_cosechadora']
    PilotoAuto_cosechadora=request.json['PilotoAuto_cosechadora']
    jdlink_cosechadora=request.json['jdlink_cosechadora']
    combine_cosechadora=request.json['combine_cosechadora']
    activeyield_cosechadora=request.json['activeyield_cosechadora']
    imagen_cosechadora=request.json['imagen_cosechadora']
    stock_cosechadora=request.json['stock_cosechadora']
    
    cosechadora.modelo_cosechadora=modelo_cosechadora
    cosechadora.motor_cosechadora=motor_cosechadora
    cosechadora.potencia_cosechadora=potencia_cosechadora
    cosechadora.plataforma_cosechadora=plataforma_cosechadora
    cosechadora.capacidadTolva_cosechadora=capacidadTolva_cosechadora
    cosechadora.CapacidadDescarga_cosechadora=CapacidadDescarga_cosechadora
    cosechadora.PilotoAuto_cosechadora=PilotoAuto_cosechadora
    cosechadora.jdlink_cosechadora=jdlink_cosechadora
    cosechadora.combine_cosechadora=combine_cosechadora
    cosechadora.activeyield_cosechadora=activeyield_cosechadora
    cosechadora.imagen_cosechadora=imagen_cosechadora
    cosechadora.stock_cosechadora=stock_cosechadora

    db.session.commit()    
    return cosechadora_schema.jsonify(cosechadora)    

@app.route('/cosechadoras/<id_cosechadoras>',methods=['DELETE'])
def delete_cosechadora(id_cosechadoras):
    cosechadora=Cosechadora.query.get(id_cosechadoras)
    db.session.delete(cosechadora)
    db.session.commit()                     
    return cosechadora_schema.jsonify(cosechadora) 
