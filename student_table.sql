BEGIN TRANSACTION;
CREATE TABLE Student(
    roll_no INTEGER PRIMARY KEY,
    name TEXT(20),
    city TEXT(20),
    age INTEGER, course TEXT);
INSERT INTO "Student" VALUES(1,'Amit','Navsari',20,'BCA');
INSERT INTO "Student" VALUES(2,'Bhavin','Surat',21,'BBA');
INSERT INTO "Student" VALUES(3,'Chirag','Navsari',19,'BCA');
INSERT INTO "Student" VALUES(4,'Divya','Vyara',20,'BBA');
INSERT INTO "Student" VALUES(5,'Esha','Navsari',22,'BCA');
INSERT INTO "Student" VALUES(6,'Farhan','Surat',21,'BBA');
INSERT INTO "Student" VALUES(7,'Gita','Navsari',20,'BBA');
INSERT INTO "Student" VALUES(8,'Harsh','Bardoli',19,'BBA');
INSERT INTO "Student" VALUES(9,'Isha','Navsari',21,'BCA');
INSERT INTO "Student" VALUES(10,'Jay','Valsad',20,'BBA');
CREATE TABLE students(roll no intger primary key, name text,subject1 integer, subject2 integer ,subject3 integer);
INSERT INTO "students" VALUES(1,'Amit',45,60,70);
INSERT INTO "students" VALUES(2,'Bhavin',78,66,54);
INSERT INTO "students" VALUES(3,'Chirag',32,48,59);
INSERT INTO "students" VALUES(4,'Divya',88,91,79);
INSERT INTO "students" VALUES(5,'Esha',55,62,68);
INSERT INTO "students" VALUES(6,'Farhan',67,70,72);
INSERT INTO "students" VALUES(7,'Gita',91,85,90);
INSERT INTO "students" VALUES(8,'Harsh',40,35,44);
INSERT INTO "students" VALUES(9,'Isha',73,77,80);
INSERT INTO "students" VALUES(10,'Jay',60,58,65);
INSERT INTO "students" VALUES(66,'harsh',88,9,77);
CREATE TABLE tblstudent09(rollno int primary key, name text, gender text, marks integer);
INSERT INTO "tblstudent09" VALUES(66,'harsh','male',88);
COMMIT;
