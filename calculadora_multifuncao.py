#CALCULADORA MULTI-FUNÇÃO

def calculadora():
    print("CALCULADORA------Bem vindo a calculadora")
    print("Digite '0' se quiser parar e voltar ao menu")
    while True:
        numero1 = float(input("Digite o primero número"))
        if numero1 == 0.0:
              menu()
        operacao = input("""Escolha a operacao:
        A)multiplicação
        B)Adição
        C)Divisão
        D)Subtração
        Digite apenas a alternativa:""")
        numero2 = float(input("Digite o segundo número"))
        
        if operacao == "A" or operacao == "a":
          print(numero1 * numero2)
        elif operacao == "B" or operacao == "b":
            print(numero1 + numero2)
        elif operacao == "C" or operacao == "c":
            print(f"{numero1 / numero2}, e o resto é {numero1 % numero2}")
        elif operacao == "D" or operacao == "d":
            print(numero1 - numero2)

def media():
    print("DETERMINADOR DE MÉDIA------Bem vindo ao determinador de média")
    print("Digite '0' se quiser parar e voltar ao menu")
    
    while True:
        contador = 0
        numeros1 = input("""Digite os números que quer determinar a média
no seguinte formato: x, x, x, x:""")
        if numeros1 == "0":
            menu()
        lista1 = numeros1.split(",")
        for n in lista1:
            contador += int(n.strip())
        print(contador / len(lista1))

def par_ou_impar():
    print("PAR OU ÍMPAR------Bem vindo ao par ou impar")
    print("Digite '0' se quiser parar e voltar ao menu")

    while True:
        numero3 = int(input("Digite um número e direi se é par ou ímpar:"))
        if numero3 == 0:
            menu()
        elif numero3 % 2 == 0:
            print(f"O número {numero3} é par")
        else:
            print(f"O número {numero3} é ímpar")

def tabuada():
    print("TABUADA-----Bem vindo a tabuada")
    print("Digite '0' se quiser parar e voltar ao menu")

    while True:
        numero4 = int(input("Digite um número para mostrarmos sua tabuada:"))
        if numero4 == 0:
            menu()
        soma = 1
        while soma <= 10:
            print(f"{numero4} x {soma} = {numero4 * soma}")
            soma+=1

def menu():
    opcoes = input("""MENU-----Olá! Bem-vindo!
    Escolha uma opcao:
    A) Tabuada 
    B) Calculadora 
    C) Determinador de média
    D) Par ou Impar
    Digite a opcao que você quer(apenas a letra):""")
    
    if opcoes == "B" or opcoes == "b":
        calculadora()
    elif opcoes == "C" or opcoes == "c":
        media()
    elif opcoes == "D" or opcoes == "d":
        par_ou_impar()
    elif opcoes == "A" or opcoes == 'a':
        tabuada()


menu()


