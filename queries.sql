/* all by year */

SELECT year,week,deaths
from
(
SELECT p.year,p.week,sum(d.deaths) deaths
FROM weeklyplus p,weekly_deaths d
WHERE 
p.yearreal=d.year+2000 and p.weekreal=d.week
group by p.year,p.week
order by p.year,p.week
) q

