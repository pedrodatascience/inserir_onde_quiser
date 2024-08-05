# lista de nomes
nomes = ['Fulano', 'Ciclano', 'João']

#usuário insere nome
novo_nome = input('\nInforme o nome: ').capitalize()
posicao = int(input('Informe a posição do nome: '))

# insere o novo nome no local indicado
nomes.insert(posicao, novo_nome)

#imprime a lista
for nome in nomes:
    print(nome)

#ordena a lista
nomes.sort()

#exibe a lista ordenada
for nome in nomes:
    print(nome)