#Task 1 - Ədədin cüt və ya tək olmasını təyin edən program yazın.

print("1. Write a program that determines whether a number is even or odd.")

number=int(input("\nEnter the number : "))

if(number==0):
    print("\nThe number 0 is neither an even number nor an odd number.")
elif(number%2==0):
    print("\nThe number",number,"is even.")
else:
    print("\nThe number",number,"is odd.")


#Task 2 - 2. İki ədəd daxil edin onlardan kiçik olanı ekrana çıxarın.( 41,42 - Ekrana kiçik ədəd (41) çıxsın)

print("\n2. Enter two numbers and display the smaller one on the screen.")

num1=float(input("\nEnter the first number : "))
num2=float(input("Enter the second number : "))

if(num1>num2):
    print("\nThe number",num2,"is the smallest of the two numbers.")
else:
    print("\nThe number",num1,"is the smallest of the two numbers.")


#Task 3 -  Daxil edilən ədədin mənfi və ya müsbət olmasını təyin edən program yazın. ( 0 halını da nəzərə alın)

print("\n3. Write a program that determines whether the entered number is negative or positive.(Consider the case of 0).")

num=float(input("\nEnter the number : "))

if(num==0):
    print("\nThe number 0 is neither positive nor negative.")
elif(num>0):
    print("\nThe number",num,"is positive.")
else:
    print("The number",num,"is negative.")


#Task 4 - 4. Kalkulyator düzəltməli. İki kəsr ədəd daxil edilir a və b. Ekrana seçimlər çıxır. 1) a + b 2) a – b 3) a * b 4) a / b. Seçilən rəqəmə əsasən, nəticə ekrana çıxır

print("\n4. You need to make a calculator. Two fractions are included a and b. Options appear on the screen:\n\t\b1) a + b \n\t\b\b2) a - b \n\t\b\b\b\b3) a * b\n\t\b\b\b\b4) a / b.\n   Based on the selected number, the result is displayed.")

num1=float(input("\nEnter the first fraction : "))
num2=float(input("Enter the second fraction : "))
arithmetic_operation=input("\nType arithmetic operation that you need (addition, subtraction, multiplication, division): ")

if(arithmetic_operation=="addition"):
    print("\nAddition of the numbers is",num1+num2,".")
elif(arithmetic_operation=="subtraction"):
    print("Subtraction of the numbers is",num1-num2,".")
elif(arithmetic_operation=="multiplication"):
   print( "Multiplication of the numbers is",num1*num2,".")
elif(arithmetic_operation=="division"):
    print("Ddivision of the numbers is",num1/num2,".")
else:
    print("Unknown arithmetic opearation")


Task 5 - İstifadəçi ədəd daxil edir, ədədin 1-50 aralığında olub olmadığını yoxlayan program yazın.

#print("\n5. The user enters a number, write a program that checks whether the number is in the range 1-50.")

#num=float(input("Enter the number : "))

#if(num>=1 and num<=50):
    #print("The number",num,"is in the range 1-50.")
#else:
    #print("The number",num,"is not in the range 1-50.")


#Task 6 - İstifadəçi iki ədəd daxil edir. ( X və Y ) Əgər X Y-ə qalıqsız bölünürsə ekrana Yes çıxır, əks halda No.

#print("\n6. The user enters two numbers(X and Y). If X is divisible by Y without a remainder,\"Yes\" appears on the screen,otherwise \"No\".")

#X=float(input("\nEnter the first number (X) : "))
#Y=float(input("Enter the second number (Y) : "))

#if(X%Y==0):
    #print("\nYes, X is divisible by Y without a remainder")
#else:
    #print("\nNo, X is not divisible by Y without a remainder")


#Task 7 - 7. İstifadəçi ədəd daxil edir. Onun 3-ə, 5-ə, 7-ə qalıqsız bölünüb bölünməməsini yoxlayın (ayrı-ayrı).
        
#print("\n7. The user enters the numbers. Check if it is divisible by 3, 5, 7 without remainder (separately).")     

#num=float(input("Enter the number : "))

#if(num%3==0):
    #print("\nThe number",num,"is divisible by 3 without remainder.")
#if(num%5==0):
    #print("\nThe number",num,"is divisible by 5 without remainder.")
#if(num%7==0):
    #print("\nThe number",num,"is divisible by 7 without remainder.")


#Task 8 - Ədədin modulunu hesablayan program yazın.(ədədin modulu həmişə müsbət olur ,müsbət də ,mənfi də göndərsəniz nəticə müsbət olmalıdı, hər iki halda.)

#print("\n8. Write a program that calculates the modulus of a number.")

#num=float(input("\nEnter the number : "))

#if(num<0):
    #print("\nThe modulus of a number is",abs(num))
#else:
    #print("\nThe modulus of a number is",num)


#Task 9 - Maksimum 4 rəqəmli ədəd daxil edilir. Ədədin neçə rəqəmdən ibarət olduğunu hesablayan program yazın.

#print("\n9. A number with 4 digits or less is entered. Write a program that calculates how many digits a number consists of.")

#num=int(input("\nEnter the number : "))
    
#if(num>=1000 and num<=9999 and num//1000>0):
    #print("\nThe number is 4-digit.")
#elif(num>=100 and num<=999 and num//100>0):
    #print("\nThe number is 3-digit.")
#elif(num>=10 and num<=99 and num//10>0):
    #print("\nThe number is 2-digit.")
#elif(num>=0 and num<=9 and num//1>=0):
   #print("\nThe number is 1-digit.")
#else:
    #print("\nThe number is not 4-digit number.")


#Task 10 - 5 rəqəmli ədəd daxil edilir. Onun polindrom olub olmamasını təyin edən program yazın.

#print("\n10. 5-digit number is entered. Write a program that determines whether it is a polyndrome.")

#num=int(input("\nEnter the 5-digit number : "))


#if(num>=10000 and num<=99999 and num//10000==num%10):
    #print("\nThe number is a polyndrome.")
#elif(num>=0 and num<=9999 or num>=100000):
    #print("\nThe number is not 5-digit number.")
#else:   
    #print("\nThe number is not a polyndrome.")


#Task 11 - 11.Əvvəldən şifrə saxlanılır. Istfiadəçi şifrə daxil edir , əgər şifrə bazadakı şifrəyəbərabər olsa, ekrana , --Access succesfully completed-- çıxır, əks halda --Acces denied--çıxır.

#print("\n11. The password is saved from the beginning. The user enters the password, if the password is equal to the password in the database, \"--Access succesfully completed--\" appears on the screen , otherwise \"--Acces denied--\"  appears on the screen.")

#password="123456"

#password=input("\nEnter the password : ")

#if(password=="123456"):
    #print("\n--Access succesfully completed--")
#else:
    #print("\n--Acces denied--")


#Task 12 - Ümumi olaraq qəbul olunub ki , 1 insan yaşı 7 it yaşına bərabərdir ( 1 il insan üçün = 7 il it üçün). Amma bu sadə hesablama çox hallarda səhv hesab olunur, çünki itlər öz yetkin yaşlarına 2 ilə çatırlar. Buna görə də, bəzi insanlar ilk iki il üçün itin yaşını 10.5 yaş olaraq hesablamağı düzgün hesab edirlər, daha sonrakı illəri isə 4 ildən hesablayırlar. (məsələn 3 insan ili = 25 it ili ) Yuxarıda verilən məlumatlara görə insan ilini it ilinə çevirən program yazmalısınız. Əmin olunki sizin program ilk iki il üçün ayrı sonrakı illər üçün ayrı hesablamanı reallaşdırır. Əgər istifadəçi tərəfindən mənfi ədəd daxil edilərsə, Sizin programınız , istifadəçiyə mənfi ədəd daxil etdiyini bildirməlidir

print("\n12. According to the information, you need to write a program that turns the human year into the dog year. Make sure your program performs a separate calculation for the first two years and for subsequent years. If negative numbers are entered by the user, your program must notify the user that you have entered a negative number.")

humanYear=int(input("\nEnter the year of human : "))

if(humanYear==1):
    print("\n1 human year is equal to 10.5 dog year.")
elif(humanYear==2):
    print("\n2 human year is equal to 21 dog year.")
elif(humanYear==3):
     print("\n3 human year is equal to 25 dog year.")
elif(humanYear==4):
    print("\n4 human year is equal to 29 dog year.")
elif(humanYear==5):
    print("\n5 human year is equal to 34 dog year.")
else:
    print("\nThe number that you entered is negative")
 
 
#Task 13 - Bürcü tapan program yazın.

print("\n13. Write a program that finds the constellation.")

month=input("\nEnter the month that you were born with number : ")
day=input("Enter the day that you were born : ")

if(month==12 and day>=22 and day<=31 or month==1 and 1<=day<=19):
    print("Your constellation is capricorn.")
elif(month==1 and day>=20 and day<=31 or month==2 and 1<=day<=18):
    print("Your constellation is aquarius.")
elif(month==2 and day>=19 and day<=30 or month==3 and 1<=day<=20):
    print("Your constellation is fish.")
elif(month==3 and day>=21 and day<=31 or month==4 and 1<=day<=19):
    print("Your constellation is ram.")
elif(month==4 and day>=20 and day<=30 or month==5 and 1<=day<=20):
    print("Your constellation is bull.")
elif(month==5 and day>=21 and day<=31 or month==6 and 1<=day<=20):
    print("Your constellation is twins.")
elif(month==6 and day>=21 and day<=30 or month==7 and 1<=day<=22):
    print("Your constellation is cancer.")
elif(month==7 and day>=23 and day<=31 or month==8 and 1<=day<=22):
    print("Your constellation is lion.")
elif(month==8 and day>=23 and day<=30 or month==8 and 1<=day<=22):
    print("Your constellation is girl.")
elif(month==9 and day>=23 and day<=31 or month==8 and 1<=day<=22):
    print("Your constellation is scales.")
elif(month==10 and day>=23 and day<=30 or month==8 and 1<=day<=21):
    print("Your constellation is scorpion.")
elif(month==11  and day>=22 and day<=31 or month==8 and 1<=day<=21):
    print("Your constellation is archer .")


