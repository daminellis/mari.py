import mysql.connector
from tkinter import messagebox, Tk, Label, Entry, Button, Toplevel

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="exerfinal"
)

# Criar o cursor
cursor = conexao.cursor()

# Função para autenticação
def fazer_login():
    cpf_digitado = int(cpf_entry.get())
    senha_digitada = senha_entry.get()

    # Consultar o banco de dados para verificar o login
    cursor.execute("SELECT * FROM cadastro WHERE cpf = %s AND senha = %s", (cpf_digitado, senha_digitada))
    usuario = cursor.fetchone()

    if usuario:
        exibir_menu_principal(usuario)
    else:
        messagebox.showerror("Erro de Login", "CPF ou senha incorretos.")

# Função para exibir o menu principal após o login
def exibir_menu_principal(usuario):
    janela_menu = Toplevel(janela)
    janela_menu.title("Menu Principal")

    # Botão para adicionar gasto
    adicionar_gasto_button = Button(janela_menu, text="Adicionar Gasto", command=lambda: abrir_janela_adicionar_gasto(usuario))
    adicionar_gasto_button.pack(pady=10)

# Função para abrir a janela de adicionar gasto
def abrir_janela_adicionar_gasto(usuario):
    janela_adicionar_gasto = Toplevel(janela)
    janela_adicionar_gasto.title("Adicionar Gasto")

    # Criar campos de entrada
    nome_label = Label(janela_adicionar_gasto, text="Nome:")
    nome_label.grid(row=0, column=0, padx=10, pady=10)
    nome_entry = Entry(janela_adicionar_gasto)
    nome_entry.grid(row=0, column=1, padx=10, pady=10)

    valor_label = Label(janela_adicionar_gasto, text="Valor:")
    valor_label.grid(row=1, column=0, padx=10, pady=10)
    valor_entry = Entry(janela_adicionar_gasto)
    valor_entry.grid(row=1, column=1, padx=10, pady=10)

    observacao_label = Label(janela_adicionar_gasto, text="Observação:")
    observacao_label.grid(row=2, column=0, padx=10, pady=10)
    observacao_entry = Entry(janela_adicionar_gasto)
    observacao_entry.grid(row=2, column=1, padx=10, pady=10)

    # Função para adicionar gasto a lista do usuário
    def adicionar_gasto():
        nome_gasto = nome_entry.get()
        valor_gasto = float(valor_entry.get())
        observacao_gasto = observacao_entry.get()

        # Inserir novo gasto no banco de dados associado ao usuário
        cursor.execute("INSERT INTO gastos (nome, valor, observacao, cpf_cadastro) VALUES (%s, %s, %s, %s)",
                       (nome_gasto, valor_gasto, observacao_gasto, usuario[0]))
        conexao.commit()

        messagebox.showinfo("Gasto Adicionado", "Gasto adicionado com sucesso!")
        janela_adicionar_gasto.destroy()

    # Criar botão para adicionar gasto
    adicionar_gasto_button = Button(janela_adicionar_gasto, text="Adicionar Gasto", command=adicionar_gasto)
    adicionar_gasto_button.grid(row=3, column=0, columnspan=2, pady=10)

# Função para abrir a janela de cadastro
def abrir_janela_cadastro():
    janela_cadastro = Toplevel(janela)
    janela_cadastro.title("Cadastro de Usuário")

    # Criar campos de entrada
    cpf_label = Label(janela_cadastro, text="CPF:")
    cpf_label.grid(row=0, column=0, padx=10, pady=10)
    cpf_entry_cadastro = Entry(janela_cadastro)
    cpf_entry_cadastro.grid(row=0, column=1, padx=10, pady=10)

    senha_label = Label(janela_cadastro, text="Senha:")
    senha_label.grid(row=1, column=0, padx=10, pady=10)
    senha_entry_cadastro = Entry(janela_cadastro, show="*")
    senha_entry_cadastro.grid(row=1, column=1, padx=10, pady=10)

    nome_label = Label(janela_cadastro, text="Nome:")
    nome_label.grid(row=2, column=0, padx=10, pady=10)
    nome_entry_cadastro = Entry(janela_cadastro)
    nome_entry_cadastro.grid(row=2, column=1, padx=10, pady=10)

    idade_label = Label(janela_cadastro, text="Idade:")
    idade_label.grid(row=3, column=0, padx=10, pady=10)
    idade_entry_cadastro = Entry(janela_cadastro)
    idade_entry_cadastro.grid(row=3, column=1, padx=10, pady=10)

    salario_label = Label(janela_cadastro, text="Salário:")
    salario_label.grid(row=4, column=0, padx=10, pady=10)
    salario_entry_cadastro = Entry(janela_cadastro)
    salario_entry_cadastro.grid(row=4, column=1, padx=10, pady=10)

    # Função para cadastrar usuãrio na nova janela
    def cadastrar_usuario():
        cpf_digitado = int(cpf_entry_cadastro.get())
        senha_digitada = senha_entry_cadastro.get()
        nome_digitado = nome_entry_cadastro.get()
        idade_digitada = int(idade_entry_cadastro.get())
        salario_digitado = float(salario_entry_cadastro.get())

        # Inserir novo usuário no banco de dados
        cursor.execute("INSERT INTO cadastro (cpf, senha, nome, idade, salario) VALUES (%s, %s, %s, %s, %s)", 
                       (cpf_digitado, senha_digitada, nome_digitado, idade_digitada, salario_digitado))
        conexao.commit()

        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
        janela_cadastro.destroy()

    # Criar botão de cadastro na janela
    cadastro_button_cadastro = Button(janela_cadastro, text="Cadastrar", command=cadastrar_usuario)
    cadastro_button_cadastro.grid(row=5, column=0, columnspan=2, pady=10)

# Função para exibir o menu principal após o login
def exibir_menu_principal(usuario):
    janela_menu = Toplevel(janela)
    janela_menu.title("Menu Principal")

    # Botão para adicionar gasto
    adicionar_gasto_button = Button(janela_menu, text="Adicionar Gasto", command=lambda: abrir_janela_adicionar_gasto(usuario))
    adicionar_gasto_button.pack(pady=10)

    # Botão para visualizar gastos
    visualizar_gastos_button = Button(janela_menu, text="Visualizar Gastos", command=lambda: visualizar_gastos(usuario))
    visualizar_gastos_button.pack(pady=10)

    # Botão para alterar gasto
    alterar_gasto_button = Button(janela_menu, text="Alterar Gasto", command=lambda: abrir_janela_alterar_gasto(usuario))
    alterar_gasto_button.pack(pady=10)

    # Botão para excluir gastos
    excluir_gastos_button = Button(janela_menu, text="Excluir Gastos", command=lambda: excluir_gastos(usuario))
    excluir_gastos_button.pack(pady=10)

# Função para visualizar gastos
def visualizar_gastos(usuario):
    # Criar a janela para visualizar gastos
    janela_visualizar_gastos = Toplevel(janela)
    janela_visualizar_gastos.title("Visualizar Gastos")

    # Consultar gastos associados ao usuário
    cursor.execute("SELECT * FROM gastos WHERE cpf_cadastro = %s", (usuario[0],))
    gastos = cursor.fetchall()

    # Exibir gastos na nova janela
    for gasto in gastos:
        label_gasto = Label(janela_visualizar_gastos, text=f"ID: {gasto[0]}, Nome: {gasto[1]}, Valor: {gasto[2]}, Observação: {gasto[3]}")
        label_gasto.pack()

    # Calcular a soma dos valores dos gastos
    total_valor = sum([gasto[2] for gasto in gastos])

    # Exibir a soma no final da lista
    label_soma = Label(janela_visualizar_gastos, text=f"Soma dos Gastos: {total_valor}")
    label_soma.pack()

# Função para abrir a janela de alterar gasto
def abrir_janela_alterar_gasto(usuario):
    # Consultar gastos associados ao usuário
    cursor.execute("SELECT * FROM gastos WHERE cpf_cadastro = %s", (usuario[0],))
    gastos = cursor.fetchall()

    # Verificar se há gastos para atualizar
    if not gastos:
        messagebox.showinfo("Nenhum Gasto", "Não há gastos para atualizar.")
        return

    janela_alterar_gasto = Toplevel(janela)
    janela_alterar_gasto.title("Alterar Gasto")

    # Exibir gastos na nova janela
    for gasto in gastos:
        label_gasto = Label(janela_alterar_gasto, text=f"ID: {gasto[0]}, Nome: {gasto[1]}, Valor: {gasto[2]}, Observação: {gasto[3]}")
        label_gasto.pack()

    # Criar campo de entrada para o ID do gasto a ser alterado
    id_gasto_label = Label(janela_alterar_gasto, text="ID do Gasto a ser Alterado:")
    id_gasto_label.pack(pady=10)
    id_gasto_entry = Entry(janela_alterar_gasto)
    id_gasto_entry.pack(pady=10)

    # Verificar se o ID do gasto fornecido é válido
    def validar_id_gasto():
        id_gasto = int(id_gasto_entry.get())
        if id_gasto not in [g[0] for g in gastos]:
            messagebox.showerror("ID Inválido", "ID do gasto fornecido não é válido.")
            return False
        return True

    # Criar campos de entrada para as novas informações 
    novo_nome_label = Label(janela_alterar_gasto, text="Novo Nome:")
    novo_nome_label.pack(pady=10)
    novo_nome_entry = Entry(janela_alterar_gasto)
    novo_nome_entry.pack(pady=10)

    novo_valor_label = Label(janela_alterar_gasto, text="Novo Valor:")
    novo_valor_label.pack(pady=10)
    novo_valor_entry = Entry(janela_alterar_gasto)
    novo_valor_entry.pack(pady=10)

    nova_observacao_label = Label(janela_alterar_gasto, text="Nova Observação:")
    nova_observacao_label.pack(pady=10)
    nova_observacao_entry = Entry(janela_alterar_gasto)
    nova_observacao_entry.pack(pady=10)

    # Função para alterar gasto pelo ID
    def alterar_gasto():
        if not validar_id_gasto():
            return

        id_gasto = int(id_gasto_entry.get())
        novo_nome = novo_nome_entry.get()
        novo_valor = float(novo_valor_entry.get())
        nova_observacao = nova_observacao_entry.get()

        # Alterar informações do gasto no banco de dados
        cursor.execute("UPDATE gastos SET nome = %s, valor = %s, observacao = %s WHERE id_gasto = %s",
                       (novo_nome, novo_valor, nova_observacao, id_gasto))
        conexao.commit()

        messagebox.showinfo("Gasto Alterado!", "Gasto alterado com sucesso!")
        janela_alterar_gasto.destroy()

    # Criar botão para alterar gasto
    alterar_gasto_button = Button(janela_alterar_gasto, text="Alterar Gasto", command=alterar_gasto)
    alterar_gasto_button.pack(pady=10)

# Função para excluir gastos
def excluir_gastos(usuario):
    # Consultar gastos associados a cada usuário
    cursor.execute("SELECT * FROM gastos WHERE cpf_cadastro = %s", (usuario[0],))
    gastos = cursor.fetchall()

    # Verificar se há gastos para excluir
    if not gastos:
        messagebox.showinfo("Nenhum Gasto", "Não há gastos para excluir.")
        return

    # Criar a janela para excluir gastos
    janela_excluir_gastos = Toplevel(janela)
    janela_excluir_gastos.title("Excluir Gastos")

    # Exibir gastos na nova janela
    for gasto in gastos:
        label_gasto = Label(janela_excluir_gastos, text=f"ID: {gasto[0]}, Nome: {gasto[1]}, Valor: {gasto[2]}, Observação: {gasto[3]}")
        label_gasto.pack()

    # Criar campo de entrada para o ID do gasto a ser excluído
    id_gasto_label = Label(janela_excluir_gastos, text="ID do Gasto a ser Excluído:")
    id_gasto_label.pack(pady=10)
    id_gasto_entry = Entry(janela_excluir_gastos)
    id_gasto_entry.pack(pady=10)

    # Função para excluir gasto pelo ID
    def excluir_gasto():
        id_gasto = id_gasto_entry.get()

        # Verificar se o ID do gasto fornecido é válido
        if not id_gasto.isdigit() or int(id_gasto) not in [g[0] for g in gastos]:
            messagebox.showerror("ID Inválido", "ID do gasto fornecido não é válido.")
            return

        # Excluir gasto no banco de dados, considerando o ID do usuário
        cursor.execute("DELETE FROM gastos WHERE id_gasto = %s AND cpf_cadastro = %s", (int(id_gasto), usuario[0]))
        conexao.commit()

        messagebox.showinfo("Gasto Excluído", "Gasto excluído com sucesso!")
        janela_excluir_gastos.destroy()

    # Criar botão para excluir gasto
    excluir_gasto_button = Button(janela_excluir_gastos, text="Excluir Gasto", command=excluir_gasto)
    excluir_gasto_button.pack(pady=10)

# Criar a janela principal
janela = Tk()
janela.title("Login")

# Criar campos de entrada para login
cpf_label = Label(janela, text="CPF:")
cpf_label.grid(row=0, column=0, padx=10, pady=10)
cpf_entry = Entry(janela)
cpf_entry.grid(row=0, column=1, padx=10, pady=10)

senha_label = Label(janela, text="Senha:")
senha_label.grid(row=1, column=0, padx=10, pady=10)
senha_entry = Entry(janela, show="*")
senha_entry.grid(row=1, column=1, padx=10, pady=10)

# Criar botões de login e cadastro
login_button = Button(janela, text="Login", command=fazer_login)
login_button.grid(row=2, column=0, pady=10)

cadastro_button = Button(janela, text="Cadastro", command=abrir_janela_cadastro)
cadastro_button.grid(row=2, column=1, pady=10)

# Iniciar o loop da interface 
janela.mainloop()

# Fechar a conexão com o banco de dados ao fechar a janela
conexao.close()
