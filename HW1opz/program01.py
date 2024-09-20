# -*- coding: utf-8 -*-

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

def ex1(int_seq, subtotal):
    # Inserisci qui il tuo codice

    val = [int(i) for i in int_seq.split(',')]                  # Estrae i valori dalla stringa
    ris = 0                                                     # Contatore possibilità
    
    for i in range(len(val)):                                   # Itera sul range 0, <numero di valori>
        somma = val[i]                                          # Inizializza la somma come il valore i-esimo

        if somma == subtotal:                                   # In caso il valore iniziale sia pari al
            ris += 1                                            #  subtotale allora bisogna aggiungerlo ai
                                                                #  possibili valori

        for j in val[i+1:]:                                     # Itera sui valori successivi all'i-esimo

            somma += j                                          # Somma il valore alla semisomma
            
            if somma == subtotal:                               # Se la somma dei valori fin'ora analizzati è pari
                                                                #  subtotal
                ris += 1                                        # Aggiorna il contatore di possibili stringhe
            elif somma > subtotal:                              # Altrimenti se è maggiore
                break                                           # Passiamo al valore i-esimo successivo

    return ris                                                  # Ritorniamo il numero di sottostringhe valide


if __name__ == '__main__':
    # Inserisci qui i tuoi test personali
    print(ex1('3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2', 9))
