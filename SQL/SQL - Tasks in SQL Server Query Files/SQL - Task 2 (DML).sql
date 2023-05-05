CREATE DATABASE AcademyDB2
GO
USE AcademyDB2
GO
CREATE TABLE Departments(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Financing]	MONEY NOT NULL DEFAULT 0,
[Name] NVARCHAR(100) NOT NULL,

CONSTRAINT CK_Departments_Financing CHECK([Financing] > 0),
CONSTRAINT CK_Departments_Name CHECK([Name] != ''),
CONSTRAINT UQ_Departments_Name UNIQUE([Name])
)
GO
CREATE TABLE Faculties(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Dean] NVARCHAR(MAX) NOT NULL,
[Name] NVARCHAR(100) NOT NULL,

CONSTRAINT CK_Faculties_Dean CHECK([Dean] != ''),
CONSTRAINT CK_Faculties_Name CHECK([Name] != ''),
CONSTRAINT UQ_Faculties_Name UNIQUE([Name])
)
GO
CREATE TABLE Groups(
[Id] INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
[Name] NVARCHAR(100) NOT NULL,
[Rating] INT NOT NULL,
[Year] INT NOT NULL,

CONSTRAINT CK_Groups_Name CHECK([Name] != ''),
CONSTRAINT UQ_Groups_Name UNIQUE([Name]),
CONSTRAINT CK_Groups_Rating Check([Rating] >= 0 AND [Rating] <= 5),
CONSTRAINT CK_Groups_Year Check([Year] >= 1 AND [Year] <= 5),
)
GO 
CREATE TABLE Teachers(
[Id] INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
[EmploymentDate] DATE NOT NULL,
[IsAssistant] BIT NOT NULL DEFAULT 0,
[IsProfessor] BIT NOT NULL DEFAULT 0,
[Name] NVARCHAR(MAX) NOT NULL,
[Position] NVARCHAR(MAX) NOT NULL,
[Premium] MONEY NOT NULL DEFAULT 0, 
[Salary] MONEY NOT NULL,
[Surname] NVARCHAR(MAX) NOT NULL,

CONSTRAINT CK_Teacher_EmploymentDate CHECK([EmploymentDate] > '01.01.1990'),
CONSTRAINT CK_Teacher_Name CHECK([Name] != ''),
CONSTRAINT CK_Teacher_Position CHECK([Position] != ''),
CONSTRAINT CK_Teacher_Premium CHECK([Premium] >= 0),
CONSTRAINT CK_Teacher_Salary CHECK([Salary] > 0),
CONSTRAINT CK_Teacher_Surname CHECK([Surname] != ''),
CONSTRAINT CK_Teacher_IsAssistant CHECK([IsAssistant] IN (0,1)),
CONSTRAINT CK_Teacher_IsProfessor CHECK([IsProfessor] IN (0,1)),
)

INSERT INTO Departments([Financing], [Name])
VALUES (13000,'Asset Management'),
	   (9000,'Business Development'),
	   (24000,'Creative Services'),
	   (53000,'Engineering'),
	   (3000,'General Management'),
	   (16000,'Technology'),
	   (13500,'Board Of Directors'),
	   (137000,'Investor Relations')

INSERT INTO Teachers([EmploymentDate],[IsAssistant],[IsProfessor],[Name],[Position],[Premium],[Salary],[Surname])
VALUES ('1999-7-7', 1, 0,'Urielle','Teaching assistant',200,1100,'Connor'),
	   ('2002-5-5', 0, 1,'Hector','Groundskeeper',100,1000,'Stafford'),
	   ('2010-4-4', 0, 1,'Damian','Teaching assistant',50,1500,'Burns'),
	   ('1998-12-12', 1, 0,'Katelyn','Sports coach',600,1010,'Washington'),
	   ('2006-2-5', 0, 1,'Patricia','Academic coordinator',500,1200,'James'),
	   ('1992-1-2', 1, 0,'Max','Sports coach',100,600,'Maxli'),
	   ('2005-6-2', 1, 0,'John','Academic coordinator',600,400,'Johnlu')

INSERT INTO GROUPS ([Name],[Rating],[Year])
VALUES ('FBES3212',5,2),
	   ('ASDJ1234',2,1),
	   ('FDHJ5632',1,5),
	   ('DJHD9832',2,3),
	   ('AOHD3452',2,5),
	   ('DSKJ5527',0,4),
	   ('HJDF6543',3,5)

INSERT INTO Faculties ([Dean],[Name])
VALUES ('Ina','Computer Science'),
	   ('Gannon','Math'),
	   ('Lila','Genetics and Microbiology'),
	   ('Sutton','Science'),
	   ('Raven','Ecology and Evolutionary Biology'),
	   ('Craig','English'),
	   ('Rivera','History')

--1. Print departments table but arrange its fields in the reverse order.
SELECT [Surname],[Salary],[Premium],[Position],[Name],[IsProfessor],[IsAssistant],[EmploymentDate],[Id]
FROM Teachers

--2. Print group names and their ratings using “Group Name” 
--and “Group Rating”, respectively, as names of the fields.
SELECT [Name] AS "Group Name",
	   [Rating] AS "Group Rating"
FROM GROUPS

----3. Print for the teachers their surname, percentage of wage rate 
----to premium ratio and percentage of wage rate to the salary ratio 
----(the amount of wage rate and premium).
--???

--4. Print the faculty table as a single field in the following format: 
--"The dean of faculty [faculty] is [dean]".
SELECT 'The dean of faculty ' + [Name]+ ' is ' + [Dean] FROM Faculties

--5. Identify names of the teachers who are professors and whose 
--wage rate exceeds 1050.
SELECT [Name]
FROM Teachers
WHERE [IsProfessor] = 1 AND [Salary] > 1050

--6. Print names of the departments whose funding is less than 
--11,000 or more than 25,000.
Select [Name]
FROM Departments
WHERE [Financing] < 11000 OR [Financing] > 25000

--7. Print names of faculties other than Computer Science.
SELECT [Name]
FROM Faculties
WHERE [NAME] <> 'Computer Science'	

--8. Print names and positions of teachers who are not professors.
SELECT [Name] AS "Name of Teacher",
       [Position] AS Position
FROM Teachers
WHERE [IsProfessor] = 0

--9. Print surnames, positions, wage rates, and premia of assistants 
--whose premium is in the range from 160 to 550.
SELECT [Surname] AS Surname,
	   [Position] AS Position,
	   [Salary] as Salary,
	   [Premium] as Premium
FROM Teachers AS T
WHERE [T].Premium BETWEEN 160 AND 550

--10.Print surnames and wage rates of assistants.
SELECT [Surname] AS Surname,
	   [Salary] AS Salary
FROM Teachers AS T 
WHERE T.IsAssistant = 1

--11.Print surnames and positions of the teachers who were hired 
--before 01.01.2000.
SELECT [Surname] AS Surname,
	   [Position] AS Position
FROM Teachers
WHERE [EmploymentDate] < '01.01.2000'

--12.Print names of the departments in alphabetical order up 
--to  the  Software Development Department. The output field 
--should be named "Name of Department".
SELECT [Name] AS "Name of Department"
FROM Departments
ORDER BY [Name]

--13.Print names of the assistants whose salary (amount of wage 
--rate and premium) is not more than 1200.
SELECT [Name]
FROM Teachers
WHERE [Salary] + [Premium] <=1200

--14.Print names of groups of the 5th year whose rating is in the range 
--from 2 to 4.
SELECT [Name]
FROM Groups
WHERE [Year] = 5 AND [Rating] BETWEEN 2 AND 4

--15.Print names of assistants whose wage rate is less than 550 or 
--premium is less than 200.
SELECT [Name] 
FROM Teachers
WHERE [IsAssistant] = 1 AND ([Salary] < 550 OR [Premium] < 200)