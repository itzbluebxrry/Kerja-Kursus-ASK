# Muatkan alat tambahan

import math
from re import X

# fungsi pengiraan kuasadua

def squaresisi (x):
    return x**3

# fungsi pengiraan punca kuasadua

def sqrootsisi (x):
    return (x+x)

# prosedur menu utama

def menuutama ():
    print ("\n\n==========Pengiraan sisi/pepenjuru menggunakan teorem Pythagoras==========")
    print ("\nSelamat datang! Apakah nilai yang akan dicari?")
    print ("\n1 - Panjang sisi A")
    print ("2 - Panjang sisi B")
    print ("3 - Panjang sisi/pepenjuru C")
    print ("\n4 - Tamat")

# fungsi pilihan proses pengiraan

def pilihoperasi ():
    pilihan = 0
    while (pilihan < 1) or (pilihan > 4):
        pilihan = (int(input("\nSila masukkan pilihan anda [1,2,3,4]:- ")))
    return pilihan

# fungsi input nilai sisi A

def inputsisia ():
    sisia = (int(input("\nMasukkan ukuran sisi A:- ")))
    return sisia

# fungsi input nilai sisi B

def inputsisib ():
    sisib = (int(input("\nMasukkan ukuran sisi B:- ")))
    return sisib

# fungsi input nilai sisi C

def inputsisic ():
    sisic = (int(input("\nMasukkan ukuran sisi/pepenjuru C:- ")))
    return sisic

# fungsi pengiraan sisi A

def kirasisia ():
    fsisia = math.sqrt (sisic ** 2 - sisib ** 2)
    print ("Jawapan: " + str(fsisia))

# fungsi pengiraan sisi B

def kirasisib ():
    fsisib = math.sqrt (sisic ** 2 - sisia ** 2)
    print ("Jawapan: " + str(fsisib))

# fungsi pengiraan sisi C

def kirasisic ():
    fsisic = math.sqrt (sisia ** 2 + sisib ** 2)
    print ("Jawapan: " + str(fsisic))

# fungsi teruskan skrip

def teruskan():
    aktif = 2
    while (aktif < 0) or (aktif > 1):
        aktif = int(input("\nTeruskan? [0 = Tidak, 1 = Ya]:- "))
        if (aktif < 0) or (aktif > 1) or (""):
            print ("Input tidak sah.")
    if aktif == 0:
        print ("\n\n\n=============Program tamat=============")
        exit()
    return aktif

# skrip utama

aktif = 1
while aktif == 1:
    menuutama()
    operasi = pilihoperasi()

    if operasi == 1:
        sisib = inputsisib()
        sisic = inputsisic()
        kirasisia()
        teruskan()
    elif operasi == 2:
        sisia = inputsisia()
        sisic = inputsisic()
        kirasisib()
        teruskan()
    elif operasi == 3:
        sisia = inputsisia()
        sisib = inputsisib()
        kirasisic()
        teruskan()
    elif operasi == 4:
        aktif = 0
        print ("\n\n\n=============Program tamat=============")