# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:41:16 2020

@author: Alessandro Cabizzosu
"""

    
def creaListaCodici(scelta,n,cuo,numero_iniziale,anno,plasma):
    #presidio={1:'02',2:'02',3:'13',4:'13'}
    
    punto_prelievo={1:'00',2:'04',3:'03',4:'05'}
    codice_lavorazione={1:5, 2:7}
    unita=numero_iniziale
    lista=[]
    for i in range(n):
        codice='K14' + '{:02d}'.format(cuo) + str(anno) + punto_prelievo[scelta] + \
        '{:04d}'.format(unita) + ',' + str(codice_lavorazione[plasma]) + '\n'
        lista.append(codice)
        unita += 1
    return lista

def creaListaPfc(n_unità):
    
    lista=[]
    for i in range(n_unità):
        codice='K16pool_' + str(i+1) + ',' + '21' + '\n' 
        lista.append(codice)
    return lista

print('\n' "PROGRAMMA PER LA CREAZIONE MANUALE DELLA LISTA DI LAVORO DEI SEPARATORI" '\n')


print('Scegli che tipo di prodotto vuoi lavorare: \n')
print('Se Sangue intero: premi 1')
print('Se Pool di Piastrine: premi 2')
scelta_prodotto=int(input())
while scelta_prodotto != 1 and scelta_prodotto != 2:
    print('ERRORE! Inserisci 1 o 2')
    print('Scegli che tipo di prodotto vuoi lavorare: \n')
    print('Se Sangue intero: premi 1')
    print('Se Pool di Piastrine: premi 2')
    scelta_prodotto=int(input())

x='1'
path='C://OutputData//Ordini.txt'
lista=[]
while(x == '1'):
    
    
    if scelta_prodotto == 1:
        print('Scegli il CUO: digita 02 oppure 13 ')
        cuo=int(input())
        if cuo < 0:
                print('Percorso attuale: {}'.format(path))
                print('Inserisci il percorso:\n')
                path=input()
                continue
        while cuo != 2 and cuo != 13:
            print('ERRORE! Inserisci il CUO corretto: 02 oppure 13')
            print('Scegli il CUO: digita 02 oppure 13 ')
            cuo=int(input()) 
        print('Scegli che tipo di prelievi vuoi inserire: \n')
        print('Premi 1 per prelievi centro fisso Nuoro')
        print('Premi 2 per prelievi centro mobile Nuoro')
        print('Premi 3 per prelievi centro fisso Sorgono')
        print('Premi 4 per prelievi centro mobile Sorgono')
        scelta=int(input())
        while scelta != 1 and scelta != 2 and scelta != 3 and scelta != 4 :
            print('ERRORE! Inserisci il codice corretto: 1, 2, 3 o 4')
            print('Scegli che tipo di prelievi vuoi inserire: \n')
            print('Premi 1 per prelievi centro fisso Nuoro')
            print('Premi 2 per prelievi centro mobile Nuoro')
            print('Premi 3 per prelievi centro fisso Sorgono')
            print('Premi 4 per prelievi centro mobile Sorgono')
            scelta=int(input())
        n=int(input('Inserisci numero prelievi: '))
        num_iniziale=int(input('Inserisci le ultime 4 cifre della prima unità: '))
        anno=int(input('Inserisci ultime 2 cifre anno: '))
        plasma=int(input('Inserisci 1 per plasma B o 2 per plasma C: '))
        lista.extend(creaListaCodici(scelta,n,cuo,num_iniziale,anno,plasma))
        x=input('Se vuoi inserire altre sacche premi 1, altrimenti premi 2: ')
        while x != '1' and x != '2':
            print('ERRORE! Inserisci 1 o 2')
            x=input('Se vuoi inserire altre sacche premi 1, altrimenti premi 2: ')
        continue    
    elif scelta_prodotto == 2:
        n_unità=int(input('Inserisci n. di pool: '))
        lista=creaListaPfc(n_unità)          
        break
        
        
    
print("Le unità sono state inserite correttamente!")  

f=open(path,'a') #per windows
#f=open('/Users/mac/Desktop/OutputData/Ordini.txt','a') # per mac
f.writelines(lista)
f.close()


