CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    First Name TEXT NOT NULL,
	Last Name TEXT NOT NULL,
	Slack Handle TEXT NOT NULL UNIQUE,
	CohortId INTEGER,
    FOREIGN KEY(CohortId)
    REFERENCES Cohort (Id)
    		ON DELETE CASCADE
        	ON UPDATE NO ACTION
);

CREATE TABLE Instructor (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    First Name TEXT NOT NULL,
	Last Name TEXT NOT NULL,
	Slack Handle TEXT NOT NULL UNIQUE,
	CohortId INTEGER,
	Specialty TEXT NOT NULL,
    FOREIGN KEY(CohortId)
    REFERENCES Cohort (Id)
    		ON DELETE CASCADE
        	ON UPDATE NO ACTION
);

CREATE TABLE Exercise (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
	Language TEXT NOT NULL
);

CREATE TABLE Assignment (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ExerciseId INTEGER,
    StudentId INTEGER,
	FOREIGN KEY(ExerciseId)
    REFERENCES Exercise (Id)
    		ON DELETE CASCADE
        	ON UPDATE NO ACTION,
    FOREIGN KEY(StudentId)
    REFERENCES Student (Id)
    		ON DELETE CASCADE
        	ON UPDATE NO ACTION
);

-- create cohorts
INSERT INTO Cohort (Name) VALUES ('c33');
INSERT INTO Cohort (Name) VALUES ('c34');
INSERT INTO Cohort (Name) VALUES ('c35');

-- create students
INSERT INTO Student (First, Last, Slack, CohortId) VALUES ('Alex','Rumsey', 'Alex', 1);
DELETE FROM Student WHERE first='Alex';
INSERT INTO Student (First, Last, Slack, CohortId) VALUES ('Tyler','C', 'Tyler', 2);
INSERT INTO Student (First, Last, Slack, CohortId) VALUES ('Sam','Birky', 'Sam', 3);
INSERT INTO Student (First, Last, Slack, CohortId) VALUES ('Matthew','M', 'Matty Matt', 3);
INSERT INTO Student (First, Last, Slack, CohortId) VALUES ('Drew','Lalapalooza', 'Lil Drew', 3);
INSERT INTO Student (First, Last, Slack, CohortId) VALUES ('Danny','Barker', 'DB', 1);
INSERT INTO Student (First, Last, Slack, CohortId) VALUES ('Sydney','Noh', 'Syd', 1);
INSERT INTO Student (First, Last, Slack, CohortId) VALUES ('Shane','Name', 'Shane', 3);
INSERT INTO Student (First, Last, Slack, CohortId) VALUES ('Scott','Silver', 'Silver', 2);

-- create instructors
INSERT INTO Instructor (First, Last, Slack, CohortId, Specialty) VALUES ('Maddie', 'Pepper', 'MissPepper', 3, 'JavaScript');
INSERT INTO Instructor (First, Last, Slack, CohortId, Specialty) VALUES ('Mo', 'Silvera', 'MoMo', 1, 'C#');
INSERT INTO Instructor (First, Last, Slack, CohortId, Specialty) VALUES ('Steve', 'Brownlee', 'coach', 2, 'Full Stack');
INSERT INTO Instructor (First, Last, Slack, CohortId, Specialty) VALUES ('Joe', 'Shepherd', 'joe', 2, 'Python');
INSERT INTO Instructor (First, Last, Slack, CohortId, Specialty) VALUES ('Leah', 'Hoefling', 'leah', 1, 'C#');
INSERT INTO Instructor (First, Last, Slack, CohortId, Specialty) VALUES ('Kristen', 'Norris', 'KNorris', 3, 'JavaScript');

-- create exercises
INSERT INTO Exercise (Name, Language) VALUES ('Chicken Monkey', 'JavaScript');
INSERT INTO Exercise (Name, Language) VALUES ('Animal Kennel', 'React');
INSERT INTO Exercise (Name, Language) VALUES ('Kandy Korner', 'React');
INSERT INTO Exercise (Name, Language) VALUES ('StudentExercises', 'SQL');
INSERT INTO Exercise (Name, Language) VALUES ('Keahua Arboretum', 'Python');

-- create student's exercises
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (1,3);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (1,2);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (2,1);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (2,4);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (3,5);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (3,1);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (4,2);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (4,3);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (5,1);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (5,4);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (6,2);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (6,3);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (7,2);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (7,5);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (8,1);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (8,4);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (9,3);
INSERT INTO  Assignment (ExerciseId, StudentId) VALUES (9,5);