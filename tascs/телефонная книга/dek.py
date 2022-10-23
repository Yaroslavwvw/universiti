import random
from random import randint as Gang # из библиотеки  random импортирую randint и даю ему название Gang



def deg_to_rad(deg):
    '''

    :param deg: Градусы в десятичном представлении
    :return: Радианы
    '''
    rad = (deg * 3.141592653589793238462643383279502884197169399375105820974944) / 180
    return rad

def rad_to_deg(rad):
    '''

    :param rad: Градусы в радианах
    :return: Градусы в десятичном представлении
    '''
    deg = (rad * 180) / 3.14

    return deg

def deg_to_gms(a):
    '''

    :param a: Градусы в десятичном представлении
    :return: Градусы минуты секунды
    '''
    gr = int(a)
    min_n_sek = a - gr
    min = int(min_n_sek * 60)
    sek = ((min_n_sek * 60) - min) * 60
    print(f"{gr}°, {min}', {sek}″")

def gms_to_deg(gr, min, sek):
    '''

    :param gr: градусы
    :param min: минуты
    :param sek: секунды
    :return: градусы в десятичном представлении
    '''
    deg = sek / 3600 + min / 60 + gr
    print(deg)

def main():
    print(__name__)
    gms_to_deg(36, 58, 12)
    deg_to_gms(36.97)
    print(deg_to_rad(36))
    print(rad_to_deg(36))
if __name__ == "__main__":
    main()