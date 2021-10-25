#problema 13
def get_temp(temp: float, from_scale: str, to: str):
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

if __name__ == "__main__":
    test_get_temp()
    while True:
        from_scale = input("dati valoarea scarii in care va fi data temperatura,K Kelvin,C Celsius,F Farenhide")
        to_scale = input("dati valoarea scarii in care va fi tarnsformata temperatura,K Kelvin,C Celsius,F Farenhide")
        temp = int(input("dati temperatura:"))
        returned = get_temp(temp, from_scale, to_scale)
        print ("temperatura calculata este: " + str(returned))
        optiune: str == input("daca doriti sa iesiti apasati x,altfel orice alta tasta")
        if optiune == "x":
            break


