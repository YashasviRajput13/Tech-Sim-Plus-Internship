# # #LIST
# marks = [45,44,36,50,23]
# print(type(marks))

# #########Function for List
# #Reverse the List
# print(marks[::-1])

# #APPEND
# marks.append(99)

# #INSERTION
# marks.insert(2,88)
# print(marks)

# #EXTEND
# marks2 = [12,34,56]
# #marks.extend([45,44])
# marks.extend(marks2)
# print(marks)

# #SORT
# marks.sort()
# print(marks)    
# #REVERSE
# marks.reverse() 
# print(marks)    
# marks.sort(reverse=True)
# print(marks) 

# #PERCENTAGE CALCULATION
# marks = [9,7,4,3,10]
# total = sum(marks)
# count = len(marks)
# percentage = (total / (count * 10)) * 100
# print(percentage)   

# #SPLIT
# msg = "Hello all, How are you?"
# msg = msg.split("o") #Splitting based on "o"
# #msgL2 = msgL2.split() #Splitting based on space
# print(len(msg))

#File
# filename = "image.jpg"
# file = filename.split(".")
# print(file[-1])

# #<Problem/>
# id = "pro-1234-xyz"
# idname = id.split("-")
# #via slicing
# print(idname)
# print(idname[1])

#INPUT
# a=int(input("enter a : "))
# b=int(input("enter b : "))
# print(a+b)
# print(type(a))

# name=(input("enter your name: "))
# age=(int(input("enter ur age : ")))
# print("the name of user is",name,"and age is",age)
# print(((name)+"\n")* age) 

#CONDITION
# age=(int(input("enter ur age : ")))
# if age>=18:
#     print("u can vote")
# else:
#     print("NA")

# age=int(input("enter a age: "))
# if age < 12:
#     print("r=150")
# elif age >=60:
#     print("r=200")
# else:
#     print("r=300")   

#2d list#########
# li = [[56,78],[23,56,44,67],[45,12],[5,6]]
# print(len(li))
# print(len(li[1]))

#####LOOP
# for i in range(1,11,1): #(1,11)esa bhi likh skte h 
#     print(i)
# print("hello")

# for i in range(1,11,2):
#     print(i)
# print("bye...")    

# for i in range(10,0,-1):
#     print(i)
# print("bye...") 

# for i in range(-1,-11,-1):
#     print(i)
# print("bye...") 

# for i in range(-11,-1,1):
#     print(i)
# print("bye...")  

# for i in range(3,31,3):
#     print(i)

# for i in range(3,31,3):
#     print(i+5)               

# for i in range(1,10,1):
#     print(i*i)

# li=[11,22,33,44,55]
# for i in li:
#     print(i)

# li=[11,22,33,44,55]
# for i in li:
#     print(i)
#     li.append(100)

# twoD_list=[[45,11],[67,32],[89,14]]

# for n in twoD_list:
#     print(n)

# twoD_list=[[45,11],[67,32],[89,14]] 

# for n in twoD_list:
#     print(n[0]+n[1])

#######WHILE LOOP
# i=1
# while i<=5:
#     print(i)
#     i+=1

# i = 5
# while i>0:
#     print(i)
#     i-=1

# i = 0
# while True:
#     print("heya",i)
#     if i == 5:
#         break
#     i+=1

# import math
# print (math.sqrt(400))
# print(round(66.9))
# print(math.ceil(66.9))
# print(math.floor(66.9))

# from math import sqrt,tan
# print(sqrt(9))
# print(tan(45))

