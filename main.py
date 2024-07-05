from media import media 
from mediana import mediana
from moda import moda
from desvio import desvio


def comparar(lista):
    menor  =  min(lista)
    maior = max(lista)
    amplitude =  maior  -  menor
    print(f'''
    MENOR NOTA  -  {menor}
    MAIOR NOTA  -  {maior}
    AMPLITUDE - {amplitude}
    
    ''')


def system_notes():
    lista_nome = []
    lista_notas = []
    s = input('Digite n para parar')
    
    while s != 'n':
        nome =  input('Digite o nome do aluno') 
        nota1  =  float(input('Digite a nota do aluno'))
        nota2  =  float(input('Digite a nota do aluno'))
        nota3  =  float(input('Digite a nota do aluno'))
        lista_notas += (nota1, nota2, nota3,'|')
        print(lista_notas)
        lista_nome.append(nome)
        s = input('Digite n para parar')
        
    print('Nomes:', lista_nome)
    print('Notas', lista_notas)  
    print('-----//--------------------------//-------------------')
 
    if '|' in lista_notas:
            lista_notas.remove('|')
            print(lista_notas)
            moda1 =  moda(lista_notas)
            media1 =  media(lista_notas)
            mediana1 =  mediana(lista_notas)
            desvio1  =  desvio(lista_notas)
            print(f'''ESTATISTICA:
            MODA - {moda1}
            MEDIA - {media1}
            MEDIANA - {mediana1}
            DESVIO - {desvio1}  
            
            ''')
    





system_notes()    