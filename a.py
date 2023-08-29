class ControleEstoque:
    produtos_nomes = []
    produtos_quantidades = []

    
    def adicionar_produto(nome, quantidade):
        ControleEstoque.produtos_nomes.append(nome)
        ControleEstoque.produtos_quantidades.append(quantidade)
        print(f"Produto '{nome}' adicionado com quantidade {quantidade}.")

    
    def listar_produtos():
        print("Lista de Produtos:")
        for nome, quantidade in zip(ControleEstoque.produtos_nomes, ControleEstoque.produtos_quantidades):
            print(f"{nome}: {quantidade} unidades")

    
    def substituir_produto(nome_antigo, nome_novo):
        if nome_antigo in ControleEstoque.produtos_nomes:
            indice = ControleEstoque.produtos_nomes.index(nome_antigo)
            ControleEstoque.produtos_nomes[indice] = nome_novo
            print(f"Produto '{nome_antigo}' substituído por '{nome_novo}'.")
        else:
            print(f"Produto '{nome_antigo}' não encontrado na lista.")

while True:
    print("\nMenu:")
    print("1. Listar produtos")
    print("2. Adicionar produto")
    print("3. Substituir produto")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ControleEstoque.listar_produtos()
    elif opcao == "2":
        nome = input("Digite o nome do novo produto: ")
        quantidade = int(input("Digite a quantidade do novo produto: "))
        ControleEstoque.adicionar_produto(nome, quantidade)
    elif opcao == "3":
        nome_antigo = input("Digite o nome do produto a ser substituído: ")
        nome_novo = input("Digite o nome do novo produto: ")
        ControleEstoque.substituir_produto(nome_antigo, nome_novo)
    elif opcao == "4":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Escolha novamente.")