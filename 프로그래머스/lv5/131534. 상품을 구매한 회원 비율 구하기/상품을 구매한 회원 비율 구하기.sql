select 
    year(SALES_DATE) YEAR,
    month(SALES_DATE) MONTH,
    count(distinct(USER_ID)) PUCHASED_USERS,
    round(count(distinct(USER_ID)) / (
        select count(*) from USER_INFO where year(JOINED)='2021'), 1) PUCHASED_RATIO
from ONLINE_SALE
where USER_ID in (
    select USER_ID from USER_INFO where year(JOINED)='2021'
)
group by YEAR, MONTH
order by 1, 2