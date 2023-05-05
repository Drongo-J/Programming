use [master];
go

if db_id('UniversityDb') is not null
begin
	drop database [UniversityDb];
end
go

create database [UniversityDb];
go

use [UniversityDb];
go

create table [Assistants]
(
	[Id] int not null identity(1, 1) primary key,
	[TeacherId] int not null
);
go

create table [Curators]
(
	[Id] int not null identity(1, 1) primary key,
	[TeacherId] int not null
);
go

create table [Deans]
(
	[Id] int not null identity(1, 1) primary key,
	[TeacherId] int not null,
);
go

create table [Departments]
(
	[Id] int not null identity(1, 1) primary key,
	[Building] int not null check ([Building] between 1 and 5),
	[Name] nvarchar(100) not null unique check ([Name] <> N''),
	[FacultyId] int not null,
	[HeadId] int not null
);
go

create table [Faculties]
(
	[Id] int not null identity(1, 1) primary key,
	[Building] int not null check ([Building] between 1 and 5),
	[Name] nvarchar(100) not null unique check ([Name] <> N''),
	[DeanId] int not null
);
go

create table [Groups]
(
	[Id] int not null identity(1, 1) primary key,
	[Name] nvarchar(10) not null unique check ([Name] <> N''),
	[Year] int not null check ([Year] between 1 and 5),
	[DepartmentId] int not null
);
go

create table [GroupsCurators]
(
	[Id] int not null identity(1, 1) primary key,
	[CuratorId] int not null,
	[GroupId] int not null
);
go

create table [GroupsLectures]
(
	[Id] int not null identity(1, 1) primary key,
	[GroupId] int not null,
	[LectureId] int not null
);
go

create table [Heads]
(
	[Id] int not null identity(1, 1) primary key,
	[TeacherId] int not null,
);
go

create table [LectureRooms]
(
	[Id] int not null identity(1, 1) primary key,
	[Building] int not null check ([Building] between 1 and 5),
	[Name] nvarchar(10) not null unique check ([Name] <> N'')
);
go

create table [Lectures]
(
	[Id] int not null identity(1, 1) primary key,
	[SubjectId] int not null,
	[TeacherId] int not null
);
go

create table [Schedules]
(
	[Id] int not null identity(1, 1) primary key,
	[Class] int not null check ([Class] between 1 and 8),
	[DayOfWeek] int not null check ([DayOfWeek] between 1 and 7),
	[Week] int not null check ([Week] between 1 and 52),
	[LectureId] int not null,
	[LectureRoomId] int not null
);
go

create table [Subjects]
(
	[Id] int not null identity(1, 1) primary key,
	[Name] nvarchar(100) not null unique check ([Name] <> N'')
);
go

create table [Teachers]
(
	[Id] int not null identity(1, 1) primary key,
	[Name] nvarchar(max) not null check ([Name] <> N''),
	[Surname] nvarchar(max) not null check ([Surname] <> N'')
);
go

alter table [Assistants]
add foreign key ([TeacherId]) references [Teachers]([Id]);
go

alter table [Curators]
add foreign key ([TeacherId]) references [Teachers]([Id]);
go

alter table [Deans]
add foreign key ([TeacherId]) references [Teachers]([Id]);
go

alter table [Departments]
add foreign key ([FacultyId]) references [Faculties]([Id]);
go

alter table [Departments]
add foreign key ([HeadId]) references [Heads]([Id]);
go

alter table [Faculties]
add foreign key ([DeanId]) references [Deans]([Id]);
go

alter table [Groups]
add foreign key ([DepartmentId]) references [Departments]([Id]);
go

alter table [GroupsCurators]
add foreign key ([CuratorId]) references [Curators]([Id]);
go

alter table [GroupsCurators]
add foreign key ([GroupId]) references [Groups]([Id]);
go

alter table [GroupsLectures]
add foreign key ([GroupId]) references [Groups]([Id]);
go

alter table [GroupsLectures]
add foreign key ([LectureId]) references [Lectures]([Id]);
go

alter table [Heads]
add foreign key ([TeacherId]) references [Teachers]([Id]);
go

alter table [Lectures]
add foreign key ([SubjectId]) references [Subjects]([Id]);
go

alter table [Lectures]
add foreign key ([TeacherId]) references [Teachers]([Id]);
go

alter table [Schedules]
add foreign key ([LectureId]) references [Lectures]([Id]);
go

alter table [Schedules]
add foreign key ([LectureRoomId]) references [LectureRooms]([Id]);
go


INSERT INTO Subjects([Name])
VALUES('C#'),('C++'),('JavaScript'),('Kimya'),('Bialogiya'),
('Piano'),('Violence')

INSERT INTO Teachers([Name],[Surname])
VALUES('Omer','Cavanshirli'),('Amin','Quliyev'),
('Elvin','Camalzade'),('Tural','Novruzov')

INSERT INTO Lectures([SubjectId],[TeacherId])
VALUES(1,1),(2,1),(3,1),(4,2),(5,2),(1,3),(3,3),(4,3),(6,4),(7,4),(5,4),(2,2)

INSERT INTO LectureRooms([Name],[Building])
VALUES('A-101',1),('A-102',2),('A-103',3),('A-104',4),('A-105',5)

INSERT INTO Schedules([Class],[DayOfWeek],[Week],[LectureId],[LectureRoomId])
VALUES(1,2,2,1,1),(2,1,3,2,2),(3,3,1,3,3),(4,4,4,4,4),(5,5,2,5,5),
(6,6,1,6,1),(7,1,2,7,2),(8,3,5,8,3),(4,2,5,9,1),(6,2,2,10,5),
(7,5,4,11,2),(5,3,4,12,2)

INSERT INTO Assistants([TeacherId])
VALUES(2),(4)

INSERT INTO Deans([TeacherId])
VALUES(1),(3)

INSERT INTO Curators([TeacherId])
VALUES(1),(2),(4)

INSERT INTO Heads([TeacherId])
VALUES(1)

INSERT INTO Faculties([Name],[DeanId],[Building])
VALUES('Programming',1,2),('Classic Musiqi Aletleri',2,3),('Doctor',1,1)


INSERT INTO Departments([Name],[FacultyId],[HeadId],[Building])
VALUES('Komputer Muhendisliyi',1,1,2),('Biokimya Muhendisliyi',2,1,1),
('Music',3,1,3),('Ituf',1,1,2),('Kimya Muhendisliyi',3,1,1)

INSERT INTO Groups([Name],[Year],[DepartmentId])
VALUES('3212',4,2),('1122',3,3),('4433',2,4),('5544',4,1),('3344',3,1)

INSERT INTO GroupsCurators([GroupId],[CuratorId])
VALUES(1,1),(2,2),(3,3),(4,1),(5,2)

INSERT INTO GroupsLectures([GroupId],[LectureId])
VALUES(1,1),(2,2),(3,3),(4,4),(5,5),(1,6),(2,7),(3,8),(4,9),(5,10),
(1,11),(2,12)

--1. Print names of the classrooms where the teacher "Edward Hopper" lectures.
--"Edward Hopper" --> Amin

SELECT 
	LR.[Name] AS "Classroom name",
	T.[Name] AS "Teacher Name"
FROM 
	Teachers AS T
		INNER JOIN Lectures AS L ON L.TeacherId = T.Id
			INNER JOIN Schedules AS S ON S.LectureId = L.Id
				INNER JOIN LectureRooms AS LR ON LR.Id = S.LectureId
WHERE
	T.[Name] = 'Amin'


--2. Print names of the assistants who deliver lectures for the group
--"F505".
--"F505" --> 3212

SELECT 
	A.Id AS "Assistant ID",
	T.[Name] AS "Assistant Name",
	G.[Name] AS "Group Name"
FROM 
	Assistants AS A
		INNER JOIN Teachers AS T ON A.TeacherId = T.Id
			INNER JOIN Lectures AS L ON T.Id = L.TeacherId
				INNER JOIN GroupsLectures AS GL ON L.Id = GL.LectureId	
					INNER JOIN Groups AS G ON GL.GroupId = G.Id
WHERE 
	G.[Name] = '3212'


--3. Print subjects taught by the teacher "Alex Carmack" for groups
--of the 5th year.
-- 5th year --> 4th year
--"Alex Carmack" --> Elvin

SELECT
	S.[Name] AS "Subject",
	T.[Name] AS "Teacher Name",
	G.[Year] AS "Group Year"
FROM 
	Teachers AS T
		INNER JOIN Lectures AS L ON T.Id = L.TeacherId
			INNER JOIN Subjects AS S ON S.Id = L.SubjectId
				INNER JOIN GroupsLectures AS GL ON L.Id = GL.LectureId
					INNER JOIN Groups AS G ON GL.GroupId = G.Id
WHERE
	G.[Year] = 4 AND
    T.[Name] = 'Elvin'
 	  

--4. Print names of the teachers who do not deliver lectures on
--Mondays.

SELECT
	T.[Name] AS "Teacher Name"
FROM 
	Teachers AS T
		INNER JOIN Lectures AS L ON L.TeacherId = T.Id	
			INNER JOIN Schedules AS S ON S.LectureId = L.Id
WHERE 
	S.[DayOfWeek] <> 1 
GROUP BY
	T.[Name]


--5. Print names of the classrooms, indicating their buildings, in
--which there are no lectures on Wednesday of the second week
--on the third double period.

SELECT DISTINCT
	LR.[Name],
	LR.Building
FROM
	Schedules AS S
		INNER JOIN LectureRooms AS LR ON LR.Id = S.LectureRoomId
WHERE
	S.[Week] = 2 AND	
	S.[DayOfWeek] <> 3
		

--6. Print full names of teachers of the Computer Science faculty,	
--who do not supervise groups of the Software Development department.
--Software Development -> Komputer Muhendisliyi
--Computer Science --> Programming

SELECT
	*
FROM 
	Teachers AS T
		INNER JOIN Curators AS C ON T.Id = C.TeacherId
			INNER JOIN GroupsCurators AS GC ON GC.CuratorId = C.Id
				INNER JOIN Groups AS G ON G.Id = GC.GroupId 
					INNER JOIN Departments AS D ON D.Id = G.DepartmentId 
						INNER JOIN Faculties AS F ON F.Id = D.FacultyId
WHERE 
	F.[Name] = 'Programming' AND
	D.[Name] <> 'Komputer Muhendisliyi'


--7. Print numbers of all buildings that are available in the tables
--of faculties, departments, and classrooms.

SELECT 
	D.Building
FROM 
	Departments AS D
UNION
SELECT 
	F.Building
FROM 
	Faculties AS F
UNION
SELECT 
	LR.Building
FROM 
	LectureRooms AS LR


--8. Print full names of teachers in the following order: deans of
--faculties, heads of departments, teachers, curators, assistants.

SELECT
	T.[Name]
FROM
	Deans AS D
		INNER JOIN Faculties AS F ON F.DeanId = D.Id
			INNER JOIN Teachers	AS T ON T.Id = D.TeacherId
UNION
	ALL
SELECT 
	T.[Name]
FROM 
	Departments AS D 
		INNER JOIN Faculties AS F ON F.Id =D.FacultyId 
			INNER JOIN Deans AS DE ON DE.Id = F.DeanId
				INNER JOIN Teachers AS T ON T.Id = DE.TeacherId
UNION 
	ALL
SELECT 
T.[Name]
FROM 
	Teachers AS T 
UNION 
	ALL 
SELECT
	T.[Name]
FROM 
	Curators AS C
		INNER JOIN Teachers AS T ON C.TeacherId = T.Id
UNION 
	ALL
SELECT
	T.[Name]
FROM
	Assistants AS A
		INNER JOIN Teachers AS T ON A.TeacherId = T.Id
		
		
--9. Print days of the week (without repetitions), in which there are
--classes in the classrooms "A311" and "A104" of the building 6.
--6 --> 2
--"A311" and "A104" --> A-102 AND A-103

SELECT DISTINCT
	S.[DayOfWeek] AS "Day of Week"
FROM 
	Schedules AS S
		INNER JOIN LectureRooms AS LR ON LR.Id = S.LectureRoomId  
WHERE
	LR.Building = 2 AND
	(LR.[Name] = 'A-102' OR
	LR.[Name] = 'A-103')
	
