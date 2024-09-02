from contato import Contato
from agenda import Agenda

def menu():
    print(f"\nAgenda de Contatos \n 1. Adicionar Contato \n 2. Listar Contatos \n 3. Atualizar Contato \n 4. Remover Contato\n 5. Sair \n {'**' * 12} \n")

def main():
    agenda = Agenda()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_adicionar_contato(agenda)
        elif opcao == "2":
            agenda.listar_contatos()
        elif opcao == "3":
            menu_atualizar_contato(agenda)
        elif opcao == "4":
            menu_remover_contato(agenda)
        elif opcao == "5":
            exit()
        else:
            print("Opção inválida. Tente novamente.")

def menu_adicionar_contato(agenda):
    nome = input("Nome: ")
    telefone = obter_telefone_valido()
    agenda.criar_contato(nome, telefone)

def obter_telefone_valido():
    while True:
        try:
            telefone = int(input("Telefone (apenas números): "))
            return telefone
        except ValueError:
            print("Erro: O telefone deve ser apenas números. Tente novamente.")

def menu_atualizar_contato(agenda):
    if not agenda.listar_contatos():
        print("Nenhum contato para atualizar.")
        return
    try:
        indice = int(input("Informe o número ID do contato a ser atualizado:")) - 1
        assert 0 <= indice < len(agenda.contatos)
    except (ValueError, AssertionError):
        print("Índice inválido. Tente novamente.")
        return
    
    nome = input("Novo nome (deixe em branco para manter): ")
    telefone = input("Novo telefone (deixe em branco para manter): ")


    try:
        telefone = int(telefone) if telefone else None
    except ValueError:
        print("tel inválido. Tente novamente.")
        return
    
    agenda.atualizar_contato(indice, nome, telefone)

    


'''    else:
        entrada = input("Informe o número ID do contato a ser atualizado: ")

        if entrada.isdigit():
            indice = int(entrada) - 1
            if 0 <= indice < len(agenda.contatos):
                nome = input("Novo nome (deixe em branco para manter): ")
                telefone = input("Novo telefone (deixe em branco para manter): ")
                telefone = int(telefone) if telefone else None
                agenda.atualizar_contato(indice, nome if nome else None, telefone if telefone else None)
            else:
                print("Índice inválido. Tente novamente.")
        else:
            print("Entrada inválida. Tente novamente.")'''

def menu_remover_contato(agenda):
    if not agenda.listar_contatos():
        print("Nenhum contato para remover.")
    else:
        entrada = input("Informe o número do contato a ser removido: ")

        if entrada.isdigit():
            indice = int(entrada) - 1
            if 0 <= indice < len(agenda.contatos):
                agenda.excluir_contato(indice)
            else:
                print("Índice inválido. Tente novamente.")
        else:
            print("Entrada inválida. Tente novamente.")


if __name__ == "__main__":
    main()
