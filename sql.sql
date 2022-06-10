SELECT * FROM db;
SELECT c1,c2,c3 FROM db;
SELECT * FROM db WHERE parameter > 0;
SELECT col1, col2,col3 from db WHERE parameter > 0 and (parameter2< parameter3 );
SELECT * FROM db WHERE param LIKE '%string%';
SELECT * FROM db WHERE id IN (2,4);
SELECT param, CASE WHEN (param2 >100 ) THEN 'huge' else 'actually huge' end as classifiedcol FROM db
SELECT param1,param2,param3, date FROM db WHERE date >= '2022-01-01';
SELECT DISTINCT param1 FROM db ORDER BY param1 LIMIT 10;
SELECT param1 FROM db UNION SELECT param2 FROM db2
SELECT max(date) AS latest FROM db;
SELECT param1,param2,param3,date FROM db WHERE date = (SELECT max(date) FROM db);
SELECT bks.starttime FROM cd.bookings bks INNER JOIN cd.members mems on mems.memid =bks.memid WHERE mems.firstname ='David' and mems.surname ='Farrell';
SELECT bks.starttime,f.name FROM cd.bookings bks INNER JOIN cd.facilities f ON f.facid =bks.facid WHERE f.name in ('Tennis Court 2','Tennis Court 1') AND bks.starttime >='2012-09-21' AND bks.starttime <= '2012-09-22' ORDER BY bks.starttime;
SELECT DISTINCT recs.firstname as firstname, recs.surname as surname FROM cd.members mems INNER JOIN cd.members recs ON recs.memid = mems.recommendedby ORDER BY surname, firstname
SELECT mems.firstname as memfname, mems.surname as memsname, recs.firstname as recfname, recs.surname as recsname FROM cd.members mems LEFT OUTER JOIN cd.members recs ON recs.memid = mems.recommendedby ORDER BY memsname,memfname;
SELECT DISTINCT mems.firstname || ' ' || mems.surname as member, facs.name as facility FROM cd.members mems INNER JOIN cd.bookings bks ON mems.memid = bks.memid INNER JOIN cd.facilities facs ON bks.facid =facs.facid WHERE facs.name in ('a1','a2') ORDER BY member,facility