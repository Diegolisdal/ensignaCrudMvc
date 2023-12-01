from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend



# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://diegolis3:ariel1234@diegolis3.mysql.pythonanywhere-services.com/diegolis3$maquinas'
# URI de la BBDD                      driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow

# defino las tablas
class Producto(db.Model):   # la clase Producto hereda de db.Model
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    modelo_plantadora=db.Column(db.String(200))
    nroDeLineas_plantadora=db.Column(db.String(200))
    anchoDeLabor_plantadora=db.Column(db.String(100))
    cajaCentral_plantadora=db.Column(db.String(200))
    deslingue_plantadora=db.Column(db.String(50))
    tasaVariable_plantadora=db.Column(db.String(100))
    transporte_plantadora=db.Column(db.String(200))
    stock_plantadora=db.Column(db.Integer)
    imagen_plantadora=db.Column(db.String(400))
    modelo_tractor=db.Column(db.String(200))
    motor_tractor=db.Column(db.String(200))
    potencia_tractor=db.Column(db.String(200))

    def __init__(self,modelo_plantadora,nroDeLineas_plantadora,anchoDeLabor_plantadora,cajaCentral_plantadora,deslingue_plantadora,tasaVariable_plantadora,transporte_plantadora,stock_plantadora,imagen_plantadora,modelo_tractor,motor_tractor,potencia_tractor):   #crea el  constructor de la clase
        self.modelo_plantadora=modelo_plantadora   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.nroDeLineas_plantadora=nroDeLineas_plantadora
        self.anchoDeLabor_plantadora=anchoDeLabor_plantadora
        self.cajaCentral_plantadora=cajaCentral_plantadora
        self.deslingue_plantadora=deslingue_plantadora
        self.tasaVariable_plantadora=tasaVariable_plantadora
        self.transporte_plantadora=transporte_plantadora
        self.stock_plantadora=stock_plantadora
        self.imagen_plantadora=imagen_plantadora
        self.modelo_tractor=modelo_tractor
        self.motor_tractor=motor_tractor
        self.potencia_tractor=potencia_tractor


    #  si hay que crear mas tablas , se hace aqui

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','modelo_plantadora','nroDeLineas_plantadora','anchoDeLabor_plantadora','cajaCentral_plantadora','deslingue_plantadora','tasaVariable_plantadora','transporte_plantadora','stock_plantadora','imagen_plantadora','modelo_tractor','motor_tractor','potencia_tractor')




producto_schema=ProductoSchema()            # El objeto producto_schema es para traer un producto
productos_schema=ProductoSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto




# crea los endpoint o rutas (json)
@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro




@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()                     # confirma el delete
    return producto_schema.jsonify(producto) # me devuelve un json con el registro eliminado


@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
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
    modelo_tractor=request.json['modelo_tractor']
    motor_tractor=request.json['motor_tractor']
    potencia_tractor=request.json['potencia_tractor']
    new_producto=Producto(modelo_plantadora,nroDeLineas_plantadora,anchoDeLabor_plantadora,cajaCentral_plantadora,deslingue_plantadora,tasaVariable_plantadora,transporte_plantadora,stock_plantadora,imagen_plantadora,modelo_tractor,motor_tractor,potencia_tractor)
    db.session.add(new_producto)
    db.session.commit() # confirma el alta
    return producto_schema.jsonify(new_producto)


@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)

    modelo_plantadora=request.json['modelo_plantadora']
    nroDeLineas_plantadora=request.json['nroDeLineas_plantadora']
    anchoDeLabor_plantadora=request.json['anchoDeLabor_plantadora']
    cajaCentral_plantadora=request.json['cajaCentral_plantadora']
    deslingue_plantadora=request.json['deslingue_plantadora']
    tasaVariable_plantadora=request.json['tasaVariable_plantadora']
    transporte_plantadora=request.json['transporte_plantadora']
    stock_plantadora=request.json['stock_plantadora']
    imagen_plantadora=request.json['imagen_plantadora']
    modelo_tractor=request.json['modelo_tractor']
    motor_tractor=request.json['motor_tractor']
    potencia_tractor=request.json['potencia_tractor']


    producto.modelo_plantadora=modelo_plantadora
    producto.nroDeLineas_plantadora=nroDeLineas_plantadora
    producto.anchoDeLabor_plantadora=anchoDeLabor_plantadora
    producto.cajaCentral_plantadora=cajaCentral_plantadora
    producto.deslingue_plantadora=deslingue_plantadora
    producto.tasaVariable_plantadora=tasaVariable_plantadora
    producto.transporte_plantadora=transporte_plantadora
    producto.stock_plantadora=stock_plantadora
    producto.imagen_plantadora=imagen_plantadora
    producto.modelo_tractor=modelo_tractor
    producto.motor_tractor=motor_tractor
    producto.potencia_tractor=potencia_tractor
    db.session.commit()    # confirma el cambio
    return producto_schema.jsonify(producto)    # y retorna un json con el producto




@app.route('/')
def hello_world():
    return 'Hello from Flask!'

