select 
    t1.PRODUCT_ID,
    t1.PRODUCT_NAME,
    sum(PRICE * AMOUNT) as TOTAL_SALES
from FOOD_PRODUCT t1
join FOOD_ORDER t2 on t1.PRODUCT_ID = t2.PRODUCT_ID
where PRODUCE_DATE like '2022-05-%'
group by 1
order by 3 desc, 1