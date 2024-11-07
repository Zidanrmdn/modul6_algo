# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:00:23 2024

@author: ASUS
"""
def nilai_keseluruhan ():
    

    skor = 0 
    nilaimurid = list()
    ulang = 0
    nomor = 0
    
    while ulang == 0:
        nomor += 1
        x = str(input('masukkan nilai : ')).upper()
        
        if x == "":
            break
            
        else: 
            
            if x == 'A':
                skor = (4)
                print(('Nilai = {1} ').format(nomor,skor))
                
            elif x == 'A-': 
                skor = (3.75)
                print(('Nilai = {1} ').format(nomor,skor))
                
            elif x == 'B+':
                skor = (3.50)
                print(('Nilai = {1} ').format(nomor,skor))
                
            elif x == 'B':
                skor = (3)
                print(('Nilai = {1} ').format(nomor,skor))
                
            elif x == 'B-':
                skor = (2.75)
                print(('Nilai = {1} ').format(nomor,skor))
                
            elif x == 'C+':
                skor = (2.50)
                print(('Nilai = {1} ').format(nomor,skor))
                
            elif x == 'C':
                skor = (2.)
                print(('Nilai = {1} ').format(nomor,skor))
                
            elif x == 'C-':
                skor = (1.75)
                print(('Nilai = {1} ').format(nomor,skor))
                
            elif x == 'D':
                skor = (1.50)
                print(('Nilai = {1} ').format(nomor,skor))
                 
            elif x == 'E':
                skor = (1.25)
                print(('Nilai = {1} ').format(nomor,skor))
                
            else: 
                print('saya tidak mengerti...')
                skor = 0
            nilaimurid.append(skor)
            
    rata2 = sum(nilaimurid) / len(nilaimurid)
    print('rata rata nilai murid tersebut:', rata2)
nilai_keseluruhan ()    