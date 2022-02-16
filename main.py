#problema 13
def get_temp(temp: float, from_scale: str, to: str):
    '''
    Transformă o temperatură dată într-o scară dată într-o altă scară dată
    :param temp: temeperatura data intr-o anumita scara
    :param from_scale: scara din care trebuie transformat
    :param to: scara in care trebuie transformat
    :return: temeperatura transformata in scara ceruta
    '''
    if from_scale == 'C' :
        if to == 'F' :
            temp = temp * 1.8 + 32
        if to == 'K' :
            temp = temp + 273.15
    if from_scale == 'F' :
        if to == 'C' :
            temp = (temp - 32) * 5 / 9
        if to == 'K' :
            temp = (temp - 32) / 1.8 + 273.15
    if from_scale == 'K' :
        if to == 'C' :
            temp = temp - 273.15
        if to == 'F' :
            temp = (temp - 273.15) * 1.8 + 32
    temp = float("{:.2f}".format(temp))
    return temp

def test_get_temp() :
    assert (get_temp(27, 'C', 'K') == 174.9) is False
    assert (get_temp(327.15, 'K', 'C') == 54) is True
    assert (get_temp(85, 'F', 'C') == 29.44) is True

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

#Problema 5
def is_palindrome(n):
    '''
    verifica daca un numar este palindrom
    :param n: un numar intreg
    :return: 1 daca numarul n este palindrom, sau o in caz contrar
    '''
    copie = n
    inv = 0
    while copie != 0:
        cif = copie % 10
        inv = inv * 10 + cif
        copie = copie // 10
    if n == inv:
        return 1
    return 0

def test_is_palindrome():
    assert is_palindrome(121) == 1
    assert is_palindrome(1456) == 0

if __name__ == "__main__":
    test_get_temp()
    test_get_cmmmc()
    test_is_palindrome()
    l = []
    while True:
        optiune = input("Pentru tasta 1 continuati cu problema 13\n"
                        "Pentru tasta 2 continuati cu problema 14\n"
                        "Pentru tasta 3 continuati cu problema 5\n"
                        "Pentru tasta x programul se va incheia:")
        if optiune == "1":
            from_scale = input("dati valoarea scarii in care va fi data temperatura,K Kelvin,C Celsius,F Farenhide")
            to_scale = input("dati valoarea scarii in care va fi tarnsformata temperatura,K Kelvin,C Celsius,F Farenhide")
            temp = float(input("dati temperatura:"))
            returned = get_temp(temp, from_scale, to_scale)
            print("temperatura calculata este: " + str(returned))
        if optiune == "2":
            l = citireLista()
            print(get_cmmmc(l))
        if optiune == "3":
            n = int(input("Dati o valoare pentru n: "))
            print(is_palindrome(n))
        if optiune == "x":
            break


