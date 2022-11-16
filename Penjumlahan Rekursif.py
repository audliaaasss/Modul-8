# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:08:58 2022

@author: Audi Aulia
"""

def penjumlahan (bil = 0, jml = 0, i = 1):
    if (jml <= 0):
        return 0
    else:
        bil = int(input("Masukkan bilangan ke-" + str(i) + " : "))
        if (jml == 1):
            return bil
        else:
            i+=1
            return bil + penjumlahan(bil, jml-1, i)
        
jumlah = int(input("Masukkan Jumlah : "))
total = penjumlahan(jml = jumlah)
print ("Hasil dari penjumlahan adalah : " + str(total))