#funzione 1

insieme_di_parole = 'BARICA ABARICI ABARICO ABATINI ABATINO ABBACAI ABBACHI ABBADAI ABBADIA ABBADIE ABBAGLI ABBAIAI ABBAINI ABBAINO ABBALLA ABBALLE ABBALLI ABBALLO ABBANCA ABBANCO ABBARBA ABBARBI ABBARBO ABBARCA ABBARCO ABBARRA ABBARRI ABBARRO ABBASSA ABBASSI ABBASSO ABBASTA ABBASTI ABBASTO ABBATTA ABBATTE ABBATTI ABBATTO ABBAZIA ABBAZIE ABBELLA ABBELLI ABBELLO ABBIADA ABBIADI ABBIADO ABBIAMO ABBIANO ABBIATE ABBICAI ABBICCI ABBICHI ABBIGLI ABBINAI ABBISCI ABBITTA ABBITTI ABBITTO ABBOCCA ABBOCCO ABBOFFA ABBOFFI ABBOFFO ABBONAI ABBONDA ABBONDE ABBONDI ABBONDO ABBONII ABBORDA ABBORDI ABBORDO ABBORRA ABBORRE ABBORRI ABBORRO ABBOTTA ABBOTTI ABBOTTO ABBOZZA ABBOZZI ABBOZZO ABBRACI ABBRAGI ABBREVI ABBRIVA ABBRIVI ABBRIVO ABBRUCI ABBRUMA ABBRUMI ABBRUMO ABBRUNA ABBRUNI ABBRUNO ABBRUTI ABBUFFA ABBUFFI ABBUFFO ABBUIAI ABBUINO ABBUONA ABBUONI ABBUONO ABDICAI ABDICHI ABDOTTA ABDOTTE ABDOTTI ABDOTTO ABDUANA ABDUANE ABDUANI ABDUANO ABDURRA ABDURRE ABDURRO ABDUSSE ABDUSSI ABENULA ABENULE ABERRAI ABETAIA ABETAIE ABETINA ABETINE ABETINI ABETINO ABIETTA ABIETTE ABIETTI ABIETTO ABILITA ABILITI ABILITO ABISSAI ABITANO ABITARE ABITATA ABITATE ABITATI ABITATO ABITAVA ABITAVI ABITAVO ABITERA'
parole =insieme_di_parole.split(' ')  #rendere una lista separata da marcatori in questo caso ' '

'''
len()
è anche un metodo integrato in Python,
che restituisce il numero di stringhe in un array o conta la lunghezza degli elementi
in un oggetto. 
Questo metodo accetta solo un parametro:
una stringa, byte, elenco, oggetto, set o una raccolta.
Solleverà un’eccezione TypeError se l’argomento è mancante o non valido.
'''
print(len(parole))

#funzione 2

'''
Il metodo count() è un metodo integrato in Python.
 
 Richiede tre parametri e restituisce il numero di occorrenze
  in base alla sottostringa data:

    substring (richiesto) - una parola chiave da cercare nella stringa
    start (opzione) - indice da dove inizia la ricerca
    end (opzione) - indice di dove finisce la ricerca

Nota: l’indice inizia da 0 in Python.

Sintassi di count():
string.count(substring, start, end)
'''

ricerca = parole.count('albino')

print(ricerca)

'''
Il metodo listdir() del modulo os prende il percorso della directory
come input e restituisce una lista di tutti i file in quella directory.
Poiché vogliamo trovare il file specifico nella directory,
dovremo scorrere i nomi dei file per trovare il file richiesto.
L’esempio di codice seguente mostra come trovare un file specifico
iterando attraverso il file usando il metodo listdir() in Python.

'''

import os

files2 = os.listdir("subcartella esercizio 3")
print(files2)

myfile = ''
for root, dirs, files in os.walk("bsfrd"):
    for file in files:
        if file == files:
            print(file)



print(len(files2))

'''
CLASSI

Le classi servono a unire insieme dati e funzionalità.
Creare una classe equivale a creare un nuovo tipo,
a partire dal quale possono essere create nuove istanze (oggetti).
Ciascuna istanza può avere degli attributi suoi propri,
che ne mantengono lo stato.
Le istanze possono anche avere dei metodi (definiti nella classe)
che ne modificano lo stato.

La definizione delle classi, come quella delle funzioni (l’istruzione def)
deve essere eseguita prima di avere qualsiasi effetto.
(Si potrebbe anche collocare la definizione in un ramo di un’istruzione if,
o all’interno di una funzione.)

le istruzioni all’interno di una definizione di classe sono in genere definizioni
di funzione: ma sono permesse anche altre istruzioni,
talvolta sono anzi utili (ne riparleremo in seguito).
Le definizioni di funzione all’interno della classe di solito hanno una particolare lista
di parametri, dovuta alle convenzioni di chiamata per i metodi 

Quando il flusso di esecuzione del codice entra nella definizione della classe,
un nuovo namespace viene creato e usato come scope locale: ovvero, 
tutte le successive assegnazioni di variabili locali finiscono in questo nuovo namespace. 
In particolare, le definizioni di funzione collegano qui il nome della funzione

Quando si esce dalla definizione della classe nel modo normale
(perché il flusso di esecuzione abbandona la classe), viene creato un oggetto-classe.
Questo oggetto è in sostanza un «contenitore» per il contenuto del namespace
creato dalla definizione della classe: diremo di più sugli oggetti-classe 
nella prossima sezione. Lo scope locale originario (quello che era attivo subito prima
di entrare nella definizione della classe) viene ripristinato e l’oggetto-classe
viene collegato in questo namespace al nome fornito nell’intestazione
della definizione della classe (nel nostro esempio, ClassName).
'''


'''class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print('ciao sono', self.nome)

class Insegnate(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        #super aumenta il grado da parametro di classe figli a madre
        self.materia = materia

    def saluta(self):
        print('Buongiorno sono', self.nome, self.cognome)

    def dati_voto(self):
        print('bravo, un bel 8')



persona1 = Persona('Luca', 'Borbone')
insegnate1 = Insegnate('Maria', 'Rossi', 'Matematica')

insegnate1.saluta()
insegnate1.dati_voto()'''



'''
database per studenti
'''
'''
class studente:
    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi

    def scheda_personale(self):
        return f'Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso di studi:{self.corso_di_studi}'


studente1 = studente('mike','pitone','programmazzione')
studente2 = studente('marta','rossi', 'scienze')
'''


'''
#locazione dei file
print(studente1)
print(studente2)
'''

'''
#due modiu di richieamare il file maa la seconda utile per le input
print(studente1.scheda_personale())
print(studente.scheda_personale(studente2))
'''


'''
Getter e Setter non sono gli stessi di altri linguaggi di programmazione
orientati agli oggetti.
Fondamentalmente,lo scopo principale dell'utilizzo di getter e setter nei programmi
orientati agli oggetti è garantire l'incapsulamento dei dati.
Le variabili private in Python non sono in realtà campi nascosti come in altri linguaggi
orientati agli oggetti. 
Getter e Setter in Python sono spesso usati quando:

Usiamo getter e setter per aggiungere la logica di convalida
 per ottenere e impostare un valore.
 Per evitare l'accesso diretto a un campo di classe,
 ad esempio le variabili private non possono essere accessibili direttamente
 o modificate da un utente esterno.
 
 
 Per ottenere proprietà getter e setter, se definiamo i normali metodi 
 get() e set() non rifletterà alcuna implementazione speciale. 
 
 
 Esempio:
 
 # Python program showing a use
# of get() and set() method in
# normal function
  
class Geek:
    def __init__(self, age = 0):
         self._age = age
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x
  
raj = Geek()
  
# setting the age using setter
raj.set_age(21)
  
# retrieving age using getter
print(raj.get_age())
  
print(raj._age)

Output:

21
21

Nelle funzioni di codice sopra get_age() e set_age() 
agiscono come normali funzioni e non hanno alcun impatto come getter e setter,
per ottenere tale funzionalità Python ha una funzione speciale property().
Nelle funzioni di codice sopra get_age() e set_age()
agiscono come normali funzioni e non hanno alcun impatto come getter e setter,
per ottenere tale funzionalità Python ha una funzione speciale property().



Utilizzo della funzione property() per ottenere il comportamento di getter e setter

In Python property() è una funzione incorporata che crea e restituisce un oggetto proprietà.
Un oggetto proprietà ha tre metodi:
getter(), setter() e delete(). 
La funzione property() in Python ha quattro argomenti proprietà (fget, fset, fdel, doc),
fget è una funzione per recuperare un valore di attributo.
fset è una funzione per impostare un valore di attributo.
fdel è una funzione per eliminare un valore di attributo.
doc crea una docstring per l'attributo.
Un oggetto proprietà ha tre metodi, getter(), setter() e delete() per specificare
fget, fset e fdel individualmente.

Per esempio

# Python program showing a
# use of property() function
  
class Geeks:
     def __init__(self):
          self._age = 0
       
     # function to get value of _age
     def get_age(self):
         print("getter method called")
         return self._age
       
     # function to set value of _age
     def set_age(self, a):
         print("setter method called")
         self._age = a
  
     # function to delete _age attribute
     def del_age(self):
         del self._age
     
     age = property(get_age, set_age, del_age) 
  
mark = Geeks()
  
mark.age = 10
  
print(mark.age)

Output:

setter method called
getter method called
10


Nel codice sopra c'è solo un'istruzione print alla riga #264
ma l'output è costituito da tre righe a causa del metodo setter set_age()
chiamato nella riga #262 e del metodo getter get_age() chiamato nella riga #264.
Quindi l'età è un oggetto proprietà che aiuta a mantenere sicuro l'accesso della variabile
privata
Utilizzo dei @property decorators per ottenere il comportamento di getter e setter
Nel metodo precedente abbiamo usato la funzione property() 
per ottenere il comportamento di getter e setter.
Tuttavia,getter e setter vengono utilizzati anche per convalidare l'acquisizione
e l'impostazione del valore degli attributi.
C'è un altro modo per implementare la funzione di proprietà,
ad esempio usando decoratore.
Python @property è uno dei decoratori integrati.
Lo scopo principale di qualsiasi decoratore è modificare i metodi o gli attributi
della classe in modo tale che l'utente della classe non debba apportare alcuna modifica
 al codice.
 
 Per esempio
 
 # Python program showing the use of
# @property
  
class Geeks:
     def __init__(self):
          self._age = 0
       
     # using property decorator
     # a getter function
     @property
     def age(self):
         print("getter method called")
         return self._age
       
     # a setter function
     @age.setter
     def age(self, a):
         if(a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
         print("setter method called")
         self._age = a
  
mark = Geeks()
  
mark.age = 19
  
print(mark.age)

Output:

setter method called
getter method called
19

Nel codice sopra è chiaro che come usare @property decorator per creare getter e setter
in modo Python.
La riga 311-313 funge da codice di convalida che solleva un ValueError
se proviamo a inizializzare l'età con un valore inferiore a 18,
in questo modo è possibile applicare qualsiasi tipo di convalida nelle funzioni 
getter o setter.

'''




