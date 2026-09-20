import json
import os
from funcoes_financeiro import *

# verificar se o programa existe arquivo, se não existir, criar um arquivo.
verificacao()

banco_inicial = leitura_banco_dados()

# Define o contador com base na quantidade de itens que já existem
# Se já existem 2 ganhos, len() será 2. No loop, ele somará +1 e o próximo ID será 3.

# Pega o último item da lista ([-1]) e olha o "id" dele. Se a lista estiver vazia, começa com 0.
cont = banco_inicial["ganhos"][-1]["id"] if banco_inicial["ganhos"] else 0
cont_1 = banco_inicial["despesas"][-1]["id"] if banco_inicial["despesas"] else 0
while True:
    print("-" * 23)
    print("Gerenciador Financeiro")
    print("-" * 23)

    print()

    saldo_ganho = soma_valor("ganhos")
    saldo_despesa = soma_valor("despesas")
    saldo_liquido = saldo_ganho - saldo_despesa

    print(f"Saldo Ganhos: R$ {saldo_ganho:.2f}")
    print(f"Saldo Despesas: R$ {saldo_despesa:.2f}")
    if saldo_liquido < 0:
        print(f"Saldo liquido: R$ \033[31m{abs(saldo_liquido):.2f}\033[m")
    else:
        print(f"Saldo liquido: R$ \033[32m{saldo_liquido:.2f}\033[m")

    print()

    print("Opções:\n\n[1] Receita\n[2] Despesas\n[3] Lista Receita\n[4] Lista Despesa\n[5] Sair")

    print()
    try:
        escolha = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite apenas o número !")
        print()
        continue

    os.system("clear")
    if escolha == 1:
        try:
            print("=" * 30)
            print(f'{"Receitas":^30}')
            print("=" * 30)

            print()

            cont += 1
            receita = dados_padrao(cont)
            atualiza_banco("ganhos", receita)
            print()
        except ValueError:
            print("Valor incorreto")
            print("Digite apenas números!")
            continue
    elif escolha == 2:
        try:
            print("=" * 30)
            print(f'{"Despesas":^30}')
            print("=" * 30)

            print()

            cont_1 += 1
            despesa = dados_padrao(cont_1)
            atualiza_banco("despesas", despesa)
            
        except ValueError:
            print("Valor incorreto")
            print("Digite apenas números!")
            continue
    elif escolha == 3:
        ver_lista("ganhos")
        print()
        apagar_item_lista("ganhos")
    elif escolha == 4:
        ver_lista("despesas")
        print()
        apagar_item_lista("despesas")
    elif escolha == 5:
        print("Saindo . . .")
        break
    elif escolha < 1 or escolha > 5:
        print("Digite o valor correspondente as opções anexadas !'")
        print()
        continue
    