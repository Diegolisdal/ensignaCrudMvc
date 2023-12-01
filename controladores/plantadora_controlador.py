from app import *
from flask import jsonify,request

from modelos.plantadora_modelo import *

@app.route('/plantadoras',methods=['GET'])
def get_Plantadoras():
    all_plantadoras=Plantadora.query.all()         # el metodo query.all() lo hereda de db.Model
    result=plantadoras_schema.dump(all_plantadoras)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/plantadoras/<id_plantadoras>',methods=['GET'])
def get_plantadora(id_plantadoras):
    plantadora=Plantadora.query.get(id_plantadoras)
    return plantadora_schema.jsonify(plantadora)   # retorna el JSON de una plantadora recibido como parametro

@app.route('/plantadoras', methods=['POST']) # crea ruta o endpoint
def create_plantadora():
    #print(request.json)  # request.json contiene el json que envio el cliente
    modelo_plantadora=request.json['modelo_plantadora']
    nroDeLineas_plantadora=request.json['nroDeLineas_plantadora']
    anchoDeLabor_plantadora=request.json['anchoDeLabor_plantadora']
    cajaCentral_plantadora=request.json['cajaCentral_plantadora']
    deslingue_plantadora=request.json['deslingue_plantadora']
    tasaVariable_plantadora=request.json['tasaVariable_plantadora']
    transporte_plantadora=request.json['transporte_plantadora']
    stock_plantadora=request.json['stock_plantadora']
    imagen_plantadora=request.json['imagen_plantadora']
    new_plantadora=Plantadora(modelo_plantadora,nroDeLineas_plantadora,anchoDeLabor_plantadora,cajaCentral_plantadora,deslingue_plantadora,tasaVariable_plantadora,transporte_plantadora,stock_plantadora,imagen_plantadora)
    db.session.add(new_plantadora)
    db.session.commit() # confirma el alta
    return plantadora_schema.jsonify(new_plantadora)

@app.route('/plantadoras/<id_plantadoras>' ,methods=['PUT'])
def update_plantadora(id_plantadoras):
    plantadora=Plantadora.query.get(id_plantadoras)
    modelo_plantadora=request.json['modelo_plantadora']
    nroDeLineas_plantadora=request.json['nroDeLineas_plantadora']
    anchoDeLabor_plantadora=request.json['anchoDeLabor_plantadora']
    cajaCentral_plantadora=request.json['cajaCentral_plantadora']
    deslingue_plantadora=request.json['deslingue_plantadora']
    tasaVariable_plantadora=request.json['tasaVariable_plantadora']
    transporte_plantadora=request.json['transporte_plantadora']
    imagen_plantadora=request.json['imagen_plantadora']
    stock_plantadora=request.json['stock_plantadora']
    
    plantadora.modelo_plantadora=modelo_plantadora
    plantadora.nroDeLineas_plantadora=nroDeLineas_plantadora
    plantadora.anchoDeLabor_plantadora=anchoDeLabor_plantadora
    plantadora.cajaCentral_plantadora=cajaCentral_plantadora
    plantadora.deslingue_plantadora=deslingue_plantadora
    plantadora.tasaVariable_plantadora=tasaVariable_plantadora
    plantadora.transporte_plantadora=transporte_plantadora
    plantadora.imagen_plantadora=imagen_plantadora
    plantadora.stock_plantadora=stock_plantadora

    db.session.commit()    # confirma el cambio
    return plantadora_schema.jsonify(plantadora)    # y retorna un json con la plantadora

@app.route('/plantadoras/<id_plantadoras>',methods=['DELETE'])
def delete_plantadora(id_plantadoras):
    plantadora=Plantadora.query.get(id_plantadoras)
    db.session.delete(plantadora)
    db.session.commit()                     # confirma el delete
    return plantadora_schema.jsonify(plantadora) # me devuelve un json con el registro eliminado
