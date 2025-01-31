produtos = []

carrinho = {}

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    for produto in produtos:
        print(f"Nome: {produto['nome']} - Preço: R${produto['preco']} - Quantidade: {produto['quantidade']}")

def adicionar_carrinho():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))

    for produto in produtos:
        if produto["nome"] == nome:
            if nome in carrinho:
                carrinho[nome] += quantidade
            else:
                carrinho[nome] = quantidade
            print("Produto adicionado ao carrinho!")
            return

    print("Produto não encontrado!")

def exibir_carrinho():
    for produto, quantidade in carrinho.items():
        for p in produtos:
            if p["nome"] == produto:
                total = p["preco"] * quantidade
                print(f"Nome: {produto} - Quantidade: {quantidade} - Valor total: R${total}")

def finalizar_compra():
    total = 0
    for produto, quantidade in carrinho.items():
        for p in produtos:
            if p["nome"] == produto:
                total += p["preco"] * quantidade

    print(f"Total da compra: R${total}")

while True:
    print("\n--- Mercado ---")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Adicionar ao carrinho")
    print("4 - Exibir carrinho")
    print("5 - Finalizar compra")
    print("6 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        adicionar_carrinho()
    elif opcao == 4:
        exibir_carrinho()
    elif opcao == 5:
        finalizar_compra()
    elif opcao == 6:
        break
