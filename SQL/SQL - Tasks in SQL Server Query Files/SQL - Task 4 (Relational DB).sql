create database University
go
use	 University

create table Curators
(
	[Id] int primary key identity(1,1) not null,
	[Name] nvarchar(20) not null,
	[Surname] nvarchar(25) not null,
	check([Name]!=null),
	check([Surname]!=null)
)

create table Faculties
(
	[Id]int primary key identity(1,1) not null,
	[Financing] money default(0) not null,
	check([Financing]>0),
	[Name]nvarchar(100) not null,
	unique([Name]),
	check([Name]!=null)
)

create table Departments
(
	[Id] int primary key identity(1,1) not null,
	unique(Id),
	[Financing] money default(0) not null,
	check([Financing]>0),
	[Name] nvarchar(100) not null,
	check([Name]!=null),
	unique([Name]),
	[FacultyId] int foreign key references Faculties(Id) not null
)

create table Groups
(
	[Id]int primary key identity(1,1) not null,
	[Name]nvarchar(50) not null,
	unique([Name]),
	check([Name]!=null),
	[Year] int not null,
	check([Year]>0 and [Year]<6),
	[DepartmentId]int foreign key references Departments(Id) not null
)

create table GroupsCurators
(
	[Id] int primary key identity(1,1) not null,
	[CuratorId]int foreign key references Curators(Id) not null,
	[GroupId]int foreign key references Groups(Id) not null,
)

create table Subjects
(
	[Id]int primary key identity (1,1) not null,
	[Name]nvarchar(100) not null,
	check([Name]!=null),
	unique([Name])
)

create table Teachers
(
	[Id]int primary key identity(1,1) not null,
	[Name]nvarchar(max) not null,
	check([Name]!=null),
	[Salary]money not null,
	check([Salary]>0),
	[Surname]nvarchar(max) not null,
	check([Surname]!=null)
)

create table Lectures
(
	[Id]int primary key identity(1,1) not null,
	[ClassRoom]nvarchar(max) not null,
	check([ClassRoom]!=null),
	[SubjectId]int foreign key references Subjects(Id) not null,
	[TeacherId]int foreign key references Teachers(Id) not null
)

create table GroupsLectures(
   [Id] int primary key identity(1,1) not null,
   [GroupId]int foreign key references Groups(Id) not null,
   [LectureId] int foreign key references Lectures(Id) not null
)

insert into Curators([Name],[Surname])
Values('Veli','Veliyev'),
('Aysel','Sukurova'),
('Ayxan','Memmedov')

insert into Faculties([Name],[Financing])
Values('It',1000),
('Programming',1500),
('Design',900)

insert into Departments([Name],[Financing],[FacultyId])
Values('Insan Huquqlari',4200,1),
('tedris Sobesi',600,2)

insert into Teachers([Name],[Surname],[Salary])
Values('Elvin','Camalzade', 1200),
('Tural','Novruzov',1000),
('Ismayil','Hesimov',1000)

insert into Groups([Name],[Year],[DepartmentId])
values('3212',3,1),('1225',4,2),('6745',4,2)

insert into Subjects([Name])
values('C#'),('C++'),('JavaScript'),('Python')

insert into Lectures([ClassRoom],[SubjectId],[TeacherId])
Values('A',2,1),('B',1,3),('C',3,2),('D',4,1)

insert into GroupsCurators([CuratorId],[GroupId])
values(1,2),(2,1),(1,1),(2,2),(3,1),(3,1)

insert into GroupsLectures([GroupId],[LectureId])
values(2,3),(1,4),(3,2),(1,1)


--1. Print all possible pairs of lines of teachers and groups.
SELECT
	 T.[Name] + ' ' + T.[Surname] AS "Teacher Fullname",
	 G.[Name] AS "Group Name"
FROM
	 Teachers AS T, 
	 Lectures AS L,
	 GroupsLectures AS GL, 
	 Groups AS G
WHERE 
	 T.[Id] = L.[TeacherId] AND
	 L.[Id] = GL.[LectureId] AND
     GL.[GroupId] = G.[Id]


--2. Print names of faculties, where financing fund of departments 
--exceeds financing fund of the faculty.
SELECT
	F.[Name] AS "Faculty Name"
FROM 
	Faculties AS F,
	Departments AS D
WHERE
	D.[FacultyId] = F.[Id] AND
	D.[Financing] > F.[Financing]

	
--3. Print names of the group curators and groups names they are 
--supervising.
SELECT 
	C.[Name] + C.[Surname] AS "Curator Fullname",
	G.[Name] AS "Group Name"
FROM
	Curators AS C,
	Groups AS G,
	GroupsCurators AS GC
WHERE GC.CuratorId = C.Id AND
	  GC.GroupId = G.Id


--4. Print names of the teachers who deliver lectures in the group 
--"P107". P107 databasede olmadigi ucun evezine 3212 yazdim 
SELECT 
	T.[Name] AS "Teacher Name",
	G.[Name] AS "Group Name",
	L.[ClassRoom] AS "Classroom"
FROM 
	Teachers AS T,
	Lectures AS L,
	GroupsLectures AS GL,
	Groups AS G
WHERE 
	T.[Id] = L.[TeacherId] AND
	L.[Id] = GL.[LectureId] AND
	GL.[GroupId] = G.[Id] AND
	G.[Name] = '3212'


--5. Print names of the teachers and names of the faculties where 
--they are lecturing.
SELECT 
	T.[Name] AS "Teacher Name",
	F.[Name] AS "Faculty Name",
	L.[ClassRoom] AS "Classroom"
FROM 
	Teachers AS T,
	Lectures AS L,
	GroupsLectures AS GL,
	Groups AS G,
	Departments AS D,
	Faculties AS F
WHERE
	T.[Id] = L.[TeacherId] AND
	L.[Id] = GL.[LectureId] AND
	GL.[GroupId] = G.[Id] AND
	G.[DepartmentId] = D.[Id] AND
	D.[FacultyId] = F.[Id]


--6. Print names of the departments and names of the groups that 
--relate to them.
SELECT 
	D.[Name] AS "Department Name",
	G.[Name] AS "Group Name"
FROM
	Departments AS D,
	Groups AS G
WHERE 
	G.DepartmentId = D.Id


--7. Print names of the subjects that the teacher "Samantha Adams" 
--teaches. "Samantha Adams" olmadigin ucun Elvin yazdim
SELECT 
	T.[Name] AS "Teacher Name",
	S.[Name] As "Subject Name"
FROM 
	Teachers AS T,
	Lectures AS L,
	Subjects AS S
WHERE
	L.[SubjectId] = S.[Id] AND
    L.[TeacherId] = T.[Id] AND	
	T.[Name] = 'Elvin'


--8. Print names of the departments, where "Database Theory" 
--is taught. "Database Theory" evezine Programming yazdim
SELECT 
	D.[Name] AS "Department Name",
	F.[Name] AS "Faculty Name"
FROM
	Departments AS D,
	Faculties AS F
WHERE 
	D.[FacultyId] = F.[Id] AND
	F.[Name] = 'Programming'


--9. Print names of the groups that belong to the "Computer Science" faculty.
--"Computer Science" evezine Programming yazdim
SELECT  
	G.[Name] AS "Group Name",
	F.[Name] AS "Faculty Name"
FROM 
	Groups AS G,
	Departments AS D,
	Faculties AS F
WHERE 
	G.[DepartmentId] = D.[Id] AND
	D.[FacultyId] = F.[Id] AND 
	F.[Name] = 'Programming'

--10. Print names of the 5th year groups, as well as names of the faculties to which they relate
--5 olmadigi ucun 3 yazdim
SELECT  
	G.[Name] AS "Group Name",
	G.[Year] AS "Year",
	F.[Name] AS "Faculty Name"
FROM 
	Groups AS G,
	Departments AS D,
	Faculties AS F
WHERE 
	G.[DepartmentId] = D.[Id] AND
	D.[FacultyId] = F.[Id] AND 
	G.[Year] = 3


--11. Print full names of the teachers and lectures they deliver (names 
--of subjects and groups), and select only those lectures that are 
--delivered in the classroom "B103". "B103" olmadigi ucun evezine A yazdim
SELECT 
	T.[Name] + ' ' + T.[Surname] AS "Teacher Fullname",
	G.[Name] AS "Group Name",
	S.[Name] AS "Subject Name",
	L.[ClassRoom] AS "Classroom"
FROM 
	Teachers AS T,
	Lectures AS L,
	GroupsLectures AS GL,
	Groups AS G,
	Subjects AS S	
WHERE 
	T.[Id] = L.[TeacherId] AND
	L.[Id] = GL.[LectureId] AND
	GL.[GroupId] = G.[Id] AND
	L.[SubjectId] = S.[Id] AND
	L.[ClassRoom] = 'A'