-- MAX
select max(joindate) as latest
	from cd.members;        
-- 
select firstname, surname, joindate
	from cd.members
	where joindate = 
		(select max(joindate) 
			from cd.members);
-- Another way
select firstname, surname, joindate
	from cd.members
    order by joindate desc
    limit 1;
-- WRONG: pairing up a list with a single value    
-- select firstname, surname, max(joindate)
--         from cd.members

-- alias, INNER JOIN-on 
select bks.starttime
	from 
		cd.bookings bks
		inner join cd.members mems
			on mems.memid = bks.memid 
	where 
		mems.firstname='David' 
		and mems.surname='Farrell' ;   

SELECT bks.starttime as start, facs.name as name
	FROM cd.bookings bks inner join cd.facilities facs on 
	bks.facid=facs.facid
	where bks.starttime>='2012-09-21' and bks.starttime<'2012-09-22'
	and name LIKE 'Tennis Court%'

-- self inner join
select distinct mems.firstname as firstname, mems.surname as surname
	from
		cd.members mems
		inner join cd.members recs
			on mems.memid=recs.recommendedby
order by surname, firstname
-- left/right outer join (useful when we need optional data, 
-- LEFT OUTER JOIN: even if a given row on 'LEFT' side doesn't match anything, it produces an empty output)
SELECT mems.firstname as memfname, mems.surname as memsname, recs.firstname as recfname, recs.surname as recsname
FROM cd.members mems left outer join cd.members recs
on recs.memid=mems.recommendedby
order by memsname, memfname

-- postgre string concat: str1 || str2 
-- multiple inner join
-- 'order by' comes AFTER 'where'
SELECT distinct mems.firstname || ' ' || mems.surname as member, facs.name as facility
FROM cd.members mems 
	inner join cd.bookings bks on mems.memid=bks.memid
	inner join cd.facilities facs on bks.facid=facs.facid
where facs.name like 'Tennis Court%'
order by member, facs.name

-- case-when then-end
SELECT mems.firstname || ' ' || mems.surname as member, 
	facs.name as facility,
	case 
		when mems.memid = 0 then
			bks.slots*facs.guestcost
		else
			bks.slots*facs.membercost
	end
	as cost
FROM 
	cd.members mems
	INNER JOIN cd.bookings bks on mems.memid=bks.memid
	INNER JOIN cd.facilities facs on bks.facid=facs.facid
WHERE
	bks.starttime >= '2012-09-14' and bks.starttime < '2012-09-15'
	and (
		case 
	  		when mems.memid=0 then
	  			bks.slots*facs.guestcost > 30
	  		else
	  			bks.slots*facs.membercost > 30
	  		end
	)
	
ORDER BY cost DESC
-- BETTER WAY
select member, facility, cost from (
	select 
		mems.firstname || ' ' || mems.surname as member,
		facs.name as facility,
		case
			when mems.memid = 0 then
				bks.slots*facs.guestcost
			else
				bks.slots*facs.membercost
		end as cost
		from
			cd.members mems
			inner join cd.bookings bks
				on mems.memid = bks.memid
			inner join cd.facilities facs
				on bks.facid = facs.facid
		where
			bks.starttime >= '2012-09-14' and
			bks.starttime < '2012-09-15'
	) as bookings
	where cost > 30
order by cost desc;     

-- subqueries
select distinct mems.firstname || ' ' ||  mems.surname as member,
	(
	  	select recs.firstname || ' ' || recs.surname as recommender 
		from cd.members recs 
		where recs.memid = mems.recommendedby
	)
	from 
		cd.members mems
order by member;