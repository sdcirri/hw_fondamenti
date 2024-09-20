# -*- coding: utf-8 -*-
'''
Una serie di poster rettangolari sono stati affissi ad un muro.  I
   loro lati sono orizzontali e verticali. Ogni poster può essere
   parzialmente o totalmente coperto dagli altri. Chiameremo
   perimetro la lunghezza del contorno dell'unione di tutti i posters
   sul muro. Si guardi l'immagine in "posters.png" in cui i poster sulla
   parete compaiono in bianco coi bordi blu e la si confronti con l'immagine
   "posters1.png" in cui in rosso vengono evidenziati i soli
   bordi che contribuiscono al perimetro.

Vogliamo un programma che calcola il perimetro dei poster e produce
   una immagine simile a "posters1.png".

Progettare dunque una funzione
     ex1(ftesto, filepng)
   che prenda come parametri
   - ftesto, l'indirizzo di un file di testo contenente le informazioni sulla
     posizione dei poster sul muro,

   - filepng, nome del file immagine in formato PNG da produrre

   e restituisca il perimetro dei poster come numero di pixel rossi.

Il file di testo contiene tante righe quanti sono i poster,
   nell'ordine in cui sono stati affissi alla parete. In ciascuna
   riga ci sono le coordinate intere del vertice in basso a sinistra e
   del vertice in alto a destra del poster. I valori di queste
   coordinate sono dati come coppie ordinate della coordinata x
   seguita dalla coordinata y. Si veda ad esempio il file
   rettangoli_1.txt contenente le specifiche per i 7 posters in
   "posters.png".
   
L'immagine da salvare in filepng deve avere lo sfondo nero, altezza h
   +10 e larghezza w+10 dove h è la coordinata x massima del muro su
   cui compaiono poster e w la coordinata y massima del muro su cui
   compaiono posters. I bordi visibili dei poster sono colorati di
   rosso o di verde a seconda che appartengano al perimetro o meno.
   Notare che un pixel si trova sul perimetro (e quindi è rosso) se nel
   suo intorno (gli 8 pixel adiacenti) si trova almeno un pixel esterno
   a tutti i poster.

   Per caricare e salvare i file PNG si possono usare le funzioni load
   e save presenti nel modulo "images".

Per esempio: ex1('rettangoli_1.txt', 'test_1.png') deve costruire un file PNG
   identico a "posters1.png" e restituire il valore 1080.
   
NOTA: il timeout previsto per questo esercizio è di 1.5 secondi per ciascun
   test

ATTENZIONE: quando caricate il file assicuratevi che sia nella
    codifica UTF8 (ad esempio editatelo dentro Spyder)

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


def drawHLine(src, x, y, w, c=(0, 0, 0)):
    '''
    Disegna una riga orizzontale
    di colore c
    '''
    for i in range(x, x + w):                                                   # Per ogni colonna da x a x+w
        src[y][i] = c                                                           # Imposta il pixel i-esimo nella riga y a c


def drawVLine(src, x, y, h, c=(0, 0, 0)):
    '''
    Disegna una riga verticale
    di colore c
    '''
    for i in range(y, y + h):                                                   # Per ogni riga da y a y+h
        src[i][x] = c                                                           # Imposta il pixel i-esimo nella colonna x a c


def drawRect(src, x, y, w, h, c=(0, 0, 0)):
    '''
    Disegna un rettangolo w*h di colore c
    a partire dal punto (x, y)
    '''
    for j in range(y, y + h):
        for i in range(x, x + w):
            src[j][i] = c


def drawBorderedRect(src, x1, y1, x2, y2, border=(0, 0, 0), fill=(0, 0, 0)):
    '''
    Disegna un rettangolo di colore fill con
    un bordo di colore border dati il vertice
    in basso a sinistra (x1, y1) e il vertice
    in alto a destra (x2, y2)
    '''
    w, h = x2 - x1, y2 - y1
    drawRect(src, x1, y1, w, h, fill)                                           # Disegna il rettangolo
    
    # Traccia i 4 lati del rettangolo
    drawHLine(src, x1, y1, w, border)
    drawVLine(src, x1, y1, h, border)
    drawHLine(src, x1, y2, w + 1, border)
    drawVLine(src, x2, y1, h + 1, border)


def adjacentBlack(src, x, y):
    '''
    Controlla che almeno uno degli 8 pixel
    adiacenti a (x, y) sia nero
    '''
    return (0, 0, 0) in (
                            src[y][x + 1],
                            src[y + 1][x],
                            src[y][x - 1],
                            src[y - 1][x],
                            src[y + 1][x + 1],
                            src[y - 1][x - 1],
                            src[y - 1][x + 1],
                            src[y + 1][x - 1]
                        )


def getPerimeter(src):
    '''
    Calcola il perimetro della somma
    dei lati visibili dei poster nell'immagine
    '''
    w, h = len(src[0]), len(src)                                                # Dimensioni dell'immagine
    p = 0                                                                       # Perimetro
    
    for j in range(h):                                                          # Per ogni pixel dell'immagine
        for i in range(w):
            if src[j][i] == (0, 255, 0) and adjacentBlack(src, i, j):           # Se è verde (fa parte di un lato) ed ha
                                                                                #  un pixel nero adiacente (è visibile)
                src[j][i] = (255, 0, 0)                                         # Evidenzialo di rosso
                p += 1                                                          # Incrementa il perimetro di 1
    
    return p                                                                    # Ritorna il perimetro


def getPosters(ftesto):
    '''
    Legge le coordinate dei vertici dei
    poster da ftesto
    '''
    p = []                                                                      # Lista dei poster (matrice di vertici)
    with open(ftesto) as f:                                                     # Apri il file
        for i in f.readlines():                                                 # Per ogni riga (= un poster)
            x1, y2, x2, y1 = [int(j) for j in i.split()]                        # Ottieni le coordinate dei due vertici
            p.append([(x1, y1), (x2, y2)])                                      # Aggiungi i punti alla matrice

    return p                                                                    # Ritorna i poster


def ex1(ftesto, filepng):
    '''
    Crea un'immagine e disegna i poster secondo
    le coordinate in ftesto e ritorna il perimetro
    dei lati visibili, salvando l'immagine finale
    in filepng
    '''
    posters = getPosters(ftesto)                                                # Legge le coordinate dei poster da ftesto
    iw = max([i[0][0] for i in posters] + [i[1][0] for i in posters]) + 10      # Calcola le dimensioni dell'immagine
    ih = max([i[0][1] for i in posters] + [i[1][1] for i in posters]) + 10
    img = createImg(iw, ih)                                                     # Crea un'immagine vuota (nera)

    for i in posters:                                                           # Per ogni poster
        x1, y1 = i[0]                                                           # Scompatta le coordinate dei vertici
        x2, y2 = i[1]
        drawBorderedRect(img, x1, y1, x2, y2, (0, 255, 0), (255, 255, 255))     # Disegna il poster

    p = getPerimeter(img)                                                       # Calcola il perimetro
    images.save(img, filepng)                                                   # Salva l'immagine
    return p                                                                    # Ritorna il perimetro


if __name__ == '__main__':
    pass
