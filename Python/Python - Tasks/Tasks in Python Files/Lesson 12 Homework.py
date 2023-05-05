#Sizde universitetde oxuyan telebelerin siyahisi  var.
#students=[]
          #name  surname   group_name    gender age score  speciality
#student1=["tural","Eliyev","group_az_123","male",21,76.5,"Programming"]
#student2=["ali","Memmedov","group_az_234","male",25,100,"IT"]
#student3=["leyla","Eliyeva","group_az_450","female",21,98.5,"IT"]
#student4=["tural","Eliyev","group_az_123","male",18,76.5,"Programming"]
#student5=["nergiz","Orucova","group_az_450","female",20,76.3,"IT"]
#student6=["elshen","Memmedli","group_az_234","male",27,89.2,"Design"]
#student7=["ramiz","Quliyev","group_az_450","male",16,76.5,"Design"]
#student8=["aygun","Semedova","group_az_234","female",29,90.5,"Programming"]
#student9=["murad","Eliyev","group_az_234","male",28,76.1,"IT"]
#student10=["nadir","Nadirli","group_az_123","male",32,76.5,"Programming"]


#Ekrana chixarma uchun normal funksiya yazin
#MAP vs FILTER in istifadesi ile bu melumatlari chixarin
#1.Butun telebelerin ballarindan 10 bal chixin ve neticeni seliqeli shekilde ekrana chixarin
#2.Butun telebelerin adlarinin ilk herfini boyuk herfe chevirib ekrana chixarin
#3.Butun telebelein group adlarinin hamisinin boyuk herflere kechirin ve ekrana chixarin
#4.Adi a herfi ile bashlayan telebeleri ekrana chixarin,
#5.Yalniz qiz telebeleri ekrana chixarin,
#6.Yalniz oglan telebeleri ekrana chixarin,
#7.Ortalamasi 80 den yuxari olanlari chixarin
#8.Ixtisasi Programming olanlari ve yashi 23 den boyuk olanlari ekrana chixarin
#9.group_az_123 bu qrupda olan telebelerin ballarindan 3 bal chixin ekrana chixarin
#10.group_az_450 oxuyan oglan telebeleri ekrana chixarin

#=================================================================================================================================#

#You have a list of students studying at the university.
#students=[]

          #name  surname   group_name    gender age score  speciality
#student1=["tural","Əliyev","group_az_123","male",21,76.5,"Programming"]
#student2=["əli","Məmmədov","group_az_234","male",25,100,"IT"]
#student3=["leyla","Əliyeva","group_az_450","female",21,98.5,"IT"]
#student4=["tural","Əliyev","group_az_123","male",18,76.5,"Programming"]
#student5=["nərgiz","Orucova","group_az_450","female",20,76.3,"IT"]
#student6=["elşən","Məmmədli","group_az_234","male",27,89.2,"Design"]
#student7=["ramiz","Quliyev","group_az_450","male",16,76.5,"Design"]
#student8=["aygün","Səmədova","group_az_234","female",29,90.5,"Programming"]
#student9=["murad","Əliyev","group_az_234","male",28,76.1,"IT"]
#student10=["nadir","Nadirli","group_az_123","male",32,76.5,"Programming"]


student1=["tural","Əliyev","group_az_123","male",21,76.5,"Programming"]
student2=["əli","Məmmədov","group_az_234","male",25,100,"IT"]
student3=["leyla","Əliyeva","group_az_450","female",21,98.5,"IT"]
student4=["aydın","Səlimov","group_az_123","male",18,76.5,"Programming"] #2 dənə eyni şagird xüsusiyyətləri var idi (yaşlarında başqa), 4-cü şagird 1-nin eynisi olduğuna görə adını, soyadını dəyişdim.
student5=["nərgiz","Orucova","group_az_450","female",20,76.3,"IT"]
student6=["elşən","Məmmədli","group_az_234","male",27,89.2,"Design"]
student7=["ramiz","Quliyev","group_az_450","male",16,76.5,"Design"]
student8=["aygün","Səmədova","group_az_234","female",29,90.5,"Programming"]
student9=["murad","Əliyev","group_az_234","male",28,76.1,"IT"]
student10=["nadir","Nadirli","group_az_123","male",32,76.5,"Programming"]

students=[student1,student2,student3,student4,student5,student6,student7,student8,student9,student10]


def line():
    return print("------------------------------------------------------------------------------------------------------------------------")

def s():
    return print()

def printStudents(students):
    print(student1)
    print(student2)
    print(student3)
    print(student4)
    print(student5)
    print(student6)
    print(student7)
    print(student8)
    print(student9)
    print(student10)
    print()
    print()

def printIntroduciton():
    s()
    line()
    print("You have a list of students studying at the university :")
    s()
    printStudents(students)
    line()
    s()
    print("Tasks (Type functions to display them. Extract this informations using MAP and FILTER.):")
    print("1. Subtract 10 points from the scores of all students and display the results neatly.")
    print("2. Turn the first letter of the names of all students into capital letters and display them on the screen.")
    print("3. Convert all students' group names to capital letters and display them.")
    print("4. Display the students whose names begin with the letter \"A\".")
    print("5. Show only girls' informations on the screen.")
    print("6. Show only boys' informations on the screen.") 
    print("7. Show those whose average is above 80.")
    print("8. Display those who are specializing in programming and those who are over 23 years old at the same time.")
    print("9. Subtract 3 points from the students in the group \"group_az_123\" and display them on the screen.")
    print("10. Display male students studying in the group \"group_az_450\".")
    s()
    s()

printIntroduciton()
line()

print("\t\t\t\t\t\t=================")
print("\t\t\t\t\t\t| Task 1 Answer |")
print("\t\t\t\t\t\t=================")
s()
print("1. Subtract 10 points from the scores of all students and display the results neatly.")

def printStudentsAndScores(students):
    for s in students:
        print("   ========================")
        print("   Student :",s[0].capitalize(),s[1])
        print("   Student's score :",s[5])
    print("   ========================")
s()
print("   Students' results before subtracting 10 points :")
s()
printStudentsAndScores(students)

subtract10point=lambda s: s[5]-10
g=list(map(subtract10point,students))

def SubtractionOf10Points():
    y=0
    for x in students:
        x[5]=g[y]
        y+=1

SubtractionOf10Points()

s()
print("   Subtracted 10 point from each students :")
s()
printStudentsAndScores(students)
s()

line()

print("\t\t\t\t\t\t=================")
print("\t\t\t\t\t\t| Task 2 Answer |")
print("\t\t\t\t\t\t=================")
s()
print("2. Turn the first letter of the names of all students into capital letters and display them on the screen.")

studentsNameCapital=lambda s: s[0].capitalize()
names=list(map(studentsNameCapital,students))

def printNames():
    for x in names:
        print(f'   Student name : {x}')
s()
printNames()
s()
line()

print("\t\t\t\t\t\t=================")
print("\t\t\t\t\t\t| Task 3 Answer |")
print("\t\t\t\t\t\t=================")
s()
print("3. Convert all students' group names to capital letters and display them.")
s()

groupNamesCapital=lambda s: s[2].upper()
group_names=list(map(groupNamesCapital,students))

names=[]
for x in students:
    names.append(x[0].capitalize())
surnames=[]
for x in students:
    surnames.append(x[1].capitalize())

y=0
a=1
def printGroupNames():
    global y
    for x in group_names:
        print("   ================================")
        print("   Student :",names[y],surnames[a])
        print("   Group name :",x)
        y+=1
    print("   ================================")

printGroupNames()
s()
line()

print("\t\t\t\t\t\t=================")
print("\t\t\t\t\t\t| Task 4 Answer |")
print("\t\t\t\t\t\t=================")
s()
print("4. Display the students whose names begin with the letter \"A\".")
s()

startsWithALambda=lambda s: s[0][0]=="a" or s[0][0]=="A"

startsWithA=list(filter(startsWithALambda,students))

def printNamesStartsWithA():
    for x in startsWithA:
        print("   ",x[0].capitalize(),x[1],"'s name starts with letter \"A\".")

printNamesStartsWithA()
s()
line()

print("\t\t\t\t\t\t=================")
print("\t\t\t\t\t\t| Task 5 Answer |")
print("\t\t\t\t\t\t=================")
s()
print("5. Show only girls' informations on the screen.")
s()

girlsInfoLambda=lambda s: s[3]=="female"

girlsInfo=list(filter(girlsInfoLambda,students))

def printInfoGirls():
    y=0
    for x in girlsInfo:
        s()
        print("   =========================================")
        s()
        print("   Name of the student :",x[y].capitalize())
        print("   Surnmame of the student :",x[y+1])
        print("   Group name of the student :",x[y+2])
        print("   Gender of the student :",x[y+3].capitalize())
        print("   Age of the student :",x[+4])
        print("   Score of the student :",x[+5])
        print("   Speciality of the student :",x[y+6])
    s()
    print("   =========================================")

printInfoGirls()
s()
line()

print("\t\t\t\t\t\t=================")
print("\t\t\t\t\t\t| Task 6 Answer |")
print("\t\t\t\t\t\t=================")
s()
print("6. Show only boys' informations on the screen.")
s()

boysInfoLambda=lambda s: s[3]=="male"

boysInfo=list(filter(boysInfoLambda,students))

def printInfoBoys():
    y=0
    for x in boysInfo:
        s()
        print("   =========================================")
        s()
        print("   Name of the student :",x[y].capitalize())
        print("   Surnmame of the student :",x[y+1])
        print("   Group name of the student :",x[y+2])
        print("   Gender of the student :",x[y+3].capitalize())
        print("   Age of the student :",x[+4])
        print("   Score of the student :",x[+5])
        print("   Speciality of the student :",x[y+6])
    s()
    print("   =========================================")

printInfoBoys()
s()
line()

print("\t\t\t\t\t\t=================")
print("\t\t\t\t\t\t| Task 7 Answer |")
print("\t\t\t\t\t\t=================")
s()
print("7. Show those whose average is above 80.")
s()


averageOver80Lambda=lambda s: s[5]>80

averageOver80=list(filter(averageOver80Lambda,students))

def printStudentwithScoreOver80():
    for x in averageOver80:
        print("   Students whose average is above 80 :",x[0].capitalize(),x[1])


printStudentwithScoreOver80()
s()
line()

print("\t\t\t\t\t\t=================")
print("\t\t\t\t\t\t| Task 8 Answer |")
print("\t\t\t\t\t\t=================")
s()
print("8. Display those who are specializing in programming and those who are over 23 years old at the same time.")
s()

programmersOverAge23Lambda=lambda s: s[4]>23 and s[6]=="Programming"

programmersOverAge23=list(filter(programmersOverAge23Lambda,students))

def printProgrammersNameOverAge23():
    for x in programmersOverAge23:
        print("   Student who is programmer and over 23 years old :",x[0].capitalize(),x[1])

printProgrammersNameOverAge23()
s()
line()

print("\t\t\t\t\t\t=================")
print("\t\t\t\t\t\t| Task 9 Answer |")
print("\t\t\t\t\t\t=================")
s()
print("9. Subtract 3 points from the students in the group \"group_en_123\" and display them on the screen.")
s()

studentsFromGroup_az_123Lambda=lambda s: s[2]=="group_az_123"

studentsFromGroup_az_123=list(filter(studentsFromGroup_az_123Lambda,students))

studentsFromGroup_az_123ScoreSubtract3Lambda=lambda s: s[5]-3

t=list(map(studentsFromGroup_az_123ScoreSubtract3Lambda,studentsFromGroup_az_123))

def printStudentsFromGroup_az_123AndScores():
    for s in studentsFromGroup_az_123:
        print("   ========================")
        print("   Student :",s[0].capitalize(),s[1])
        print("   Student's score :",s[5])
    print("   ========================")

print("   Students' results before subtracting 3 points :")
s()
printStudentsFromGroup_az_123AndScores()

def SubtractionOf3Points():
    y=0
    for x in studentsFromGroup_az_123:
        x[5]=t[y]
        y+=1

SubtractionOf3Points()
s()
print("   Subtracted 3 point from each students of the \"group_az_123\" :")
s()
printStudentsFromGroup_az_123AndScores()
s()
line()

print("\t\t\t\t\t\t==================")  
print("\t\t\t\t\t\t| Task 10 Answer |")
print("\t\t\t\t\t\t==================")  
s()
print("10. Display male students studying in the group \"group_az_450\".")
s()

boysInGroup_az_450Lambda=lambda s: s[2]=="group_az_450" and s[3]=="male"

boysInGroup_az_450=list(filter(boysInGroup_az_450Lambda,students))

def printBoysInGroup_az_450():
    for x in boysInGroup_az_450:
        print("   Male student studying in the group \"group_az_450\" :",x[0].capitalize(),x[1])

printBoysInGroup_az_450()
s()
line()
