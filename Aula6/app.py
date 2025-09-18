from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chave forte'
bootstrap = Bootstrap(app)
moment = Moment(app)

class LoginForm(FlaskForm):
    username = StringField('', validators=[DataRequired()])
    password = PasswordField('', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class NameForm(FlaskForm):
    name = StringField('Informe o seu nome:', validators=[DataRequired()])
    sobrenome = StringField('Informe o seu sobrenome', validators=[DataRequired()])
    instituto = StringField('Informe a sua instituição de ensino', validators=[DataRequired()])
    disciplina = SelectField(
        'Informe a sua disciplina:',
        choices=[
            ('DSWA5', 'DSWA5'),
            ('DWBA4', 'DWBA4'),
            ('Gestão de projetos', 'Gestão de projetos')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Você alterou seu nome!')
        session['name'] = form.name.data
        session['sobrenome'] = form.sobrenome.data
        session['instituto'] = form.instituto.data
        session['disciplina'] = form.disciplina.data
        return redirect(url_for('home'))
    remote_addr = request.remote_addr
    host = request.host
    print("Sessão atual: ", dict(session))
    return render_template('index.html', form=form, name=session.get('name'), sobrenome=session.get('sobrenome'), instituto=session.get('instituto'), disciplina=session.get('disciplina'), remote_addr=remote_addr, host=host, current_time=datetime.utcnow())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        session['username'] = form.username.data
        return redirect(url_for('acesso'))
    return render_template('login.html', form=form, current_time=datetime.utcnow())

@app.route('/acesso')
def acesso():
    return render_template('acesso.html', username=session.get('username'), current_time=datetime.utcnow())

@app.route('/rotainexistente')
def not_found_route():
    return render_template('notfound.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html'), 404