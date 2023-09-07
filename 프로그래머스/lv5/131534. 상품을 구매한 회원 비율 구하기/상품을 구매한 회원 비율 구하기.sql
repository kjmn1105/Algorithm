# 09:06

select 
    year(sales_date) YEAR,
    month(sales_date) MONTH,
    count(distinct U.user_id) PUCHASED_USERS,
    round(count(distinct U.user_id) / (select count(distinct user_id) from USER_INFO where year(joined) = 2021), 1) PUCHASED_RATIO
from USER_INFO U
join ONLINE_SALE S on U.user_id = S.user_id
where year(joined) = 2021
group by 1, 2
order by 1, 2