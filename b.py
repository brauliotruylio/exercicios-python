def adicionar_produto(produtos_nomes, produtos_quantidades, nome, quantidade):
    produtos_nomes.append(nome)
    produtos_quantidades.append(quantidade)
    print(f"Produto '{nome}' adicionado com quantidade {quantidade}.")

def listar_produtos(produtos_nomes, produtos_quantidades):
    print("Lista de Produtos:")
    for nome, quantidade in zip(produtos_nomes, produtos_quantidades):
        print(f"{nome}: {quantidade} unidades")

def substituir_produto(produtos_nomes, nome_antigo, nome_novo):
    if nome_antigo in produtos_nomes:
        indice = produtos_nomes.index(nome_antigo)
        produtos_nomes[indice] = nome_novo
        print(f"Produto '{nome_antigo}' substituído por '{nome_novo}'.")
    else:
        print(f"Produto '{nome_antigo}' não encontrado na lista.")

produtos_nomes = []
produtos_quantidades = []

while True:
    print("\nMenu:")
    print("1. Listar produtos")
    print("2. Adicionar produto")
    print("3. Substituir produto")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_produtos(produtos_nomes, produtos_quantidades)
    elif opcao == "2":
        nome = input("Digite o nome do novo produto: ")
        quantidade = int(input("Digite a quantidade do novo produto: "))
        adicionar_produto(produtos_nomes, produtos_quantidades, nome, quantidade)
    elif opcao == "3":
        nome_antigo = input("Digite o nome do produto a ser substituído: ")
        nome_novo = input("Digite o nome do novo produto: ")
        substituir_produto(produtos_nomes, nome_antigo, nome_novo)
    elif opcao == "4":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Escolha novamente.")