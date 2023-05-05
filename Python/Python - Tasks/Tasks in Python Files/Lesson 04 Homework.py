#Task 1 - •	İstifadəçi iki kəsr ədəd daxil edir. Onların tam və kəsr hissələrinin cəmini tapın. ( Məsələn : 1.5 və 3.2 - Tam hissə cəmi 4 , kəsr hissə cəmi 0.7 edir) 

print("\n1. The user enters two fractions. Find the sum of their whole and fractional parts.")

firstF=float(input("\nEnter the first fraction : "))
secondF=float(input("Enter the second fraction : "))

wholePart1=int(firstF)
wholePart2=int(secondF)
fractionPart1=firstF-wholePart1
fractionPart2=secondF-wholePart2

print("\nThe whole part of the first number : ",wholePart1)
print("The whole part of the second number : ",wholePart2)

print("The fraction part of the first number : ",fractionPart1)
print("The fraction part of the second number : ",fractionPart2)

sumWholePart=wholePart1+wholePart2
sumFractionPart=fractionPart1+fractionPart2

print("\nThe sum of the whole parts : ",sumWholePart)
print("The sum of the fraction parts : ",sumFractionPart)


#Task 2 - İstifadəçi sahib olduğu pulu daxil edir (Kəsr halda: məsələn 15.30). İstifadəçinin neçə manat və neçə qəpiyi olduğunu ekrana çıxarın. ( Ekrana 15 manat, 20 qəpik çıxmalıdır) 

print("\n2. The user enters the money he owns (in case of fraction). Display how many manats and how many kopecks the user has.")

money=float(input("\nEnter the money (in case of fraction): "))

manat=int(money)
kopecks=money-int(money)

print("\nHe has",(int(money)) ,"manat",end=' ')
print(int(100*kopecks),"kopecks.")


#Task 3 - İstifadəçi kütləni tonla daxil edir (Kəsr ədədi ilə). Ekrana ton,kiloqram,qram halında çıxarın. (Məsələn 126.456789 Ton, Ekrana 126 Ton, 456 kq, 789 q çıxmalıdır)

print("\n3. The user enters the weight in tones (in case of fraction(e.g 123.456789). Display in tons, kilograms, grams.")

tonesFraction=float(input("\nEnters the weight in tones : "))

tones=int(tonesFraction)
kg=(int(tonesFraction*1000))-1000*tones
gr=int((tonesFraction*1000000)-int(tonesFraction*1000)*1000)

print("\n",tonesFraction,"is",tones,"tones,",kg,"kilograms,",gr,"grams.")


#Task 4 - İstifadəçi aeroporta məsafəni və ora çatmaq üçün sahib olduğu vaxtı daxil edir. Aeroporta çatmaq üçün hansı sürətlə getməli olduğunu tapan proqram yazın.

print("\n4. The user enters the distance to the airport and the time he has to get there. Write a program that finds how fast you need to go to get to the airport.")

distance=float(input("\nEnter the distance to the airport : "))
time=float(input("Enter the time you have to get there (with hour) : "))

s=distance/time

print("\nYou need to go ",s,"km/hour to get there on time.")


#Task 5 - İstifadəçi telefon danışığının başlanğıc (saat, dəqiqə, saniyə ) və son (saat, dəqiqə, saniyə) zamanını daxil edir. Danışığın dəqiqəsi 20 qəpik olarsa, ümumi qiyməti ekrana çıxarın.

print("\n5. The user enters the start (hours, minutes, seconds) and end time (hours, minutes, seconds) of the phone call. If the call costs 20 kopecks per minute, display the total price.")

start=float(input("\nEnter the start time (e.g as 12.3456) : "))
end=float(input("Enter the end time (e.g as 12.3456) : "))

hoursS=int(start)
hoursE=int(end)
minutesS=int(start*100)-100*hoursS
minutesE=int(end*100)-100*hoursE
secondsS=int(start*10000)-int(start*100)*100
secondsE=int(end*10000)-int(end*100)*100

hoursSminute=hoursS*60    
hoursEminute=hoursE*60 
secondsSminute=secondsS/60
secondsEminute=secondsE/60

diffirenceH=hoursS*60-hoursE*60 
diffirenceM=minutesS-minutesE
diffirenceS=secondsS/60-secondsE/60

total=((hoursE*60-hoursS*60)*0.20+(minutesE-minutesS)*0.20+(secondsE/60-secondsS/60)*0.20)

print("\nThe total price is",int(total),"Azn",int((total-int(total))*100),"kopecks.")


#Task - 6 İstifadəçi AZN ilə pul daxil edir. Əlavə olaraq dolların,avronun, rublun məzənnəsini daxil edir.İstifadəçinin neçə dollar ,avro və rubl ala biləcəyini ekrana çıxarın. VACİB QEYD : Bununla birlikdə dollar,avro və rubl tam ədəd olmalıdır. Artıq qalan pul yenidən AZN olaraq göstərilsin. (Məs: 100 AZN , dolların məzənnəsi = 1.71 , Ekrana –> 58$ , qalıq 80 qəpik)

print("\n6. User enters money in AZN. Then, he enters the exchange rates of the dollar, euro and ruble. Display how many dollars, euros and rubles the user can receive. The dollar, euro and ruble must be in full numbers. The remaining money should be shown again in AZN.")

azn=float(input("\nEnter the amount of AZN : "))

dollar=float(input("\nEnter the exchange rate for of dollar AZN : "))
euro=float(input("Enter the exchange rate of euro for AZN : "))
ruble=float(input("Enter the exchange rate of ruble for AZN : "))

countDollar=azn*dollar
countEuro=azn*euro
countRuble=azn*ruble

The_remaining_money_from_dollar_with_azn=countDollar-(int(countDollar))
The_remaining_money_from_euro_with_azn=countEuro-int(countEuro)
The_remaining_money_from_ruble_with_azn=countRuble-int(countRuble)

d=(The_remaining_money_from_dollar_with_azn)*100
e=(The_remaining_money_from_euro_with_azn)*100
r=(The_remaining_money_from_ruble_with_azn)*100

print("\nEntered amount of Azn is",int(countDollar),"$ and remaining money that wasn't converted is",int(d),"kopecks.")
print("Entered amount of Azn is",int(countEuro),"€ and remaining money that wasn't converted is",int(e),"kopecks.")
print("Entered amount of Azn is",int(countRuble),"₽ and remaining money that wasn't converted is",int(r),"kopecks.")


#Task 7 - İstifadəçi iş gününün başlanğıcından keçən saniyə ilə zamanı daxil edir. (Məsələn 9:00da başlayıbsa və saat 10dursa, 3600 saniyə keçib) . Yazdığınız program, işçinin iş gününün sonuna kimi neçə TAM SAAT işləyəcəyini çıxarmalıdır. İş günü 8 saatdır. ( Tam saat – 4 saat 50 dəq qalıbsa , tam saat 4 saatdır)

print("\n7. The user enters the time in seconds from the beginning of the working day. The program you write should determine how many full hours the employee will work by the end of the workday. The working day is 8 hours.")

seconds=float(input("\nEnter the time in seconds from the beginning of the working day : "))

youWillWork=int(8-seconds/3600)

print("\nYou have to work approximately",youWillWork,"hours to finish the workday.")


#Task 8 - •	İstifadəçi bir notebookun qiymətini, almaq istədiyi sayı, və endirim faizini daxil edir. Program ekrana ümumi sifarişin neçə AZN olacağını çıxarır.

print("\n8. The user enters the price of a notebook, the number he wants to buy, and the discount rate. The program has to display how much the total order will be.")

price=float(input("\nEnter the price of notebook : "))
count=int(input("Enter the count of notebooks you want to buy : "))
discountRate=float(input("Enter the discount rate : "))

Azn=(price*count)-(price*count)/100*discountRate

print("\nThe order will cost",int(Azn),"AZN",end=' ')
print(int((Azn-int(Azn))*100),"kopecks.") 


#Task 9 - •	İstifadəçi menecerin aylıq satışlarının cəmini AZN ilə daxil edir. Menecerin aylıq maaşı 100$ + 5% satışlardan gələn gəlirdən ibarətdir.  Menecerin maaşını hesablayan program yazın.

print("\n9. The user enters the total monthly sales of the manager in AZN. The manager's monthly salary is $ 100 and 5% of sales revenue. Write a program that calculates the manager's salary.")

TheTotalMonthlySale=float(input("\nEnter the total monthly sales of the manager in AZN : "))

TheTotalMonthlySaleWithDollar=TheTotalMonthlySale/1.7

managersSalary=100+(TheTotalMonthlySaleWithDollar*5/100)

print("\nThe manager's salary is",int(managersSalary),"$",end=' ')
print(int((managersSalary-int(managersSalary))*100),"cent.")


