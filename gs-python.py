
print("Agendamento de exame e ficha do paciente "
      "\ninsira os dados do pacientes:")

from datetime import datetime

import re


class Cor:
    RESET = '\033[0m'
    CINZA = '\033[37m'
    VERDE = '\033[36m'
    ROSA = '\033[95m'  # Rosa
    AZUL = '\033[94m'


#função para verificar se o telefone do usuário está no formato válido
def verificaTelefone(var):
    padrao = re.compile(r'^\(\d{2}\) \d{5}-\d{4}$')
    if padrao.match(var):
        return True
    else:
        return False


#Função para verificar se a data do usuário está no formato válido
def verificaData(data):
    try:
        datetime.strptime(data, '%d-%m-%Y')
        return True
    except ValueError:
        return False


#Função para verificar se o input do usuário é um número inteiro
def verificaNum(var, msg, alerta):
    while not var.isnumeric():
        print(alerta)
        var = input(msg)
    var = int(var)
    return var

#Função para verificar se o input do usuário é uma opção válida cadastrada
def verificaLista(var, lista, msg, alerta):
    while var not in lista:
        print(alerta)
        var = input(msg)
    return var

#Função para verificar se a opção do usuário é sim ou nao
def verificaOpcao(var, msg):
    listaOpcao = ["sim", "nao"]
    while var not in listaOpcao:
        print(f"A resposta deve ser: {listaOpcao}")
        var = input(msg)
    if var == listaOpcao[0]:
        return True
    else:
        return None

def listaAppend(var, msg):
    fichaPaciente.append(f"{Cor.CINZA}{msg}{Cor.RESET}{Cor.VERDE}{var}{Cor.RESET}")

fichaPaciente = []

nome = input("Nome do paciente:")
listaAppend(nome, "nome do paciente:")

idade = input("Idade do paciente:")
idade = verificaNum(idade,"Idade do paciente",
                    "A Idade deve ser cadastrada em números inteiros(1, 10, 55, 80 etc...)" )
listaAppend(idade, "Idade do paciente:")


while True:
    dataNascimento = input("Data de nascimento do paciente DD-MM-YYYY:")

    if verificaData(dataNascimento) == True:
        break
    else:
        print("Data de nascimento inválida, deve ser preenchida neste formato: DD-MM-YYYY")
listaAppend(dataNascimento, "Data de Nascimento:")

endereco = input("Endereço do paciente:")
listaAppend(endereco, "Endereço:")

while True:
    telefone = input("Telefone para contato do paciente ex (dd) 92118-4570:")

    if verificaTelefone(telefone) == True:
        break
    else:
        print("Formato de telefone inválido!")
listaAppend(telefone, "Telefone(cel):")


listaSexo = ["masculino", "feminino"]

sexo = input("Sexo do paciente:")
sexo = verificaLista(sexo, listaSexo, "Sexo do paciente:",
                     f"O sexo deve ser uma opção válida ex:{listaSexo}")
listaAppend(sexo,"Sexo:")


listaSangue = ["a-", "a+", "b+", "b-", "ab+", "ab-", "o+", "o-"]

tipoSanguineo = input("Tipo Sanguíneo do paciente:")
tipoSanguineo = verificaLista(tipoSanguineo, listaSangue, "Tipo Sanguíneo do paciente:",
                              f"O tipo sanguíneo deve ser uma opção existente ex:{listaSangue}")
listaAppend(tipoSanguineo, "Tipo Sanguíneo:")


opcaoAlergia = input("O paciente tem alguma alergia?")
opcaoAlergia = verificaOpcao(opcaoAlergia,"O paciente tem alguma alergia?")

if opcaoAlergia is not None:
    alergia = input("Qual?")
    listaAppend(alergia, "Alergia:")


opcaoSaudeCronico = input("O paciente tem algum problema de saúde crônico?")
opcaoSaudeCronico = verificaOpcao(opcaoSaudeCronico,"O paciente tem algum problema de saúde crônico?")

if opcaoSaudeCronico is not None:
    saudeCronico = input("Qual?")
    listaAppend(saudeCronico, "Problema de saúde crônico:")


listaPrioritario = ["pcd", "idoso", "gestante"]

opcaoPrioridade = input("O paciente é prioritário?")
opcaoPrioridade = verificaOpcao(opcaoPrioridade, "O paciente é prioritário?")

if opcaoPrioridade is not None:
    prioritario = input(f"Qual das categorias:{listaPrioritario}")
    prioritario = verificaLista(prioritario, listaPrioritario, f"Qual das categorias:{listaPrioritario}",
                                f'A opção deve ser uma destas :{listaPrioritario}')
    listaAppend(prioritario, "Atendimento priotitário:")


listaExames = ["raio-x", "ultrassom", "tomografia", "ressonancia", "ecocardiograma"]

exame = input(f"{listaExames} \n Exame que deseja realizar:")
exame = verificaLista(exame, listaExames, f"{listaExames} \n Exame que deseja realizar:",
                     "Escolha entre uma das opções apresentadas!")
listaAppend(exame, "Pedido de Exame:")


while True:
    dataExame = input("Data para realização do exame DD-MM-YYYY:")

    if verificaData(dataExame) == True:
        print("Agendamento realizado com sucesso!")
        break
    else:
        print("Data inválida, deve ser preenchido neste formado: DD-MM-YYYY (dia-mês-ano).")
listaAppend(dataExame, "Data do Exame:")


print(f"{Cor.VERDE}Ficha completa do paciente{Cor.RESET}")
for i in range(len(fichaPaciente)):
    print(fichaPaciente[i])


print(f"Muito Obrigado por utilizar os serviços do {Cor.ROSA}Healt{Cor.RESET}{Cor.AZUL}Connect{Cor.RESET}")
