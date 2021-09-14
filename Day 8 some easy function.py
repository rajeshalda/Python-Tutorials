#mystr="RAJESH IS GOOD BOY"
#print(type(mystr)) #<class 'str'>


#print(mystr.isalnum()) #False  isalnum means alpha numeric string

#mystr="RajeshAldaIsGoodBoy"
#print(mystr.isalnum())  #True  isalnum means alpha numeric string

#true means only alpha numeric string with no spaces
#false means there space or somthong else

mystr="Rajesh Alda Is Good Boy"
print(mystr.endswith("Boy")) #True its right
print(mystr.endswith("BDOY")) #False its not end with bdoy

print(mystr.count("o")) #result 3

mystrr="rajesh alda is good boy"
print(mystrr.capitalize()) #result  Rajesh alda is good boy capitalize the first later

print(mystrr.find("is")) #result 12   number index to find any string in string

yourstr="RAJESH ALDA IS GOOD BOY"
strr="rajesh alda is good boy"
print(mystrr.lower()) #result rajesh alda is good boy
print(strr.upper()) #result RAJESH ALDA IS GOOD BOY

allstr="RAJESH ALDA IS GOOD BOY"
print(allstr.replace("IS","are")) #RAJESH ALDA are GOOD BOY
