from flask import Flask
from view.oloko import loca1

# Eis aqui as dependencias para fazer bundle ^^
from flask_assets import Environment, Bundle

app = Flask(__name__)

# Preparando tudo para deixar voando
assets = Environment(app)

# Aqui que a mágica acontece
app.register_blueprint(loca1)
