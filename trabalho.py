cliente = {
"nome": input("Digite seu nome: ").strip(), # Guarda o nome do cliente
"email": input("Digite seu e-mail: ").strip(), # Guarda o e-mail
"saldo": float(input("Digite seu saldo inicial (R$): ").strip()) # Saldo convertido
}

# -----------------------------------------
# TABELA DE PREÇOS 
# -----------------------------------------
# Dicionário que funciona como a "tabela FIPE" dos carros, com valores fixos.

tabela_precos = {
"911": 3500.00,
"750S": 2890.00,
"M5": 5555.99
}

carros_para_aluguel = [
("M5","BMW"),
("911", "PORSCHE"),
("750S","MCLAREN")
]

carros_para_venda = [
("M5","BMW"),
("911", "PORSCHE"),
("750S","MCLAREN")
]

#menu principal 
def menu_principal():
    print("===bem vindo ao sistema de aluguel a venda de carros===")
    print("1. alugar carro")
    print("2. comprar carro")
    print("3. sair")
    print("4. ver saldo")

#funçãa para aluagar carro 
def alugar_carro():
    print("=== carros disponiveis para aluguel ===")
    for i in range(len(carros_para_aluguel)):
        print(f"- {carros_para_aluguel[i]} ")

    escolha = input("Digite o nome do carro que deseja alugar: ").strip()

    modelos_disponiveis = [carro[0] for carro in carros_para_aluguel]

    if escolha in modelos_disponiveis:
        preco = tabela_precos.get(escolha, None)
        if preco:
            if cliente["saldo"] >= preco:
                cliente["saldo"] -= preco
                print(f"Você alugou o carro {escolha} por R$ {preco:.2f}.")
            else:
                print("Saldo insuficiente para alugar este carro.")
        else:
            print("Carro não encontrado na tabela de preços.")
    else:
        print("Carro indisponível para aluguel.")

#função para comprar carro
def comprar_carro():
    print("=== carros disponiveis para venda ===")
    for carro in carros_para_venda:
        print(f"- {carro[0]} , {carro[1]}")

    escolha = input("Digite o nome do carro que deseja comprar: ").strip()

    modelos_disponiveis = [carro[0] for carro in carros_para_venda]

    if escolha in modelos_disponiveis:
        preco = tabela_precos.get(escolha, None)
        if preco:
            if cliente["saldo"] >= preco:
                cliente["saldo"] -= preco
                print(f"Você comprou o carro {escolha} por R$ {preco:.2f}.")
            else:
                print("Saldo insuficiente para comprar este carro.")
        else:
            print("Carro não encontrado na tabela de preços.")
    else:
        print("Carro indisponível para venda.")

#função para ver saldo
def ver_saldo():
    print(f"Seu saldo atual é R$ {cliente['saldo']:.2f}.")

#loop principal
while True:
    menu_principal()
    escolha = input("Digite um número de 1 a 4: ")

    if escolha == "1":
        alugar_carro()
    elif escolha == "2":
        comprar_carro()
    elif escolha == "3":
        print("Obrigado por usar o sistema. Até logo!")
        break
    elif escolha == "4":
        ver_saldo()
    else:
        print("Opção inválida. Tente novamente.")
