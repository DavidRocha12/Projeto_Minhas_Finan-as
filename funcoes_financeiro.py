import json
import os

def leitura_banco_dados():
    # Leitura do arquivo de dados para manipulação de dados
    with open("financeiro.json", "r", encoding="utf-8") as arquivo:
        banco_dados = json.load(arquivo)
    return banco_dados


def salvar_banco_dados(dados):
    # atualiza dados arquivo gravando o que foi modificado.
    with open("financeiro.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)


def verificacao():
    """Verificando se existe arquivo, se não existir o arquivo vai ser criado."""
    try:
        banco_dados = leitura_banco_dados()
    # Se não existir vai criar o arquivo
    except FileNotFoundError:
        banco_dados = {
            "ganhos" : [],
            "despesas" : []
        }

    salvar_banco_dados(banco_dados)


def dados_padrao(contador):
    """Variáveis de entrada de Dados, sendo adicionados em um dicionário."""
    entrada = input("Descrição: ").title()
    preco = float(input("Valor: R$ "))

    tipo_despesa = {
        "id" : contador,
        "Descricao" : entrada,
        "Valor" : preco}
    return tipo_despesa


def atualiza_banco(opcao, tipo_despesa):
   # Leitura de Dados
    banco_dados = leitura_banco_dados()

    # Obs.:
    # você adiciona diretamente a lista existente, sem precisar usar o for, o for é utilizado apenas para
    # fazer a leitura e mostrar na tela, se adicionar utilizando o for vai duplicar os valores da lista.
    banco_dados[opcao].append(tipo_despesa)

     # Salvando arquivo com dados atualizados
    salvar_banco_dados(banco_dados)


def ver_lista(tipo):
    # Designe de visualização da lista do arquivo
    banco = leitura_banco_dados()

    print("*" * 40)
    titulo = f"Lista de {tipo}"
    print(f"{titulo:^40}")
    print("*" * 40)

    print()
    if banco[tipo]:
        for item in banco[tipo]:
            print(f'{item["id"]} - {item["Descricao"] :.<28} R$ {float(item["Valor"]):.2f}')
    else:
        print("Lista vazia!")


def apagar_item_lista(tipo):
    # Removendo itens da lista selecionando o item desejado
    banco_dados = leitura_banco_dados()
    if banco_dados[tipo]:
        print()
        try:
            escolha_dados = input("Deseja apagar algum item da lista? [S]im/[N]ão ")
            print()
            if escolha_dados[0] in "Ss":
                id_apagar = int(input("Digite o id do item a ser apagado: "))
                apagar = None
                for id, valor in enumerate(banco_dados[tipo]):
                    if id_apagar == valor["id"]:
                        apagar = id
                if apagar is not None:
                    banco_dados[tipo].pop(apagar)
                    salvar_banco_dados(banco_dados)
                    print()
                    print("Item apagado com Sucesso!")
                else:
                    print("Id inválido, verifique o Id correto!")
            elif escolha_dados[0] in "Nn":
                os.system("clear")
                print("Voltando para o menu principal!")
            else:
                os.system("clear")
                print("Digite apenas Sim ou Não!")
        except IndexError:
            os.system("clear")
            print("Nada foi informado! \nVoltando ao Menu!")
    else:
        print("Não existe nada a ser apagado!")


def soma_valor(tipo):
    # Soma de valores para mostrar saldos
    banco_de_dados = leitura_banco_dados()

    soma = 0
    for item in banco_de_dados[tipo]:
        soma += item["Valor"]

    return soma