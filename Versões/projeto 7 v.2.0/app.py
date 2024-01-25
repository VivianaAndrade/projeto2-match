from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ' ', 'templates')
app = Flask(__name__, template_folder=template_path)

app = Flask(__name__)
app.secret_key = 'chave_secreta'  # Usado para flashes de mensagens

class SistemaInscricaoEvento:
    def verificar_condicoes(self, nome, idade, endereco, sp_residencia, horario_disponivel):
        if idade < 18:
            flash("A participação é restrita a maiores de idade.", "warning")
            return False
        elif not sp_residencia:
            flash("A participação é restrita a moradores de São Paulo.", "warning")
            return False
        elif not horario_disponivel:
            flash("Os participantes devem atestar que o evento ocorre à noite.", "warning")
            return False
        else:
            return True

    def verificar_vagas_disponiveis(self, nome, idade, endereco, sp_residencia, horario_disponivel):
        # Verificar se ainda existem vagas disponíveis
        vagas_disponiveis = self.verificar_limite_vagas()

        if vagas_disponiveis > 0:
            self.salvar_participante(nome, idade, endereco, sp_residencia, horario_disponivel)
            flash("Inscrição validada com sucesso!", "success")
        else:
            flash("Desculpe, as inscrições estão encerradas.", "danger")

    def verificar_limite_vagas(self):
        # Verificar o limite de vagas a partir do arquivo CSV
        arquivo_csv = "participantes.csv"

        if not os.path.exists(arquivo_csv):
            # Se o arquivo CSV não existir, criar com o cabeçalho
            with open(arquivo_csv, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nome", "Idade", "Endereco", "Reside em SP", "Pode comparecer à noite"])

        with open(arquivo_csv, 'r') as file:
            # Contar o número de participantes já cadastrados
            reader = csv.reader(file)
            total_participantes = sum(1 for row in reader) - 1  # Descontar o cabeçalho

        # Definir o limite de vagas
        limite_vagas = 50
        vagas_disponiveis = limite_vagas - total_participantes
        return vagas_disponiveis

    def salvar_participante(self, nome, idade, endereco, sp_residencia, horario_disponivel):
        # Salvar informações do participante no arquivo CSV
        arquivo_csv = "participantes.csv"

        with open(arquivo_csv, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome, idade, endereco, sp_residencia, horario_disponivel])

@app.route('/', methods=['GET', 'POST'])
def index():
    sistema = SistemaInscricaoEvento()

    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        endereco = request.form['endereco']
        sp_residencia = 'Reside em SP' in request.form
        horario_disponivel = 'Pode comparecer à noite' in request.form

        if sistema.verificar_condicoes(nome, idade, endereco, sp_residencia, horario_disponivel):
            sistema.verificar_vagas_disponiveis(nome, idade, endereco, sp_residencia, horario_disponivel)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)