-- retrieving everything from a table
select * from cd.facilities

-- retrieve only two columns from a table
select name, membercost from cd.facilities;

-- using the where clause to select items from a table
select * from cd.facilities where membercost > 0;

-- another where clause using two conditions and calculations
select facid, name, membercost, monthlymaintenance from cd.facilities where 
            membercost > 0 
            and 
            membercost < (monthlymaintenance / 50)

-- using like in where condition
select * from cd.facilities where name like '%Tennis%'

-- selecting two different facid using where
select * from cd.facilities where facid in (1,5)

-- using case and creating a new column
select name, case when (monthlymaintenance > 100) then 'expensive' else 'cheap' end as Cost from cd.facilities

-- working with dates
select memid, surname, firstname, joindate from cd.members where joindate > '2012-09-01 00:00:00'

-- selecting distinct names
select distinct surname from cd.members order by surname limit 10;

-- using union
select surname from cd.members union select name from cd.facilities

-- selecting latest date of a column
select max(joindate) as latest from cd.members 

-- selecting additional details based on a condition
select firstname, surname, joindate from cd.members
	where joindate = 
		( select max(joindate) from cd.members );


-- using joins

select bks.starttime 
	from 
		cd.bookings bks
		inner join cd.members mems
			on mems.memid = bks.memid
	where 
		mems.firstname='David' 
		and mems.surname='Farrell'; 


select bks.starttime as start, facs.name as name
	from 
		cd.facilities facs
		inner join cd.bookings bks
			on facs.facid = bks.facid
	where 
		facs.name in ('Tennis Court 2','Tennis Court 1') and
		bks.starttime >= '2012-09-21' and
		bks.starttime < '2012-09-22'
order by bks.starttime;         

select distinct recs.firstname as firstname, recs.surname as surname
	from 
		cd.members mems
		inner join cd.members recs
			on recs.memid = mems.recommendedby
order by surname, firstname;

select mems.firstname as memfname, mems.surname as memsname, recs.firstname as recfname, recs.surname as recsname
	from 
		cd.members mems
		left outer join cd.members recs
			on recs.memid = mems.recommendedby
order by memsname, memfname;          





   