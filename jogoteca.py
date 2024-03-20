from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

game1 = Jogo('Tetris', 'Puzzle', 'Atari')
game2 = Jogo('God of War', 'Ação', 'Playstation')
game3 = Jogo('The Last of Us', 'Ação', 'Playstation')
game4 = Jogo('Grand Theft Auto', 'Ação', 'Playstation')
game5 = Jogo('Minecraft', 'Ação', 'Playstation')
game6 = Jogo('The Witcher', 'Ação', 'Playstation')
game7 = Jogo('The Legend of Zelda', 'Ação', 'Playstation')
game8 = Jogo('Super Mario', 'Plataforma', 'Nintendo')
lista = [game1, game2, game3, game4, game5, game6, game7, game8]

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Título Padrão', jogos=lista)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo='New Game')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' autenticado com sucesso!')
        return redirect('/')
    else:
        flash('Usuario: ' + session['usuario_logado'] + ' não logado')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Deslogado')
    return redirect('/')

app.run(debug=True)