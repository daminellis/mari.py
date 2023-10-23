import mysql.connector


def conectar_banco():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='mercearia'
    )

def listar_registros():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f'ID: {i[0]} | Produto: {i[1]} | Valor: R${i[2]:.2f}')
    cursor.close()
    conexao.close()

def criar_registro():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    nome_produto = input('Nome do produto: ')
    valor = float(input('Valor: '))
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    print('Registro criado com sucesso.')

def atualizar_registro():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    id = int(input('ID do registro a ser atualizado: '))
    nome_produto = input('Novo nome do produto: ')
    valor = float(input('Novo valor: '))
    comando = f'UPDATE vendas SET nome_produto = "{nome_produto}", valor = {valor} WHERE idVendas = {id}'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    print('Registro atualizado com sucesso.')

def excluir_registro():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    id = int(input('ID do registro a ser excluído: '))
    comando = f'DELETE FROM vendas WHERE idVendas = {id}'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    print('Registro excluído com sucesso.')

while True:
    print("\nMenu:"
    "1 - LISTAR REGISTROS"
    "2 - CRIAR REGISTROS"
    "3 - ATUALIZAR REGISTRO"
    "4 - EXCLUIR REGISTRO"
    "5 - SAIR")

    escolha = input("Escolha a opção desejada: ")

    if escolha == '1':
        listar_registros()
    elif escolha == '2':
        criar_registro()
    elif escolha == '3':
        atualizar_registro()
    elif escolha == '4':
        excluir_registro()
    elif escolha == '5':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
