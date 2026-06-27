import sqlite3
conexao = sqlite3.connect('produtos.db')
conexao.execute('''
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY,
    quantidade INTEGER,
    nome TEXT
    )
''')
conexao.commit()

opcao1 = "1- atualizar estoque"
opcao2 = "2- remover do estoque"
opcao3 = "3- ver estoque"
opcao4 = "4- ver relatorio estoque"
opcao5 = "5- remover produto do catálogo"

while True:
    print(opcao1)
    print(opcao2)
    print(opcao3)
    print(opcao4)
    print(opcao5)

    resposta = int(input('Digite o numero da opçao desejada : '))

    if resposta == 1:
        ordem = conexao.execute("SELECT id, nome FROM produtos")
        check = ordem.fetchall()
        for id_produto, nome in check:
            print(f"{id_produto}. {nome}")
        produto_id = int(input('Digite o numero do produto: '))
        quantidade = int(input('Digite a quantidade de estoque a mais: '))
        conexao.execute(
            "UPDATE produtos SET quantidade = quantidade + ? WHERE id = ?",
            (quantidade, produto_id),
        )
        conexao.commit()
        print('Produto atualizado com sucesso!')

    elif resposta == 2:
        ordem = conexao.execute("SELECT id, nome FROM produtos")
        check = ordem.fetchall()
        for id_produto, nome in check:
            print(f"{id_produto}. {nome}")
        produto_id = int(input('Digite o numero do produto: '))
        quantidade = int(input('Digite a quantidade do estoque que quer remover: '))

        # Busca o estoque atual SÓ desse produto, antes de comparar
        estoque_atual_query = conexao.execute(
            "SELECT quantidade FROM produtos WHERE id = ?", (produto_id,)
        )
        estoque_atual = estoque_atual_query.fetchone()[0]

        if quantidade > estoque_atual:
            print("Estoque insuficiente")
        else:
            conexao.execute(
                "UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?",
                (quantidade, produto_id),
            )
            conexao.commit()
            print('Produto atualizado com sucesso!')

    elif resposta == 3:
        relatorio = conexao.execute("SELECT id, nome, quantidade FROM produtos")
        check = relatorio.fetchall()
        if not check:
            print("Nada no estoque")
        else:
            for id_produto, nome, quantidade in check:
                print(f"{nome}: {quantidade} unidades")

    elif resposta == 4:
        baixo = conexao.execute(
            "SELECT nome, quantidade FROM produtos WHERE quantidade < ? ORDER BY quantidade ASC",
            (10,),
        )
        produtos_baixo = baixo.fetchall()

        total_query = conexao.execute("SELECT SUM(quantidade) FROM produtos")
        total = total_query.fetchone()[0]
        if total is None:
            total = 0

        mais = conexao.execute(
            "SELECT nome, quantidade FROM produtos ORDER BY quantidade DESC LIMIT 1"
        )
        produto_mais = mais.fetchone()

        menos = conexao.execute(
            "SELECT nome, quantidade FROM produtos ORDER BY quantidade ASC LIMIT 1"
        )
        produto_menos = menos.fetchone()

        print("\n--- Produtos com estoque abaixo de 10 ---")
        if not produtos_baixo:
            print("Nenhum produto com estoque baixo.")
        else:
            for nome, quantidade in produtos_baixo:
                print(f"{nome}: {quantidade} unidades")

        print(f"\nTotal de unidades em estoque: {total}")

        if produto_mais:
            print(f"Produto com mais estoque: {produto_mais[0]} ({produto_mais[1]} unidades)")
        if produto_menos:
            print(f"Produto com menos estoque: {produto_menos[0]} ({produto_menos[1]} unidades)")

    elif resposta == 5:
        ordem = conexao.execute("SELECT id, nome FROM produtos")
        check = ordem.fetchall()
        for id_produto, nome in check:
            print(f"{id_produto}. {nome}")
        produto_id = int(input('Digite o numero do produto: '))
        conexao.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        conexao.commit()
        print('Produto removido com sucesso!')

    else:
        print("Erro: escolha uma das opções citadas")

    continuar = input("\nPressione Enter para continuar ou digite 'sair' para encerrar: ")
    if continuar.capitalize() == "Sair":
        print("Encerrando...")
        break

conexao.close()