# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:06:58 2022

@author: Audi Aulia
"""

def pemangkatan():
    print()
    print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    angka = input("Masukkan Angka : ")
    if angka == '':
        print("Terima Kasih telah menggunakan program ini. Program selesai")
        return 0
    pangkat = input("Masukkan Pangkatnya : ")
    hasil = int(angka)**int(pangkat)
    print("Hasilnya adalah : ", hasil)
    pemangkatan()

pemangkatan()
