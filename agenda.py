def saudacao (nome):
    print(f"Olá,{nome} bem vindo(a)!")
nome = input("digite seu nome: ")
saudacao(nome)

def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = [nome_contato, telefone_contato, email_contato, False]
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado com sucesso")
    return

def ver_contato(contatos):
    print("\nLista de contatos")
    for indice, contato in enumerate(contatos, start=1):
        status_favorito = "⭐" if contato[3] else ""
        nome_contato = contato[0]
        print(f"{indice}. {nome_contato} {status_favorito} ")
        

def editar_contato(contatos,indice_contato,novo_nome_contato,novo_email_contato,novo_numero_contato):
    indice_contato_ajustado = int(indice_contato)-1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado][0] = novo_nome_contato
        contatos[indice_contato_ajustado][2] = novo_email_contato
        contatos[indice_contato_ajustado][1] = novo_numero_contato
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato} {novo_email_contato} {novo_numero_contato} com sucesso")
        return

"""[0] nome
[1] telefone
[2] email
[3] favorito
"""
def contatos_favoritos(contatos, indice_contato):
    indice = int(indice_contato) -1
    if 0 <= indice < len(contatos):
        contatos[indice][3] =True
        print(f"Contato {indice +1} Marcado como favorito ☆ ")
    else:
        print("Indice de contato invalido")
        return

def deletar_contato(contatos, indice_contato):
    indice = int(indice_contato) - 1

    if 0 <= indice < len(contatos):
        contato_removido = contatos.pop(indice)
        print(f"Contato {contato_removido[0]} foi removido com sucesso")
    else:
        print("Indice de contato inválido")
def ver_informacoes(contatos):
    print("\n📒 Lista de Contatos")
    print("----------------------------")
    for indice, contato in enumerate(contatos, start=1):
        status_favorito = "⭐" if contato[3] else ""
        nome_contato = contato[0]
        email_contato = contato[1]
        numero_contato = contato[2]
        print(f"{indice}.nome:{nome_contato} {status_favorito}\n📞Telefone:{numero_contato} \n📧Email:{email_contato}  \n----------------------------")
contatos = []

while True:
    print("\nMenu do gerenciador da agenda")
    print("1. Adicionar Contato")
    print("2. Ver Contato")
    print("3. Editar contato")
    print("4. Marcar como favorito")
    print("5. deletar contato")
    print("6.ver infomações do contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")
    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar:")
        telefone_contato = input("Digite o telefone deste contato: ")
        email_contato = input("Digite o email deste contato: ")
        adicionar_contato(contatos,nome_contato,telefone_contato,email_contato)
    if escolha == "2":
        ver_contato(contatos)

    if escolha == "3":
        ver_contato(contatos)
        indice_contato=input("Digite o numero do contato que deseja alterar:")
        novo_nome = input("Digite o novo nome do contato:")
        novo_email=input("Digte o novo email do contato:")
        novo_numero =input("Digite o novo numero do contato:")
        editar_contato(contatos,indice_contato,novo_nome,novo_email,novo_numero)

    if escolha == "4":
        ver_contato(contatos)
        indice_contato= input("Digite o numero do contato que deseja marcar como favorito:")
        contatos_favoritos(contatos,indice_contato)

    if escolha == "5":
        ver_contato(contatos)
        indice_contato = input("Digite o número do contato que deseja excluir: ")
        deletar_contato(contatos, indice_contato)

    if escolha == "6":
     ver_informacoes(contatos)


    elif escolha == "7":
        print("programa finalizado")
        break
