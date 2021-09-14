var1="rajesh alda"
var2=20
var3=45.23
print(var1)
print(var2)
print(var3)

#result rajesh alda
#result 20
#result 45.23

var10="rajesh alda"
var20=20
var30=45.23
var40="ramesh bari"
var50=30
print(var10 + var40) #contenat
print(var20 + var50)
print(var30 + var20)
#print(var10 + var20) # error

print(type(var10)) #its shows type of variable string/integer/float etc..
print(type(var20))
print(type(var30))

var22=45
var33=55
print(var22 + var33)

var44="45"
var55="55"
print(var44 + var55) #result 4555
print(int(var44)+int(var55)) #result100 #typecasting

print(10 * "hello")  #to write multiple times hello

#hellohellohellohellohello

print(10 * "hello\n")  #to write multiple times hello

#hello
#hello
#hello
#hello

var12="45"
var14="55"
print(10 * str(int(var12)+int(var14)))
#result 100100100100100100100100100100

var15="2"
var16="3"
print(10 * int(int(var15)+int(var16)))
#result 50

var15="2"
var16="3"
print(10 * float(int(var15)+int(var16)))
#result 50.
###
#print("enter a number")
#kit =input()
#print("you entered:", kit)

#print("enter a string")
#n=str(input())             #rajesh
#print("you enterd:",n)

#print("enter a string")
str1=input("enter your string")
print("\n you entered:",str1)

print("enter any number", end="")
num=input()
print(" you have entered:", num)

print("enter any string", end="")
num=str(input())
print(" you have entered:", num)