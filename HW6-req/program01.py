# -*- coding: utf-8 -*-
'''
Il sindaco si una città deve pianificare un nuovo quartiere.  Voi fate
parte dello studio di architetti che deve progettare il quartiere.  Vi
viene fornito un file che contiene divisi in righe, le informazioni
che descrivono in pianta le fasce East-West (E-W) di palazzi, ciascuno
descritto da larghezza, altezza, colore da usare in pianta.

I palazzi devono essere disposti in pianta rettangolare
in modo che:
  - tutto intorno al quartiere ci sia una strada di larghezza minima
    indicata.
  - in direzione E-W (orizzontale) ci siano le strade principali,
    dritte e della stessa larghezza minima, a separare una fascia di
    palazzi E-W dalla successiva.  Ciascuna fascia E-W di palazzi può
    contenere un numero variabile di palazzi.  Se una fascia contiene
    un solo palazzo verrà disposto al centro della fascia.
  - in direzione North-South (N-S), tra ciascuna coppia di palazzi
    consecutivi, ci dev'essere almeno lo spazio per una strada
    secondaria, della stessa larghezza minima delle altre.

Vi viene chiesto di calcolare la dimensione minima dell'appezzamento
che conterrà i palazzi.  Ed inoltre di costruire la mappa che li
mostra in pianta.

Il vostro studio di architetti ha deciso di disporre i palazzi in modo
che siano **equispaziati** in direzione E-W, e di fare in modo che
ciascuna fascia E-W di palazzi sia distante dalla seguente dello
spazio minimo necessario alle strade principali.

Per rendere il quartiere più vario, il vostro studio ha deciso che i
palazzi, invece di essere allineati con il bordo delle strade
principali, devono avere se possibile un giardino davanti (a S) ed uno
dietro (a N) di uguale profondità.  Allo stesso modo, dove possibile,
lo spazio tra le strade secondarie ed i palazzi deve essere
distribuito uniformemente in modo che tutti possano avere un giardino
ad E ed uno a W di uguali dimensioni.  Solo i palazzi che si
affacciano sulle strade sul lato sinistro e destro della mappa non
hanno giardino su quel lato.

Vi viene fornito un file txt che contiene i dati che indicano quali
palazzi mettere in mappa.  Il file contiene su ciascuna riga, seguiti
da 1 virgola e/o 0 o più spazi o tab, gruppi di 5 valori interi che
rappresentano per ciascun palazzo:
  - larghezza
  - altezza
  - canale R del colore
  - canale G del colore
  - canale B del colore

Ciascuna riga contiene almeno un gruppo di 5 interi positivi relativi
ad un palazzo da disegnare. Per ciascun palazzo dovete disegnare un
rettangolo del colore indicato e di dimensioni indicate

Realizzate la funzione ex(file_dati, file_png, spaziatura) che:
  - legge i dati dal file file_dati
  - costruisce una immagine in formato PNG della mappa e la salva nel
    file file_png
  - ritorna le dimensioni larghezza,altezza dell'immagine della mappa

La mappa deve avere sfondo nero e visualizzare tutti i palazzi come segue:
  - l'argomento spaziatura indica il numero di pixel da usare per lo
    spazio necessario alle strade esterne, principali e secondarie,
    ovvero la spaziatura minima in orizzontale tra i rettangoli ed in
    verticale tra le righe di palazzi
  - ciascun palazzo Ã¨ rappresentato da un rettangolo descritto da una
    quintupla del file
  - i palazzi descritti su ciascuna riga del file devono essere
    disegnati, centrati verticalmente, su una fascia in direzione
    E-W della mappa
  - i palazzi della stessa fascia devono essere equidistanti
    orizzontalmente l'uno dall'altro con una **distanza minima di
    'spaziatura' pixel tra un palazzo ed il seguente** in modo che tutti
    i primi palazzi si trovino sul bordo della strada verticale di
    sinistra e tutti gli ultimi palazzi di trovino sul bordo della
    strada di destra
    NOTA se la fascia contiene un solo palazzo dovrà essere disegnato
    centrato in orizzontale
  - ciascuna fascia di palazzi si trova ad una distanza minima in
    verticale dalla seguente per far spazio alla strada principale
    NOTE la distanza in verticale va calcolata tra i due palazzi più
    alti delle due fasce consecutive.
    Il palazzo più grosso della prima riga si trova appoggiato al
    bordo della strada principale E-W superiore.
    Il palazzo più grosso dell'ultima riga si trova appoggiato al
    bordo della strada principale E-W inferiore
  - l'immagine ha le dimensioni minime possibili, quindi:
     - esiste almeno un palazzo della prima/ultima fascia a
       'spaziatura' pixel dal bordo superiore/inferiore
     - esiste almeno una fascia che ha il primo ed ultimo palazzo a
       'spaziatura' pixel dal bordo sinistro/destro
     - esiste almeno una fascia che non ha giardini ad E ed O

    NOTA: nel disegnare i palazzi potete assumere che le coordinate
        saranno sempre intere (se non lo sono avete fatto un errore).
    NOTA: Larghezza e altezza dei rettangoli sono tutti multipli di due.
'''

import images


def createImg(w, h, c=(0, 0, 0)):
    '''
    Crea un'immagine vuota (nera di default)
    di dimensioni w*h
    '''
    return [
                [c for j in range(w)]
                for i in range(h)
           ]


def drawRect(src, x, y, w, h, c=(0, 0, 0)):
    '''
    Disegna un rettangolo w*h di colore c
    a partire dal punto (x, y)
    '''
    for i in range(y, y + h):
        src[i][x:x + w] = [c] * w


def getPalaces(ftesto):
    '''
    Legge le piante dei
    palazzi da ftesto
    '''
    p = []                                                                      # Matrice dei palazzi
    with open(ftesto) as f:                                                     # Apri il file
        for i in f.readlines():                                                 # Per ogni riga del file (= un isolato)
            l = []                                                              # Isolato
            row = [int(j) for j in ''.join(i.split()).split(',')[:-1]]          # Estrai i valori dalla riga
            for j in range(0, len(row), 5):                                     # Per ogni slice di 5 valori
                w, h, r, g, b = (row[j + k] for k in range(5))                  # Ottieni larghezza, altezza e colore
                l.append((w, h, (r, g, b)))                                     # Aggiungi il palazzo all'isolato
            p.append(l)                                                         # Aggiungi l'isolato alla matrice

    return p                                                                    # Ritorna i palazzi


def getWidthHeight(palaces, spaziatura):
    '''
    Calcola la larghezza e l'altezza
    della pianta da disegnare, ritorna
    le dimensioni della pianta e le dimensioni
    degli isolati
    '''
    pw = []                                                                     # Larghezza W-E degli isolati
    maxh = []                                                                   # Lato N-S massimo per ogni isolato
    for i in palaces:                                                           # Per ogni isolato
        pw.append(sum([j[0] for j in i]) + spaziatura * (len(i) - 1))           # Stima la larghezza assumendo che sia il più largo
        maxh.append(max([j[1] for j in i]))                                     # Trova il lato N-S massimo e aggiungilo alla lista

    maxw = max(pw)                                                              # Trova l'isolato più largo
    w = maxw + spaziatura * 2                                                   # Prendi il più largo e assegnalo alla
                                                                                #  larghezza finale della pianta
    h = sum(maxh) + spaziatura * (len(palaces) + 1)                             # Calcola l'altezza della pianta finale
                                                                                #  (somma lati massimi + strade)
    return w, h, maxw, maxh                                                     # Ritorna le dimensioni calcolate


def drawBlock(img, b, bindex, x, y, maxh, deltaw):
    '''
    Disegna l'isolato b a partire da (x, y)
    secondo le misure date
    '''
    for i in b:                                                                 # Per ogni palazzo dell'isolato
        deltah = (maxh[bindex] - i[1]) // 2                                     # Calcola la dimensione dei due giardini
        if len(b) == 1:                                                         # Se l'isolato contiene un solo palazzo
            x += deltaw                                                         # Assumi due strade secondarie ai lati e spostati a destra
        drawRect(img, x, y + deltah, i[0], i[1], i[2])                          # Disegna il palazzo da dove ti trovi
        x += i[0] + deltaw                                                      # E spostati di (lungh. palazzo + lungh. strada)


def drawPalaces(p, spaziatura, w, h, maxw, maxh):
    '''
    Disegna la pianta del quartiere
    e la ritorna
    '''
    img = createImg(w, h)                                                       # Crea la pianta con le dimensioni calcolate
    x, y = spaziatura, spaziatura                                               # Coordinate per il disegno

    for i, ix in enumerate(p):                                                  # Per ogni isolato
        deltaw = (maxw - sum([j[0] for j in ix]))                               # Calcola la dimensione delle strade secondarie
        if len(ix) > 1:                                                         # Se l'isolato contiene più di un palazzo
            deltaw //= (len(ix) - 1)                                            # Assumi strade = palazzi - 1
        else:                                                                   # Altrimenti
            deltaw //= 2                                                        # Assumi due strade
        drawBlock(img, ix, i, x, y, maxh, deltaw)                               # Disegna l'isolato con i parametri calcolati
        x = spaziatura                                                          # Finito l'isolato ritorna a ovest
        y += maxh[i] + spaziatura                                               # E spostati a sud

    return img                                                                  # Ritorna la pianta disegnata


def ex(file_dati, file_png, spaziatura):
    '''
    Disegna la pianta del quartiere
    descritto in file_dati, la scrive
    in file_png e ritorna le dimensioni
    '''
    p = getPalaces(file_dati)                                                   # Legge i dati sulla pianta dal file di testo
    w, h, maxw, maxh = getWidthHeight(p, spaziatura)                            # Calcola le dimensioni della pianta e dell'isolato
    img = drawPalaces(p, spaziatura, w, h, maxw, maxh)                          # Disegna i palazzi con le caratteristiche richieste
    images.save(img, file_png)                                                  # Salva l'immagine nel file richiesto

    return w, h                                                                 # Ritorna le dimensioni della piantina


if __name__ == '__main__':
    # inserisci qui i tuoi test personali per debuggare
    ex('matrices/mat-16-25.txt', '/dev/null', 25)
    pass
