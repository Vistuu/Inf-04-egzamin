def plec(NumerPesel):
    if (int(NumerPesel[9]) % 2 == 0):
        return 'K'
    else:
        return'M'
    """
    nazwa funkcji:   
    **********************************************
    plec
    opis funkcji:    
    Funkcja określa płeć osoby na podstawie numeru PESEL. Jeśli dziesiąta cyfra numeru PESEL jest parzysta,
    funkcja zwraca 'K' (kobieta), w przeciwnym razie zwraca 'M' (mężczyzna).
    parametry:       
    NumerPesel - Numer PESEL w postaci ciągu znaków (string) 
    zwracany typ i opis: 
    string - 'K' lub 'M', w zależności od płci
    autor:                
    <numer zdającego>
    ***********************************************
    """

def Sprawdzanie(NumerPesel):
    mnozniki = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    S = 0
    for i in range(len(NumerPesel) - 1):
        S = S + (int(NumerPesel[i]) * mnozniki[i])
    M = S % 10
    R = 0
    if (M != 0):
        R = 10 - M
    return R == int(NumerPesel[10])

    """
    nazwa funkcji:   
    **********************************************
    Sprawdzanie
    opis funkcji:    
    Funkcja sprawdza poprawność numeru PESEL na podstawie sumy kontrolnej. Oblicza sumę kontrolną, porównuje ją
    z ostatnią cyfrą numeru PESEL i zwraca True, jeśli suma kontrolna jest zgodna, w przeciwnym razie zwraca False.
    parametry:       
    NumerPesel - Numer PESEL w postaci ciągu znaków (string)
    zwracany typ i opis: 
    bool - True, jeśli suma kontrolna jest zgodna, False w przeciwnym razie
    autor:                
    <numer zdającego>
    ***********************************************
    """
 
NumerPesel = "55030101193"
NumerPesel = str(input("podaj numer Pesel: "))
if(plec(NumerPesel) == "K"):
    print("Kobieta")
else:
    print("Mężczyzna")
if(Sprawdzanie(NumerPesel)):
    print("Zgodność sumy kontrolnej")
else:
    print("Niezgodność sumy kontrolnej")
