from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://diegolis3:ariel1234@diegolis3.mysql.pythonanywhere-services.com/diegolis3$maquina4'
# URI de la BBDD                      driver de la BD  user:clave@URLBBDD/nombreBBDD

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none

db= SQLAlchemy(app)   #crea el objeto db plantadora de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma plantadora de de la clase Marshmallow

# tabla plantadora
class Plantadora(db.Model):   # la clase plantadora hereda de db.Model
    id_plantadoras=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    modelo_plantadora=db.Column(db.String(200))
    nroDeLineas_plantadora=db.Column(db.String(200))
    anchoDeLabor_plantadora=db.Column(db.String(100))
    cajaCentral_plantadora=db.Column(db.String(200))
    deslingue_plantadora=db.Column(db.String(100))
    tasaVariable_plantadora=db.Column(db.String(100))
    transporte_plantadora=db.Column(db.String(200))    
    imagen_plantadora=db.Column(db.String(400))
    stock_plantadora=db.Column(db.Integer)
    
    def __init__(self,modelo_plantadora,nroDeLineas_plantadora,anchoDeLabor_plantadora,cajaCentral_plantadora,deslingue_plantadora,tasaVariable_plantadora,transporte_plantadora,stock_plantadora,imagen_plantadora):   #crea el  constructor de la clase
        self.modelo_plantadora=modelo_plantadora   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.nroDeLineas_plantadora=nroDeLineas_plantadora
        self.anchoDeLabor_plantadora=anchoDeLabor_plantadora
        self.cajaCentral_plantadora=cajaCentral_plantadora
        self.deslingue_plantadora=deslingue_plantadora
        self.tasaVariable_plantadora=tasaVariable_plantadora
        self.transporte_plantadora=transporte_plantadora
        self.stock_plantadora=stock_plantadora
        self.imagen_plantadora=imagen_plantadora    

# tabla tractor
class Tractor(db.Model):   # la clase Tractor hereda de db.Model
    id_tractores=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    modelo_tractor=db.Column(db.String(200))
    motor_tractor=db.Column(db.String(200))
    potencia_tractor=db.Column(db.String(100))
    transmision_tractor=db.Column(db.String(200))
    toma_tractor=db.Column(db.String(100))
    sistema_tractor=db.Column(db.String(100))
    levante_tractor=db.Column(db.String(200))
    imagen_tractor=db.Column(db.String(400))
    stock_tractor=db.Column(db.Integer)
    
    def __init__(self,modelo_tractor,motor_tractor,potencia_tractor,transmision_tractor,toma_tractor,sistema_tractor,levante_tractor,imagen_tractor,stock_tractor):   #crea el  constructor de la clase
        self.modelo_tractor=modelo_tractor   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.motor_tractor=motor_tractor
        self.potencia_tractor=potencia_tractor
        self.transmision_tractor=transmision_tractor
        self.toma_tractor=toma_tractor
        self.sistema_tractor=sistema_tractor
        self.levante_tractor=levante_tractor
        self.imagen_tractor=imagen_tractor
        self.stock_tractor=stock_tractor    

# tabla cosechadora
class Cosechadora(db.Model):   # la clase Cosechadora hereda de db.Model
    id_cosechadoras=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    modelo_cosechadora=db.Column(db.String(200))
    motor_cosechadora=db.Column(db.String(200))
    potencia_cosechadora=db.Column(db.String(100))
    plataforma_cosechadora=db.Column(db.String(200))
    capacidadTolva_cosechadora=db.Column(db.String(100))
    CapacidadDescarga_cosechadora=db.Column(db.String(100))
    PilotoAuto_cosechadora=db.Column(db.String(200))
    jdlink_cosechadora=db.Column(db.String(200))
    combine_cosechadora=db.Column(db.String(200))
    activeyield_cosechadora=db.Column(db.String(200))
    imagen_cosechadora=db.Column(db.String(400))
    stock_cosechadora=db.Column(db.Integer)
    
    def __init__(self,modelo_cosechadora,motor_cosechadora,potencia_cosechadora,plataforma_cosechadora,capacidadTolva_cosechadora,CapacidadDescarga_cosechadora,PilotoAuto_cosechadora,jdlink_cosechadora,combine_cosechadora,activeyield_cosechadora,imagen_cosechadora,stock_cosechadora):   #crea el  constructor de la clase
        self.modelo_cosechadora=modelo_cosechadora   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.motor_cosechadora=motor_cosechadora
        self.potencia_cosechadora=potencia_cosechadora
        self.plataforma_cosechadora=plataforma_cosechadora
        self.capacidadTolva_cosechadora=capacidadTolva_cosechadora
        self.CapacidadDescarga_cosechadora=CapacidadDescarga_cosechadora
        self.PilotoAuto_cosechadora=PilotoAuto_cosechadora
        self.jdlink_cosechadora=jdlink_cosechadora
        self.combine_cosechadora=combine_cosechadora
        self.activeyield_cosechadora=activeyield_cosechadora
        self.imagen_cosechadora=imagen_cosechadora
        self.stock_cosechadora=stock_cosechadora    

with app.app_context():
    db.create_all()  #  crea  tablas
   
#  ************************************************************



class PlantadoraSchema(ma.Schema):
    class Meta:
        fields=('id_plantadoras','modelo_plantadora','nroDeLineas_plantadora','anchoDeLabor_plantadora','cajaCentral_plantadora','deslingue_plantadora','tasaVariable_plantadora','transporte_plantadora','imagen_plantadora','stock_plantadora')

plantadora_schema=PlantadoraSchema()            # El objeto plantadora_schema es para traer una plantadora
plantadoras_schema=PlantadoraSchema(many=True)  # El objeto plantadoras_schema es para traer multiples registros de plantadoras

class TractorSchema(ma.Schema):
    class Meta:
        fields=('id_tractores','modelo_tractor','motor_tractor','potencia_tractor','transmision_tractor','toma_tractor','sistema_tractor','levante_tractor','imagen_tractor','stock_tractor')

tractor_schema=TractorSchema()           
tractores_schema=TractorSchema(many=True)  

class CosechadoraSchema(ma.Schema):
    class Meta:
        fields=('id_cosechadoras','modelo_cosechadora','motor_cosechadora','potencia_cosechadora','plataforma_cosechadora','capacidadTolva_cosechadora','CapacidadDescarga_cosechadora','PilotoAuto_cosechadora','jdlink_cosechadora','combine_cosechadora','activeyield_cosechadora','imagen_cosechadora','stock_cosechadora')

cosechadora_schema=CosechadoraSchema()            
cosechadoras_schema=CosechadoraSchema(many=True)  

# crea los endpoint o rutas (json)

#GET plantadoras
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

#GET tractores
@app.route('/tractores',methods=['GET'])
def get_Tractores():
    all_tractores=Tractor.query.all()         
    result=tractores_schema.dump(all_tractores)                                                   
    return jsonify(result)       
               
@app.route('/tractores/<id_tractores>',methods=['GET'])
def get_tractor(id_tractores):
    tractor=Tractor.query.get(id_tractores)
    return tractor_schema.jsonify(tractor)  
 
#GET cosechadoras
@app.route('/cosechadoras',methods=['GET'])
def get_Cosechadoras():
    all_cosechadoras=Cosechadora.query.all()         
    result=cosechadoras_schema.dump(all_cosechadoras)                                                   
    return jsonify(result)      
                 
@app.route('/cosechadoras/<id_cosechadoras>',methods=['GET'])
def get_cosechadora(id_cosechadoras):
    cosechadora=Cosechadora.query.get(id_cosechadoras)
    return cosechadora_schema.jsonify(cosechadora)   


#DELETE plantadoras
@app.route('/plantadoras/<id_plantadoras>',methods=['DELETE'])
def delete_plantadora(id_plantadoras):
    plantadora=Plantadora.query.get(id_plantadoras)
    db.session.delete(plantadora)
    db.session.commit()                     # confirma el delete
    return plantadora_schema.jsonify(plantadora) # me devuelve un json con el registro eliminado

#DELETE tractores
@app.route('/tractores/<id_tractores>',methods=['DELETE'])
def delete_tractor(id_tractores):
    tractor=Tractor.query.get(id_tractores)
    db.session.delete(tractor)
    db.session.commit()                     
    return tractor_schema.jsonify(tractor) 

#DELETE cosechadoras
@app.route('/cosechadoras/<id_cosechadoras>',methods=['DELETE'])
def delete_cosechadora(id_cosechadoras):
    cosechadora=Cosechadora.query.get(id_cosechadoras)
    db.session.delete(cosechadora)
    db.session.commit()                     
    return cosechadora_schema.jsonify(cosechadora) 

#POST plantadoras
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

#POST tractores
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

#POST cosechadoras
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


#PUT plantadoras
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

#PUT tractores
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

#PUT cosechadoras
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


@app.route('/')
def hello_world():
    return 'FUNCIONAAAAAAA'

