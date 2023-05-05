#Task 1 - Əsl rəqəmlər o rəqəmlərdir ki bölənlərinin cəmi (rəqəmin özünü bölən kimi hesablamırıq) özünə bərabər olsun. Əsl rəqəmləri tapan funksiya yazın. Ola bilər ki sizə funksiya lazım olsun.

print("1. Real numbers are those numbers whose sum (we do not count the number as a divisor) is equal to itself. Write the function that finds the perfect numbers. You may need a function.")

#Perfect numbers : 6,28,496,8128

def perfect_number_finder(num):
    sum=0
    for x in range(1,num):
        if(num%x==0):
            sum+=x
    if(sum==num):
        return True
    return False

num=int(input("\nEnter a number : "))

if(perfect_number_finder(num) is True):
    print("\nThe number",num,"is Perfect number.")
else:
    print("\nThe number",num,"is not Perfect number.")


#Task 2 - 36 arasında rəqəm qəbul edən, və buna uyğun kartı ekrana çıxaran funskiya yazın.

print("\n\n2. Type a function that accepts a number between 36 and displays the corresponding card.")

def appointSymbol(card_no):
    if(card_no>=1 and card_no<=9):
        print("Ürək")
    elif(card_no>=10 and card_no<=18):
        print("Xaç")
    elif(card_no>=19 and card_no<=27):
        print("Kərpic")
    elif(card_no>=28 and card_no<=36):
        print("Pika")

def showCart(number):
    appointSymbol(number)
    result=number%9
    if(result==1):
        print("6")
    elif(result==2):
        print("7")
    elif(result==3):
        print("8")
    elif(result==4):
        print("9")
    elif(result==5):
        print("10")
    elif(result==6):
        print("Valent")
    elif(result==7):
        print("Dama")
    elif(result==8):
        print("Karol")
    elif(result==0):
        print("Tuz")
    

showCart(12)

#Task 3 - Verilən rəqəmi müəyyən dəqiqliyə qədər yuvarlaqlaşdıran funksiya yazın. (Funksiya iki parametr qəbul edir, birinci parametr rəqəm, ikinci parametr isə vergüldən sonra neçə rəqəm qalmalıdır)

#First Program

print("\n\n3. Round-off a number to a given number of significant digits.(First Program)") 

def roundNumber(num1,num2):
    product=1
    for i in range(num2):
        product*=10
    num1=num1*product
    num1=int(num1)
    num1=num1/product
    return num1

result=roundNumber(15.123456,2)
print(result)

#Second Program

#round() özü funksiyadır? 

print("\n\n3. Round-off a number to a given number of significant digits.(Second Program)") 

fraction=float(input("\nEnter the fraction : "))
numberOfDecimals=int(input("Enter the number of decimals : "))
result=round(fraction,numberOfDecimals)

print("\nIf you round",fraction,"",numberOfDecimals," decimal places you will get",result,".")


#Task 4 - Rəqəmin xoşbəxt olub olmadığını tapan funksiya yazın. (Xoşbəxt rəqəm ilk 3 rəqəmin cəmi son 3 rəqəmin cəminə bərabər olmalıdır)

print("\n\n4. Write a function that finds whether the number is happy.")


def isHappy(num):
    if(num<100):
        num=int(input("Enter another number : "))
    sumL3=num%10+(num//10)%10+(num//100)%10
    while (num>999):
        num=num//10
    if(num>=100 and num<=999):
        sumF3=num%10+(num//10)%10+(num//100)%10
        if(sumF3==sumL3):
            print("\nNumber is Happy.")
        else:
            print("\nNumber is not Happy.")

num=int(input("\nEnter a number : "))
isHappy(num)   


#Task 5 - İki tarix qəbul edən və bu tarixlər arasındakı fərqi tapan funksiya yazın. Bu funksiyanı yazarkən ilin uzun və ya qısa olduğunu tapan funksiyanı da yazmalısınız.

print("\n\n5. Write a function that finds the difference between two dates.")

from datetime import date

date_one = date(2020, 3, 2)
date_two = date(2022, 6, 4)

difference = date_two - date_one

print(difference)


#Task 6 - Göndərilən massivin ədədi ortasını tapan funksiya yazın.

print("\n\n 6. Write a function that finds the arithmetic mean of the sent array.")

def arithmeticMean(*args):
    sum=0
    for x in (args):
        sum+=x
        def no_of_argu(*args):
            return(len(args))
    arithmeticM=sum/len(args)
    return arithmeticM

result=arithmeticMean(1,2,3,4,5,6,7,8,9,10)
print("\nArithmetic mean of the numbers is",result)
 

#Task 9 -  Göndərilən massivi əksinə çevirən funksiya yazın.

print("\n\n9. Reverse a list array.")


def reverse(*args):
    newArgs=args[::-1]
    return newArgs

print(reverse(12,23,12,23,121,13,41))


