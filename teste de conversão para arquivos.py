## teste de conversão para txt com funções built-in
# criar um dicionário vazio para preencher com as chaves: nome, telefone e email, e os valores dessas chaves serão inputados pelo usuário
# os índices precisam ser atualizados também no txt
# para sugerir um banco de dados é necessário que tenha um cabeçalho com o nome das colunas
# ponto encontrado: precisa haver uma verificação do arquivo, se tem informações nele ou não para que ele seja "criado" (como fazer?)

## teste com csv usando apenas built-in do python
# função entender o status do arquivo (existência), atribuir o cabeçalho e garantir que caso exista, siga complementando informações
def agenda_csv(dicionario, index):
    try:
        with open('agenda.csv', 'r') as agenda:
            if agenda.read().strip() == '':
                raise FileNotFoundError  
    except FileNotFoundError:
        with open('agenda.csv', 'a') as agenda:
            agenda.write('ID,Nome,Telefone,Email\n')

  #abrir o arquivo para gravar as informações inputadas
    with open('agenda.csv', 'a') as agenda:
        agenda.write(f'{index},{dicionario["Nome: "]},{dicionario["Telefone: "]},{dicionario["Email: "]}\n')

dict_contatos = {}
index = 1  

#loop condicional para coleta de informações, executado através de comandos de ecolha
while True:
    menu = input('1. salvar contatos\n2. sair\nDigite uma opção: ')

    if menu == '1': 
        dict_contatos['Nome: '] = input('Digite o nome do contato: ')
        dict_contatos['Telefone: '] = input('Digite o telefone do contato: ')
        dict_contatos['Email: '] = input('Digite o email do contato: ')

        print(dict_contatos)
        agenda_csv(dict_contatos, index)  
        index += 1 

      #loop condicional para deferir continuidade da coleta através de comando de permissão
        while True: 
            continuar = input('Deseja adicionar outro contato? (s/n): ')
            if continuar.lower() == 'n':
                print('Saindo da agenda...')
                exit()
            elif continuar.lower() == 's':
                break 
            else:
                print('Opção inválida. Digite "s" para continuar ou "n" para sair.')
    elif menu == '2':
        print('Você saiu da agenda.')
        break 
    else:
        print('Opção inválida. Tente novamente.')
