class Contato:
    def __init__(self, nome, telefone, email, endereco, post_code) -> None:
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._endereco = endereco
        self._post_code = post_code
        
    def __repr__(self) -> str:
        # texto = f"Nome: {self._nome} \nTelefone: {self._telefone} \nEmail: {self._email} \nEndereço: {self._endereco} \nCEP: {self._post_code}"
        return "estou aqui"#f"Nome: {self._nome} \nTelefone: {self._telefone} \nEmail: {self._email} \nEndereço: {self._endereco} \nCEP: {self._post_code}"
    
    def __str__(self):
        return f"Nome: {self._nome} \nTelefone: {self._telefone} \nEmail: {self._email} \nEndereço: {self._endereco} \nCEP: {self._post_code}"
        # return f'Nome: {self.nome}, Telefone: {self.telefone}, E-mail: {self.email}'


    def atualizar(self, nome=None, telefone=None, email=None, endereco=None, post_code=None):
        if nome:
            self._nome = nome
        if telefone:
            self._telefone = telefone
        if email:
            self._email = email
        if endereco:
            self._endereco = endereco
        if email:
            self._post_code = post_code
    
    # GETTERS e SETTERS
    
    ## Getter Nome:
    @property
    def nome(self):
        return self._nome
    
    # Setter Nome:
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip() != "":
            self._nome = novo_nome
        else:
            raise ValueError("Nome inválido. Deve ser uma string não vazia.")
        # if novo_nome.isalpha():
        #     self._nome = novo_nome
        # else: 
        #     print("Esse nome não é aceitável")
            
    
    ## Getter Telefone:
    @property
    def telefone(self):
        return self._telefone
    
    ## Getter Email:
    @property
    def email(self):
        return self._email
    
    ## Getter Endereço:
    @property
    def endereco(self):
        return self._endereco
    
    ## Getter Código Postal:
    @property
    def post_code(self):
        return self._post_code
    
    # SETTERS
    
    @email.setter
    def email(self, novo_email):
        # quero impedir que o usuário cadastre outros emails além do gmail
        if "@gmail.com" not in novo_email:
            print("Esse email não é aceitável")
        else: 
            self._email = novo_email

class Agenda:
    def __init__(self):
        self.contatos = []

    def criar_contato(self, nome, telefone, email, endereco, post_code):
        novo_contato = Contato(nome, telefone, email, endereco, post_code)
        self.contatos.append(novo_contato)
        print(novo_contato)
        #print(f'Contato {nome} adicionado com sucesso!')

    def listar_contatos(self):
        if not self.contatos:
            print('Nenhum contato na agenda.')
        else:
            for idx, contato in enumerate(self.contatos, start=1):
                print(f'{idx}. {contato}')

    def atualizar_contato(self, indice, nome=None, telefone=None, email=None, endereco=None, post_code=None):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].atualizar(nome, telefone, email, endereco, post_code)
            print(f'Contato {indice + 1} atualizado com sucesso!')
        else:
            print('Índice de contato inválido.')

    def excluir_contato(self, indice):
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

        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            endereco = input("Endereço: ")
            post_code = input("CEP: ")
            agenda.criar_contato(nome, telefone, email, endereco, post_code)

        elif opcao == '2':
            agenda.listar_contatos()

        elif opcao == '3':
            agenda.listar_contatos()
            indice = int(input("Informe o número do contato a ser atualizado: ")) - 1
            nome = input("Novo nome (deixe em branco para manter): ")
            telefone = input("Novo telefone (deixe em branco para manter): ")
            email = input("Novo e-mail (deixe em branco para manter): ")
            endereco = input("Novo endereço (deixe em branco para manter): ")
            post_code = input("Novo CEP (deixe em branco para manter): ")
            agenda.atualizar_contato(indice, nome, telefone, email, endereco, post_code)

        elif opcao == '4':
            agenda.listar_contatos()
            indice = int(input("Informe o número do contato a ser removido: ")) - 1
            agenda.excluir_contato(indice)

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
    