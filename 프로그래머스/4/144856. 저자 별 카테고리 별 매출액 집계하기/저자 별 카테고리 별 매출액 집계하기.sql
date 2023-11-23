select 
    t1.AUTHOR_ID, 
    AUTHOR_NAME,
    CATEGORY,  
    sum(PRICE * SALES) as TOTAL_SALES
from BOOK t1, AUTHOR t2, BOOK_SALES t3
where 
    t1.AUTHOR_ID = t2.AUTHOR_ID and
    t1.BOOK_ID = t3.BOOK_ID and
    left(SALES_DATE, 7) = '2022-01'
group by 
    t1.AUTHOR_ID, CATEGORY
order by 1, 3 desc