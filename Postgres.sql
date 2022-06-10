-- Excersices form interactive postgresql exercises

--How can you retrieve all the information from the cd.facilities table?

SELECT * FROM cd.facilities;

--You want to print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs?
SELECT name, membercost FROM cd.facilities;

-- How can you produce a list of facilities that charge a fee to members? 
SELECT * FROM cd.facilities WHERE membercost > 0;

--How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, 
--facility name, member cost, and monthly maintenance of the facilities in question.

SELECT facid, name, membercost, monthlymaintenance  FROM cd.facilities 
WHERE membercost<(monthlymaintenance/50) 
and membercost>0;

-- How can you produce a list of all facilities with the word 'Tennis' in their name? 
SELECT * FROM cd.facilities WHERE name LIKE '%Tennis%';

--How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.
SELECT * FROM cd.facilities WHERE facid IN(1,5); 

--How can you produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.
SELECT name, CASE WHEN monthlymaintenance>100 THEN 'expensive' ELSE 'cheap' END AS monthlymaintenance FROM cd.facilities;

--How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, firstname, and joindate of the members in question. 
SELECT memid, surname, firstname, joindate FROM cd.members WHERE joindate>'2012-09-01';

--How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
SELECT DISTINCT surname FROM cd.members ORDER BY surname FETCH FIRST  10 ROWS ONLY;

--You, for some reason, want a combined list of all surnames and all facility names. Yes, this is a contrived example :-). Produce that list! 
SELECT surname FROM cd.members UNION SELECT name FROM cd.facilities;

 -- You'd like to get the signup date of your last member. How can you retrieve this information? 
SELECT joindate AS latest FROM cd.members ORDER BY joindate DESC FETCH FIRST 1 ROWS ONLY;

--You'd like to get the first and last name of the last member(s) who signed up - not just the date. How can you do that? 
SELECT firstname, surname, joindate FROM cd.members ORDER BY joindate DESC FETCH FIRST 1 ROWS ONLY;

-- How can you produce a list of the start times for bookings by members named 'David Farrell'? 
select bks.starttime 
	from 
		cd.bookings bks
		inner join cd.members mems
			on mems.memid = bks.memid
	where 
		mems.firstname='David' 
		and mems.surname='Farrell';  
--without inner join
SELECT starttime FROM cd.bookings WHERE memid IN (SELECT memid FROM cd.members WHERE firstname='David' AND surname='Farrell');

--without join and only in one select statement
SELECT b.starttime FROM cd.bookings b, cd.members m WHERE 
b.memid = m.memid AND m.firstname='David' AND m.surname='Farrell';

--How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time. 
SELECT b.starttime AS start, f.name FROM cd.bookings b, cd.facilities f WHERE
f.facid = b.facid 
AND b.starttime >= '2012-09-21'
AND b.starttime < '2012-09-22'
AND f.name LIKE 'Tennis%'
ORDER BY b.starttime;

--How can you output a list of all members who have recommended another member? Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname). 
SELECT DISTINCT m.firstname, m.surname FROM cd.members m, cd.members m2 WHERE m2.recommendedby = m.memid
ORDER BY surname, firstname;

--How can you output a list of all members, including the individual who recommended them (if any)? Ensure that results are ordered by (surname, firstname).
SELECT m.firstname, m.surname, m2.firstname, m2.surname FROM cd.members m LEFT JOIN cd.members m2 ON m2.memid = m.recommendedby ORDER BY surname, firstname;

--How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name followed by the facility name. 
SELECT DISTINCT  m.firstname || ' ' || m.surname AS member, f.name FROM cd.members m, cd.bookings b, cd.facilities f
WHERE f.facid=b.facid AND b.memid=m.memid AND f.name LIKE 'Tennis%' ORDER BY member, f.name;

--How can you output a list of all members, including the individual who recommended them (if any), without using any joins? Ensure that there are no duplicates in the list, and that each firstname + surname pairing is formatted as a column and ordered.
SELECT DISTINCT m.firstname || ' ' || m.surname AS member, m2.firstname || ' ' || m2.surname AS recommender FROM cd.members m LEFT JOIN cd.members m2 ON m2.memid = m.recommendedby ORDER BY member, recommender;

--The club is adding a new facility - a spa. We need to add it into the facilities table. Use the following values:
--facid: 9, Name: 'Spa', membercost: 20, guestcost: 30, initialoutlay: 100000, monthlymaintenance: 800.
INSERT INTO cd.facilities VALUES(9,'Spa', 20, 30, 100000, 800);

--Let's try adding the spa to the facilities table again. This time, though, we want to automatically generate the value for the next facid, rather than specifying it as a constant. Use the following values for everything else:

    --Name: 'Spa', membercost: 20, guestcost: 30, initialoutlay: 100000, monthlymaintenance: 800.
INSERT INTO cd.facilities select (SELECT MAX(facid) from cd.facilities)+1,'Spa', 20, 30, 100000, 800;

--We made a mistake when entering the data for the second tennis court. The initial outlay was 10000 rather than 8000: you need to alter the data to fix the error. 
UPDATE cd.facilities SET initialoutlay=10000 WHERE facid=1;

--We want to increase the price of the tennis courts for both members and guests. Update the costs to be 6 for members, and 30 for guests. 
UPDATE cd.facilities SET membercost = 6, guestcost= 30 WHERE facid IN(0,1);

--We want to alter the price of the second tennis court so that it costs 10% more than the first one. Try to do this without using constant values for the prices, so that we can reuse the statement if we want to. 
UPDATE cd.facilities SET 
membercost=(SELECT membercost*1.1 FROM cd.facilities WHERE facid = 0),
guestcost = (SELECT guestcost*1.1 FROM cd.facilities WHERE facid = 0)
WHERE facid=1;

--As part of a clearout of our database, we want to delete all bookings from the cd.bookings table. How can we accomplish this? 
Delete from cd.bookings;

-- We want to remove member 37, who has never made a booking, from our database. How can we achieve that? 
delete from cd.members where memid=37;

--In our previous exercises, we deleted a specific member who had never made a booking. How can we make that more general, to delete all members who have never made a booking? 
delete from cd.members where memid not in (select distinct memid from cd.bookings);