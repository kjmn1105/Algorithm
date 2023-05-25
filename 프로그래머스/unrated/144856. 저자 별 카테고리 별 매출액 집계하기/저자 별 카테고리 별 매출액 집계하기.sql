select
    t1.AUTHOR_ID,
    AUTHOR_NAME,
    CATEGORY,
    sum(PRICE * SALES) as TOTAL_SALES
from BOOK t1
join AUTHOR t2 on t2.AUTHOR_ID = t1.AUTHOR_ID
join BOOK_SALES t3 on t1.BOOK_ID = t3.BOOK_ID
where left(t3.SALES_DATE, 7) = '2022-01'
group by AUTHOR_ID, CATEGORY
order by AUTHOR_ID asc, CATEGORY desc