class Participante:
    def __init__(self, nome, idade, endereco, reside_em_sp):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.reside_em_sp = reside_em_sp


class Evento:
    def __init__(self):
        # Lista para armazenar participantes e número máximo de vagas
        self.participantes = []
        self.vagas_disponiveis = 50

    def cadastrar_participante(self, nome, idade, endereco, reside_em_sp):
        # Criar um objeto Participante
        participante = Participante(nome, idade, endereco, reside_em_sp)
        
        # Adicionar participante à lista
        self.participantes.append(participante)
        
        # Verificar as condições de elegibilidade
        self.verificar_condicoes(participante)

    def verificar_condicoes(self, participante):
        # Verificar idade mínima
        if not participante.idade >= 18:
            print("Desculpe, apenas maiores de idade podem se inscrever.")
            self.participantes.remove(participante)
            return
        
        # Verificar se o participante reside em São Paulo
        if not participante.reside_em_sp:
            print("Desculpe, a participação é restrita a moradores de São Paulo.")
            self.participantes.remove(participante)
            return
        
        # Verificar a disponibilidade de vagas
        self.verificar_vagas_disponiveis()

    def verificar_vagas_disponiveis(self):
        # Verificar se há vagas disponíveis
        if self.vagas_disponiveis == 0:
            print("Desculpe, as inscrições estão encerradas.")
            return
        
        # Reduzir o número de vagas disponíveis
        self.vagas_disponiveis -= 1
        print("Inscrição validada. Bem-vindo(a) ao evento!")


evento = Evento()

# Interagir com o usuário para realizar o cadastro de participantes
while True:
    # Obter informações do participante do usuário
    nome = input("Digite o nome do participante (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break

    idade = int(input("Digite a idade do participante: "))
    endereco = input("Digite o endereço do participante: ")
    reside_em_sp = input("O participante reside em São Paulo? Digite 'sim' ou 'nao': ")

    # Converter a resposta para um valor booleano
    reside_em_sp = True if reside_em_sp.lower() == "sim" else False

    # Cadastrar o participante no evento
    evento.cadastrar_participante(nome, idade, endereco, reside_em_sp)
