import random
import os
import time
def começar():
    os.system('clear') or None
    print(" Cripto :)")
    print(' 1 : encriptar')
    print(' 2 : decriptar')
    r = input("    ")
    
    if r == "1":
        encriptar()
    
    elif r == "2":
        decriptar()
    else:
        os.system('clear') or None
        print(f" '{r}' não é uma das opções")
        print (' Retornando ao menu em:')
        a = 3
        for i in range(1, 4):
            print(a)
            a = a - 1
            time.sleep(1)
        começar()




def decriptar():
    os.system('clear') or None
    print(' Insira a chave:')
    chave = int(input(' '))
    os.system('clear') or None
    print(' Insira a mensagem criptografada')
    frase_encriptada = str(input(' '))
    frase_decriptada = ""
    for i in frase_encriptada:
        valor_original = ord(i)
        for j in range(chave):
            if valor_original == 32:
                valor_original = 126
            else:
                valor_original = valor_original - 1
        frase_decriptada += chr(valor_original)
    os.system('clear') or None
    print("Frase decriptada:\n")
    print(frase_decriptada)
    input('Aperte qualquer tecla para retornar ao menu.')
    os.system('clear') or None
    print (' Retornando ao menu em:')
    a = 3
    for i in range(1, 4):
        print(a)
        a = a - 1
        time.sleep(1)
    começar()

def encriptar():
    os.system('cls') or None
    print("Digite uma frase para ser encriptada:")
    frase_original = str(input())
    chave = random.choice(range(3, 50))
    frase_encriptada = ''
    for i in frase_original:
        valor_original = ord(i)
        for j in range(chave):
            if valor_original == 126:
                valor_original = 32
            else:
                valor_original += 1
            
        frase_encriptada += chr(valor_original)
        
    os.system('clear') or None
    print("Frase encriptada:\n")
    print(frase_encriptada)
    print("\nA chave é:\n")
    print(chave)
    print('\nA chave é uma sequência númerica essencial para o processo de decriptação, sendo assim guarde-a com frase caso queira decripta-la.\n')
    input('Aperte qualquer tecla para retornar ao menu\n')
    os.system('clear') or None
    print (' Retornando ao menu em:')
    a = 3
    for i in range(1, 4):
        print(a)
        a = a - 1
        time.sleep(1)
    começar()


        
    
começar()
