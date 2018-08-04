# Módulos que serão usados
from flask import Blueprint, render_template, Flask
from flask_assets import Environment, Bundle

loca1 = Blueprint('loca1', __name__,
                        template_folder='template')

@loca1.route('/loca1/<NomeDoFulano>')
def show(NomeDoFulano):
	#return "pois é " + NomeDoFulano + " python é isso"
	return render_template("boas-vindas.html",nome=NomeDoFulano)
