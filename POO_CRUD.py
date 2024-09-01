class Contato:
    def __init__(self, nome, telefone) -> None:
        self._nome = nome
        self._telefone = telefone
        
    def __repr__(self) -> str:
        return f'Nome: {self._nome} \t Telefone: {self._telefone}'
    
    def __len__(self) -> None:
        return 0
    
    def atualizar(self, nome=None, telefone=None):
        if nome:
            self._nome = nome
        if telefone:
            self._telefone = telefone
            
    @property
    def nome(self):
        return self._nome
    
    @property
    def telefone(self):
        return self._telefone
    
    @nome.setter
    def nome(self, novo_nome):
        if all(caracter.isalpha() or caracter.isspace() for caracter in novo_nome):
            # isinstance(novo_nome, str) and novo_nome.strip() != "":
            self._nome = novo_nome
        else:
            raise ValueError("Nome inválido. Deve ser uma string não vazia.")

    @telefone.setter
    def telefone(self, novo_telefone):
        if isinstance(novo_telefone, str) and novo_telefone.strip() != "":
            self._telefone = novo_telefone
        else:
            raise ValueError("Telefone inválido. Deve ser uma string não vazia.")

class Agenda:
    def __init__(self):
        self.contatos = []
        
    def criar_contato(self, nome, telefone):
        novo_contato = Contato(nome, telefone)
        self.contatos.append(novo_contato)
        print(novo_contato)
        
    def listar_contatos(self):
        if not self.contatos:
            print('Nenhum contato na agenda.')
            return False
        else:
            for idx, contato in enumerate(self.contatos, start=1):
                print(f'{idx}. {contato}')
    
    def atualizar_contato(self,indice, nome=None, telefone=None):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].atualizar(nome, telefone)
            print(f'Contato {indice + 1} atualizado com sucesso!')
        else:
            print('Índice de contato inválido.')
    
    def excluir_contato(self,indice):
        if 0 <= indice < len(self.contatos):
            contato_removido = self.contatos.pop(indice)
            print(f'Contato {contato_removido.nome} removido com sucesso!')
        else:
            print('Índice de contato inválido.')
            
            
def menu():
    print("\nAgenda de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Atualizar Contato")
    print("4. Remover Contato")
    print("5. Sair")
    
def main():
    agenda = Agenda()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        # Opção para adicionar contato:
        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            agenda.criar_contato(nome, telefone)

        # Opção para listar contatos:
        elif opcao == '2':
            agenda.listar_contatos()

        # Opção para atualizar contatos:
        elif opcao == '3':
            # agenda.listar_contatos()
            if agenda.listar_contatos() == False:
                print("Opção inválida. Tente novamente.")
            else:
                indice = int(input("Informe o número do contato a ser atualizado: ")) - 1
                nome = input("Novo nome (deixe em branco para manter): ")
                telefone = input("Novo telefone (deixe em branco para manter): ")
                agenda.atualizar_contato(indice, nome, telefone)

        # Opção para remover contatos:
        elif opcao == '4':
            # agenda.listar_contatos()
            if agenda.listar_contatos() == False:
                print("Opção inválida. Tente novamente.")
            else:
                indice = int(input("Informe o número do contato a ser removido: ")) - 1
                agenda.excluir_contato(indice)


        # Opção para sair:
        elif opcao == '5':
            print("Saindo...")
            break

        # Opção caso seja digitado alguma opção não definida:
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()