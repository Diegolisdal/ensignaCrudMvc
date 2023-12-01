from app import db,ma,app

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

with app.app_context():
    db.create_all()  #  crea  tablas

class PlantadoraSchema(ma.Schema):
    class Meta:
        fields=('id_plantadoras','modelo_plantadora','nroDeLineas_plantadora','anchoDeLabor_plantadora','cajaCentral_plantadora','deslingue_plantadora','tasaVariable_plantadora','transporte_plantadora','imagen_plantadora','stock_plantadora')

plantadora_schema=PlantadoraSchema()            # El objeto plantadora_schema es para traer una plantadora
plantadoras_schema=PlantadoraSchema(many=True)  # El objeto plantadoras_schema es para traer multiples registros de plantadoras
