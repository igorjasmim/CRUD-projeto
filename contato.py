class Contato:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone
        
    def __len__(self) -> None:
        return 0
    
    def atualizar(self, nome=None, telefone=None):
        if nome:
            self._nome = nome
        if telefone:
            self._telefone = telefone

    def __repr__(self) -> str:
        return f'Nome: {self._nome} \t Telefone: {self._telefone}'
            
    @property
    def nome(self):
        return self._nome
    
    @property
    def telefone(self):
        return self._telefone 
        
    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome.strip() or not novo_nome.isalpha():
            raise ValueError("Nome inválido. Deve conter apenas letras e não deve ser vazio ou numérico.")
        self._nome = novo_nome
    
    @telefone.setter
    def telefone(self, novo_telefone):
        if not isinstance(novo_telefone, int):
            raise ValueError("O telefone deve ser um número inteiro")
        self._telefone = novo_telefone