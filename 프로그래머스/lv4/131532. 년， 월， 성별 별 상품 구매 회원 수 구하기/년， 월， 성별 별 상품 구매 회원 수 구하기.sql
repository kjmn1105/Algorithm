# select 
#     year(SALES_DATE) year,
#     month(SALES_DATE) month,
#     count(distinct USER_ID) USERS
# group by 


select 
    YEAR, MONTH, GENDER, count(distinct USER_ID) USERS
from (
    select T1.USER_ID, GENDER, year(SALES_DATE) year, month(SALES_DATE) month
    from ONLINE_SALE T2
    join USER_INFO T1 on T1.USER_ID = T2.USER_ID
    where gender is not null) as TEMP
group by YEAR, MONTh, GENDER
order by 1, 2, 3