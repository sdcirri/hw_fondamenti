# -*- coding: utf-8 -*-
'''
Un pixel artist di fama mondiale di nome Fred Zuppa ha recentemente
prodotto diversi capolavori sottoforma di immagini quadrate raster
codificate su pixels in scala di grigi. Le immagini che ha disegnato
possono prendere valori da 0 a 255 compresi. Sfortunatamente le famose
opere sono andate perdute in quanto il suo disco rigido (ahilui!) ha
smesso di funzionare e ovviamente il buon Fred e' disperato. I
programmi per recuperarle dal filesystem non funzionano purtroppo e
cosi' Fred si affida al suo amico informatico di fiducia, il quale gli
dice:

   "Fratello, in verita' ti dico, se ti ricordi la dimensione delle
   immagini e i valori dei pixel di cui erano formate e delle
   proprieta' particolari delle tue opere, allora possiamo provare a
   scrivere un generatore ricorsivo che le produca tutte in base ai
   tuoi input, cosi' facendo possiamo provare a recuperarle!"

Il mattino seguente Fred riesce a dare le informazioni necessarie
sottoforma di:
   1. `D` parametro intero che descrive la dimensione dell'immagine
       quadrata.
   2. `colors` una lista di interi che descrive i colori delle
      immagini di Fred.  I colori di Fred sono compresi fra 0, 255.
      colors puo' essere quindi [128, 0, 255] mentre NON puo' essere
      [-100, 999]
   3. Un testo `img_properties` che descrive le proprieta' delle sue
      immagini: Il testo puo' descrivere nessuna proprita' (stringa
      vuota) oppure puo' descrivere una proprieta' che riguarda i
      pattern che le immagini devono contenere.

       Ad esempio:

       Se `img_properties` e' vuota allora le immagini non devono soddisfare
       nessuna proprieta'. Viceversa se `img_properties` e' uguale a
       'pattern_{type}_' allora signifca che le immagini devono
       mostrare il pattern di tipo `type` specificato nella stringa.
       Il pattern puo' essere di un solo tipo.

       I tipi di pattern possibili sono i quattro seguenti:
          a) 'pattern_diff_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine
          di dimensione uguale a 2x2, questa sottoimmagine deve avere i
          pixel di colore tutti diversi.

                 valid        not valid
            |  96 | 255 |   |   0 | 255 |
            | 128 |   0 |   | 255 |  96 |


          b) 'pattern_cross_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine
          di dimensione uguale a 2x2, questa sottoimmagine deve
          avere i pixel sulla diagonale uguali fra loro e i pixel
          sulla antidiagonale uguale fra loro ma pixel delle due
          diagonali devono essere diverse.

               valid          not valid     not valid
            |  96 | 255 |   |  0 | 255 |   | 61 | 61 |
            | 255 |  96 |   | 96 |   0 |   | 61 | 61 |

          c) 'pattern_hrect_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine di
          dimensione 2x2, questa sottoimmagine deve avere i pixel
          sulle righe tutti uguali ma righe adiacenti di colore
          diverso.

                 valid       not valid        not valid
            |   0 |   0 |   | 255 | 255 |    | 43 | 43 |
            | 128 | 128 |   | 0   | 255 |    | 43 | 43 |

          d) 'pattern_vrect_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine di
          dimensione 2x2, questa sottoimmagine deve avere i pixel
          sulle colonne tutti uguali ma colonne adiacenti di colore
          diverso.

                valid         not  valid    not valid
             | 0 | 255 |     | 0  | 0  |    | 22 | 22 |
             | 0 | 255 |     | 0  | 255|    | 22 | 22 |

Implementare la funzione ricorsiva o che usa metodi ricorsivi:
  
      images = ex(colors, D, img_properties)

che prende in ingresso la lista di colori `colors`, la dimensione
delle immagini `D` e una stringa `img_properties` che ne descrive le
proprieta' e generi ricorsivamente tutte le immagini seguendo le
proprieta' suddette.  La funzione deve restituire l'elenco di tutte le
immagini come una lista di immagini.  Ciascuna immagine e' una tupla di
tuple dove ogni intensita' di grigio e' un intero.
L'ordine in cui si generano le immagini non conta.

     Esempio: immagine 2x2 di zeri (tutto nero) e':
        img = ( (0, 0), (0, 0), )


Il timeout per ciascun test è di 1 secondo.

***
E' fortemente consigliato di modellare il problema come un albero di
gioco, cercando di propagare le solo le "mosse" necessarie nella
ricorsione e quindi nella costruzione della soluzione in maniera
efficiente; oppure, in maniera alternativa, cercate di "potare" l'albero di
gioco il prima possibile.
***

Potete visualizzare tutte le immagini da generare invocando

     python test_01.py data/images_data_15.json

questo salva su disco tutte le immagini attese del test 15 e crea
un file HTML di nome `images_data_15.html` nella directory radice
del HW con cui e' possibile vedere le immagini aprendo il file html
con browser web.
'''

memo_validate = {}                                                                      # Cache per validateImg()
memo_tree = {}                                                                          # Cache per mkTree*()


def pattern_cross(img):
    return img[0][0] == img[1][1] != img[0][1] == img[1][0]


def pattern_hrect(img):
    return img[0][0] == img[0][1] != img[1][0] == img[1][1]


def pattern_vrect(img):
    return img[0][0] == img[1][0] != img[0][1] == img[1][1]


def validateImg(img, prop, size):
    '''
    Valida l'immagine img secondo
    la proprietà prop
    '''
    memo_id = str(img) + prop
    
    if memo_id in memo_validate:
        return memo_validate[memo_id]

    valid = True

    for i in range(size - 1):
        for j in range(size - 1):
            subimg = [                                                                  # Prende una sottoimmagine
                [img[j][i], img[j][i + 1]],                                             #  arbitraria
                [img[j + 1][i], img[j + 1][i + 1]]
            ]
            if prop == 'pattern_cross_':
                valid &= pattern_cross(subimg)
            elif prop == 'pattern_hrect_':
                valid &= pattern_hrect(subimg)
            elif prop == 'pattern_vrect_':
                valid &= pattern_vrect(subimg)
            # Controlli su pattern_diff_ non necessari
            #  per come è stata implementata la funzione

    memo_validate[memo_id] = valid

    return valid


class NodeImg:
    def __init__(self, s, p, c, content=[]):
        self.size = s                                                                   # Dimensione dell'immagine
        self.properties = p                                                             # Proprietà dell'immagine
        self.colors = c                                                                 # Colori dell'immagine
        self.content = content                                                          # Immagine

    def __str__(self):
        return '{} @{}'.format(self.size, id(self))                                     # Rappresentazione come stringa

    def __repr__(self):
        return 'Node(size={}**2, len(lchild)={})'.format(self.size, len(self.lchild))   # Rappresentazione stampabile

    def fill(self, color):
        '''
        Riempie l'immagine del
        colore dato (se accettabile)
        '''
        if color in self.colors:
            self.content = [
                [color for __ in range(self.size)]
                for _ in range(self.size)
            ]

    def validate(self):
        '''
        Valida l'immagine
        '''
        return validateImg(self.content, self.properties, self.size)


def getMirrorNode(node, leftright=True):
    '''
    Crea un nuovo nodo con le stesse
    caratteristiche di node e contenuto
    ribaltato rispetto all'orizzontale
    (leftright=True) o alla verticale
    (leftright=False)
    '''
    mirror = NodeImg(node.size, node.properties, node.colors)

    if leftright:
        mirror.content = [list(reversed(i)) for i in node.content]
    else:
        mirror.content = list(reversed(node.content))
    return mirror


def imgToTuple(img):
    '''
    Converte le immagini nel
    formato richiesto
    '''
    return tuple(map(tuple, img))


def copyImg(img):
    '''
    Ritorna una copia dell'immagine
    '''
    return [i.copy() for i in img]


def mkTree_cross(colors, D, valid=[], lnodes=[], root=None, step=0):
    '''
    Generatore di albero di gioco
    ottimizzato per pattern_cross_
    '''
    memo_id = 'cross' + str(colors) + str(D)                                            # ID per memoization

    if memo_id in memo_tree:                                                            # Cerca in cache prima di
        return memo_tree[memo_id]                                                       #  eseguire la funzione

    if root is None:                                                                    # Crea la root se non definita
        root = NodeImg(D, 'pattern_cross_', colors)

    if root.content not in lnodes:                                                      # Aggiunge la root ai nodi noti
        lnodes.append(root.content)

    for i, x in enumerate(colors):
        for y in colors[:i] + colors[i + 1:]:                                           # Per ogni coppia di colori
            if step == 0:
                root.fill(x)                                                            # Riempie l'immagine con il primo

            child = NodeImg(D, 'pattern_cross_', colors, content=copyImg(root.content)) # Genera un figlio

            for j in range(step % 2, D, 2):                                             # Disegna un motivo a scacchiera sulla riga
                child.content[step][j] = y                                              #  corrente (shiftato di 1 se è dispari)

            if child.content not in lnodes:                                             # Se il figlio non è noto
                lnodes.append(child.content)                                            # Aggiungilo ai nodi noti
                
                if child.validate():                                                    # Se è un'immagine valida
                    mirror = getMirrorNode(child)                                       # Ottieni il nodo speculare (valido comunque)
                    lnodes.append(mirror.content)                                       # E aggiungilo ai nodi noti
                    valid += [imgToTuple(child.content), imgToTuple(mirror.content)]    # Aggiungi entrambi ai pattern validi
                    step = 0                                                            # Resetta la riga corrente e continua con
                                                                                        #  la coppia di colori successivi
                else:                                                                   # Se non è valido
                    mkTree_cross([x, y], D, valid, lnodes, child, step+1)               # Crea un sottoalbero con la sola coppia
                                                                                        #  di colori e passa alla riga successiva

    memo_tree[memo_id] = root, valid                                                    # Memorizza il risultato in cache

    return root, valid


def mkTree_vrect(colors, D, valid=[], lnodes=[], root=None):
    '''
    Generatore di albero di gioco
    ottimizzato per pattern_vrect_
    '''
    if D == 0:
        return None, []

    memo_id = 'vrect' + str(colors) + str(D)
    
    if memo_id in memo_tree:
        return memo_tree[memo_id]

    if root is None:                                                                    # Crea la root se non definita
        root = NodeImg(D, 'pattern_vrect_', colors)
        root.fill(colors[0])                                                            # E la riempie con un colore

    bar = root.content[0]                                                               # Prende la prima riga della root

    if root.content not in lnodes:
        lnodes.append(root.content)

    for i in range(D):                                                                  # Per ogni pixel
        for j in colors:                                                                # Per ogni colore
            newbar = bar.copy()                                                         # Riga per generare l'immagine successiva
            newbar[i] = j                                                               # Riempie il pixel corrente con il colore corrente
            ccontent = [newbar] * D                                                     # 'Moltiplica' la riga per ottenere un'immagine
            child = NodeImg(D, 'pattern_vrect_', colors, content=ccontent)

            if child.content not in lnodes:
                lnodes.append(child.content)

                if child.validate():
                    mirror = getMirrorNode(child)
                    lnodes.append(mirror.content)
                    valid += [imgToTuple(child.content), imgToTuple(mirror.content)]

                mkTree_vrect(colors, D, valid, lnodes, child)

    memo_tree[memo_id] = root, valid

    return root, valid


def mkTree_hrect(colors, D, valid=[], lnodes=[], root=None):
    '''
    Generatore di albero di gioco
    ottimizzato per pattern_hrect_
    '''
    memo_id = 'hrect' + str(colors) + str(D)
    
    if memo_id in memo_tree:
        return memo_tree[memo_id]

    if root is None:
        root = NodeImg(D, 'pattern_hrect_', colors)
        root.fill(colors[0])

    line = [i[0] for i in root.content]                                                 # Prende la prima colonna della root per generare
                                                                                        #  permutazioni con lo stesso procedimento di pattern_vrect_

    if root.content not in lnodes:
        lnodes.append(root.content)

    for i in range(D):
        for j in colors:
            newline = line.copy()
            newline[i] = j
            ccontent = [[k] * D for k in newline]
            child = NodeImg(D, 'pattern_hrect_', colors, content=ccontent)

            if child.content not in lnodes:
                lnodes.append(child.content)

                if child.validate():
                    mirror = getMirrorNode(child, leftright=False)
                    lnodes.append(mirror.content)
                    valid += [imgToTuple(child.content), imgToTuple(mirror.content)]
    
                mkTree_hrect(colors, D, valid, lnodes, child)

    memo_tree[memo_id] = root, valid

    return root, valid


def surround(mat, x, y, d):
    '''
    Ritorna l'intorno dell'elemento m[y][x]
    '''
    l = x - 1 if x >= 1 else x
    u = y - 1 if y >= 1 else y
    r = x + 1 if x < d - 1 else x
    d = y + 1 if y < d - 1 else y

    return mat[u][l:r+1] + [mat[y][l], mat[y][r]] + mat[d][l:r+1]


def mkTree_diff(colors, D, valid=[], step=[0, 0], root=None):
    '''
    Generatore di albero di gioco
    ottimizzato per pattern_diff_
    '''
    if D == 0:
        return None, []

    def updateStep(step, d):
        '''
        Funzione per l'aggiornamento
        dello step (coordinate del pixel
        attualmente analizzato)
        '''
        newstep = step.copy()

        newstep[0] += 1
        if newstep[0] >= d:
            newstep[0] = 0
            newstep[1] += 1

        if newstep[1] >= d:
            newstep = [0, 0]

        return newstep

    x, y = step                                                                         # Coordinate del pixel esaminato
    for i in colors:                                                                    # Per ogni colore
        if root is None:                                                                # Se la root è nulla
            rcontent = [                                                                # Parti da un'immagine vuota
                [None for _ in range(D)]
                for __ in range(D)
            ]
        else:
            rcontent = root.content                                                     # Altrimenti parti dalla root

        if i not in surround(rcontent, x, y, D):                                        # Se il colore non è presente attorno al pixel
            ccontent = copyImg(rcontent)                                                # Copia la root nel figlio
            ccontent[y][x] = i                                                          # Puoi impostarlo
            child = NodeImg(D, 'pattern_diff_', colors, content=ccontent)

            if ccontent[D - 1][D - 1] is None:                                          # Se l'immagine è incompleta
                mkTree_diff(colors, D, valid, updateStep(step, D), child)               # Crea un sottoalbero con root il figlio e parti
                                                                                        #  dal pixel successivo
            else:
                # Per come sono costruite le immagini, non è necessario
                #  alcun tipo di controllo sulla validità
                valid.append(imgToTuple(ccontent))

    return root, valid


def mkTree(colors, D, lnodes=[], root=None):
    '''
    Generatore di albero di gioco generico
    '''
    if D == 0:
        return None, []

    memo_id = 'other' + str(colors) + str(D)
    
    if memo_id in memo_tree:
        return memo_tree[memo_id]

    if root is None:
        root = NodeImg(D, '', colors)
        root.fill(colors[0])

    rcontent = imgToTuple(root.content)
    if rcontent not in lnodes:
        lnodes.append(rcontent)

    for i in range(D):
        for j in range(D):
            for k, x in enumerate(colors):
                ccontent = copyImg(root.content)
                ccontent[j][i] = x
                child = NodeImg(D, '', colors, content=ccontent)
                ccontent = imgToTuple(child.content)
                if ccontent not in lnodes:
                    lnodes.append(ccontent)
                    mkTree(colors, D, lnodes, child)

    memo_tree[memo_id] = root, lnodes

    return root, lnodes


def ex(colors, D, img_properties):    
    if img_properties == 'pattern_vrect_':                                              # Sceglie il procedimento più appropriato
        _, valid = mkTree_vrect(colors, D)                                              #  per la ricerca in base alle proprietà
    elif img_properties == 'pattern_hrect_':
        _, valid = mkTree_hrect(colors, D)
    elif img_properties == 'pattern_cross_':
        _, valid = mkTree_cross(colors, D)
    elif img_properties == 'pattern_diff_':
        _, valid = mkTree_diff(colors, D)
    else:
        _, valid = mkTree(colors, D)

    return valid


if __name__ == '__main__':
    pass
