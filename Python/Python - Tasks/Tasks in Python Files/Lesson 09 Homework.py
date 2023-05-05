#Task 1 - Sətirdəki bütün saitləri sayan program yazın.( A E İ O U).

#Əgər istifadəçi boşluq daxil edərsə və yaxud sözün daxilində hərf, durğu işarələri olarsa, proqram istifadfəçini yeni söz yazmasını istəyir.

print("\n1. Write a program that counts all the vowels in a line. (A E İ O U).")


counter=0

def vowelCounter(word):
    global counter
    for x in (word):
        if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U"):
            counter+=1
    return counter\

word=input("\nEnter the word : ")

while True:
    if(word.isalpha()==False):
         word=input("\nEnter the word, which not includes other things (such as spaces,punctuations,digits) : ")    
    else:
        break

result=vowelCounter(word)

if (result==1):
    print("\nThere is",counter,"vowel in the word \"",word,"\".")
elif (result==0):
    print("\nThere is no vowel in the word \"",word,"\".")
else:
    print("\nThere are",counter,"vowels in the word \"",word,"\".")

  
print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 2 - Sətirdəki bütün samitləri sayan program yazın.

#Əgər istifadəçi boşluq daxil edərsə və yaxud sözün daxilində hərf olarsa, proqramlar istifadfəçini yeni söz yazmasını istəyir.

#Method 1

print("\n2. Write a program that counts all the consonants in a word.")
print("\nMethod 1")
counter=0

def vowelCounter(word):
    global counter
    for x in (word):
        if(x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U"):
            counter+=1
    return counter

word=input("\nEnter the word : ")

while True:
    if(word.isalpha()==False):
         word=input("\nEnter the word, which not includes other things (such as spaces,punctuations,digits) : ")    
    else:
        break

result=len(word)-vowelCounter(word)

if (result==1):
    print("\nThere is",result,"consonant in the word \"",word,"\".")
elif (result==0):
    print("\nThere is no consonant in the word \"",word,"\".")
else:
    print("\nThere are",result,"consonants in the word \"",word,"\".")


#Method 2

print("\n\nMethod 2")

counter=0

def consonantCounter(word):
    global counter
    for x in (word):
        if(x!="a" and x!="e" and x!="i" and x!="o" and x!="u" and x!="A" and x!="E" and x!="I" and x!="O" and x!="U"):
            counter+=1
    return counter

word=input("\nEnter the word : ")

while True:
    if(word.isalpha()==False):
         word=input("\nEnter the word, which not includes other things (such as spaces,punctuations,digits) : ")    
    else:
        break

result=consonantCounter(word)

if (result==1):
    print("\nThere is",counter,"consonant in the word \"",word,"\".")
elif (result==0):
    print("\nThere is no consonant in the word \"",word,"\".")
else:
    print("\nThere are",counter,"consonants in the word \"",word,"\".")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 3 - Sətri PigLatin edən funksiya yazın.(Piglatin meselen :Food =>oodfay , Fun=>unfay setri kichik edir ve ilk herfi sona kechirir ve sona ay sozunu elave edir)

#Sözün içində başqa bir böyük hərfin olmasını, rəqəm və ya boşluq daxil edilməsini də nəzərə almışam.

print("\n3. Write the function that translates the word into PigLatin. (Piglatin, for example: Food => oodfay, Fun => unfay makes the word lowercase and ends the first letter and adds the word \"ay\" to the end)")

def getPigLatinForm(word):
    a=word[0]
    b=word[1:]
    d=str(b.lower())
    c=str(a.lower())
    result=d+c+"ay"
    return result

word=input("\nEnter the word : ")

while True:
    if(len(word.strip())==0):
         word=input("\nEnter the word, not space : ")
    elif(word.isalpha()==False):
         word=input("\nEnter the word, which not includes digit : ")    
    else:
        break

result=getPigLatinForm(word)

print("\nIf you change the word \"",word,"\" into PigLatin, you get \"",result,"\".")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 4 - Funksiya sətirdəki boşluqları müəyyən simvolla əvəzləsin. (Simvolu istifadəçi funksiyaya göndərir)

print("\n4. Let the function replace the spaces in the line with a certain symbol. (The user sends the symbol to the function)")

def replaceSpaceWith(line,symbol):
       return line.replace(" ",symbol)
       

line=input("\nEnter a line with spaces and words : ")
symbol=input("\nEnter the symbol that you want replace with spaces : ")
result=replaceSpaceWith(line,symbol)
print("\nThat is what the line looks like when you add \"",symbol,"\" to the spaces : ",result)


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 5 - Sətir str1 sətir str2-nin suffixi olub olmadığını yoxlayan funksiya yazın.("sa","salam")

#Suffix - son şəkilçi.

#Hər iki ehtimalı - string 1-in string 2-nin suffixi olmasını və tam tərsini string 2-in string 1-nin suffixi olmasını nəzərə aldım.

print("\n5. Write a function that checks whether string1 is a suffix for string 2. (\"he\", \"hello\")")

def isSuffix(str1,str2):
    if (len(str1)>len(str2)):
        if (str1.endswith(str2)) is True:
            return True
        return False
    elif (len(str1)<len(str2)):
        if (str2.endswith(str1) is True):
            return True
        return False


str1=input("\nEnter the first string : ")
str2=input("\nEnter the second string : ")

while True:
    if(str1.isalpha()==False):
         str1=input("\nEnter the first string again, which not includes other things (such as spaces,punctuations,digits) : ")    
    if(str2.isalpha()==False):
         str2=input("\nEnter the second string again, which not includes other things (such as spaces,punctuations,digits) : ")
    else:    
        break

result=isSuffix(str1,str2)


if (len(str1)>len(str2)):
    if (result==True):
        print("\nThe string ""\"",str2,"\" is the suffix of the string \"",str1,"\".")
    if (result==False):
        print("\nThe string ""\"",str2,"\" is not the suffix of the string \"",str1,"\".")
elif (len(str1)<len(str2)):
    if (result==True):
        print("\nThe string ""\"",str1,"\" is the suffix of the string \"",str2,"\".")
    if (result==False):
        print("\nThe string ""\"",str1,"\" is not the suffix of the string \"",str2,"\".")


print("\n\n------------------------------------------------------------------------------------------------------------------------")



#Task 6 -  Sətir str sətir str2-nin prefixi olub olmadığını tapan funksiya yazın.

#Prefix - ön şəkilçi.

#Hər iki ehtimalı - string 1-in string 2-nin prefixi olmasını və tam tərsini string 2-in string 1-nin prefixi olmasını nəzərə aldım.

print("\n5. Write a function that checks whether string1 is a suffix for string 2. (\"he\", \"hello\")")

def isPrefix(str1,str2):
    if (len(str1)>len(str2)):
        if (str1.startswith(str2)) is True:
            return True
        return False
    elif (len(str1)<len(str2)):
        if (str2.startswith(str1) is True):
            return True
        return False


str1=input("\nEnter the first string : ")
str2=input("\nEnter the second string : ")

while True:
    if(str1.isalpha()==False):
         str1=input("\nEnter the first string again, which not includes other things (such as spaces,punctuations,digits) : ")    
    if(str2.isalpha()==False):
         str2=input("\nEnter the second string again, which not includes other things (such as spaces,punctuations,digits) : ")
    else:    
        break

result=isPrefix(str1,str2)


if (len(str1)>len(str2)):
    if (result==True):
        print("\nThe string ""\"",str2,"\" is the prefix of the string \"",str1,"\".")
    if (result==False):
        print("\nThe string ""\"",str2,"\" is not the prefix of the string \"",str1,"\".")
elif (len(str1)<len(str2)):
    if (result==True):
        print("\nThe string ""\"",str1,"\" is the prefix of the string \"",str2,"\".")
    if (result==False):
        print("\nThe string ""\"",str1,"\" is not the prefix of the string \"",str2,"\".")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 7 - Sətirin polindrom olub olmadığını yoxlayan funskiya yazın.

print("\n7. Write a function that checks whether the string is a palindrome.")

def palindrome(string):
    global string1
    if(len(string)%2==0):
        string1=string.lower()
        a=len(string1)/2
        b=string1[:int(a)]
        c=string1[int(a):]
        d=c[::-1]
        if (b==d):
            return True
        return False
    else:
        string1=string.lower()
        x=len(string1)//2
        y=string1[int(x)+1:]
        u=string1[:int(x)]
        e=u[::-1]
        if (e==y):
            return True
        return False

string=input("\nEnter the string to check : ")
while True:
    if(string.isalpha() is False):
         string=input("\nEnter the word, which not includes other things (such as spaces,punctuations,digits) : ")    
    else:
         break

result=palindrome(string)

if (result==True):
    print("\nThe string \"",string1,"\" is a Palindrome.")
else:
    print("\nThe string \"",string1,"\" is not a Palindrome.")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 8 -  -The- sözünün cümlədə neçə dəfə olduğunu tapan funksiya yazın.

print("\n8. Type a function that finds how many times the word \"The\" is in the sentence.")

def findThe (sentence):
    sentence2=sentence.lower()   #"The"-nin istənilən yazılma forması üçün.("THe","The","the","tHE","thE","THE")
    return sentence2.count("the")

sentence=input("\nEnter the sentence : ")
result=findThe(sentence)
numberOfWords=len(sentence.split())

if (numberOfWords > 1): #If it is a sentence
    if (result > 1):
        print("\nThere are",result,"times the word \"the\" in the sentence.")
    elif (result == 1):
        print("\nThere is 1 word \"the\" in the sentence.")
    else:
        print("\nThere is no word \"the\" in the sentence.")
else:  #If it is not a sentence
    if (result == 1):
        print("\nThere is 1 word \"the\".")
    else:
        print("\nThere is no word \"the\".")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 9 - Cümlədə ən çox hansı hərfin işləndiyini tapan funksiya yazın.

print("\n9. Write a function that finds out which letter is used the most in the sentence.")

def findTheMostUsedLetter(sentence):
    max=0
    letter=""
    for l in sentence:
        counter=sentence.count(l)
        if (counter > max):
            max=counter
            letter=l
    return letter

sentence=input("\nEnter the sentence : ")

while True:
    if (len(sentence)<=2):
        sentence=input("Enter the sentence or word that includes letters more than 2 : ")
    else:
        break
result=findTheMostUsedLetter(sentence)

print("\nThe most used letter is \"",result,"\".")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 10 - Cümlədəki ən uzun sözü tapan funksiya yazın.(split lazim ola biler)

#print("\n10. Write the function that finds the longest word in the sentence.")


def theLongestWord(sentence):
    max=0
    word=""
    a=list_of_words=sentence.split()    
    for x in a:
        counter=len(x)
        if (counter > max):
            max=counter
            word=x
    return word

sentence=input("\nEnter the sentence : ")
result=theLongestWord(sentence)
print("\nThe longest word in the sentence is \"",result,"\".")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


#Task 11 - Cümlədəki ən kiçik sözü tapan funksiya tapın(split lazim ola biler)

print("\n11. Write the function that finds the shortest word in the sentence.")

def theShortestWord(sentence):
    min=0
    word=""
    a=list_of_words=sentence.split()   
    for x in a:
        if (x.strip==0):
            continue
            counter=len(x)
            if (counter < min):
                min=counter
                word=x
        return word


sentence=input("\nEnter the sentence : ")
result=theShortestWord(sentence)
print("\nThe shortest word in the sentence is \"",result,"\".")


print("\n\n------------------------------------------------------------------------------------------------------------------------")


