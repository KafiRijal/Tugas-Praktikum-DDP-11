import math

def tambah(bil1, bil2):
    hasil= bil1+bil2
    print("hasil tambah dari", bil1, "+", bil2,"=", hasil)
def kurang(bil1, bil2):
    hasil= bil1-bil2
    print("hasil kurang dari", bil1, "-", bil2,"=", hasil)
def pangkat(bil1, bil2):
    hasil= math.pow(bil1, bil2)
    print("hasil pangkat dari", bil1, "^", bil2,"=", hasil)
def kali(bil1, bil2):
    hasil= bil1*bil2
    print("hasil kali dari", bil1, "*", bil2,"=", hasil)
def bagi(bil1, bil2):
    hasil= bil1/bil2
    print("hasil bagi dari", bil1, "/", bil2,"=", hasil)
def log(bil1):
    hasil= math.log(bil1)
    print("hasil log dari", bil1, "=", hasil)
def akar(bil1):
    hasil= math.sqrt(bil1)
    print("hasil akar dari", bil1, "=", hasil)
def sin(bil1):
    hasil= math.sin(math.radians(bil1))
    print("hasil sin dari", bil1, "=", hasil)
def cos(bil1):
    hasil= math.cos(math.radians(bil1))
    print("hasil cos dari", bil1, "=", hasil)
def tan(bil1):
    hasil= math.tan(math.radians(bil1))
    print("hasil tan dari", bil1, "=", hasil)
