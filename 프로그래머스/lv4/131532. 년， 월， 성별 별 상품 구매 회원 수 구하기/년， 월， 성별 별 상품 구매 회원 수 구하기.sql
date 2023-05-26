select 
    year(SALES_DATE) as YEAR,
    month(SALES_DATE) as MONTH,
    GENDER,
    count(distinct(t1.USER_ID)) as USERS
from
    USER_INFO t1
    join ONLINE_SALE t2 on t1.USER_ID = t2.USER_ID
where gender in (0, 1)
group by year, month, gender
order by year, month, gender


    