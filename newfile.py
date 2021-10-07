#my frist day is 27/5/2021 time 10 pm
#(1)
#prinr///
#print('hello world')

#(2)
#(1)singlu line comments///
"""singlu lina comments"""

#(2)mult line comment///
"""mult
line
comments"""
#(2)(3)
#second line condinue///

#print("dhanush",end="")
#print(" super")
#(2)(4)
#escape suquences///

#/n
#/t
# name n ku //use"""

#(3)(i)

#varelbl crent ///
#var1 = 33
#var2 = 45
#print(var1-var2)

#(3)(2)

#data types///
"""
string    =(dhanush super)this is"string"
integers=int this is 14ena number
float      =float this is 55.66 ena number
"""
#(4)

#var1="hello world"
#var2=34
#var3=55.66
#print(type(var1))
#print(var2+var3)
#var1="2"
#var2="2"
#var3=55.66
#print(type(var1))
#print(var2+var1)

"""str to int enme
cancnt is var1is"2"+var2 is "2" =22 yes ok"""
#game user///

"""print("Enter you name")
var1=input( )
print("your name is:",var1)"""

#name="dhanush""
#print(100*name)

#(5)

#typecasting///
"""var1="2"
var2="2"
var3=55.66
int()
str()
float()
print(100*str(int(var1)+int(var2)))"""

#(6)

#input ()functions
#print("enter your name")
#name=input()
#print("your name is:",name)
#var1=input("enter your number")
#print("you enter number is:",var1)
#print("you enter number is:",int(var1)+6)

#(7)
#Excercise(1)
#calculator///
#print("enter your first number")
#var1=input()
#print("enter your 2nd number")
#var2=input ()
#print("tha sum of number is:",int(var1)+int(var2))

#(8)

#string slicing (part-1)///

#mystr="my name is dhanush"
#print(mystr[ :14])
#[Start: stop+1]
#print (mystr[:19:2])
#[start:stop:step]
#print(mystr[-15:-10])

#(9)

#string slicing (part-2)

#var="I am a good boy"
#print(var.index("g"))
#functions
#print(var.replace("good","bad"))
#functions
#print (var.find("g"))
#functions
#search Google python string functions

#buy web site development
'''product="redmi note 8 | rs14000 | new"
name=product[:product.index("|")]
print(name)'''

#(10)

#string slicing(part-3)//

"""price=product[product.index("|")+2:product.rindex("|")]
print(price)
condition=product[product.rindex("|")+2:]
print (condition)
print("Tha name of the product is",name)
print("Tha price of the product is", price)
print("Tha condition of the product is", condition)
slicing is oovare"""

#(11)
#list///
#web=["gomathi","Mani","Dhanush","Aathish"]
#print(web[0])
#numbers=[6,5,8,4]
#numbers.sort( )
#numbers.reverse()
#print (numbers)
#numbers.append(6)
#print(numbers)
#numbers.insert(1,44)
#print(numbers)
#numbers.remove(6)
#print(numbers)
#numbers.pop()
#print(numbers)
#numbers[0]=5
#print (numbers)

#mutable//
#numbers=[6,5,8,4]
#print(numbers)
#immutable//
#numbertq=(5,6,3,9)
#print (numbertq)//
#a=1
#b=2
#a,b=b,a
#print (a,b)
#search Google python list functions

#(12)

#Dictionaries///

#d1={}
#print(type (d1))
#d1={"gomathi":"fish","Mani":"very good","Dhanush":"bad"}
#print(d1["Dhanush"])
#d1={"gomathi":"fish","Mani":"very good","dhanush":{"m":"good morning","n":"good night"}}
#print(d1["dhanush"])
#d1["Aathish"]="fish"
#print(d1)
#add functions//
#del d1["Aathish"]
#print(d1)
#delete functions//
#d2=d1
#del d2["Mani"]
#print(d2)

#d2=d1.copy( )
#del d2["Mani"]
#print(d2)
#print(d1.get("Mani"))
#d1.update({"Aathish":"fish"})
#print(d1)
#add functions//
#print(d1.keys())
#keys functions//
#print(d1.items())
#search Google Dictionaries functions in python

#Exercise(2)//
#d1={"mani":654663673,"dhanush":756545333}
#key=input("enter your name is see number")
#print("Tha number of",key,"is",d1[key])

#(13)

#if else and elif///
#var1=56
#var2=int(input ())

#if var2>var1:
    #print("greater")
#elif var2==var1:
	#print("equal")
#else:    
    #print("smaller")
"""print("Enter your age")
age=int(input ())
if age >18:
 	  print ("you can drive")
elif age==18:
	   print("we will think")
elif age<18:
	  print("you can not drive")"""
	  
#(14)

#Loops///
#while loops//

"""i=1
while i<=5:
	print ("dhanush")
	i=i+1"""
	
#(15)

#Nested loops//

#i=1
#k=1
#while i<=5:
    #print("dhanush",end="")
    #k=1
	#while k<=5:
		  #print ("super",end="")
		  #k=k+5
	#i=i+5
	#print ()
	
#(16)
#for loops///
#list1=["Dhanush",23,43,26]
#for i in list1:
	#print(i)
#list1=["Dhanush",23,43,26]
#for i in list1:
	#i=anya name
	#print(i,"add anya name")
#Nest matadd/
#x="Dhanush"
#for I in x:
	#print (I)
#///////
#for I in "str and list and dictionaries any one":
	#print (I)
#//////
#for I in range(1,11):
	#print (I)
#range multiple print
#for I in range(1,11):
	#print ("dhanush")
#/////
#for I in range(1,101):
#	if l%5==0:
#		print(I)

#(17)
#break and continue///
#part(1)//
#break//
#i=0
#while True:
#	i=i+1
#	print (i)
#	if i>5:
#		print ("greater than 5")
#		continue
#	if i>100:
#		print ("this number is greater than hundred")
#		break

#continue//
#while True:
#   i = int(input ("enter your number :"))
#   if i > 100:
#      print ("congratulation your have enter number is more than hundred")
#      break
#   else:
#      print ("try again")  
#      continue

#part(2)//
#break
#i=0
#while True:
	#i=i+1
	#print (i)
	#if i==100:
		#break
		
#continue
#for i in range(1,11):
#	if i==6:
#		continue
#	print(i)

#while True:
#	k=int(input ("enter a number greater than 100:"))
#	if k<100:
#		print ("try again")
#	elif k>100:
#		print ("congratulation you won")
#		break

#(18)
#short hand if else
#a=int(input ("Enter first number"))
#b=int(input ("Enter second number"))
#if a>b:
#	print ("thambi a b avida greater as irukk u")
#else:
#	print ("thambi b a avida greater as irukk u")

#(19)
#built in functions and user defined functions//

#built functions//

#a=1
#b=2
#c=sum((a,b))
#print (c)

#user defined functions//
#def functions ()
#example//
#type ()
#str()
#def functions ():
#	print ("good morning sir")
#functions ( )
#par Mater////

#def functions (a,b):
#	print (a+b)
#	return a+b
#print(functions (5,9))//
#v=functions (5,9)
#print (v)#not sote
#print (v)

#example//

#def functions1(a,b):
#	"""This is functions which takes average"""
#docstrings
#	average=a+b/2
#	print (average)
#	return (average)
#functions1(7,6)
#print (functions1.__doc__)
#practice search hacking rank

#exercise(3)//
#q and a
#guessing number//
#game loops game development////
#guessing_number=18
#countoften=1
#while countoften<=10:
#    print ("guess the number")
#    userinput=int(input ())
#    if userinput>18:
#        print ("guess number is High,, please enter low number")
#    elif userinput<18:
#        print ("guess number is low,, please enter High number")
#    elif userinput==18:
#        print ("congratulation you won")
#        print ("you have won in", countoften,"life")
#        break
#    print(10-countoften,"life's left")
#    countoften=countoften+1
#if countoften>10:
#	print ("your lose")

#(20)

#operators///

#1] Arithmetic operators
#2] assigment operators
#3] comparision operators
#4]logical operators
#5] identity operators
#6] membership operators
#7] bitwise operators

#1] Arithmetic operators//
#exdonents
#print (5+6)
#print (5-6)
#print (5*6)
#print (5/6)
#print (5**6)
#print (5%6)
#print (5//6)

#2] assigment operators//
#x=1
#x+=8
#print (x)

#3] comparision operators//
#if 8<and>and==

#4] logical operators//
#Google search

#5] identify operators//
#a=1
#b=2
#print (a is b)
#print (a is not b)

#6] membership operators
#in and not in
#a=[2,5,7,4,1,9]
#print (1 in a)
#print(1 not in a)

#7] bitwise operators
#Google search

#(21)
#try except exception handling///
#try except//
#print("enter your first number")
#num1=input()
#print("enter your 2nd number")
#num2=input ()
#try:
#	print("tha sum of number is:",int(num1)+int(num2))
#except:
#	print ("this is a very important line")
#Exception error place see	
#except Exception as e:
#	print (e)
#	print ("this is a very important line")

#(22)
#File IO Basics///
#volatile memory (ram) temporary
#non volatile memory(hard disk) permanent

#Basics mode
"""
"r"-open file for reading(default mode)
"w"-used for writing
"x"-creates file if not exists
"a"-(append)-and more content at tha end
"t"-text mode(default mode)
"b"-binary mode
"+"-read and write
"""

#(23)

#read mode///

#f=open("file.txt")
#content=f.read()
#print(content)
#f=open("file.txt")
#content=f.read(12)
#print(content)

#for line in content:
#	print (line)

#for line in f:
#	print (line)

#f=open("file.txt")
#print (f.readline())

#(24)

#writing and appending

#writing///
#(clean and write)

#f=open("file.txt","w")
#f.write("happy birthday dhanush")
#f.write("happy birthday dhanush")
#f.close ()

#appending
#(joint line append mode)

#f=open("file.txt","a")
#f.write("happy birthday dhanush")
#f.close ()

#(25)

#seek() and tell() functions
#tell()

#f=open ("file.txt")
#print (f.tell())
#print (f.readline())
#print (f.readline())
#print (f.tell())
#f.close()

#seek()
#f=open ("file.txt")
#print (f.readline())
#f.seek(9)
#print (f.readline())
#f.close()

#(26)

#with blocks///

#with open("file.txt") as f:
#	print (f.readline())

#(27)
#more functions

#def add():
#	a=1
#	b=2
#	print (a+b)
#add()

#def add(a,b):
#	print (a+b)
#add(
#def biodata (name,age)
#	print (name)
#	print (age)
#biodata("dhanush",18)
#key world
#biodata(age=18,name="Dhanush")


#age=18defined value

#def biodata (name,age=18):
#	print (name)
#	print (age)
#age=18 defined value
#biodata ("Dhanush")

#(28)

#more functions///
#add more number and crite

#def add(a,*b):#(6,7,8,9,10)
#    for i in b:
#    	a=a+i
#    	print (a)
#    
#add(5,6,7,8,9,10)

#(29)
#kwargs(keyword variable length argument)///

#def person (name,**others):
#	print (name)
#	print (others)
#	
#person("Dhanush",age=18,state="tamilnadu",phonenumber=1736376272) 

#(30)
#scope,global variables and local variables///

#a=10 #global variables
#def functions ():
#	a=15#local variables
#	print (a)
#print (a)

#a=10 
#def functions ():
#	print (a)
#functions()
#print (a)

#a=10 
#def functions ():
#	global a
#	a=15
#	print (a)
#functions ()
#print (a)

#(31)
#passing a list in a function
#def identified (lst):
# even=0
# odd=0
# for i in lst:#mistake 1 there is no variable or parameter called list
#  if i%2==0:
#   even=even+1
#  else: #you should have used else because elif takes arguments
#   odd=odd+1
# print ("number of even number", even)
# print ("number of odd number",odd)   
#lst=[1,3,24,56,76,23,12]
#identified (lst) #you didnt close the brack

#(32)
#fibonacci series///
#01123581321
#def fibo(x):
#	a=0
#	b=1
#	print (0)
#	print (1)
#	for i in range(2,x):
#	      c=a+b
#          a=b
#          a=c
#          print (c)
#        
#fibo(5)  

#(33)
#factorial
#6!=6*5*4*3*2*1
#def factorial(a):
#	f=1
#	for i in range(1,a+1):
#		f=f*i
#	print ("factorial of",a,"is",f)	
#factorial(7)

#(34)
#recursions///
#import sys
#sys.setrecursionlimit(2000)
#i=0
#def wishes():
#	global i
#	i=i+1
#	print ("good morning",i)
#	wishes()
#wishes()

#def wishes():
#	print ("good morning")
#	wishes()
#wishes()

#(35)
#factorial using recursions
#def factorial (x):
#	if x==0:
#		return 1
#	return x*factorial (x-1)
#result=factorial(5)
#print (result

#(36)
#lambda functions
#a=lambda x,y:x+y
#print (a(5,7))

#(37)
#modules
#import flack
#external module
#pip install module name

#(38)
#booleans
#int=123
#float=2.6
#str="Dhanush"
#bool=true and false
#a=1
#if a==1:#true and false
#	print("a is one")

#(39)
#using module
#using random module
#import random
#randomnumber=random.randint(1,10)
#print (randomnumber)

#(40)
#F string
#normal string
#a=1
#b=2
#print ("Tha value of a is::",a,"The value of b is::",b)
#F string
#a=1
#b=2
#print (f"tha value of a is:: {a} Tha value of b is:: {b}")

#import math
#namber=200
#print (f"tha math is{(namber)*math.cos(90)}")

#excercise(4)
#pattern print
#print ("How many rows of stars do you want??")
#rows=int(input ())
#print ("Enter 1 for straight pattern and Enter 0 for reverse pattern")
#pattern=int(input ())
#new=bool(pattern)

#if new==True:
#	for i in range (1,rows+1):
#		for j in range (1, i+1):
#			print ("*",end="")
#		print ()
#elif new==False:
#	for i in range (rows,0,-1):
#		for j in range (1,i+1):
#				print ("*",end="")
#		print ()

#(41)
#time module///
#import time
#initial=time.time()
#k=0
#while k<45:
#	print ("I am a good boy")
#	k=k+1
#print ("Time for execution of while loop:",time.time()-initial)

#initial2=time.time()
#for i in range (45):
#	print ("I am a good boy")
#print ("Time for execution of for loop:",time.time()-initial2)

#search Google module
#import time
#localtime=time.asctime(time.localtime(time.time()))
#print (localtime)
#time.sleep(2)2sec wait

#(42)
#Enumerate functions///
#nomler functions
#l1=['potato','tomato','biscit','kurkure','pizza']
#i=1
#for items in l1:
#	if i%2 is not 0:
#		print (items)
#	i+=1
#	
#enumerate
#for index,items in enumerate(l1):
#	if index%2==0:
#		print (items)
		
#(43)
#How Does import works

#(44)
#if__name__==__main__
#create file"dhanush
#def printer(str):
#	print (f"the is a name {str}")
#def add(a,b):
#	print (a+b)
#if__name__=="__main__":
#	print (6+7)
#	print ("loose")
#print ("this is name is",__name__)

#import dhanush
#dhanush.printer("dhanush")
#dhanush.add(4,7)

#(45)
#join functions
#list=["pubg","free fire","cod"]

#👎for i in list:
#	print (i,"and",end="")
#print ("tha pular game")


#a="and ". join(list)
#print(a,"this is a pular game")

#(46)
#map() and filter ()and Reduce ()

#map
#numbers=["36","63","6","12","86"]
#numbers=list(map(int, numbers))
#print(type(numbers[4]))

#def square (a):
#	return a*a
#num=[1,2,3,4,5,6,7,8,9,10]
#for i in num:
#	print (i)
#	
#num=list(map(square,num))
#for i in num:
#	print (i)

#oplai	
#num=list(map(lambda a:a*a,num))
#for i in num:
#	print (i)	

