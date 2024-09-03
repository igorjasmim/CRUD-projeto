<<<<<<< HEAD
from contato import Contato  # Aqui importamos a biblioteca Contato criada para gerenciar os contatos da lista


class Agenda:
    def __init__(self):
        self.contatos = []

    def criar_contato(self, nome, telefone):
        novo_contato = Contato(nome, telefone)
        self.contatos.append(novo_contato)
        print(novo_contato)

    def listar_contatos(self):  # lista os contatos e informa se a lista esta vazia
        if not self.contatos:
            print('Nenhum contato na agenda.')
            return False
        else:
            for idx, contato in enumerate(self.contatos, start=1):
                print(f'{idx}. {contato}')
            return len(self.contatos)

    def atualizar_contato(self, indice, nome=None, telefone=None):  # atualiza um contato existente
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].atualizar(nome, telefone)
            print(f'Contato {indice + 1} atualizado com sucesso!')
        else:
            print('Índice de contato inválido.')

    def excluir_contato(self, indice):  # excluir um contato pelo indice
        if 0 <= indice < len(self.contatos):
            contato_removido = self.contatos.pop(indice)
            print(f'Contato {contato_removido.nome} removido com sucesso!')
        else:
            print('Índice de contato inválido.')
=======
from contato import Contato

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
            return len(self.contatos)
    
    def atualizar_contato(self, indice, nome=None, telefone=None):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].atualizar(nome, telefone)
            print(f'Contato {indice + 1} atualizado com sucesso!')
        else:
            print('Índice de contato inválido.')
    
    def excluir_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            contato_removido = self.contatos.pop(indice)
            print(f'Contato {contato_removido.nome} removido com sucesso!')
        else:
            print('Índice de contato inválido.')
>>>>>>> 8a0aec1fb5516f81d067bd23db27e5c8a15f580d
