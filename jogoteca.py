from flask import Flask, render_template, request

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

@app.route('/')
def index():
    return render_template('lista.html', titulo='Games', jogos=lista)

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
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(debug=True)

#app.run(host='0.0.0.0', port=8080)