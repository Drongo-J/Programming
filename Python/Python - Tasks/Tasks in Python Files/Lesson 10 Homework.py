#Task 1 - -30 və 20 arasında random rəqəmlərdən ibarət ölçüsü 10 olan massiv yaradın. Birinci müsbət ədəddən sonra gələn bütün rəqəmləri toplayan program yazın

print("\n1. Create a list of random numbers between -30 and 20, which has 10 numbers. Write a program that adds all the numbers that come after the first positive number.")

import random

def sumOfNumbersAfterX(list):
    global x
    for x in list:
        if x > 0:
            break
    sum=0
    for y in list[list.index(x):]:
        sum+=y
    return sum
    return x

        
list=random.sample(range(-30,20),10)
print("\n  It is the list :",list)
result=sumOfNumbersAfterX(list)

print("\n  And",result,"is the sum of the first positive number - (",x,") and numbers after it.")



print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 2 - Ölçüsü 20 olan və random rəqəmlərdən ibarət siyahi yaradın. Siyahi da maximum və minimum elemtini tapan program yazın. 

print("\n\n2. Create a list of 20 random numbers. Write a program that finds the maximum and minimum element in the list.")

import random

def getMax(list):
    max=0
    for x in list:
        if (x > max):
            max=x
    return max

def getMin(list):
    min=1001
    for x in list:
        if (x < min):
            min=x
    return min

list=list=random.sample(range(1000),20)
result=getMax(list)
result2=getMin(list)
print("\n  In this list --> ",list)
print("\n ",result,"is the biggest number (maximum element).")
print("\n ",result2,"is the smallest number (minimum element).")

print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 3 - 10 ölçülü kəsr ədədlərdən ibarət siyahi yaradın. Neçə rəqəmin kəsr hissəsinin olmadığını ekrana çıxaran program yazın. (məs: {12,12.5, 10.1, 1,2} kəsr hissəsi olmayan ədədlər 3)


print("\n\n3. Create a list of 10-dimensional fractions. Write a program that displays how many numbers do not have a fraction.")

def dontHaveFraction(list):
    counter=0
    for x in list:
        if (int(x) == x):
            counter+=1
    return counter

list=[10,10.5,11,11.5,12,12.5,13,13.5,14,14.5]
result=dontHaveFraction(list)
result2=len(list)-result

if (result==1):
    print("\n  Only one of them doesn't have a fractioal part")
else:
    print("\n  In the list",result,"of them do not have a fractional part.")
if (result2==1):
    print("\n  But",result2,"element of the list have the fractional part.")
else:
    print("\n  But",result2,"elements of the list have the fractional part.")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 4 - 1 və 200 arasında random rəqəmlərdən ibarət ölçüsü 20 olan siyahi yaradın. 1 rəqəmli, 2 rəqəmli, 3 rəqəmli ədədlərin faiz nisbəti ilə müqayisəsini edən program yazın.


print("\n\n4. Create a list of random numbers between 1 and 200, which includes 20 numbers. Write a program that compares 1-digit, 2-digit, and 3-digit numbers to percentages.")
import random

def typeOfNumber(list):
    global digit1_counter
    global digit2_counter
    global digit3_counter
    digit1_counter=0
    digit2_counter=0
    digit3_counter=0
    for x in list:
        if (x > 0 and x < 10):
            digit1_counter+=1
        elif (x > 9 and x < 100):
            digit2_counter+=1
        elif (x > 99 and x < 1000):
            digit3_counter+=1
    return digit1_counter
    return digit2_counter
    return digit3_counter

list=random.sample(range(1,200),20)
typeOfNumber(list)
print("\n  In this list -->",list)
if (digit1_counter==1):
    print("\n  There is only 1 time 1-digit number.")
elif(digit1_counter==0):
    print("  There is no 1-digit number")
else:
    print("\n  There are",digit1_counter,"times 1-digit number.")

if (digit2_counter==1):
    print("  There is only 1 time 2-digit number.")
elif(digit2_counter==0):
    print("  There is no 2-digit number")
else:
    print("  There are",digit2_counter,"times 2-digit number.")

if (digit3_counter==1):
    print("  There is only 1 time 3-digit number.")
elif(digit3_counter==0):
    print("  There is no 3-digit number")
else:
    print("  There are",digit3_counter,"times 3-digit number.")


print("\n  If we convert these to percentages, we get : ")

print("\n ",digit1_counter*5,"% of the list includes 1-digit numbers.")
print(" ",digit2_counter*5,"% of the list includes 2-digit numbers.")
print(" ",digit3_counter*5,"% of the list includes 3-digit numbers.")

#Müqayisə

if (digit1_counter>digit2_counter>digit3_counter):
    print("\n  The percentage of 1-digit numbers is greater than the other ones.")
elif (digit1_counter>digit3_counter>digit2_counter):
    print("\n  The percentage of 1-digit numbers is greater than the other ones.")
elif (digit2_counter>digit1_counter>digit3_counter):
    print("\n  The percentage of 2-digit numbers is greater than the other ones.")
elif (digit2_counter>digit3_counter>digit1_counter):
    print("\n  The percentage of 2-digit numbers is greater than the other ones.")
elif (digit3_counter>digit1_counter>digit2_counter):
    print("\n  The percentage of 3-digit numbers is greater than the other ones.")
elif (digit3_counter>digit2_counter>digit1_counter):
    print("\n  The percentage of 3-digit numbers is greater than the other ones.")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 5 - 2 və 200 arasında random rəqəmlərdən ibarət ölçüsü 20 olan siyahi yaradın. Siyahidaki bütün sadə rəqəmləri ekrana çıxaran program yazın.

print("\n\n5. Create a list of random numbers between 2 and 200, which has 20 numbers. Write a program that displays all the prime numbers in the list.")

import random

list=random.sample(range(2,200),20)
print("\n  This is the list :",list)
print("\n  And these are prime numbers from the list :")

for num in list:
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(" ",num,end="")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 6 - Ölçüsü 10 olan massiv yaradın və içərsini random rəqəmlərlə doldurun. Massivdəki rəqəmlərin yerlərini tərsinə çevirən program yazın. (0-cı indeksi 9-la, 1-i 8-lə və s.)

print("\n\n6. Create an array of 10 digits and fill it with random numbers. Write a program that reverses the positions of numbers in an array.")

import random

def reverse(list):
    list1=list[::-1]
    return list1

list=random.sample(range(1,100),10)
result=reverse(list)
print("\n  The normal list is this : ",list)
print("\n  And reversed form of its numbers is this : ",result)


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 7 -  Ölçüsü 10 olan massiv yaradın və içərsini random rəqəmlərlə doldurun. Massivdəki qonşu elementlərin yerini dəyişən program yazın.(indexler vasitesiyle etmek lazimdir)

import random

print("\n\n7. Create an array of 10 numbers and fill it with random numbers. Write a program that changes the location of adjacent elements in the array.(should be done through indices)")

def changeAdjacents(list):
    for i in range(0,9,2):
        a=list[i]
        list[i]=list[i+1]
        list[i+1]=a
    return list


list=random.sample(range(1,100),10)
print("\n  The normal list is this : ",list)
result=changeAdjacents(list)
print("\n  And when you change the location of adjacent elements you get this : ",result)


print("\n\n------------------------------------------------------------------------------------------------------------------------")



#Task 8 -  Ölçüsü 5 olan iki siyahi yaradın A və B . Ölçüsü 10 olan üçüncü siyahi yaradın C. C siyahisina A və B dən sıra ilə elemntləri kopyalayın . (məs: С[0]=A[0], С[1]=B[0], C[2]=A[1], C[3]=B[1] və s.)

print("\n\n8. Create two lists of 5 digits - (A) and (B). Then create a third list of 10 digits - (C). Write a program that copies the elements from (A) and (B) to the list (C) in a row.")

import random

def copyAandBtoC(listA,listB,listC):
    y=0
    for x in range(0,10,2):
        if y==5:
            break
        listC[x]=listA[y]
        listC[x+1]=listB[y]
        y+=1
    return listC

listA=random.sample(range(10,100),5)
listB=random.sample(range(10,100),5)
listC=random.sample(range(0,10),10)
result=copyAandBtoC(listA,listB,listC)

print("\n  This is the list (A) -",listA)
print("  This is the list (B) -",listB)
print("\n  And this is the new list (C), which was created from lists A and B : ",result)


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 9 - Bir massivi ikinci massivə kopya edən program yazın. Şərt: kopya edərkən birinci sıfırdan kiçik elementlər daha sonra 0-lar daha sonra 0-dan böyük elementləri kopya etməlidir.

print("\n\n9. Write a program that copies one array to another and aligns the numbers in a row.")

import random

def copy(list1,list2):
    for x in range(0,len(list1)):  
        list2[x]=list1[x]
        return list2

list1=random.sample(range(-99,99),11)
list2=random.sample(range(-99,99),11)
result=copy(list1,list2)
print("\n  This is the list which is not aligned in a row :",result)
result.sort()
print("\n  And this is a sorted form of list :",result)


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 10 8-ci ilə eyni olduğundan yazmadım

