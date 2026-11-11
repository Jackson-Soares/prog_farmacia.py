'''criar um sistema de vendas:
cadastrar produtos e cliente; estoque; vendas;
contas a pagar e receber; painel de controle'''

estoque_de_produtos= {}

while True:
    print("\n=== MENU - CADASTRO DE PRODUTOS ===") # o \n é uma quebra de linha.
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Buscar Produto por descrição")
    print("4 - Editar Produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\t--- Iniciando cadastro ---\n")
        codigo = input("Código de barras: ").strip() # Digitar o Código antes de qualquer dado, evita fazer todo cadastro caso já exista #
        if codigo in estoque_de_produtos:
            print(f"\nErro: Já existe um produto cadastrado com este Código!")   
        
        else:   # Se não existir, continue o cadastro. #
            descricao = input("Descrição do Produto: ").strip()
            validade = input("Validade: ").strip()
            preco_texto = input ("Preço: ").strip()
            preco_texto = preco_texto.replace("," , ".").strip()
            preco_texto = float(preco_texto)
            estoque = int (input ("Estoque: "))
            indicacao = input ("Indicação: ").strip()
            posologia = input ("Posologia: ").strip()
            contraindicacao = input("Contraindicações: ").strip()

            produto = {
                "descricao": descricao,
                "validade": validade,
                "preco": preco_texto,
                "estoque": estoque,
                "indicacao": indicacao,
                "posologia" : posologia,
                "contraindicacao" : contraindicacao,
            }
            estoque_de_produtos[codigo] = produto #adiciona produto cadastrado ao dicionário cadastro_de_produtos
            print(f"\n Produto cadastrado com sucesso!")
    
    elif opcao == "2":
            if not estoque_de_produtos:
                print("Nenhum produto cadastrado ainda.")
            else:
                 print("\t--- LISTA DE PRODUTOS ---\n")
                 for codigo, dados in estoque_de_produtos.items():
                      print(f"Código: {codigo}")
                      print(f"Descrição: {dados['descricao']}")
                      print(f"Validade: {dados['validade']}")
                      print(f"Preço: {dados['preco']:.2f}")
                      print(f"Estoque: {dados['estoque']}")
                      print(f"Indicação: {dados['indicacao']}")
                      print(f"Posologia: {dados['posologia']}")
                      print(f"Contraindicação: {dados['contraindicacao']}")
                      print("=" * 20)
        
           

