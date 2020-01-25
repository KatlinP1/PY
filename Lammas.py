# teksti kirj harj.1 
# smt= "Twinkle, twinkle, little star \n\t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n\t How I wonder what you are" 
# print (smt)

#hetkeaeg harj.3
#import datetime
#x= datetime.datetime.now ()
#print (x) 

# ringi pindala arvutamine (impordi math)
#import math
#r= input ("raadius? ")
#s= math.pi * (float(r) **2)
#print (s)

#ringi ümbermõõdu arvutamine 
#import math 
#r= input ("raadius? ")
#v= 2* math.pi *(float(r))
#print (v)

#nime kirjutamine
#first= "Vello"
#last = "Kitten"
#nimi = first+ " " +last
#print (nimi)

#SPLIT teeb tekstist listi (listi tegemine)
#numbr = "3, 5, 7, 23"
#kass = numbr.split (",")
#print (kass[2])
#print (kass)

#color_list = ["Red","Green","White" ,"Black"]
#print (color_list[0])
#print (color_list[3])

#summa 615 saamine harj.10
#n="5"
#nn=n+n
#nnn=n+n+n
#value = int(n) + int(nn) + int(nnn)
#print (value)

#või siis kirjutada funktsioonidena DEF on funktiooni 
#def  kitten (n):
    #n = str(n)
    #nn= n+n
    #nnn=n+n+n
    #value = int(n) + int(nn) + int(nnn)
    #print (value)
    #return value
#kitten("5")

#päevade vahe arvutamine
#from datetime import date
#date1= date(2014, 7, 2)
#date2= date(2014, 7, 11) 
#x= date2-date1
#print (x) 

# numbrite erinevuse leidmine
#def kitten (n):
    #x= abs(n-17)
    #if n > 17:
        #return x*2
    #return x

#print (kitten (5))
#print (kitten(20))

#millele arv lähemal asub
#def kitten (n):
    #x= abs(1000-n)
    #if x<= 100: 
        #print (1000)
        #return "1000"
    #x= abs (2000-n)
    #if x<= 100:
        #print (2000)
        #return "2000"
    #return "no"

#es = int(input ("kitten"))
#kitten (es)

#harj. 18 
#def kitten (a,b,c):
    #sum = a+b+c
    #if a==b and b==c:
        #return 3*sum 
    #return sum 

#y= kitten (3,3,3)
#print (y)

#harj. 19
#def kitten (x):
    #if x.find ("Is")==0:
        #return x 
    #return ("Is %s" % x)

#print (kitten ("Vello"))
#print (kitten ("Is Vello"))

#mitu korda sõna printida 
#def kitten (str,y): 
    #y= abs(y)
    #return y* str

#print (kitten ("kass", 5))

# paaris v paaritu arv 
#def kitten (y):
    #if abs(y) % 2 ==0: 
        #return "even" 
    #if abs(y) % 2==1:
        #return "odd"

#print (kitten (6))

#list = [4,34,56,10000,98,78,944,24,4,60,87,44]
#count =0

#for x in list:
    #if x==4:
        #count +=1 
#print (count)

#listist mingi nr.ini
#numbers = [    
    #386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    #399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    #815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    #958,743, 527
    #]

#for x in numbers: 
    #if x== 237:
        #break
    #if x % 2 == 0:
        #print (x)

#ül nr 29
#color_list_1 = set(["White", "Black", "Red"]) 
#color_list_2 = set(["Red", "Green"]) 

#c = color_list_1.difference (color_list_2)
#print (c)

#kolmnurga pindala arvutamine 
#h= input ("kõrgus?")
#a= input ("alus?")

#s= float(h) * float(a) /2
#print (s)

#ül 33
#def kitten (a,b,c): 
    #if a==b or b==c:
        #return 0
 
    #return a+b+c
#print (kitten (4,5,6)) 

#ül 34
#def kitten (a,b): 
    #sum = a+b
    #if sum in range (15, 20): 
        #return 20 
    #else: 
        #return sum    
    
#print (kitten (5,5))
#print (kitten (10,6))

#ül35
#def kitten (a,b):
    #if  a==b: 
        #return True
    #if a+b == 5: 
        #return True 
    #if abs (a-b) ==5:
        #return True 
    #return False 

#print (kitten (5,5))

# ül 36 
#def kitten (a,b):
    #if isinstance(a,int) and isinstance(b,int): 
        #return a+b
    #return False

#print (kitten (4,10))

#ül 37
#name = input("name")
#age = input ("age")
#address = input("address")

#print ("%s\n%s\n%s" % (name,age,address))

#ül38
#x= int (input ("x"))
#y= int(input ("y"))
#print ((x + y) * (x + y))

#ül39
#year= 7
#money =10000
#i= 3.5

#money2= money
#for x in range (0,year):
    #money2 = (i/100)*money2 + money2 
#print (money2)

#ül48
#x= "987.6543"
#print (float(x))
#print (int(float(x)))
#print (x)

#ül58
#n = int(input ("n"))
#sum = 0
#while (n>0): 
    #sum+=n 
    #n-=1
#print (sum)

#ül 59 
#cm = 1000
#m= cm /100.0 
#km = cm /10000.0 

#print ("pikkus meetrites =" , m)
#print ("pikkus kilomeetrites =" , km)

#cm = int (input ("cm"))
#jalg = cm * 30,48  
#toll = cm * 2,54

#print ("pikkus jalgades=", jalg)
#print ("pikkus tollides=", toll)

#ül 61
#jalg = int (input ("jalg"))
#toll= jalg *12
#jard= jalg * 0.33

#print ("jalg tollides", toll)
#print ("jalg jardides", jard)

#ül62
#1 min= 60 sek 
#1 tund= 3600 sek 
#1 päev=86400 sek 

#d= int(input ("day "))
#h= int (input("tund "))
#m= int (input("minut "))

#s= (d*86400) + (h*3600) + (m*60)
#print (s)

#import datetime
#x =  datetime.datetime.now ()
#y = x+ datetime.timedelta(0, s)
#print (y)

#ül 68
#arv=int (input("n"))
#arv=str(arv)
#sum= 0
#for x in arv:
    #x= int (x) 
    #sum+=x 
#print (sum)


