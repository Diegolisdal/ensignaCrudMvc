from app import db,ma,app

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

class CosechadoraSchema(ma.Schema):
    class Meta:
        fields=('id_cosechadoras','modelo_cosechadora','motor_cosechadora','potencia_cosechadora','plataforma_cosechadora','capacidadTolva_cosechadora','CapacidadDescarga_cosechadora','PilotoAuto_cosechadora','jdlink_cosechadora','combine_cosechadora','activeyield_cosechadora','imagen_cosechadora','stock_cosechadora')

cosechadora_schema=CosechadoraSchema()            
cosechadoras_schema=CosechadoraSchema(many=True)  
