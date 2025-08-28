from flask import Flask, redirect, request, abort, make_response
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/identificacao">Identificação</a></li>
        <li><a href="/contexto">Contexto da Requisição</a></li>
    </ul>
    """

@app.route('/identificacao')
def identificacao():
    return """
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Aluno: Carlos Custódio</h2>
    <h2>Prontuário: PT3032043</h2>
    <h2>Instituição: IFSP</h2>
    <p>
        <a href="/">Voltar</a>
    </p>
    """

@app.route('/contexto')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    ip_remoto = request.remote_addr
    host_app = request.host

    return f"""
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Seu navegador é: {user_agent}</h2>
    <h2>O IP do computador remoto é: {ip_remoto}</h2>
    <h2>O host da aplicação é: {host_app}</h2>
    <p>
        <a href="/">Voltar</a>
    </p>
    """

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
