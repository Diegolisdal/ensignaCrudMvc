from flask import Flask, jsonify, request
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_cors import CORS
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://diegolis3:ariel1234@diegolis3.mysql.pythonanywhere-services.com/diegolis3$maquina4'
# URI de la BBDD                      driver de la BD  user:clave@URLBBDD/nombreBBDD

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none

db= SQLAlchemy(app)   #crea el objeto db plantadora de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma plantadora de de la clase Marshmallow

from controladores.cosechadora_controlador import *
from controladores.plantadora_controlador import *
from controladores.tractor_controlador import *

