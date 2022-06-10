--Create db
CREATE DATABASE exercises;

--CREATE TABLE FACILITIES
CREATE TABLE facilities (
    facid integer SERIAL PRIMARY KEY NOT NULL,
    name character varying(100) NOT NULL,
    membercost numeric NOT NULL,
    guestcost numeric NOT NULL,
    initialoutlay numeric NOT NULL,
    monthlymaintenance numeric NOT NULL
);

CREATE TABLE members (
    memid integer SERIAL PRIMARY KEY NOT NULL,
    surname character varying(200) NOT NULL,
    firstname character varying(200) NOT NULL,
    address character varying(300) NOT NULL,
    zipcode integer NOT NULL,
    telephone character varying(20) NOT NULL,
    recommendedby integer,
    joindate timestamp without time zone NOT NULL
    CONSTRAINT fk_recomendedby 
        FOREIGN KEY (recommendedby)
            REFERENCES members(memid) ON DELETE SET NULL
);


--Create table bookings WITH FOREIGN KEYS
CREATE TABLE bookings (
    bookid integer SERIAL PRIMARY KEY NOT NULL,
    facid integer NOT NULL,
    memid integer NOT NULL,
    starttime timestamp without time zone NOT NULL,
    slots integer NOT NULL, 
    CONSTRAINT fk_facility
        FOREIGN KEY(facid)
            REFERENCES facilities(facid),
    CONSTRAINT fk_member
        FOREIGN KEY(memid)
            REFERENCES members(memid)

);

--Inserting DATA to members table
INSERT INTO members (surname, firstname, address, zipcode, telephone, recommendedby, joindate) VALUES
('Smith', 'Darren', '8 Bloomsbury Close, Boston', 4321, '555-555-5555', NULL, '2012-07-02 12:02:05'),
('Smith', 'Tracy', '8 Bloomsbury Close, New York', 4321, '555-555-5555', NULL, '2012-07-02 12:08:23'),
('Rownam', 'Tim', '23 Highway Way, Boston', 23423, '(844) 693-0723', NULL, '2012-07-03 09:32:15'),
('Joplette', 'Janice', '20 Crossing Road, New York', 234, '(833) 942-4710', 1, '2012-07-03 10:25:05'),

--inserting into facilities
INSERT INTO facilities ( name, membercost, guestcost, initialoutlay, monthlymaintenance) VALUES
( 'Tennis Court 1', 5, 25, 10000, 200),
( 'Tennis Court 2', 5, 25, 8000, 200),
( 'Badminton Court', 0, 15.5, 4000, 50),


INSERT INTO bookings ( facid, memid, starttime, slots) VALUES
(0, 1, '2012-07-03 11:00:00', 2),
(1, 1, '2012-07-03 08:00:00', 2),
(2, 0, '2012-07-03 18:00:00', 2),
(1, 1, '2012-07-03 19:00:00', 2),
(2, 1, '2012-07-03 10:00:00', 1),
(0, 1, '2012-07-03 15:00:00', 1),
(0, 2, '2012-07-04 09:00:00', 3),
(0, 2, '2012-07-04 15:00:00', 3),
(1, 3, '2012-07-04 13:30:00', 2),
(2, 0, '2012-07-04 15:00:00', 2),
(1, 0, '2012-07-04 17:30:00', 2),

--Select everything from table facilities
SELECT * FROM cd.facilities
--  print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs
SELECT name, membercost FROM cd.facilities

-- produce a list of facilities that charge a fee to members
SELECT * FROM cd.facilities WHERE membercost > 0
-- produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.
Select facid, name, membercost, monthlymaintenance FROM cd.facilities
WHERE membercost > 0 and (membercost < monthlymaintenance/50)
-- produce a list of all facilities with the word 'Tennis' in their name
SELECT * FROM cd.facilities where name LIKE '%Tennis%'
-- etrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator. 
SELECT * FROM cd.facilities WHERE facid in(1,5)
-- produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.

SELECT name, CASE WHEN (monthlymaintenance > 100) then
		'expensive'
	else
		'cheap'
	end as cost
	from cd.facilities;    

-- Produce a list of members who joined after the start of September 2012 Return the memid, surname, firstname, and joindate of the members in question. 
SELECT memid, surname, firstname, joindate FROM cd.members WHERE joindate > '2012-09-01'
-- produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
SELECT DISTINCT surname FROM cd.members ORDER BY surname LIMIT 10
-- want a combined list of all surnames and all facility names. 
SELECT surname FROM cd.members UNION SELECT name FROM cd.facilities
-- get the signup date of your last member. 
SELECT max(joindate) FROM cd.members 
-- get the first and last name of the last member(s) who signed up - not just the date.
SELECT firstname, surname, joindate FROM cd.members ORDER BY joindate DESC limit 1

