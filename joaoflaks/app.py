from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "QualquerCoisa"
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3g1"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Usuario, Pizza, Pedido