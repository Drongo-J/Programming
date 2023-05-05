CREATE DATABASE Academy
go 
USE Academy
go
CREATE TABLE Curators
(
	[Id]INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
	[Name]NVARCHAR(MAX) NOT NULL,
	CHECK([Name]!=''),
	[Surname]NVARCHAR(MAX) NOT NULL,
	CHECK([Surname]!='')
)

go
CREATE TABLE Faculties
(
	[Id]INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
	[Name]NVARCHAR(100) NOT NULL,
	CHECK([Name]!=''),
	UNIQUE([Name])
)
go
go
CREATE TABLE Departments
(
	[Id]INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	[Building]INT NOT NULL,
	CHECK([Building]>0 AND [Building]<6),
	[Financing]MONEY DEFAULT(0) NOT NULL,
	CHECK([Financing]>0),
	[Name]NVARCHAR(100) NOT NULL,
	CHECK([Name]!=null),
	[FacultyId]INT FOREIGN KEY REFERENCES Faculties(Id) NOT NULL
)
CREATE TABLE Groups
(
	[Id]INT PRIMARY KEY IDENTITY(1,1)NOT NULL,
	[Name]NVARCHAR(100)NOT NULL,
	CHECK([Name]!=''),
	UNIQUE([Name]),
	[Year]INT NOT NULL,
	CHECK([Year]>0 and [Year]<6),
	[DepartmentId]INT FOREIGN KEY REFERENCES Departments(Id)NOT NULL
)
go
CREATE TABLE GroupsCurators
(
	[Id]INT PRIMARY KEY IDENTITY(1,1)NOT NULL,
	[GroupId]INT FOREIGN KEY REFERENCES Groups(Id)NOT NULL,
	[CuratorId]INT FOREIGN KEY REFERENCES Curators(Id)NOT NULL
)
go
CREATE TABLE Teachers
(
	[Id]INT PRIMARY KEY IDENTITY(1,1)NOT NULL,
	[IsProfessor]BIT DEFAULT(0)NOT NULL,
	[Name]NVARCHAR(100)NOT NULL,
	CHECK([Name]!=''),
	[Salary]MONEY NOT NULL,
	CHECK([Salary]>0),
	[Surname]NVARCHAR(100)NOT NULL,
	CHECK([Surname]!='')
)
go
CREATE TABLE Subjects
(
	[Id]INT PRIMARY KEY IDENTITY(1,1)NOT NULL,
	[Name]NVARCHAR(100)NOT NULL,
	CHECK([Name]!=''),
	UNIQUE([Name])
)
go
CREATE TABLE Students
(
	[Id]INT PRIMARY KEY IDENTITY(1,1)NOT NULL,
	[Name]NVARCHAR(MAX)NOT NULL,
	CHECK([Name]!=''),
	[Rating]INT NOT NULL,
	CHECK([Rating]>0 and [Rating]<6),
	[Surname]NVARCHAR(MAX)NOT NULL,
	CHECK([Surname]!='')
)

CREATE TABLE Lectures
(
	[Id]INT PRIMARY KEY IDENTITY(1,1)NOT NULL,
	[Date]DATE NOT NULL,
	[SubjectId]INT FOREIGN KEY REFERENCES Subjects(Id)NOT NULL,
	[TeacherId]INT FOREIGN KEY REFERENCES Teachers(Id)NOT NULL
)
go
CREATE TABLE GroupsStudents
(
	[Id]INT PRIMARY KEY IDENTITY(1,1)NOT NULL,
	[StudetnId]INT FOREIGN KEY REFERENCES Students(Id)NOT NULL,
	[GroupId]INT FOREIGN KEY REFERENCES Groups(Id)NOT NULL
)
go
CREATE TABLE Groupslectures
(
	[Id]INT PRIMARY KEY IDENTITY(1,1)NOT NULL,
	[GroupId]INT FOREIGN KEY REFERENCES Groups(Id)NOT NULL,
	[LectureId]INT FOREIGN KEY REFERENCES Lectures(Id)NOT NULL
)

go

INSERT INTO Teachers([Name],[Surname],[IsProfessor],[Salary])
VALUES
('Omer','Cavanshirli',1,1200),
('Amin','Quliyev',0,1300),
('Sevda','Yahyayeva',1,1216),
('Roya','Ayxan',0,1100)
go
INSERT INTO Curators([Name],[Surname])
VALUES('Zamiq','Huseynov'),('Elton','Meherremov'),('Elnare','Xelilova'),('Sevinc','Adigozelova')
go
INSERT INTO Subjects([Name])
VALUES('C#'),('C++'),('Python'),('Wpf')
go
INSERT INTO Faculties([Name])
VALUES('IT'),('Programming'),('Data Analist')
go
insert into Faculties([Name])
values('Piano'),('Violen'),('Edebiyyat Mellimliyi'),('Riyaziyyat Melliliyi')
go
INSERT INTO Departments([Name],[Building],[Financing],[FacultyId])
VALUES
('Biotibbi Texnologiya Muhendisliyi',1,7500,3)
go
insert into Departments([Name],[Building],Financing,[FacultyId])
values('Music',2,4000,4),('Math',2,4000,5),
('Mellimliy',3,3000,6),('Random Department',3,3000,7)
go
INSERT INTO Groups([Name],[Year],[DepartmentId])
VALUES
('3212',2,1),('4212',3,1),('3344',5,1),('4455',5,1)
go
INSERT INTO GroupsCurators([CuratorId],[GroupId])
VALUES(1,1),(2,2),(3,3),(4,4),(1,3),(2,4)
go
INSERT INTO Lectures([SubjectId],[TeacherId],[Date])
VALUES
(1,1,'2022-10-11'),(2,2,'2022-10-2'),(3,3,'2022-10-3'),
(4,4,'2022-10-4'),(1,3,'2022-10-5'),(2,4,'2022-10-6'),
(3,1,'2022-10-7'),(4,2,'2022-10-9')
go
INSERT INTO Lectures([SubjectId], [TeacherId],[Date])
VALUES
	(4,2,'2022-2-4')

INSERT INTO Lectures([SubjectId],[TeacherId],[Date])
VALUES
(1,4,'2022-10-15')
go
INSERT INTO Students([Name],[Surname],[Rating])
VALUES
('Aygun','Kazimova',3),('Samir','Bagirov',1),
('Faiq','Agayev',4),('Emin','Agalarov',5),
('Sevda','Alekberzade',3),('Namiq','Huseynov',4),
('Kamran','Yaqublu',2),('Cahangir','Esgerov',5),
('Azad','Sabanov',3),('Lela','Babayeva',1)
go

INSERT INTO GroupsStudents([GroupId],[StudetnId])
VALUES (1,1),(1,2),(2,3),(2,4),(3,5),(3,6),(4,7),(4,8),(1,9),(1,10)
go
INSERT INTO Groupslectures([GroupId],[LectureId])
VALUES (1,1),(1,2),(2,3),(2,4),(3,5),(3,6),(4,7),(4,8)
go


--Subqueries


--1. Print numbers of buildings if the total financing fund of the departments located in them exceeds 100,0
SELECT 
	COUNT(*) AS "Number Of Buildings"
FROM 
	(SELECT 
		*
	 FROM 
		Departments AS D
	 WHERE
		D.[Financing] > 100) AS D


----2. Print names of the 5th year groups of the Software Development department 
---- that have more than 10 double periods in the first week. - tablelarda bele bir sey yoxdur

--3. Print names of the groups whose rating (average rating of all 
--students in the group) is greater than the rating of the "D221" 
--group. D221 olmadigin ucun 3212 yazdim
SELECT 
	G.Id,
	G.[Name],
	AVG(S.Rating) AS "Group Average Rating"
FROM 
	Groups AS G,
	Students AS S,
	GroupsStudents AS GS
WHERE 
	GS.GroupId = G.Id AND
	GS.StudetnId = S.Id
GROUP BY
	G.[Id],
	G.[Name]
HAVING AVG(S.Rating) > (
	SELECT 
		AVG(S.Rating)
	FROM 
		Students AS S,
		Groups AS G,
		GroupsStudents AS GS
	WHERE 
		GS.StudetnId = S.Id AND
		GS.GroupId = G.ID AND
		G.[Name] = '3212')


--4. Print full names of teachers whose wage rate is higher than 
--the average wage rate of professors.
SELECT 
	T.[Name] + ' ' + T.Surname AS "Teacher Fullname",
	T.Salary
FROM 
	Teachers AS T
WHERE 
	T.IsProfessor = 0 AND
	T.Salary > (
		SELECT
			AVG(T.Salary)
		FROM 
			Teachers AS T
		WHERE 
			T.IsProfessor = 1)


--5. Print names of groups with more than one curator
SELECT 
	G.Id,
	G.[Name]
FROM 
	Groups AS G
WHERE
	G.Id IN(
		SELECT
			G.Id
		FROM 
			Groups AS G,
			Curators AS C,
			GroupsCurators AS GC
		WHERE 
			GC.CuratorId = C.Id AND
			GC.GroupId = G.Id
		GROUP BY
			G.Id
		HAVING 
			COUNT(G.ID) > 1)


--6. Print names of the groups whose rating (the average rating 
--of all students of the group) is less than the minimum rating 
--of the 5th year groups.
SELECT 
	G.Id,
	G.[Name],
	AVG(S.Rating) AS "Group Average Rating"
FROM 
	Groups AS G,
	Students AS S,
	GroupsStudents AS GS
WHERE 
	GS.GroupId = G.Id AND
	GS.StudetnId = S.Id
GROUP BY
	G.[Id],
	G.[Name]
HAVING AVG(S.Rating) > (
SELECT 
	MIN(S.Rating)
FROM 
	Students AS S,
	GroupsStudents AS GS,
	(SELECT 
		G.Id
	FROM
		Departments AS De,
		Groups AS G
	WHERE
		G.DepartmentId = De.Id AND
		G.[Year] = 5) AS G
WHERE 
	GS.StudetnId = S.Id AND
	GS.GroupId IN (G.Id)
)


--7. Print names of the faculties with total financing fund of the departments
--greater than the total financing fund of the 
--Computer Science department. olmadigi ucun Music yazdim
SELECT 
	D.[Id],
	D.[Name],
	D.[Financing]
FROM 
	Departments AS D
WHERE 
	D.Financing > (
SELECT 
	D.Financing
FROM 
	Departments AS D
WHERE 
	D.[Name] = 'Music')


--8. Print names of the subjects and full names of the teachers who 
--deliver the greatest number of lectures in them.

SELECT    
	S.[Name],T.[Name] 
FROM Teachers AS T,
	 Lectures AS L,
	 Subjects AS S
WHERE 
	L.TeacherId = T.Id AND
	L.SubjectId = S.Id AND
	T.Id=
	(SELECT TOP(1) 
	L.TeacherId
	FROM Teachers AS T,
		 Lectures AS L
	WHERE
		L.TeacherId = L.Id
	GROUP BY
		L.TeacherId
	ORDER BY 
		COUNT(*) DESC)

--9. Print name of the subject in which the least number of lectures 
--are delivered.
SELECT TOP(1) 
	S.[Name] AS "Subject",
	COUNT(S.ID) AS "Count Of Lectures"
FROM 
	Lectures AS L,
	Subjects AS S
WHERE 
	L.SubjectId = S.Id
GROUP BY 
	S.Id,
	S.[Name]
ORDER BY 
	"Count Of Lectures" ASC

--10. Print number of students and subjects taught at the Software 
--Development department. olmadigi ucun Math yazdim

SELECT 
	COUNT(*) 
FROM 
	Students AS S,
	GroupsStudents AS GS,
	Groups AS G,
	Departments AS D,
	Groupslectures AS GL,
	Lectures AS L
WHERE 
	GS.StudetnId = S.Id AND
	GS.GroupId = G.Id AND
	G.Id =DepartmentId AND
	D.[Name] = 'Math' AND
	GL.Id = G.Id AND
	L.Id = Gl.LectureId