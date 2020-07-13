from flask import Blueprint
from flask import jsonify
from flask import request
from flask import render_template
from RSSParser import RssParser

api = Blueprint("api", __name__)

@api.route('/', methods=['POST'])
def my_form_post():
    url = request.form['urlRSS']
    leitor = RssParser(url)
    if not leitor.noticias:
        return render_template('app/erro_leitura.html', url_leitura = url)
    else:
        return render_template('app/noticias.html', url_leitura = url, conteudo = leitor.detalhes_conteudo, 
                            noticias = leitor.noticias)