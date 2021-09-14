#mystr="Rajesh is Good Boy"
#print(mystr)

#in python index start with 0,1,2..

#in this i want only some charater that i want
mystr="RAJESH IS GOOD BOY"
print(mystr[0:3]) #RESULT RAJ
#HERE YOU 0 INCLUDE AND 3 EXCLUDE ITS TAKE 012 TOTAL 3 STRING

#R A J E S H
#0 1 2 3 4 5 6

mystr="RAJESH IS GOOD BOY"
print(len(mystr))  #length of my mystr #result 18
print(mystr[0:17])

mystr="RAJESH IS GOOD BOY"
print(len(mystr))  #length of my mystr
#print(mystr[18])  #error string index out of range
#print(mystr[0:19]) #result correct
#print(mystr[0:30]) #result correct python is intillegent
print(mystr[0:98])

mystr="RAJESH IS GOOD BOY"
print(len(mystr))  #length of my mystr #result 18
#slicing
print(mystr[0:18:1])  #RAJESH IS GOOD BOY
print(mystr[0:18:2])  #RJS SGO O
print(mystr[0:18:3])  #RE  OB
print(mystr[0:18:4])  #RSSOO
print(mystr[::])      #RAJESH IS GOOD BOY
#print(mystr[0:0:0])   #error slice step cannot be zero
print(mystr[0:0:1])   #nothing printed
print(mystr[0:0:2])   #nothing printed
print(mystr[0:1:1])   #R
print(mystr[::18])    #R
print(mystr[::100])   #R

#negative index start with ....etc -3 -2 -1
#positive index start with 0 1 2 3...etc

print(mystr[-1:]) #result Y
print(mystr[-4:-2]) #result B
print(mystr[15:16]) #result B
print(mystr[-4:]) #result BOY

#reverse the string easy way
print(mystr[::-1]) #result YOB DOOG SI HSEJAR
print(mystr[::-2]) #YBDO IHEA
