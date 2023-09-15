select
    t1.CATEGORY,
    sum(t2.SALES) as TOTAL_SALES
from BOOK t1
left join BOOK_SALES t2 on t1.BOOK_ID = t2.BOOK_ID
where DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-01'
group by CATEGORY
order by CATEGORY