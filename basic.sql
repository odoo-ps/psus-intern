-- select all columns
SELECT * FROM cd.facilities;
-- pick specified columns 
SELECT name, membercost FROM cd.facilities;

-- WHERE clause
SELECT * FROM cd.facilities WHERE membercost > 0

-- USE 50.0 instead of 50 here
SELECT facid, name, membercost, monthlymaintenance FROM cd.facilities WHERE membercost > 0 AND membercost  < monthlymaintenance/ 50.0;

-- LIKE clause
SELECT * FROM cd.facilities WHERE name LIKE '%Tennis%'

-- LIKE clause (Case insensitive)
SELECT * FROM cd.facilities WHERE lower(name) LIKE '%Tennis%'

-- 'in' operator (specify a set)
select * from cd.facilities where facid in (1,5);


-- case when - end, as
select name,
	case when (monthlymaintenance > 100) then
		'expensive'
	else
		'cheap'
	end as cost
	from cd.facilities;  
-- Date comparison format 'yyyy-mm-dd'
select memid, surname, firstname, joindate 
	from cd.members
	where joindate >= '2012-09-01'; 

-- 'dinstinct', order, limit
select distinct surname 
	from cd.members
    order by surname
    limit 10;   

-- UNION: combines the result of two SQL queries into a single table
select surname 
	from cd.members
union
select name
	from cd.facilities;

