#Part 1 (Microsoft Word-dən olan tapşırıqlar)
print("\nExercises from Part 1")

#Task 1 - İki rəqəm daxil edilir, onların ədədi ortasını tapan proqram yazın.

print("\n\n1. Find the arithmetic mean of the two numbers.")
a=float(input("\nEnter the first number : "))
b=float(input("Enter the second number : "))

Arithmetic_mean=(a+b)/2

print("\nArithmetic mean of two number : ",Arithmetic_mean)


#Task 2 - İstifadəçi a və b-ni daxil edir, ax+b=0 tənliyini hesablayıb x-i tapan proqram yazın. 

print("\n\n2. A and b are given. Find x according to the formula ax + b = 0")

First_number=float(input("\nEnter a : "))
Second_number=float(input("Enter b : "))

x=-b/a

print("\nThe value of x :",x)


#Task 3 - İstifadəçi rəqəm daxil edir, rəqəmin kubunu tapan proqram yazın.

print("\n3. Find the cube of the number.")

Number=float(input("\nEnter the number : "))

The_cube_of_the_number=Number**3

print("\nThe cube of the number : ",The_cube_of_the_number)


#Task 4 - Düzxətli bərabərsürətli hərəkətlə gedilən məsafəni növbəti düsturla hesablayın: S = v*t + (a*t**2)/2,
# burada V – sürət,  t – zaman, а – təcildir. (istifadəçi a,t,v-ni daxil edir). 

print("\n4. Calculate the distance traveled in a straight line.(V - speed, t - time, a - acceleration, S-distance)")

V=float(input("\nEnter the value of V : "))
t=float(input("Enter the value of t : "))
a=float(input("Enter the value of a : "))

S=V*t + (a*t**2)/2

print("\nThe distance traveled in a straight line (S) : ",S)


#Task 5 - İstifadəçi dolların miqdarını daxil edir. Bunu manata çevirən proqram yazın.

print("\n5. The user enters the amount of dollars. Convert it into manats.") 

D=float(input("\nEnter the value of dollars : "))

Manats=1.7*D

print("\nThe value of manats : ",Manats)


#Task 6 - Mili kilometrə çevirən proqram yazın. (1 mil – 1.609 km)

print("\n6. Convert miles to kilometers.(1 mile - 1,609 km)")

M=float(input("\nEnter the value of miles : "))

Kilometers=1.609*M

print("\nThe value of kilometers : ",Kilometers)


#Task 7 - İstifadəçi klaviaturaya aeroporta qədər olan məsafəni və onun bu məsafəni qət etmə müddədini daxil edir.
# Onun getmə sürətini hesablayın.

print("\n7. The user enters on the keyboard the distance (d) to the airport and the duration of this distance(t).Calculate its speed(s).")

d=float(input("\nEnter the distance (d) : "))
t=float(input("Enter the duration of this distance (t) : "))

s=d/t 

print("\nIts speed : ",s)


#Task 8 - N ədədinin F faizini tapan proqram yazın. 

print("\n8. Find the F percentage of the number N.")

N=float(input("\nEnter the number (N) : "))
F=float(input("Enter the percentage (F) : "))

F_percentage_of_number=N*(F/100)

print("\nAnswer : ",F_percentage_of_number)


#Task 9 - Çevrənin uzunluğu istifadəçi tərəfindən daxil edilir. Çevrənin diametrini tapan proqram yazın.

print("\n9. The length of the circle is entered by the user. Find the diameter of the circle.")

L=float(input("\nThe length of the circle which is entered by the user : "))

d=L/3.14

print("\nThe diameter of the circle : ",d)


#Task 10 - R1, R2, R3 müqavimətləri verilib. R0 müqavimətinin qiymətini 1/R0 = 1/R1+1/R2+1/R3 düsturundan istifadə edərək hesablayın. (Məsələn: R1=2, R2=4, R3=8 olarsa, R0 = 1.142857) 

print("\n10. Enter R1, R2, R3. Calculate R0 using the formula 1/R0 = 1/R1 + 1/R2 + 1/R3")

R1=float(input("\nEnter the value of R1 : "))
R2=float(input("Enter the value of R2 : "))
R3=float(input("Enter the value of R3 : "))

#Sol tərəfdə rəqəm yaza bilmədiyim üçün düsturu başqa cür yazdım.
R0 = (1/R1 + 1/R2 + 1/R3)**-1

print("\nThe value of X : ",R0)


#Part 2 (Foxit PDF Reader-dan olan tapşırıqlar)
print("\n\n\nExercises from Part 2")

#Task 1 - İstifadəçi gediləcək yolu və maşının 100 kilometr üçün neçə litrbenzin işlətdiyini daxil edir. Gediləcək yol üçün lazım olan benzinmiqdarını və onun qiymətini hesablayan proqram yazın. (benzin 1 litr-0.90 azn)

print("\n\n1. The user enters the distance and liters of gasoline that the car uses for 100km. Write a program that calculates the amount of gasoline and its price.(1l gasoline is 0.90AZN) ")

d="distance_of_the_way_to_go"
l="liters_of_gasoline_for_100_km"
a="the_amount_of_gasoline_for_the_distane_that_user_needs_to_go"
p="the_price_of_the_gasoline_that_the_car_uses_for_the_distane_that_the_user_needs_to_go"

d=float(input("\nEnter the distance of the way to go : "))
l=float(input("Enter the liters of gasoline that car uses for 100 km : "))

a=l*d/100
p=(l*d/100)*0.90

print("\nThe amount of gasoline for the distane that user needs to go : ",a)
print("The price of the gasoline (with manat) that the car uses for the distane that user needs to go : ",p)


#Task 2 - İstifadəçi otağın enini, uzunluğunu və hündürlüyünü daxil edir, otağın divarları üçün neçə kvadrat metr oboy lazım olduğunu hesablayan program yazın.

print("\n2. The user enters the width, length and height of the room. Write a program that calculates how many square meters of wallpaper the user needs for the walls of the room.")

W=float(input("\nEnter the width : "))
L=float(input("Enter the length : "))
H=float(input("Enter the height : "))

The_total_surface_area_of_the_room=2*(W*L+W*H+L*H)

print("\nSquare meters of wallpaper the user needs for the walls of the room : ",The_total_surface_area_of_the_room)


#Task 3 - Hər bir otaq üçün, 1 zibil qabı, 1şkaf, və 1 televizor almaq lazımdır. İstifadəçi otaqların sayını daxil edir. Cəmi neçə zibil qabı, neçə şkaf və neçə televizor almaq lazım olduğunu hesablayan program yazın.

print("\n3. For each room, you need to buy 1 bin, 1 wardrobe and 1 TV. The user enters the number of rooms. Write the programme that calculates the sum of bins, wardrobes and TVs.")

Rooms=int(input("\nEnter the number of rooms  : "))

The_number_of_bins_and_wardrobes_and_TVs=3*Rooms

print("\nThe number of bins, wardrobes and TVs : ",The_number_of_bins_and_wardrobes_and_TVs)


#Task 4 - İstifadəçi kitabın cəmi səhifə sayını və hər gün oxuyacağı səhifənin sayını daxil edir. Kitabın neçə gün sonra bitəcəyini hesablayan program yazın.

print("\n4. The user enters the number of pages of the book and the number of pages he will read daily. Write a program that calculates how many days the book will end.")

b="the_number_of_pages_of_the_book"
n="the_number_of_pages_of_the_book_the_user_will_read"
e="the_number_of_days_the_book_will_end"

b=int(input("\nEnter the number of pages of the book  : "))
n=int(input("Enter the number of pages you will read daily : "))

e=b/n

print("\nThe number of days the book will end : ",e)


#Task 5 - Mystatda, hər
# 12 bal ---- 5 qızıl
# 11 bal ---- 4 qızıl
# 10 bal ---- 3 qızıl
# 9 bal ---- 2 qızıl
# 8 bal ---- 1 qızıl ilə qiymətləndirilir. İstifadəçi 12,11,10,9,8 ballarının sayını daxil edir. İstifadəçinin neçə qızılı olduğunu hesablayan program yazın.

print("\n5. In Mystat,\t 12 points ---- 5 golds\n\t\t\t\b 11 points ---- 4 golds \n\t\t\t\b 10 points ---- 3 golds\n\t\t\b    9 points ---- 2 golds\n\t\t\b    8 points ---- 1 golds \n\n   The user enters the number of points 12,11,10,9,8. Write a program that calculates how much gold a user has.")

a="number_of_12_points"
b="number_of_11_points"
c="number_of_10_points"
d="number_of_9_points"
e="number_of_8_points"
s="sum_of_golds"

a=int(input("\nEnter the number of 12 points : "))
b=int(input("Enter the number of 11 points : "))
c=int(input("Enter the number of 10 points : "))
d=int(input("Enter the number of 9 points : "))
e=int(input("Enter the number of 8 points : "))

s=5*a+4*b+3*c+2*d+1*e

print("\n  The sum of golds that user has : ",s)
