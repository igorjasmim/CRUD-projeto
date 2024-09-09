# função entender o status do arquivo (existência), atribuir o cabeçalho e garantir que caso exista, siga complementando informações
def agenda_csv(contatos):
        try:    
            with open('agenda.csv', 'r') as agenda:
                if agenda.read().strip() == '':
                    raise FileNotFoundError
        except:
            with open('agenda.csv', 'a') as agenda:
                agenda.write('ID,Nome,Telefone,Email\n')

    #ler quantidade de linhas para determinar o último id
        with open('agenda.csv', 'r') as agenda: #qualqer ação realizada dentro do doc deve ser especificado em with open
            linhas = agenda.readlines()
            ler_id = len(linhas) #ler o total de linhas do arquivo gerado 

    #abrir o arquivo para gravar as informações inputadas e sequenciando a lista
        with open('agenda.csv','a') as agenda:
            agenda.write(f'{ler_id},{contatos.nome},{contatos.telefone},{contatos.email}\n')
        
#função para validar domínios dos e-mails
def validar_email(novo_email):
    emails_validos = ['@gmail.com', '@hotmail.com', '@outlook.com', '@yahoo.com.br', '@uol.com.br']
    if '@' in novo_email:
        dominio = '@' + novo_email.split('@')[-1].strip() #procurar e checar à partir do @ até o final da palavra se os caracteres inseridos correspondem
    else:
        return False
    return dominio in emails_validos #invalidar o e-mail se o domínio não for válido

#criação da classe contato e a representação das informações para o banco de dados
class Contato:
    def __init__(self, nome, telefone, email) -> None:
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self.email = email
        
    def __repr__(self) -> str:
        return f'Nome: {self._nome} \t Telefone: {self._telefone} \t E-mail: {self._email}'
    
    def __len__(self) -> None:
        return 0
    
    def atualizar(self, nome=None, telefone=None, email=None):
        if nome:
            self._nome = nome
        if telefone:
            self._telefone = telefone
        if email:
            self._email = email

     #deixando os atributos como propriedades particulares    
    @property
    def nome(self):
        return self._nome
    
    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email
    
    #utilizando o método setter para permitir a edição dos atributos
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

    @email.setter
    def email(self, novo_email):
        while not validar_email(novo_email):
            print('Este dompinio não pe válido para cadsatro.')
            novo_email = input('Por favor, insira um e-mail com domínio válido: ')
        self._email = novo_email

class Agenda:
    def __init__(self):
        self.contatos = []

    #função para criar o contato e popular o arquivo CSv    
    def criar_contato(self, nome, telefone, email):
        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)
        agenda_csv(novo_contato)
        print(novo_contato)

  #função para listar os contatos existentes na agenda       
    def listar_contatos(self):
        if not self.contatos:
            print('Nenhum contato na agenda.')
            return False
        else:
            for idx, contato in enumerate(self.contatos, start=1):
                print(f'{idx}. {contato}')
                cont = idx
            return cont
            
    #função para atualizar os contatos utilizando o index como seletor
    def atualizar_contato(self,indice, nome=None, telefone=None, email= None):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].atualizar(nome, telefone, email)
            print(f'Contato {indice + 1} atualizado com sucesso!')
        else:
            print('Índice de contato inválido.')
    
    #função para excluir contato utilizando o index como seletor
    def excluir_contato(self,indice):
        if 0 <= indice < len(self.contatos):
            contato_removido = self.contatos.pop(indice)
            print(f'Contato {contato_removido.nome} removido com sucesso!')
        else:
            print('Índice de contato inválido.')
            
#função de menu-entrada para definir a ação desejada           
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
            email = input('E-mail: ')
            agenda.criar_contato(nome, telefone, email)

        # Opção para listar contatos:
        elif opcao == '2':
            agenda.listar_contatos()

        # Opção para atualizar contatos:
        elif opcao == '3':
            # agenda.listar_contatos()
            if agenda.listar_contatos() == False:
                print("Opção inválida. Tente novamente.")
            else:
                
                entrada = input("Informe o número do contato a ser atualizado: ")
                
                if entrada.isdigit():
                    indice = int(entrada) - 1
                    if (0 <= indice) and (indice + 1 <= agenda.listar_contatos()):
                        nome = input("Novo nome (deixe em branco para manter): ")
                        telefone = input("Novo telefone (deixe em branco para manter): ")
                        email = input('Novo email (deixe em branco para manter):')
                        agenda.atualizar_contato(indice, nome, telefone, email)
                    else:
                        print("Opção inválida. Tente novamente.")
                else:
                    print("Opção inválida. Tente novamente.")

        # Opção para remover contatos:
        elif opcao == '4':
            # agenda.listar_contatos()
            if agenda.listar_contatos() == False:
                print("Opção inválida. Tente novamente.")
            else:
                entrada = input("Informe o número do contato a ser atualizado: ")
                
                if entrada.isdigit():
                    indice = int(entrada) - 1
                    if (0 <= indice) and (indice + 1 <= agenda.listar_contatos()):
                        agenda.excluir_contato(indice)
                    else:
                        print("Opção inválida. Tente novamente.")
                else:
                    print("Opção inválida. Tente novamente.")


        # Opção para sair:
        elif opcao == '5':
            print("Saindo...")
            break

        # Opção caso seja digitado alguma opção não definida:
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
