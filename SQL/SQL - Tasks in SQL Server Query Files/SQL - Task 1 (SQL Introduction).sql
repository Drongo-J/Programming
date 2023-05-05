CREATE DATABASE [AcademyDB]

USE AcademyDB

CREATE TABLE Groups(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Name] NVARCHAR(10) NOT NULL,
[Rating] INT NOT NULL,
[Year] INT NOT NULL, 

CONSTRAINT UQ_Groups_Name UNIQUE([Name]),
CONSTRAINT CK_Groups_Name CHECK([Name] != ''),
CONSTRAINT CK_Groups_Rating CHECK([Rating] >= 0 AND [Rating] <= 5),
CONSTRAINT CK_Groups_Year CHECK([Year] >= 1 AND [Year] <= 5)
)

CREATE TABLE Chairs(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Financing] MONEY NOT NULL DEFAULT 0,
[Name] nvarchar(100) NOT NULL,

CONSTRAINT UQ_Chairs_Name UNIQUE([Name]),
CONSTRAINT CK_Chairs_Financing CHECK([Financing] >= 0),
CONSTRAINT CK_Chairs_Name CHECK([Name] != '')
)

CREATE TABLE Faculties(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Name] nvarchar(100) NOT NULL,

CONSTRAINT CK_Faculties_Name CHECK ([Name] != ''),
CONSTRAINT UQ_Faculties_Name UNIQUE([Name])
)

CREATE TABLE Teachers(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[EmploymentDate] DATE NOT NULL,
[Name] NVARCHAR(Max) NOT NULL,
[Premium] MONEY NOT NULL DEFAULT 0,
[Salary] MONEY NOT NULL,
[Surname] NVARCHAR(MAX) NOT NULL,

CONSTRAINT CK_Teachers_EmploymentDate CHECK(EmploymentDate > '1990-01-01'),
CONSTRAINT CK_Teachers_Name CHECK([Name] != ''),
CONSTRAINT CK_Teachers_Premium CHECK([Premium] >= 0),
CONSTRAINT CK_Teachers_Salary CHECK([Salary] > 0),
CONSTRAINT CK_Teachers_Surname CHECK([Surname] != ''),
)