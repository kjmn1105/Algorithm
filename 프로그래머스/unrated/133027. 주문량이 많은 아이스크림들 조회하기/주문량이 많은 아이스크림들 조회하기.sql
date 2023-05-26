select
    t1.FLAVOR
from 
    JULY t1
    join FIRST_HALF t2 
    on t1.FLAVOR = t2.FLAVOR
group by t1.FLAVOR
order by sum(t1.TOTAL_ORDER + t2.TOTAL_ORDER) desc
limit 3