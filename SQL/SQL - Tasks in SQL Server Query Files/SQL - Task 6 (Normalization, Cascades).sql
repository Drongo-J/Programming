CREATE DATABASE SocialPlatformDB
GO
USE SocialPlatformDB
GO
CREATE TABLE Users(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Fullname] NVARCHAR(MAX) NOT NULL,
[Age] INT NOT NULL
)
GO
CREATE TABLE Posts(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Content] NVARCHAR(MAX) NOT NULL,
[UserId] INT FOREIGN KEY  REFERENCES Users([Id]) NOT NULL
)
GO
CREATE TABLE PostRatings(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Point] INT NOT NULL,
[PostId] INT FOREIGN KEY REFERENCES Posts([Id]) NOT NULL,
[UserId] INT FOREIGN KEY REFERENCES Users([Id]) NOT NULL,
CHECK([Point]>0 AND [Point]<6)
)
GO
CREATE TABLE Comments(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Content] VARCHAR(100) NOT NULL,
[UserId] INT FOREIGN KEY REFERENCES Users([Id]) NOT NULL,
[ParentId] INT FOREIGN KEY REFERENCES Comments([Id]), 
[PostId] INT FOREIGN KEY REFERENCES Posts([Id]) NOT NULL 
)
GO
CREATE TABLE CommentRating(
[Id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
[Point] INT NOT NULL,
[UserId] INT FOREIGN KEY REFERENCES Users([Id]) NOT NULL,
[CommentId] INT FOREIGN KEY REFERENCES Comments([Id]) NOT NULL, 
CHECK([Point]>0 AND [Point]<6)
)
GO
GO
INSERT INTO Users([Fullname],[Age])
VALUES('Nurlan Shirinov',25),
('Mehemmed Bayramov',19),
('Coshqun Gulmemmedov',20),
('Ali Ahmedov',22),
('Alirza Zahidov',17),
('Huseyin Abbasov',16)
GO
INSERT INTO Posts([Content],[UserId])
VALUES
('Great, ',5),
('I love music theme of Howling Fjord, it is so peaceful, filled with ambient elements and sounds of nature, very relaxing.',1),
('In the end if you want to get job done, you have to do it yourself, remember this well.',1),
('I can’t install 7.1 speakers in my room, there is not enough space for it. I believe 5.1 is best option in my case, what you think?',2),
('Is true that humans are social animals in general? Someone said it other day and I was wondering if it was true.',3),
('Do you guys also enjoy intelligent games? Puzzle for example? I admire thinking games.',4),
('I like your motivation, no I really do, but I am afraid it is not enough, you need more to achieve your goals.',5)

GO
INSERT INTO Comments ([Content],[PostId],[UserId],[ParentId])
VALUES('I love it when people have the critical thinking',1,1,NULL),
('Cheaters are destroying online games',2,2,NULL),
('Spammers are so annoying',3,3,NULL),
('I don’t have time for it right now',4,4,NULL),
('My understanding of this subject is really bad',5,5,NULL)

--Child Comments
INSERT INTO Comments ([Content],[PostId],[UserId],[ParentId])
VALUES('I do not like it when people talk about others behind their backs',6,1,2),
	  ('I am not sure',3,2,6),
	  ('Solving Rubik’s cube puzzle with single hand is real talent',4,3,3),
	  ('Which programming language should I learn?',2,4,2),
	  ('Yawn, reading articles is boring',4,5,3),
	  ('Nothing dangerous about it',3,2,2),
	  ('We can fix your problem in couple of seconds',4,3,2),
	  ('I had high hopes for this new crypto coins',1,4,2),
	  ('I can’t stop making mistakes when I’m nervous',1,1,5),
	  ('I mean if you will pay me well enough, I can even sleep in haunted house, no problem.',3,2,4),
	  ('We are two newbies in this game',4,3,2),
	  ('I have seen people doing mind-blowing stunts with snowboard',2,5,5),
	  ('I enjoy classic music so much',2,4,3),
	  ('I feel like I need more time',6,5,2),
	  ('Do you also use old driver?',3,4,5)



GO
INSERT INTO CommentRating([Point],[UserId],[CommentId])
VALUES(1,1,2),
      (2,2,3),
      (3,3,4),
      (4,4,5),
	  (5,4,5),
      (1,1,26),
	  (2,2,27),
	  (3,3,27),
	  (4,4,27),
	  (5,5,28),
	  (1,5,28),
	  (2,1,28),
	  (3,2,29),
	  (4,3,30),
	  (5,4,30),
	  (1,5,30),
	  (2,1,31),
	  (3,2,31)
GO

INSERT INTO PostRatings([Point],[PostId],[UserId])
VALUES(1,1,1),
(2,2,2),
(3,3,3),
(4,4,4),
(5,5,5),
(2,6,1),
(2,6,2),
(2,6,3),
(2,6,3),
(3,7,3),
(4,7,4),
(5,7,2),
(1,7,1)
GO

--1.show users,posts

SELECT 
	*
FROM
	Users AS U
		INNER JOIN 
			Posts AS P ON P.UserId = U.Id
ORDER BY 
	U.Id

--2.her bir postun adi,rating

SELECT 
	P.[Content] AS "Post",
	PR.[Point] AS "Rating"
FROM 
	Posts AS P
		INNER JOIN
			PostRatings AS PR ON P.Id = PR.PostId

--3.her bir commentin alt commentlerini gostermek ve avg gostermek

SELECT
	* 
FROM 
	Comments AS C1
		INNER JOIN 
			Comments AS C2 ON C2.ParentId = C1.Id
ORDER BY 
	C1.Id

--4.Rating ,umumi postlarin avg rating den chox olanlari gostermek

SELECT 
	P.Content, 
	PR.Point 
FROM 
	Posts AS P
		INNER JOIN PostRatings AS PR ON P.Id = PR.PostId
WHERE PR.Point > (
		SELECT 
			AVG(PR.Point)
		FROM 
			Posts AS P
				INNER JOIN PostRatings AS PR ON P.Id = PR.PostId)


--5.Ratingi umumi commentlerin ratingden chox olanlari gostermek

SELECT 
	C.Content, CR.Point 
FROM
	Comments AS C
		INNER JOIN CommentRating AS CR ON CR.CommentId = C.Id
WHERE CR.Point > (
		SELECT  
			AVG(CR.Point)
		FROM
			Comments AS C
				INNER JOIN CommentRating AS CR ON CR.CommentId = C.Id)

--6.en chox postu olan useri gostermek

SELECT 
	* 
FROM 
	Users AS U
WHERE
	U.Id = (
		SELECT TOP(1) 
			 U.Id AS "User ID"
		FROM 
			Users AS U
				INNER JOIN Posts AS P ON U.Id = P.UserId
		GROUP BY
			U.Id
		ORDER BY 
			COUNT(P.Id) DESC)

--7.postunun ratingi en chox olan user i gostermek ve rating

SELECT TOP(1)
	U.Fullname AS "User Fullname",
	P.Id AS "Post ID",
	SUM(PR.Point) AS "Sum of Ratings"
FROM 
	Posts AS P
		INNER JOIN PostRatings AS PR ON P.Id = PR.PostId
			INNER JOIN Users AS U ON U.Id = P.UserId
GROUP BY 
	P.Id,
	U.Fullname
ORDER BY 
	"Sum of Ratings" DESC

