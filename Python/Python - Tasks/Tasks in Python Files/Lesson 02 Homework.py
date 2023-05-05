#Task 1 - 1-dən verilmiş ədədə qədər olan ədədlərin cəmini tapın. (Rekursiya ilə)

print("1. Find the sum of the numbers from 1 to the given number. (With recursion)")


def sum(num):
    if (num==0):
        return num
    return sum(num-1)+num

result=sum(5)
print(result)


#Task 2 - Verilmiş ədədə qədər bütün ədədlərin 50 faizini göstərin. (Rekursiya ilə)

print("\n\n2. Display 50 percent of all numbers up to a given number. (With recursion)")
print("50 percent of all numbers: ")

def halfNums(n):
    print(n*0.5)
    if(n==1):
        return 
    halfNums(n-1)

halfNums(6)


#Task 3 - Ədədin qüvvətini tapan rekursiv funksiyanı yazın.

print("\n\n3. Write a recursive function that finds the power of number.")

def findPower(base):
    def exponent(exp):
        return base**exp
    return exponent

three=findPower(3)
print(three(4))


#Task 4 - Verilmiş intervalda bütün ədədlərin cəmini tapan funksiyanı yazın. (Rekursiya ilə)

print("\n\n4. Write a function that finds the sum of all the numbers in the given interval. (With recursion)") 

def sumAll(n1,n2):
    if(n2==n1):
        return n2
    return n2+sumAll(n1,n2-1)

print(sumAll(1,5))
