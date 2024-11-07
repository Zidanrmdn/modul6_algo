# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:12:41 2024

@author: ASUS
"""

hitung = 0
jawab = "ya"


while(jawab == "ya"):
    bulan = int(input("masukan bulan nya (1-12) : "))
    tahun = int(input("masukan tahun nya (e.g., 2024) : "))
    jawab = str(input("confirm? : "))

    
       
    def hitung_bulan():
    
      if(bulan == 1  or bulan == 3 or bulan == 5 
           or bulan == 7 or bulan == 8 
           or bulan == 10 or bulan == 12):
    	     print("Hari = 31")

          
      elif(bulan >= 13 or bulan <= 0):
          print("INVALID data")          
      
           
      elif (bulan == 2):
      
        if(tahun % 4 == 0 and bulan == 2):
          print("Hari = 29")
          return
        
        else :
            print("Hari = 28")
            
      else:
          print("Hari = 30")
        
          
    hitung_bulan()
    
    