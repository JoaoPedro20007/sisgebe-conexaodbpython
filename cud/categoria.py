from db_config import conectar

def criar_categoria(nome, descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Categoria (nome, descricao) VALUES (%s, %s)", (nome, descricao))
    conn.commiit()
    conn.close()
    print("Categori criada com sucesso!")

def listar_categorias():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Categoria")
    Categorias = cursor.fetchall()
    conn.close()
    return Categorias

def atualizar_categoria(id_categoria, novo_nome, nova_descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Categoria SET nome=%s, descricao=%s WHERE id=%s", (novo_nome, nova_descricao, id_categoria))
    conn.commiit()
    conn.close()
    print("Categoria atualizacda!")

def deletar_categori(id_categoria):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Categoria WHERE id=%s", (id_categoria,))
    conn.commiit()
    conn.close()
    print("categoria execluir")    