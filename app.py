from flask import Flask, render_template, request, redirect, url_for
from jinja2 import BaseLoader, Template

app = Flask(__name__)

class GlitchLoader(BaseLoader):
    def get_source(self, environment, template):
        url = f'https://uncovered-amazing-cucumber.glitch.me/{template}'
        response = requests.get(url)
        return response.text, url, lambda: True

app.jinja_env.loader = GlitchLoader()

class Participante:
    def __init__(self, nome, idade, endereco, reside_em_sp):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.reside_em_sp = reside_em_sp

class Evento:
    def __init__(self):
        self.participantes = []
        self.vagas_disponiveis = 50

    def cadastrar_participante(self, nome, idade, endereco, reside_em_sp):
        participante = Participante(nome, idade, endereco, reside_em_sp)
        self.participantes.append(participante)
        self.verificar_condicoes(participante)

    def verificar_condicoes(self, participante):
        if not participante.idade >= 18:
            print("Desculpe, apenas maiores de idade podem se inscrever.")
            self.participantes.remove(participante)
            return
        if not participante.reside_em_sp:
            print("Desculpe, a participação é restrita a moradores de São Paulo.")
            self.participantes.remove(participante)
            return
        self.verificar_vagas_disponiveis()

    def verificar_vagas_disponiveis(self):
        if self.vagas_disponiveis == 0:
            print("Desculpe, as inscrições estão encerradas.")
            return
        self.vagas_disponiveis -= 1
        print("Inscrição validada. Bem-vindo(a) ao evento!")

evento = Evento()

@app.route('/')
def index():
    return render_template('index.html', participantes=evento.participantes)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        endereco = request.form['endereco']
        reside_em_sp = request.form['reside_em_sp'].lower() == 'sim'  # Alteração aqui

        evento.cadastrar_participante(nome, idade, endereco, reside_em_sp)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
