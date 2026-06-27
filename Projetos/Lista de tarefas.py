import sqlite3

opcao1 = "1 Adicionar tarefa"
opcao2 = "2 Ver tarefas"
opcao3 = "3 Remover tarefa"

conexao = sqlite3.connect('../tarefas.db')

conexao.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY,
        descricao TEXT
    )
''')

conexao.execute('''
    CREATE TABLE IF NOT EXISTS configuracoes (
        chave TEXT PRIMARY KEY,
        valor TEXT
    )
''')
conexao.commit()

cursor = conexao.execute("SELECT valor FROM configuracoes WHERE chave = 'titulo'")
resultado = cursor.fetchone()

if resultado is None:
    nome = input("Digite o título da página: ")
    conexao.execute(
        "INSERT INTO configuracoes (chave, valor) VALUES (?, ?)",
        ('titulo', nome)
    )
    conexao.commit()
else:
    nome = resultado[0]

print(f"{nome.upper()}")

while True:
    print(opcao1)
    print(opcao2)
    print(opcao3)

    try:
        resposta = int(input("Escolha uma das opções: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if resposta == 1:
        adicionar = input("Digite a tarefa: ")
        conexao.execute("INSERT INTO tarefas (descricao) VALUES (?)", (adicionar,))
        conexao.commit()
        print("Tarefa adicionada!")

    elif resposta == 2:
        cursor = conexao.execute("SELECT id, descricao FROM tarefas")
        resultados = cursor.fetchall()

        if not resultados:
            print("Nenhuma tarefa cadastrada ainda.")
        else:
            for id_tarefa, tarefa in resultados:
                print(f"{id_tarefa}. {tarefa}")

    elif resposta == 3:
        cursor = conexao.execute("SELECT id, descricao FROM tarefas")
        resultados = cursor.fetchall()

        if not resultados:
            print("Não há tarefas para remover.")
        else:
            for id_tarefa, tarefa in resultados:
                print(f"{id_tarefa}. {tarefa}")

            remover = int(input("Qual tarefa quer remover (digite o número)? "))
            conexao.execute("DELETE FROM tarefas WHERE id = ?", (remover,))
            conexao.commit()
            print("Tarefa removida!")

    else:
        print("Opção inválida! Escolha 1, 2 ou 3.")

    continuar = input("\nPressione Enter para continuar ou digite 'sair' para encerrar: ")
    if continuar.capitalize() == "Sair":
        print("Encerrando...")
        break

conexao.close()