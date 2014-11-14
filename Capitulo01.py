'''
Capitulo 1
Ejercicio 2
Crea un programa que revise por anagramas en dos palabras
'''
def check_anagrams(first_word, second_word):
    '''
    Compara dos palabras y regresa 1 si es un anagrama y 0 si no.
    '''
    if(sorted(first_word)==sorted(second_word)):
        print 1
    else:
        print 0