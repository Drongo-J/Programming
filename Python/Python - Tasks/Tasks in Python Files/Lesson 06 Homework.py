#Task 1 - Ekrana istifadəçinin daxil etdiyi say qədər, ulduzlardan üfiqi xətt çıxaran proqram yazın.

print("1. write a program that draws a horizontal line with the entered number of stars.")

stars=int(input("\nEnter the number of stars : "))

i=1

while (i<=stars): 
    print("*",end=" ")
    i+=1
if(stars<=0):
    print("\nYou must write a natural number.")


#Task 2 - Ekrana 1-50 aralığındakı rəqəmlərdən ancaq cüt olanları çıxaran proqram yazın. 

print("\n\n2. Type a program that displays only even numbers from 1 to 50 on the screen.")

i=1

while(i<=50):
    if(i%2==0):
        print(i,end=" ")
    i+=1


#Task 3 - İstifadəçinin daxil etdiyi aralıqda (məs 10 və 30) cüt rəqəmlərin cəmini tək rəqəmlərin hasilini hesablayan proqram yazın.

print("\n\n3. Write a program that calculates the product of odd numbers and the sum of even numbers in the range entered by the user.")

start=int(input("\nEnter the first number of the range : "))
end=int(input("Enter the last number of the range : "))

sum=0
product=1

while(end-start==1):
    print("\nEnter numbers that differ by more than 1.")
    start=int(input("Enter the first number of the range again : "))
    end=int(input("Enter the last number of the range again : "))

while(start<=end):
    if(start%2==0):
       sum+=start
       start+=1
    elif(start%2==1):
        product*=start
        start+=1

print("\nThe sum of even numbers is : ",sum,".")
print("The product of odd numbers is : ",product,".")
        

#Task 4 -  1-100 diapazonunda 3-ə bölünüən bütün ədədləri ekrana çıxaran proqram yazın.

print("\n4. Write a program that displays all numbers divisible by 3 in the range 1-100.")

i=1
while(i<=100):
    if(i%3==0):
        print(i,end=" ") 
    i+=1


#Task 5 -  Ədədin faktorialını tapan proqram yazın.(! - faktorial işarəsidir, Məsələn 5! = 1*2*3*4*5)

print("\n\n5. Write a program that finds the factorial of a number.")

num=int(input("\nEnter a number : "))

i=1
factorial=1

while(i<=num):
    factorial*=i
    i+=1
print("\nThe factorial of the number",num,"is",factorial,".")

#Zero's factorial is 1


#Task 6 - Ədədin üstünü hesablayan proqram yazın (istifadəçi iki ədəd daxil edəcək əsas və üst məs. 2 və 3 cavab 8 alınmalıdır).

print("\n6. Write a program that raise the number to the power(the user will enter two numbers, exponent and base of power, for example, 2 and 3, the answer must be 8).")

base=int(input("\nEnter the base of the power : "))
index=int(input("Enter the index of the power : "))

i=1
power=1

while(i<=index):
    power*=base
    i+=1

print("\nWhen you raise the number",base,"to the power",index,"you get",power,".")


#Task 7 -  İstifadəçi istənilən sayda rəqəmli ədəd daxil edir, onun rəqəmlərinin sayını və onların cəmini hesablayan proqram yazın.

print("\n7. The user enters a number with any number of digits, write a program that finds the number of its digits and calculates their sum.")

n=int(input("\nEnter a number with any number of digits : "))

sum=0
digits=0

while(n>0):
    d=n%10
    n=n//10
    digits+=1
    sum+=d   

print("\nThe number of digits is",digits,".")
print("\nThe sum of digits of number is",sum,".")



#Task 8 - İstifadəçi istənilən sayda rəqəmli ədəd daxil edir, ədədi əksinə çevirən proqram yazın.

print("\n8. The user enters a number with any number of digits, write a program that converts the number to the opposite.")

num=int(input("\nEnter a number with any number of digits : "))

while(num>0):
    d=num%10
    num//=10
    print(d,end="")


#Task 9 - İstifadəçi tam ədəd daxil edir, bu ədədin qalıqsız bölündüyü bütün rəqəmləri ekrana çıxaran proqram yazın.

print("\n\n9. The user enters an integer, display all the factors.")

num=int(input("\nEnter a number : "))
i = 1

while(i<=num):
    if(num%i==0):
        print(i,end=" ")
    i+= 1


#Task 10 - İstifadəçi tam ədəd daxil edir, bu ədədin sadə olub olmamasını tapan proqram yazın.

print("\n\n10. The user enters an integer, write a program that finds whether this number is prime.")

num=int(input("\nEnter an integer : "))

i=1
factors=0

while(num>0):
    if(num==1): 
        print("\nThe number 1 is neither a prime nor a composite number.")
        break
    if(num%i==0):
        factors+=1
    i+=1  
    if(i>num):
       break

if(num!=1):
    if(factors>2):
        print("\nThe number",num,"is not a prime number.")
    if(factors<=2):
        print("\nThe number",num,"is a prime number.")

   
#Task 11 - İstifadəçi ədəd daxil edir, bu ədədin rəqəmlərinin artan ardıcıllıqla olub olmamasını yoxlayan proqram yazın. (12299 artan ardıcıllıq, 122044 artan ardıcıllıq deyil) 

print("\n11. When user enters a number, write a program that checks whether the digits in that number are in ascending order.")

num=int(input("\nEnter a number : ")) 

while(num>-10 and num<10):
        num=int(input("Enter a number of at least two digits : "))

previous=num

while(num>0):
    if((num//10)%10<=num%10):
        num//=10
        if(num<10 and num>0):
            print("\nDigits of the number",previous,"are in ascending order.")
    else:
        print("\nDigits of the number",previous,"are not in ascending order.")
        break
    
while(num<0):
    if((num//10)%10>=num%10):
        num//=10
        if(num>-10 and num<0):
            print("\nDigits of the number",previous,"are in ascending order.")
            break
    else:
        print("\nDigits of the number",previous,"are not in ascending order.")
        break





 
