from app import db,ma,app

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

with app.app_context():
    db.create_all()  #  crea  tablas

class TractorSchema(ma.Schema):
    class Meta:
        fields=('id_tractores','modelo_tractor','motor_tractor','potencia_tractor','transmision_tractor','toma_tractor','sistema_tractor','levante_tractor','imagen_tractor','stock_tractor')

tractor_schema=TractorSchema()           
tractores_schema=TractorSchema(many=True)  

