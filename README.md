# StockPy — Controle de Estoque em Python

Sistema de controle de estoque que roda no terminal, feito em Python com banco de dados SQLite.

## Funcionalidades

- Adicionar produtos ao catálogo, já com a quantidade inicial
- Adicionar unidades ao estoque de um produto
- Remover unidades do estoque, com validação de estoque insuficiente
- Listar o estoque
- Gerar relatório: total de unidades, produtos com maior e menor estoque e produtos com estoque baixo
- Remover produtos do catálogo

## Tecnologias

- Python 3
- SQLite (módulo `sqlite3` da biblioteca padrão)
- SQL: `CREATE TABLE`, `INSERT`, `UPDATE`, `DELETE`, `SELECT`, `SUM`, `ORDER BY`

## Como executar

```bash
git clone https://github.com/scudelerlucasb-a11y/StockPy.git
cd StockPy/Projetos
python Stock.py
```

O banco `produtos.db` é criado automaticamente na primeira execução.

## Menu

```text
1- atualizar estoque
2- remover do estoque
3- ver estoque
4- ver relatorio estoque
5- remover produto do catálogo
6- adicionar produto do catalogo e adicionar quantidade
```

## Estrutura

- `Projetos/Stock.py`: código principal do sistema
- Os outros arquivos da pasta `Projetos/` são exercícios menores de lógica em Python

## O que pratiquei

- CRUD completo com SQLite
- Consultas parametrizadas (`?`), em vez de montar SQL com texto
- Validação de regra de negócio (não permitir remover mais do que existe no estoque)
- Relatórios com `SUM` e `ORDER BY`

## Autor

**Lucas Braga Scudeler**
[LinkedIn](https://www.linkedin.com/in/lucas-braga-scudeler) · [GitHub](https://github.com/scudelerlucasb-a11y)
