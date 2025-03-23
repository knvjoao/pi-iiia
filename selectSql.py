from db import connect_to_db


# Observação: funções criadas para a apresentação, com fins didáticos. Arquivo seria vulnerável a SQL injection nas f-strings.

def obtain_categories(table):
    with connect_to_db() as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT DISTINCT category FROM {table};")
            return [row[0] for row in cur.fetchall()]


def obtain_titles(table, category):
    with connect_to_db() as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT title FROM {table} WHERE category LIKE %s;", (f'%{category}%',))
            return [row[0] for row in cur.fetchall()]


# Choice 3 tem séries e filmes. Usada para não repetir.
def choice_3(category):
    categories = obtain_categories(category)
    print("Categorias disponíveis:", categories)
    category_to_display = input("Digite o nome da categoria: ").strip().upper()    # Todos estão em CAPS LOCK no banco de dados.
    matching_categories = []

    for cat in categories:
        if category_to_display.lower() in cat.lower():
            matching_categories.append(cat)

    if matching_categories:
        print("Categorias correspondentes:", matching_categories)
        titles = obtain_titles(category, category_to_display)
        print("Títulos disponíveis:", titles)
    
    else:
        print("Não há categoria com este nome")


def menu():
    quit_status = False
    while not quit_status:
        choice = input("\nPrograma feito apenas para demonstrar os comandos SELECT. A parte visual dos dados está no DBeaver.\nBem-vindo(a). O que deseja consultar?\n1 - Listas de filmes\n2 - Listas de séries\n3 - Verificar lista específica\nSAIR - Sair\nOpção: ").strip().lower()
        
        if choice == "1":    # Listas de filmes
            categories = obtain_categories("filmes")
            print("Categorias de filmes: ", categories)
        
        elif choice == "2":    # Listas de séries
            categories = obtain_categories("series")
            print("Categorias de séries: ", categories)
        
        elif choice == "3":    # Verificar lista específica
            while True:
                new_choice_3 = input("\nQual a categoria da lista?\n1 - Filmes\n2 - Séries\n3 - Retornar ao menu\nOpção: ").strip().lower()
                
                if new_choice_3 == "1":
                    choice_3("filmes")

                elif new_choice_3 == "2":
                    choice_3("series")

                elif new_choice_3 == "3":
                    break

                else:
                    print("Opção inválida!")
        
        elif choice == "sair":    # Sair do programa
            quit_status = True
            print("Saindo.")
        
        else:   # Input não está nas condicionais
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
