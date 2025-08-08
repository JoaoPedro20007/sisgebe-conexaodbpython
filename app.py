# app.py

from db_config import conecter
from crud import categoria

def main():
    conexao = conecter()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM livros;") # Exemplo de consulta simples

            resultados = cursor.fetchal()

            print("\nLivros cadastrados:")
            for linha in resultados:
                print(linha)

        except Exception as e:
            print(f"Erro na execução: {e}")
        finally:
            conexao.close()
            print("\nConexão encerrada.")

if __name__ == "__main__":
    main()

def menu():
    while True:
        print("\n=== MENU SGB ===")    
        print("1. Criar Categoria")  
        print("2. Listar Categoria") 
        print("3. Atualizar Categoria") 
        print("4. Deletar Categoria") 
        print("0. Sair") 
        opcao = input("Escola uma opção: ")

        if opcao == "1":
            nome = input("Nome da categoria: ")
            descricao = input ("Dascrição")