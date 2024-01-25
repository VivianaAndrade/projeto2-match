# Cadastro de Participantes
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
endereco = input("Digite seu endereço: ")
residencia_sp = input("Você reside em São Paulo? (S/N): ")

# Verificação de Condições
if idade >= 18 and residencia_sp.upper() == "S":
    # Verificação de Vagas Disponíveis
    vagas_disponiveis = 50
    if vagas_disponiveis > 0:
        # Feedback aos Participantes
        print("Inscrição validada! Você está inscrito no evento.")
        vagas_disponiveis -= 1
    else:
        print("As inscrições estão encerradas.")
else:
    # Feedback aos Participantes
    if idade < 18:
        print("Desculpe, apenas maiores de idade podem se inscrever.")
    if residencia_sp.upper() != "S":
        print("Desculpe, a participação é restrita a moradores de São Paulo.")