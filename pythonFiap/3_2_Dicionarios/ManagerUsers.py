'''usuarios={}
opcao=input("O que deseja realizar?\n" +
            "<I> - Para Inserir um usuário\n"+
            "<P> - Para Pesquisar um usuário\n"+
            "<E> - Para Excluir um usuário\n"+
            "<L> - Para Listar um usuário: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login: ").upper()
        nome=input("Digite o nome: ").upper()
        data=input("Digite a última data de acesso: ")
        estacao=input("Qual a última estação acessada: ").upper()
        usuarios[chave]=[nome, data, estacao]
    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n"+
                  "<P> - Para Pesquisar um usuário\n"+
                  "<E> - Para Excluir um usuário\n"+
                  "<L> - Para Listar um usuário: ").upper()'''

'''usuarios={}
opcao=input("O que deseja realizar?\n" +
            "<I> - Para Inserir um usuário\n"+
            "<P> - Para Pesquisar um usuário\n"+
            "<E> - Para Excluir um usuário\n"+
            "<L> - Para Listar um usuário: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave = input("Digite o login: ").upper()
        usuarios[chave] = [input("Digite o nome: ").upper(),
                           input("Digite a última data de acesso: "),
                           input("Qual a última estação acessada: ").upper()]
    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n"+
                  "<P> - Para Pesquisar um usuário\n"+
                  "<E> - Para Excluir um usuário\n"+
                  "<L> - Para Listar um usuário: ").upper()'''

'''usuarios={}
opcao=input("O que deseja realizar?\n" +
            "<I> - Para Inserir um usuário\n"+
            "<P> - Para Pesquisar um usuário\n"+
            "<E> - Para Excluir um usuário\n"+
            "<L> - Para Listar um usuário: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        usuarios[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                       input("Digite a última data de acesso: "),
                                                       input("Qual a última estação acessada: ").upper()]
    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n"+
                  "<P> - Para Pesquisar um usuário\n"+
                  "<E> - Para Excluir um usuário\n"+
                  "<L> - Para Listar um usuário: ").upper()'''

'''from Funcoes.Funcoes_Dicionarios import *
usuarios={}
opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    opcao = perguntar()'''

from Funcoes.Funcoes_Dicionarios import *
usuarios={}

opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()

