# -*- coding: utf-8 -*-
'''
    Abbiamo una sequenza di N interi con N dispari. Sottoponiamo la sequenza alla seguente
    procedura che portera' all'eventuale cancellazione di elementi della sequenza:
    - Finche' nella sequenza sono presenti numeri uguali:
       - si selezionano nella sequenza i due numeri uguali ed li si eliminano ricompattando i numeri rimanenti.

    Data la sequenza di interi noi siamo interessati a trovare tutte le
    sequenze finali che e' possibile ottenere applicando la procedura descritta fintanto che è applicabile.
    Nota che tutte queste sequenze sono composte da uno stesso numero positivo di interi distinti.

    Si consideri ad esempio l'albero delle sequenze  che si ottiene a partire dalla
    1 2 0 1 0 0 1  e che e' riportato nel file game_tree.pdf
    Le foglie dell'albero sono le sequenze finali.

    Nota: questo è un esempio di albero definito implicitamente dalle regole del gioco.
    - la radice è la sequenza iniziale
    - i nodo figli di un qualsiasi nodo si ottengono eliminando una coppia di numeri uguali
    - le foglie sono le sequenze in cui non è più applicare la regola di eliminazione delle coppie

    Definire una funzione ex1(s) ricorsiva (o che fa uso di funzioni o
    metodi ricorsive/i) che prende come parametro  una  stringa  che codifica  una
    sequenza di N interi con N dispari (in questa stringa i numeri della sequenza
    compaiono uno di seguito all'altro e separati da uno spazio) e  restituisce
    l'insieme delle codifiche (stringhe con i numeri separati da uno spazio)
    delle sequenze finali che e' possibile ottenere.
      Ad esempio con s='1 2 0 1 0 0 1' la funzione ex1 deve restituire  l'insieme
      {'2 0 1', '2 1 0', '1 2 0'}


NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: Almeno una delle funzioni/metodi che risolvono l'esercizio DEVE essere ricorsiva.
ATTENZIONE: per fare in modo che il macchinario di test riconosca automaticamente la presenza della ricorsione
    questa funzione ricorsiva DEVE essere una funzione esterna oppure il metodo di una classe
    (non può essere una funzione definita all'interno di un'altra funzione/metodo)

ATTENZIONE: Non potete usare altre librerie

ATTENZIONE: assicuratevi di salvare il programma con encoding utf8
(ad esempio usando come editor Notepad++ oppure Spyder)

'''

memo_tree = {}
memo_indexes = {}
memo_leaves = {}


class Node:
    def __init__(self, n):
        self.nums = n                                                               # Sequenza del nodo
        self.sons = []                                                              # Nodi figli
        self.isLeaf = True                                                          # Flag per foglie

    def __str__(self):
        return str(self.nums)                                                       # Rappresentazione come stringa

    def __repr__(self):
        return 'Node(nums={}, len(sons)={})'.format(self.nums, len(self.sons))      # Rappresentazione stampabile

    def checkLeaf(self):
        '''
        Controlla se il nodo è una foglia
        '''
        self.isLeaf = not len(self.sons)
        return self.isLeaf


def indexes(l, v):
    '''
    Ritorna l'indice di tutte le
    occorrenze di v in l
    '''
    memo_id = str(l) + v                                                            # id per la memoization
    
    if memo_id in memo_indexes:                                                     # Se la funzione è già stata chiamata
                                                                                    #  con gli stessi parametri
        return memo_indexes[memo_id]                                                # Cerca nella cache

    ind = []                                                                        # Lista di indici
    li = -1                                                                         # Ultimo indice controllato

    for _ in range(l.count(v)):                                                     # Per ogni occorrenza trovata
        i = l.index(v, li + 1)                                                      # Cerca l'indice successivo
        ind.append(i)                                                               # Aggiungilo alla lista
        li = i                                                                      # Aggiorna l'ultimo indice

    memo_indexes[memo_id] = ind                                                     # Aggiungi il risultato alla cache

    return ind                                                                      # Ritorna la lista


def mkTree(l):
    '''
    Crea un albero a partire
    dalla sequenza l
    '''
    memo_id = str(l)

    if memo_id in memo_tree:
        return memo_tree[memo_id]

    tree = Node(l)                                                                  # Inizializza la radice
    seqs = []

    for i in set(l):                                                                # Per ogni elemento della sequenza
        if l.count(i) > 1:                                                          # Se compare più volte
            occ = indexes(l, i)                                                     # Conta le occorrenze
            for j, x in enumerate(occ):                                             # Per ogni occorrenza
                for k, y in enumerate(occ[j + 1:]):                                 # Per ogni occorrenza successiva
                    l2 = l.copy()                                                   # Copia la sequenza
                    l2.pop(y)                                                       # E rimuovi i due doppioni selezionati
                    l2.pop(x)
                    if l2 not in seqs:                                              # Se il nodo non è gia stato calcolato
                        tree.sons.append(mkTree(l2))                                # Aggiungilo ai figli
                        tree.sons[-1].checkLeaf()
                        seqs.append(l2)

    tree.checkLeaf()

    memo_tree[memo_id] = tree

    return tree


def getLeaves(tree):
    '''
    Ritorna tutte le foglie
    dell'albero tree
    '''
    memo_id = tree

    if memo_id in memo_leaves:
        return memo_leaves[memo_id]
    
    if tree.isLeaf:                                                                 # Se la radice non ha figli
        return [tree]                                                               # Ritornala come unica foglia

    l = []                                                                          # Lista di foglie
    for i in tree.sons:                                                             # Per ogni figlio
        if i.isLeaf:                                                                # Se non ha figli
            l.append(i)                                                             # Aggiungilo alle foglie
        else:                                                                       # Altrimenti
            l += getLeaves(i)                                                       # Cerca foglie nel sotto-albero

    memo_leaves[memo_id] = l

    return l


def ex1(s):
    # inserite qui sotto il vostro codice
    leaves = getLeaves(mkTree(s.split()))                                           # Genera l'albero

    seqs = set()                                                                    # Insieme di sequenze
    for i in leaves:                                                                # Per ogni foglia
        seq = ''
        for j in i.nums:                                                            # Aggiungi ogni elemento alla stringa
            seq += j + ' '                                                          #  che la rappresenta
        if seq[:-1] not in seqs:                                                    # Se la stringa non è già nell'insieme
            seqs.add(seq[:-1])                                                      # Aggiungila

    return seqs


if __name__ == '__main__':
    ex1('1 2 1 3 1 4 1 5 1 6 1 7 1 8 1 9 10 9 10 9 10 1 7 1 8')
    pass
    # inserite qui i vostri test personali
