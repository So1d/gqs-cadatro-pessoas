#Sistema de Cadastro de Pessoa - versão 2 
#novo requisito - menu, consulta, alteração e listagem 

nome1 = " "
idade1 = 0
email1 = ""
nome2 = ""
idade2 = 0
email2 = ""
nome3 = ""
idade3 = 0
email3 = ""

qnd = 0
op = 0

while op != 5:
    print("===============================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    op = int(input("Escolha uma opcao: "))

    if op == 1:
        if qnd == 3: 
            print("Cadastro cheio")
        else:
            n = input("Nome: ")
            i = int(input("Idade: "))
            e = input("Email: ")
            if qnd == 0:
                nome1 = n
                idade1 = i
                email1 = e
            elif qnd == 1:
                nome2 = n
                idade2 = i
                email2 = e
            elif qnd == 2:
                nome3 = n
                idade3 = i
                email3 = e
            qnd = qnd + 1
            print("Pessoa cadastrada!")
            print("Nome: " + n)
            print("Idade: " + str(i))
            print("Email: " + e)
            if i >= 18:
                print("Situacao: Maior de idade")
            else: 
                print("Situacao: Menor de idade")
            if op == 2:
                b = input("Nome para consultar: ")
                achou = 0
            if qnd >= 1 and b == nome1:
                achou = 1
                print("Nome: " + nome1)
                print("Idade: " + str(idade1))
                print("Email: " + email1)
                if idade1 >= 18:
                    print("Situacao: Maior de idade")
                else :
                    print("Situacao: Menor de idade")
            if qnd >= 2 and b == nome2:
                achou = 1
                print("Nome: " + nome2)
                print("Idade: " + str(idade2))
                print("Email: " + email2)
                if idade2 >= 18:
                    print("Situacao: Maior de idade")
                else :
                    print("Situacao: Menor de idade")
            if qnd >= 3 and b == nome3:
                achou = 1
                print("Nome: " + nome3)
                print("Idade: " + str(idade3))
                print("Email: " + email3)
                if idade3 >= 18:
                    print("Situacao: Maior de idade")
                else :
                    print("Situacao: Menor de idade")
    elif op == 3:
        b = input("Nome para alterar: ")
        achou = 0 
        if b == nome1: 
            achou = 1
            print("Nome: " + nome1)
            print("Idade: " + str(idade1))
            print("Email: " + email1)
            n = input("Novo nome: ")
            i = int(input("Nova idade: "))
            e = input("Novo email: ")
            nome1 = n
            idade1 = i  
            email1 = e
            print("AAlterado!")
        elif b == nome2:
            achou = 1
            print("Nome: " + nome2)
            print("Idade: " + str(idade2))
            print("Email: " + email2)
            n = input("Novo nome: ")
            i = int(input("Nova idade: "))
            e = input("Novo email: ")
            nome2 = n
            idade2 = i  
            email2 = e
            print("Alterado!")
        elif b == nome3:
            achou = 1
            print("Nome: " + nome3)
            print("Idade: " + str(idade3))
            print("Email: " + email3)
            n = input("Novo nome: ")
            i = int(input("Nova idade: "))
            e = input("Novo email: ")
            nome3 = n
            idade3 = i  
            email3 = e
            print("Alterado!")
        if achou == 0:
            print("Pessoa nao encontrada")
            
