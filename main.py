from feiticos import feiticos
from animacoes import executar_animacao

def mostrar_menu():
    print("\n=== Livro de Feitiços de Hogwarts ===")
    print("Escolha um feitiço para ver a descrição e a animação:")
    for nome in feiticos:
        print(f" - {nome.capitalize()}")
    print("Digite 'sair' para encerrar.\n")

def main():
    while True:
        mostrar_menu()
        escolha = input("Digite o nome do feitiço: ").lower().strip()

        if escolha == "sair":
            print("Até mais, jovem bruxo(a)!")
            break

        if escolha in feiticos:
            feitico = feiticos[escolha]
            print(f"\nNome: {feitico['nome']}")
            print(f"Categoria: {feitico['categoria']}")
            print(f"Descrição: {feitico['descricao']}\n")
            input("Pressione ENTER para executar a animação...")

            executar_animacao(escolha)

        else:
            print("Feitiço não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()