# A very simple Flask Hello World app for you to get started with...
from flask import Flask, redirect, request, abort, make_response
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><h2>Disciplina PTBDSWS</h2>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/redirecionamento')
def redirecionar():
    return redirect("https://ptb.ifsp.edu.br/")

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/abortar')
def abortar():
    abort(404)

@app.route('/objetoresposta')
def objeto_resposta():
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.headers["X-Custom-Header"] = "MeuHeader"
    return response

@app.route('/codigostatusdiferente')
def codigo_status_diferente():
    return "Bad request", 400
