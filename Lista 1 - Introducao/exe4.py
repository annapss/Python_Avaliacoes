# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:44:02 2021


Grupo: Anna Paula Siqueira, Maria Laura Soares, Luanda Rodrigues e Ariane Arantes -2BINFO

Questão 4
Faça um programa que recebe um número inteiro no intervalo de 1 até 3000 e o escreva o seu 
correspondente em algarismos romanos.

"""



#algarismos romanos
romU = 'I'
romD = 'X'
romC = 'C'
romM = 'M'



num = input('Diga um número entre 1 e 3000: ' )
aux = len(num)

valor = int(num) 

unidader = -1
dezena = -1
centena = -1
milhar = -1



if valor <= 1 or valor >=3000:  #parâmetro para a validação do input 
    print('invalid')
else:
         if  aux >= 1 :
             unidader = (valor//1)%10
             if aux >= 2:
                 dezena = (valor//10)%10
                 if aux >= 3:
                     centena = (valor//100)%10
                     if aux >= 4:
                         milhar = (valor//1000)%10 
                             
            
                
         if milhar == 1:
           print(end= f'{romM}')
         else:
           
           if milhar == 2:
               print(end= f'{2*romM}')
           elif milhar == 3:
               print(end= f'{3*romM}')
            
         
         if centena == 1:
            print(end= f'{romC}')
         else: 
                if centena == 2:
                   print(end= f'{romC + romC}')
                elif centena == 3:
                   print(end= f'{3*romC}')
                elif centena == 4:
                   print(end= f'{romC}D')
                elif centena == 5:
                   print(end= 'D')
                elif centena == 6:
                   print(end= f'D{romC}')
                elif centena == 7:
                   print(end= f'D{2*romC}')
                elif centena == 8:
                   print(end= f'D{3*romC}')
                elif centena == 9:
                   print(end= f'{romC+romM}') 
         
            
         if dezena == 1:
             print(end= f'{romD}')  
         else:
                if dezena == 2:
                       print(end= f'{romD + romD}')
                elif dezena == 3:
                       print(end= f'{3*romD}')   
                elif dezena == 4:
                       print(end= f'{romD}L')  
                elif dezena == 5:
                       print(end= 'L')  
                elif dezena == 6:
                       print(end= f'L{romD}')  
                elif dezena == 7:
                       print(end= f'L{2*romD}')  
                elif dezena == 8:
                       print(end= f'L{3*romD}')  
                elif dezena == 9:
                       print(end= f'{romD + romC}')   
         
            
         
         if unidader == 1:
           print(romU)
         else: 
            if unidader == 2:
                print(end= f'{2*romU}')
            elif unidader == 3:
                print(end= f'{3*romU}')
            elif unidader == 4:
                print(end= f'{romU}V')
            elif unidader == 5:
                print(end= 'V')     
            elif unidader == 6:
                 print(end= f'V{romU}')
            elif unidader == 7:
                 print (end= f'V{romU + romU}')
            elif unidader == 8:
                  print(end= f'v {romU + romU + romU}')
            elif unidader == 9:
                 print(end= f'I{romD}')
     
         
            
         
            
         
            
         
            
         
            
         
            
         
            
         
            
         
            
         
            
         
            
         
            
         
            
         
         
      
        
           
         
        
           
        
       
       
        
   
        
   
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        