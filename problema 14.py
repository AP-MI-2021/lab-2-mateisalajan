#Problema 14
def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def cmmdc(n: int, m: int):
    '''
    Calculeaza cmmdc a doua numere intregi prin scaderi repetate
    :param n: un numar intreg
    :param m: un numar intreg
    :return: cmmdc a doua numere intregi
    '''
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n

def cmmmc(n: int, m: int):
    '''
    Calculeaza cmmmc a doua numere intregi
    :param n: un numar intreg
    :param m: un numar intreg
    :return: cmmmc a doua numere intregi
    '''
    div = cmmdc(n, m)
    return n*m/div

def get_cmmmc(numbers: list[int]):
    '''
    Calculeaza cmmmc a numerelor dintr-o lista de nr. intregi
    :param numbers: lisat de numere intregi
    :return: cmmmc a numerelor din numbers
    '''
    c = numbers[0]
    d = numbers[1]
    i = 2
    multiplu = cmmmc(c, d)
    while i < len(numbers) :
        multiplu = cmmmc(multiplu, numbers[i])
        i += 1
    return multiplu


def test_get_cmmmc():
    v = [2, 10 , 12, 4]
    assert (get_cmmmc(v) == 60) is True
    v = [3, 17, 10, 8]
    assert (get_cmmmc(v) == 135) is False

if __name__ == "__main__":
    test_get_cmmmc()
    l = []
    while True:
        optiune = input("pentru tasta 1 citim lista, pentru tasta 2 afisam cmmmc, si pentru tasta 3 se termina executia: ")
        if optiune == "1":
            l = citireLista()
        if optiune == "2":
            print(get_cmmmc(l))
        if optiune == "3":
            break

