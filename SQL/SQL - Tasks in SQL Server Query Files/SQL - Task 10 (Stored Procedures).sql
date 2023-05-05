CREATE DATABASE Library;
GO
USE [Library];
GO
/****** Object:  Table [dbo].[Authors]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Authors](
	[Id] [int] NOT NULL,
	[FirstName] [nvarchar](15) NOT NULL,
	[LastName] [nvarchar](25) NOT NULL,
 CONSTRAINT [PK_Authors] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Books]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Books](
	[Id] [int] NOT NULL,
	[Name] [nvarchar](100) NOT NULL,
	[Pages] [int] NOT NULL,
	[YearPress] [int] NOT NULL,
	[Id_Themes] [int] NOT NULL,
	[Id_Category] [int] NOT NULL,
	[Id_Author] [int] NOT NULL,
	[Id_Press] [int] NOT NULL,
	[Comment] [nvarchar](50) NULL,
	[Quantity] [int] NOT NULL,
 CONSTRAINT [PK_Books] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Categories]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Categories](
	[Id] [int] NOT NULL,
	[Name] [nvarchar](30) NOT NULL,
 CONSTRAINT [PK_Categories] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Departments]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Departments](
	[Id] [int] NOT NULL,
	[Name] [nvarchar](40) NOT NULL,
 CONSTRAINT [PK_Departments] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Faculties]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Faculties](
	[Id] [int] NOT NULL,
	[Name] [nvarchar](20) NOT NULL,
 CONSTRAINT [PK_Faculties] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Groups]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Groups](
	[Id] [int] NOT NULL,
	[Name] [nvarchar](10) NOT NULL,
	[Id_Faculty] [int] NOT NULL,
 CONSTRAINT [PK_Groups] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Libs]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Libs](
	[Id] [int] NOT NULL,
	[FirstName] [nvarchar](15) NOT NULL,
	[LastName] [nvarchar](25) NOT NULL,
 CONSTRAINT [PK_Libs] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Press]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Press](
	[Id] [int] NOT NULL,
	[Name] [nvarchar](30) NOT NULL,
 CONSTRAINT [PK_Press] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[S_Cards]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[S_Cards](
	[Id] [int] NOT NULL,
	[Id_Student] [int] NOT NULL,
	[Id_Book] [int] NOT NULL,
	[DateOut] [datetime] NOT NULL,
	[DateIn] [datetime] NULL,
	[Id_Lib] [int] NOT NULL,
 CONSTRAINT [PK_S_Cards] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Students]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Students](
	[Id] [int] NOT NULL,
	[FirstName] [nvarchar](15) NOT NULL,
	[LastName] [nvarchar](25) NOT NULL,
	[Id_Group] [int] NOT NULL,
	[Term] [int] NOT NULL,
 CONSTRAINT [PK_Students] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[T_Cards]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[T_Cards](
	[Id] [int] NOT NULL,
	[Id_Teacher] [int] NOT NULL,
	[Id_Book] [int] NOT NULL,
	[DateOut] [datetime] NOT NULL,
	[DateIn] [datetime] NULL,
	[Id_Lib] [int] NOT NULL,
 CONSTRAINT [PK_T_Cards] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Teachers]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Teachers](
	[Id] [int] NOT NULL,
	[FirstName] [nvarchar](15) NOT NULL,
	[LastName] [nvarchar](25) NOT NULL,
	[Id_Dep] [int] NOT NULL,
 CONSTRAINT [PK_Teachers] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Themes]    Script Date: 14.12.2015 12:36:05 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Themes](
	[Id] [int] NOT NULL,
	[Name] [nvarchar](30) NOT NULL,
 CONSTRAINT [PK_Themes] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (10, N'Aleksandr', N'Matrosov')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (5, N'Alexey ', N'Arkhangelsky')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (4, N'Boris ', N'Carpov')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (6, N'Vladimir ', N'Korol')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (1, N'James R. ', N'Groff')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (7, N'Evangelos ', N'Petrusos')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (12, N'Kevin ', N'Reichard')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (11, N'Ludmila', N'Omelchenko')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (14, N'Mark ', N'Braun')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (8, N'Markus', N'Herhager')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (3, N'Michael ', N'Marows')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (13, N'Olga ', N'Kokoreva')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (9, N'Pavel', N'Garbar')
INSERT [dbo]. [Authors] ([Id], [FirstName], [LastName]) VALUES (2, N'Sergey ', N'Nikolsky')
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (1, N'SQL', 816, 2001, 1, 1, 1, 2, N'2nd edition', 4)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (2, N'3D Studio Max 3', 640, 2000, 3, 6, 3, 3, N'Training course', 5)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (3, N'100 components of the general purpose library Delphi 5', 272, 1999, 2, 4, 5, 4, N'Components', 2)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (4, N'Visual Basic 6', 416, 2000, 2, 5, 4, 3, N'Special reference book', 1)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (5, N'Course of mathematical analysis', 328, 1990, 4, 2, 2, 5, N'Volume 1', 2)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (6, N'C ++ Builder 5: 70 library of information input / output components', 288, 2000, 2, 3, 5, 4, N'Components', 1)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (7, N'Integrated Development Environment', 272, 2000, 2, 3, 5, 4, N'Development environment', 2)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (8, N'Help for Delphi 5 and Object Pascal', 32, 2000, 2, 4, 5, 4, N'Directory', 1)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (9, N'Visual Basic 6.0 for Application', 488, 2000, 2, 5, 6, 6, N'Directory', 3)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (10, N'Visual Basic 6', 576, 2000, 2, 5, 7, 2, N'Developer`s guide 1-st volume', 1)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (11, N'Mathcad 2000', 416, 2000, 5, 7, 8, 2, N'Complete Guide', 1)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (12, N'Novell GroupWise 5.5 e-mail and collaboration system', 480, 2000, 6, 8, 9, 2, N'Network Packages', 2)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (13, N'Windows 2000 registry', 352, 2000, 9, 12, 13, 2, N'A guide for professionals', 4)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (14, N'Unix directory', 384, 1999, 9, 13, 12, 3, N'Reference Guide', 0)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (15, N'Self-Teaching Visual FoxPro 6.0', 512, 1999, 1, 11, 11, 2, N'Self-Teaching', 1)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (16, N'Self-Teaching FrontPage 2000', 512, 1999, 7, 10, 11, 2, N'Self-Teaching', 1)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (17, N'Self-Teaching Perl', 432, 2000, 2, 9, 10, 2, N'Self-Teaching', 2)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (18, N'HTML 3.2', 1040, 2000, 7, 14, 14, 2, N'Guide', 5)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (19, N'Data base', 256, 1996, 1, 1, 4, 4, NULL, 1)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (20, N'WCF, Part 1', 250, 2010, 1, 1, 4, 2, NULL, 4)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (21, N'WCF, Part 2', 250, 2010, 1, 1, 4, 2, NULL, 4)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (22, N'WCF, Part 3', 250, 2010, 1, 1, 4, 2, NULL, 4)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (101, N'SQL server part 1', 105, 2010, 1, 1, 4, 3, N'Part 1', 1)
INSERT [dbo].[Books] ([Id], [Name], [Pages], [YearPress], [Id_Themes], [Id_Category], [Id_Author], [Id_Press], [Comment], [Quantity]) VALUES (102, N'SQL server part 2', 115, 2010, 1, 1, 4, 3, N'Part 2', 4)
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (1, N'SQL Language')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (2, N'Mathematical Analysis')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (3, N'C ++ Builder ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (4, N'Delphi ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (5, N'Visual Basic ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (6, N'3D Studio Max ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (7, N'Mathcad ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (8, N'Novell ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (9, N'Perl ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (10, N'FrontPage ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (11, N'Visual FoxPro ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (12, N'Windows 2000 ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (13, N'Unix ')
INSERT [dbo]. [Categories] ([Id], [Name]) VALUES (14, N'HTML ')
INSERT [dbo]. [Departments] ([Id], [Name]) VALUES (1, N'Programmerstva ')
INSERT [dbo]. [Departments] ([Id], [Name]) VALUES (2, N'Graphics and Designs')
INSERT [dbo]. [Departments] ([Id], [Name]) VALUES (3, N'Iron and Administration')
INSERT [dbo]. [Faculties] ([Id], [Name]) VALUES (1, N'Programming ')
INSERT [dbo]. [Faculties] ([Id], [Name]) VALUES (2, N'Web Design')
INSERT [dbo]. [Faculties] ([Id], [Name]) VALUES (3, N'Administrations')
INSERT [dbo]. [Groups] ([Id], [Name], [Id_Faculty]) VALUES (2, N'9P1 ', 1)
INSERT [dbo]. [Groups] ([Id], [Name], [Id_Faculty]) VALUES (3, N'9P2 ', 1)
INSERT [dbo]. [Groups] ([Id], [Name], [Id_Faculty]) VALUES (4, N'9A ', 3)
INSERT [dbo]. [Groups] ([Id], [Name], [Id_Faculty]) VALUES (5, N'9D ', 2)
INSERT [dbo]. [Groups] ([Id], [Name], [Id_Faculty]) VALUES (6, N'14A ', 3)
INSERT [dbo]. [Groups] ([Id], [Name], [Id_Faculty]) VALUES (7, N'19P1 ', 1)
INSERT [dbo]. [Groups] ([Id], [Name], [Id_Faculty]) VALUES (8, N'18P2 ', 1)
INSERT [dbo]. [Groups] ([Id], [Name], [Id_Faculty]) VALUES (9, N'18A ', 3)
INSERT [dbo]. [Groups] ([Id], [Name], [Id_Faculty]) VALUES (10, N'19D ', 2)
INSERT [dbo]. [Libs] ([Id], [FirstName], [LastName]) VALUES (1, N'Sergey ', N'Maksimenko')
INSERT [dbo]. [Libs] ([Id], [FirstName], [LastName]) VALUES (2, N'Dmitry ', N'Chebotarev')
INSERT [dbo]. [Press] ([Id], [Name]) VALUES (1, N'DiaSoft ')
INSERT [dbo]. [Press] ([Id], [Name]) VALUES (2, N'BHV ')
INSERT [dbo]. [Press] ([Id], [Name]) VALUES (3, N'Piter')
INSERT [dbo]. [Press] ([Id], [Name]) VALUES (4, N'Binom ')
INSERT [dbo]. [Press] ([Id], [Name]) VALUES (5, N'Nauka')
INSERT [dbo]. [Press] ([Id], [Name]) VALUES (6, N'Kudits-Image')
INSERT [dbo]. [Press] ([Id], [Name]) VALUES (7, N'Dialectics')
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (1, 2, 1, CAST(N'2001-05-17 00:00:00.000' AS DateTime), CAST(N'2001-06-12 00:00:00.000' AS DateTime), 1)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (2, 17, 18, CAST(N'2000-05-18 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (3, 6, 3, CAST(N'2001-04-21 00:00:00.000' AS DateTime), NULL, 2)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (4, 21, 4, CAST(N'2001-03-26 00:00:00.000' AS DateTime), NULL, 2)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (5, 3, 1, CAST(N'2000-05-07 00:00:00.000' AS DateTime), CAST(N'2001-04-12 00:00:00.000' AS DateTime), 1)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (6, 7, 11, CAST(N'2001-06-02 00:00:00.000' AS DateTime), NULL, 2)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (7, 16, 14, CAST(N'2001-04-05 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (8, 11, 6, CAST(N'2001-05-05 00:00:00.000' AS DateTime), CAST(N'2002-12-11 00:00:00.000' AS DateTime), 2)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (9, 17, 2, CAST(N'2001-10-01 00:00:00.000' AS DateTime), NULL, 2)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (10, 10, 13, CAST(N'2001-05-05 00:00:00.000' AS DateTime), CAST(N'2002-12-11 00:00:00.000' AS DateTime), 1)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (11, 16, 11, CAST(N'2001-05-05 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (12, 2, 2, CAST(N'1900-01-01 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (99, 5, 14, CAST(N'1900-01-01 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo].[S_Cards] ([Id], [Id_Student], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (101, 5, 4, CAST(N'1900-01-01 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (2, N'Vyacheslav ', N'Zesik', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (3, N'Olga ', N'Mantulyak', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (4, N'Olga ', N'Hrenova', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (5, N'Olga ', N'Medvedeva', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (6, N'Galina ', N'Inashchenko', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (7, N'Jury ', N'Minaev', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (8, N'Jury ', N'Domovesov', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (9, N'Russland ', N'Yarmolovich', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (10, N'Igor ', N'Udovik', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (11, N'Petr ', N'Katsevich', 8, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (12, N'Eugenius', N'Burcev', 3, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (13, N'Flora ', N'Pobirskaya', 3, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (14, N'Atalya ', N'Gridina', 3, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (15, N'Elena ', N'Akusova', 3, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (16, N'Svetlana ', N'Gorshkov', 9, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (17, N'Alexander', N'Lyubenko ', 10, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (18, N'Eugenia ', N'Cymbalyuk', 10, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (19, N'Olga ', N'Bolyachevskaya', 5, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (20, N'Stanislav ', N'Pleshakov', 7, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (21, N'Elena ', N'Taran', 4, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (22, N'Denis ', N'Rogachevsky', 6, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (23, N'Oksana ', N'Tihonova', 6, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (24, N'Petr ', N'Maximov', 3, 2)
INSERT [dbo]. [Students] ([Id], [FirstName], [LastName], [Id_Group], [Term]) VALUES (25, N'Iryna ', N'Stogneeva', 5, 2)
INSERT [dbo].[T_Cards] ([Id], [Id_Teacher], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (1, 2, 13, CAST(N'2000-01-01 00:00:00.000' AS DateTime), CAST(N'2001-07-04 00:00:00.000' AS DateTime), 1)
INSERT [dbo].[T_Cards] ([Id], [Id_Teacher], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (2, 10, 2, CAST(N'2000-03-03 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo].[T_Cards] ([Id], [Id_Teacher], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (3, 6, 12, CAST(N'2000-06-04 00:00:00.000' AS DateTime), NULL, 2)
INSERT [dbo].[T_Cards] ([Id], [Id_Teacher], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (4, 3, 1, CAST(N'2000-09-05 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo].[T_Cards] ([Id], [Id_Teacher], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (5, 8, 8, CAST(N'2000-05-05 00:00:00.000' AS DateTime), NULL, 2)
INSERT [dbo].[T_Cards] ([Id], [Id_Teacher], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (6, 5, 18, CAST(N'2001-02-02 00:00:00.000' AS DateTime), NULL, 2)
INSERT [dbo].[T_Cards] ([Id], [Id_Teacher], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (7, 12, 17, CAST(N'2001-03-04 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo].[T_Cards] ([Id], [Id_Teacher], [Id_Book], [DateOut], [DateIn], [Id_Lib]) VALUES (8, 4, 18, CAST(N'2000-07-02 00:00:00.000' AS DateTime), NULL, 1)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (1, N'Grigory ', N'Jashchuk', 1)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (2, N'Alex', N'Tumanov ', 1)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (3, N'Sergey ', N'Maksimenko', 2)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (4, N'Dmitry', N'Borovsky', 2)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (5, N'Victor ', N'Brovar', 2)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (6, N'Vadim ', N'Tkachenko', 3)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (7, N'Vyacheslav ', N'Kalashnikov', 3)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (8, N'Ruslan ', N'Kucherenko', 1)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (9, N'Andrey', N'Tendyuk', 1)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (10, N'Anatoly ', N'Vyklyuk', 2)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (11, N'Oleg ', N'Reznichenko', 3)
INSERT [dbo]. [Teachers] ([Id], [FirstName], [LastName], [Id_Dep]) VALUES (12, N'Alexander', N'Artemov ', 1)
INSERT [dbo]. [Themes] ([Id], [Name]) VALUES (1, N'Bases of data ')
INSERT [dbo]. [Themes] ([Id], [Name]) VALUES (2, N'Programming')
INSERT [dbo]. [Themes] ([Id], [Name]) VALUES (3, N'Graphic Packages')
INSERT [dbo]. [Themes] ([Id], [Name]) VALUES (4, N'High Mathematics')
INSERT [dbo]. [Themes] ([Id], [Name]) VALUES (5, N'Mathematical Packages')
INSERT [dbo]. [Themes] ([Id], [Name]) VALUES (6, N'Networks')
INSERT [dbo]. [Themes] ([Id], [Name]) VALUES (7, N'Web-design')
INSERT [dbo]. [Themes] ([Id], [Name]) VALUES (8, N'Windows 2000 ')
INSERT [dbo]. [Themes] ([Id], [Name]) VALUES (9, N'operating systems')
ALTER TABLE [dbo].[Books]  WITH CHECK ADD  CONSTRAINT [FK_Books_Author] FOREIGN KEY([Id_Author])
REFERENCES [dbo].[Authors] ([Id])
GO
ALTER TABLE [dbo].[Books] CHECK CONSTRAINT [FK_Books_Author]
GO
ALTER TABLE [dbo].[Books]  WITH CHECK ADD  CONSTRAINT [FK_Books_Category] FOREIGN KEY([Id_Category])
REFERENCES [dbo].[Categories] ([Id])
GO
ALTER TABLE [dbo].[Books] CHECK CONSTRAINT [FK_Books_Category]
GO
ALTER TABLE [dbo].[Books]  WITH CHECK ADD  CONSTRAINT [FK_Books_Press] FOREIGN KEY([Id_Press])
REFERENCES [dbo].[Press] ([Id])
GO
ALTER TABLE [dbo].[Books] CHECK CONSTRAINT [FK_Books_Press]
GO
ALTER TABLE [dbo].[Books]  WITH CHECK ADD  CONSTRAINT [FK_Books_Theme] FOREIGN KEY([Id_Themes])
REFERENCES [dbo].[Themes] ([Id])
GO
ALTER TABLE [dbo].[Books] CHECK CONSTRAINT [FK_Books_Theme]
GO
ALTER TABLE [dbo].[Groups]  WITH CHECK ADD  CONSTRAINT [FK_Groups_Faculty] FOREIGN KEY([Id_Faculty])
REFERENCES [dbo].[Faculties] ([Id])
GO
ALTER TABLE [dbo].[Groups] CHECK CONSTRAINT [FK_Groups_Faculty]
GO
ALTER TABLE [dbo].[S_Cards]  WITH CHECK ADD  CONSTRAINT [FK_S_Cards_Book] FOREIGN KEY([Id_Book])
REFERENCES [dbo].[Books] ([Id])
GO
ALTER TABLE [dbo].[S_Cards] CHECK CONSTRAINT [FK_S_Cards_Book]
GO
ALTER TABLE [dbo].[S_Cards]  WITH CHECK ADD  CONSTRAINT [FK_S_Cards_Lib] FOREIGN KEY([Id_Lib])
REFERENCES [dbo].[Libs] ([Id])
GO
ALTER TABLE [dbo].[S_Cards] CHECK CONSTRAINT [FK_S_Cards_Lib]
GO
ALTER TABLE [dbo].[S_Cards]  WITH CHECK ADD  CONSTRAINT [FK_S_Cards_Stud] FOREIGN KEY([Id_Student])
REFERENCES [dbo].[Students] ([Id])
GO
ALTER TABLE [dbo].[S_Cards] CHECK CONSTRAINT [FK_S_Cards_Stud]
GO
ALTER TABLE [dbo].[Students]  WITH CHECK ADD  CONSTRAINT [FK_Students_Group] FOREIGN KEY([Id_Group])
REFERENCES [dbo].[Groups] ([Id])
GO
ALTER TABLE [dbo].[Students] CHECK CONSTRAINT [FK_Students_Group]
GO
ALTER TABLE [dbo].[T_Cards]  WITH CHECK ADD  CONSTRAINT [FK_T_Cards_Book] FOREIGN KEY([Id_Book])
REFERENCES [dbo].[Books] ([Id])
GO
ALTER TABLE [dbo].[T_Cards] CHECK CONSTRAINT [FK_T_Cards_Book]
GO
ALTER TABLE [dbo].[T_Cards]  WITH CHECK ADD  CONSTRAINT [FK_T_Cards_Lib] FOREIGN KEY([Id_Lib])
REFERENCES [dbo].[Libs] ([Id])
GO
ALTER TABLE [dbo].[T_Cards] CHECK CONSTRAINT [FK_T_Cards_Lib]
GO
ALTER TABLE [dbo].[T_Cards]  WITH CHECK ADD  CONSTRAINT [FK_T_Cards_Teacher] FOREIGN KEY([Id_Teacher])
REFERENCES [dbo].[Teachers] ([Id])
GO
ALTER TABLE [dbo].[T_Cards] CHECK CONSTRAINT [FK_T_Cards_Teacher]
GO
ALTER TABLE [dbo].[Teachers]  WITH CHECK ADD  CONSTRAINT [FK_Teachers_Dep] FOREIGN KEY([Id_Dep])
REFERENCES [dbo].[Departments] ([Id])
GO
ALTER TABLE [dbo].[Teachers] CHECK CONSTRAINT [FK_Teachers_Dep]
GO

--
--
-- Functions Tasks
--
--

-- EN SON TARIXDE GOTURULEN KITABIN ADINI QAYTAR  -  SCALAR
GO
CREATE FUNCTION GetLastDatePickedBookTitle()
RETURNS NVARCHAR(MAX)
AS 
BEGIN
	
	DECLARE @title NVARCHAR(MAX)

	SELECT TOP(1) @title = BD.[Name]
	FROM(
		SELECT 
			B.[Name],
			S.DateOut
		FROM 
			Books AS B
				INNER JOIN S_Cards AS S ON S.Id_Book = B.Id
		UNION 
			ALL
		SELECT 
			B.[Name],
			T.DateOut
		FROM 
			Books AS B
				INNER JOIN T_Cards AS T ON T.Id_Book = B.Id) AS BD
		ORDER BY
			BD.DateOut DESC

	RETURN @title	
END
GO
DECLARE @book_title NVARCHAR(MAX)
EXECUTE @book_title = GetLastDatePickedBookTitle
PRINT('EN SON TARIXDE GOTURULEN KITABIN ADI : ' + @book_title)


-- GONDERILEN CATEGORIYAYA UYGUN OLAN KITABLAR VE MUELLIFLERI - TABLE RETURN
GO
CREATE FUNCTION GetTableOfBooksAndAuthorsByCategory
(@category_id AS INT)
RETURNS TABLE
AS
RETURN(
	SELECT
		A.FirstName + ' ' + A.LastName AS "Author",
		B.[Name] AS "Book Title"
 	FROM 
		Books AS B
			INNER JOIN Authors AS A ON A.Id = B.Id_Author
	WHERE 
		B.Id_Category = @category_id
)
GO
SELECT * FROM GetTableOfBooksAndAuthorsByCategory(1)

-- EN CHOX GOTURULEN KITABIN MUELLIFLERINI GOSTERIN ILK 10 NEFER - TABLE
-- Her bir kitabin bu databasede 1 muellifi oldugu ucun ve
-- en cox goturulen kitablarin goturulme sayi eyni oldugu ucun 
-- en cox goturulen kitablarin muelliflerini table seklinde qaytardim

GO
CREATE FUNCTION GetFirst10Bestsellers()
RETURNS TABLE
AS
RETURN(
	SELECT 
		A.FirstName + ' ' + A.LastName AS "Bestseller Author"
	FROM 
		Authors AS A
			INNER JOIN Books AS B ON B.Id_Author = A.Id
	WHERE 
		B.Id IN (
		SELECT
			BI.Id AS "Book ID"
		FROM
			(SELECT 
					B.Id
			FROM 
				Books AS B
					INNER JOIN S_Cards AS S ON S.Id_Book = B.Id
			UNION 
				ALL
			SELECT 
				B.Id
			FROM 
				Books AS B
					INNER JOIN T_Cards AS T ON T.Id_Book = B.Id) AS BI
		GROUP BY
			BI.Id
		HAVING COUNT(BI.Id) =
		(
			SELECT
				W.[Taken Book Count]
			FROM
			(
				SELECT TOP(1)
					TopBI.[Taken Book Count] ,
					TopBI.[Book ID]
				FROM (
					SELECT
						BI.Id AS "Book ID",
						COUNT(BI.Id) AS "Taken Book Count"
					FROM
						(SELECT 
							B.Id
						FROM 
							Books AS B
								INNER JOIN S_Cards AS S ON S.Id_Book = B.Id
						UNION 
							ALL
						SELECT 
							B.Id
						FROM 
							Books AS B
								INNER JOIN T_Cards AS T ON T.Id_Book = B.Id
						) AS BI
					GROUP BY
						BI.Id
					) AS TopBI
				ORDER BY 
					TopBI.[Taken Book Count] 
					DESC
			) AS W
		)
	)
)
GO
SELECT * FROM GetFirst10Bestsellers()