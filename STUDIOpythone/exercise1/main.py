'''
dati i file 
nomi.txt e punteggi.txt

fare un programma che prende la lista nomi dal file
raccolga i punteggi dal second file e li assocci
 in base all'ordine
e li srciva su un altro file in classifica
 dal più forte al più scarso chimamato 
 classifica.out
'''
if __name__  == "__main__":
    '''
    dare nome file ed utilizzare dopo = open per indicargli di importare il file
    Il file aperto rimarrà aperto fino a quando non verrà chiuso manualmente
     dal programmatore tramite la funzione close(). 
    '''
    file = open('nomi.txt')  # dare nome file ed utilizzare dopo = open per indicargli di importare il file
    file2 = open('punteggi.txt')
    content = file.read()
    content2 = file2.read()
    #print(content)
    #print(content2)

    '''
     La chiusura del file che non più in uso è essenziale poiché se non è chiuso,
      il file potrebbe danneggiarsi o l’intero programma potrebbe bloccarsi.
    Il codice seguente usa la funzione close() per chiudere il file in Python.
    '''
    file.close()
    file2.close()

    listanomi = content.splitlines()   #rendere una lista da colonna in riga
    listapunteggio = content2.split(',')  #rendere una lista separata da marcatori in questo caso ','


    '''
    zip(), che aggrega i tipi di dati iterabili in una tupla e la restituisce
    dict() crea un dizionario dalla raccolta in pythone 3 mentre nel 2 creava il dizionario
    list() trasforma in lista
    per questo caso non utilizzabile in singolo in quanto zip crea la riga e dict la trasforma in dizionario
    '''
    graduatoria = list(zip(listanomi,listapunteggio))
    #gradopunteggio = sorted(graduatoria.values()) estrai e metti in ordine solo i valori
    graduatoria.sort(reverse=True ,key=lambda x: x[1] )
    #print(graduatoria)
    '''
    #la funzione #lambda# per ottenere il tasto di confronto
    key=lambda x:x[1] indica che la chiave di confronto è il valore degli elementi del dizionario
    in questo caso gli elementi sono(punteggi.txt)
    con valore 0 indichiamo le chiavi(keys)
    in questo caso le chiavi sono(nomi.txt)
    la funzione Reverse serve a oridnare la fìlsta dal piu alto al più basso
    '''
    #grado = sorted(graduatoria.items(), key=lambda x: x[1], reverse=True)
    #print(grado)

    '''
    per creare un file si utilizza open() ma con dicitura ,w per dirgli che scriviamo sul file
    per scrivere una lista su un file in Python è usare il metodo join().
     Prende gli elementi della lista come input.
    '''
'''
Il token %s mi consente di inserire (e potenzialmente formattare) una stringa.
Nota che il token %s viene sostituito da qualsiasi cosa passo alla stringa dopo il simbolo %.
Nota anche che sto usando una tupla anche qui (quando hai solo una stringa l'uso di una tupla è facoltativo)
per illustrare che più stringhe possono essere inserite e formattate in un'unica istruzione.
'''


    with open('classifica.out', 'w') as classifica:
        msg = ['\n'.join(lst) for lst in graduatoria]
        for nome,grado in graduatoria:
            classifica.write('%s %s \n'% (nome,grado))
        classifica.close()










