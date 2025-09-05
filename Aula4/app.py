from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def home():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route("/user/<nome>/<prontuario>/<instituicao>")
def user_profile(nome = "Carlos Eduardo Custódio", prontuario="PT3032043", instituicao="IFSP"):

    return render_template('user.html', name=nome, prontuario=prontuario, instituicao=instituicao)

@app.route("/contextorequisicao/<nome>")
def contexto_requisicao(nome):
    user_agent = request.headers.get("User-Agent", "desconhecido")
    remote_ip  = request.remote_addr or "desconhecido"
    host       = request.host

    return render_template('requisicao.html',name=nome, user_agent=user_agent, remote_ip=remote_ip, host=host)  

@app.route('/rotainexistente')
def not_found_route():
    return render_template('notfound.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html'), 404
