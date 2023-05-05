#Task 1 - Ekrana istifadəçinin daxil etdiyi say qədər, ulduzlardan üfiqi xətt çıxaran proqram yazın.

print("1. write a program that draws a horizontal line with the entered number of stars.")

num=int(input("\nEnter a number : "))

while(num<0):
    print("\nYou must write a whole number.")
    num=int(input("Enter a whole number : "))

for i in range(num):
    print("*",end="")

print("\nProgram ended.")


#Task 2 - Ekrana 1-50 aralığındakı rəqəmlərdən ancaq cüt olanları çıxaran proqram yazın. 

print("\n\n2. Type a program that displays only even numbers from 1 to 50 on the screen.")

for i in range(1,50+1):
    if(i%2==0):
        print(i,end=" ")

print("\nProgram ended.")


#Task 3 - İstifadəçinin daxil etdiyi aralıqda (məs 10 və 30) cüt rəqəmlərin cəmini tək rəqəmlərin hasilini hesablayan proqram yazın.

print("\n\n3. Write a program that calculates the product of odd numbers and the sum of even numbers in the range entered by the user.(The program takes into account the first and the last number.)")

num1=int(input("\nEnter the first number of the range : "))
num2=int(input("Enter the last number of the range : "))

sum=0
product=1

while True:
        if(num1>num2):
            print("\nThe last number of the range must be larger than the first number of the range.")
            num1=int(input("Re-enter the first number of the range correctly : "))
            num2=int(input("Re-enter the last number of the range correctly : "))
        if(num2-num1==1):
            print("\nEnter numbers that differ by more than 1. Because there is no whole number between them.")
            num1=int(input("Enter the first number of the range again : "))
            num2=int(input("Enter the last number of the range again : "))
        if(num2-num1==0):
            print("\nThe first and the last number of the range can't be the same number!")
            num1=int(input("Enter the first number of the range again correctly : "))
            num2=int(input("Enter the last number of the range again correctly : "))
        elif(num2-num1>=2):
            break

for i in range(num1,num2+1):
    if(i%2==0):
        sum+=i
    else:
        product*=i
        
print("\nThe sum of the even numbers in the range",num1,"-",num2,"is",sum,".")
print("The product of the odd numbers in the range",num1,"-",num2,"is",product,".")

print("\nProgram ended.")
   

#Task 4 -  1-100 diapazonunda 3-ə bölünüən bütün ədədləri ekrana çıxaran proqram yazın.

print("\n\n4. Write a program that displays all numbers divisible by 3 in the range 1-100.")

for x in range(1,100):
    if(x%3==0):        
        print(x,end=" ")

print("\n\nProgram ended.")


#Task 5 -  Ədədin faktorialını tapan proqram yazın.(! - faktorial işarəsidir, Məsələn 5! = 1*2*3*4*5)

print("\n\n5. Write a program that finds the factorial of a number.")

num=int(input("\nEnter a number : "))
while(num<0):
    print("\nThe factorial operator is only defined for positive numbers.Hence, the factorial of negative numbers do not exist")
    num=int(input("Enter whole number [0,∞): "))

factorial=1

for x in range(1,num+1):
    factorial*=x

print("\n",num,"! is equal to",factorial,".")
print("\nProgram ended.")


#Task 6 - Ədədin üstünü hesablayan proqram yazın (istifadəçi iki ədəd daxil edəcək əsas və üst məs. 2 və 3 cavab 8 alınmalıdır).

print("\n\n6. Write a program that raise the number to the power(the user will enter two numbers, exponent and base of power, for example, 2 and 3, the answer must be 8).")

base=int(input("\nEnter the base of the power : "))
index=int(input("Enter the index of the power (nonnegative numbers) : "))
 
power=1

for x in range(index):
    power*=base

print("\nWhen you raise the number",base,"to the power",index,"you get",power,".")

print("\nProgram ended.")


#Task 7 - İstifadəçi istənilən sayda rəqəmli ədəd daxil edir, onun rəqəmlərinin sayını və onların cəmini hesablayan proqram yazın.

#Bu tapşırıq "for" komandası ilə olmadığı üçün "while" komandası ilə olanı əvvəlki ev tapşırığından köçürdüm.

print("\n\n7. The user enters a number with any number of digits, write a program that finds the number of its digits and calculates their sum.")

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

print("\nProgram ended.")


#Task 8 - İstifadəçi istənilən sayda rəqəmli ədəd daxil edir, ədədi əksinə çevirən proqram yazın.



print("\n\n8. The user enters a number with any number of digits, write a program that displays inverse of the number.")

num=int(input("\nEnter a number with any number of digits : "))

while(num>0):
    d=num%10
    num//=10
    print(d,end="")
     
print("\nProgram ended.")


#Task 9 - İstifadəçi tam ədəd daxil edir, bu ədədin qalıqsız bölündüyü bütün rəqəmləri ekrana çıxaran proqram yazın.

print("\n\n9. The user enters an whole number, display all the factors.")

num=int(input("\nEnter a whole number : "))

if(num==0):
        print("\nAll numbers other than zero are factors of zero")
                      
for x in range(1,num+1):
    if(num%x==0):
       print(x,end=" ")
       
print("\n\nProgram ended.")


#Task 10 - İstifadəçi tam ədəd daxil edir, bu ədədin sadə olub olmamasını tapan proqram yazın.

print("\n\n10. The user enters a whole number, write a program that finds whether this number is prime.")

num=int (input("\nEnter a whole number : "))

while(num<0):
    num=int(input("\nNegative numbers are neither a prime nor a composite number. Enter a whole number, not negative : "))

if(num==0): 
        print("\nThe number 0 is neither a prime nor a composite number.")
        

factors=0

for x in range(1,num+1):
    if(num==1): 
        print("\nThe number 1 is neither a prime nor a composite number.")
        break
    if(num%x==0):
        factors+=1

if(num!=1 and num!=0):
    if(factors>2):
        print("\nThe number",num,"is not a prime number.")
    if(factors<=2):
        print("\nThe number",num,"is a prime number.")


#Task 11 - İstifadəçi ədəd daxil edir, bu ədədin rəqəmlərinin artan ardıcıllıqla olub olmamasını yoxlayan proqram yazın. (12299 artan ardıcıllıq, 122044 artan ardıcıllıq deyil) 

#Bu tapşırıq "for" komandası ilə olmadığı üçün "while" komandası ilə olanı əvvəlki ev tapşırığından köçürdüm.

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









