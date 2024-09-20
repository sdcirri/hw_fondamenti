# -*- coding: utf-8 -*-
'''Nel gioco "chi la spara più grossa" si sfidano due concorrenti A e
B che generano delle sequenze di valori di lunghezza variabile,
rappresentati da un singolo carattere. Le sequenze possono essere di
lunghezza diversa poiché i valori possono essere separati da uno (o
più) spazi bianchi e tab ('\t'). Il numero di caratteri non spazio è,
comunque, uguale per ogni sequenza.

Ogni elemento della sequenza di A viene confrontato con l'elemento
corrispondente della sequenza di B e viene assegnato un punto
- al concorrente che ha generato il valore più alto (per esempio A),
  se la differenza fra il valore di A e il valore di B è inferiore o
  uguale ad un parametro k deciso all'inizio della sfida
- al concorrente che ha generato il valore più basso (per esempio B),
  se la differenza fra il valore di A e il valore di B è superiore
  a k (cioè A ha sballato)
- a nessuno, in caso di pareggio.
Al termine dell'assegnazione, vince chi ha ottenuto più punti. In caso
di pareggio, vince il giocatore che ha generato la sequenza con somma
totale dei valori inferiore.  In caso di ulteriore pareggio, il punto
è assegnato al giocatore con la prima sequenza in ordine
lessicografico. Non può capitare che due giocatori generino
esattamente la stessa sequenza di valori.

Si deve realizzare una funzione che prende in input il parametro k e
una lista di stringhe corrispondenti a un torneo di "chi la spara più
grossa" e restituisce la classifica finale del torneo. La stringa in
posizione i corrisponde alla sequenza dei valori generati dal
giocatore i.

Nel torneo, ogni giocatore sfida tutti gli altri con la propria
sequenza: ovvero, se ci sono n giocatori, ogni giocatore farà n-1
sfide. Il numero di sfide vinte determina la posizione in
classifica. In caso di parità di sfide vinte, i giocatori sono
ordinati in modo crescente in base alla posizione.

Esempio di partite a chi la spara più grossa fra tre giocatori.
    Se k=2 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2.
        Alla fine 0 ha 1 sfida, 1 ha 2 sfide e 2 ha 0 sfide, per cui
            la classifica finale sarà [1, 0, 2].

    Se k=1 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 0 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 2 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        Alla fine 0 ha 2 sfide, 1 ha 0 sfide e 2 ha 1 sfida, per cui
            la classifica finale sarà [0, 2, 1].

    Se k=10 e la lista è  [ "abc",  "dba" , "eZo"]
        La sfida 0, 1 è un pareggio, ma vince 0 perché la sua sequenza
            ha somma inferiore.
        La sfida 0, 2 è vinta da 0 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'c'.
        La sfida 1, 2 è vinta da 1 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'a'
        Alla fine 0 ha 2 sfide, 1 ha 1 sfida e 2 ha 0 sfide, per cui
            la classifica finale sarà [0, 1, 2].

    Se k=50 e la lista è  [ "A ƐÈÜ",  "BEAR" , "c Ʈ  ´  ."]
        La sfida 0, 1 è vinta da 1 per 4 punti a 0.
        La sfida 0, 2 è vinta da 2 per 3 punti a 1.
        La sfida 1, 2 è vinta da 1 per 3 punti a 1.
        Alla fine 0 ha 0 sfide, 1 ha 2 sfide e 2 ha 1 sfida, per cui
        la classifica finale sarà [1, 2, 0].

Il timeout per l'esecuzione di ciascun test è di 6 secondi (*2 sualla VM)

'''


def compareChar(a, b, k):
    '''
    Gioca una sfida tra i caratteri a e b
    e ritorna il carattere vincente
    '''
    if a == b:                                                              # In caso di pareggio
        return                                                              #  ritorna None

    va, vb = ord(a), ord(b)

    if va > vb:                                                             # Trova il maggiore
        return a if va - vb <= k else b                                     # Se il delta è <= k ritorna il maggiore,
                                                                            #  altrimenti ritorna il minore (il maggiore ha sballato)
    else:                                                                   # Necessariamente vb > va (uguaglianza esclusa all'inizio)
        return b if vb - va <= k else a


def compareStr(ia, a, ib, b, k):
    '''
    Gioca una sfida tra i giocatori ia e ib,
    che giocano rispettivamente le stringhe a e b
    e ritorna il vincitore (ia o ib)
    '''
    assert a != b, 'Errore! Sequenze uguali!'

    puntia, puntib = 0, 0                                                   # Contatori punteggio
    sommaa, sommab = 0, 0                                                   # Somme
    
    matcha = ''.join(a.split())                                             # Elimina spazi
    matchb = ''.join(b.split())

    for i in range(len(matcha)):                                            # Per ogni sfida
        sommaa += ord(matcha[i])                                            # Aggiorna le somme
        sommab += ord(matchb[i])

        win = compareChar(matcha[i], matchb[i], k)                          # Determina il carattere vincitore

        if win == matcha[i]:                                                # Se è di a
            puntia += 1                                                     # Aggiungi un punto ad a
        elif win == matchb[i]:                                              # Se è di b
            puntib += 1                                                     # Aggiungi un punto a b
                                                                            # Altrimenti non fare nulla (pareggio)
    if puntia > puntib:                                                     # Se a ha fatto più punti
        return ia                                                           # Vince a
    elif puntib > puntia:                                                   # Se b ha fatto più punti
        return ib                                                           # Vince b
    elif sommaa < sommab:                                                   # Altrimenti (pareggio) vince
        return ia                                                           #  chi ha la somma minore
    elif sommab < sommaa:
        return ib
    else:                                                                   # Altrimenti (ancora pareggio)
        return ia if matcha < matchb else ib                                # Ritorna il primo in ordine lessicografico


def mkClassifica(punti):
    '''
    Crea una classifica di giocatori data una lista di punteggi
    assumendo che la lista sia ordinata per giocatore
    '''
    gioc = range(len(punti))                                                # Crea un range di giocatori
    clas = list(zip(gioc, punti))                                           # Lo unisce alla lista dei punti (assumendo che sia ordinata per giocatore)
    clas.sort(key=lambda p: p[1], reverse=True)                             # Ordina la classifica per punteggio decrescente

    return [i[0] for i in clas]                                             # Estrae l'elemento 0 di ogni tupla (cioè i giocatori) di clas e ne ritorna la lista


def ex(matches, k):
    # Inserisci qui il tuo codice
    board = [0] * len(matches)                                              # Lista dei punteggi

    for i in range(len(matches)):                                           # Per ogni giocatore
        for j in range(i+1, len(matches)):                                  # "Sfida" tutti i successivi
            win = compareStr(i, matches[i], j, matches[j], k)               # Determina il vincitore
            board[win] += 1                                                 # Aggiunge un punto al vincitore

    return mkClassifica(board)                                              # Crea la classifica finale e la ritorna


if __name__ == "__main__":
    # Inserisci qui i tuoi test
    pass