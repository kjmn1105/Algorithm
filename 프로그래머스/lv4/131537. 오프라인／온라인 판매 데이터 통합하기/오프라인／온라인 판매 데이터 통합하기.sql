# -- 09:05 ~

with T as (
    (select 
        date_format(SALES_DATE, '%Y-%m-%d') SALES_DATE, 
        PRODUCT_ID, 
        NULL as USER_ID, 
        SALES_AMOUNT
    from OFFLINE_SALE)
    union all
    (select 
        date_format(SALES_DATE, '%Y-%m-%d') SALES_DATE, 
        PRODUCT_ID, 
        USER_ID, 
        SALES_AMOUNT
    from ONLINE_SALE)
)

select *
from T
where date_format(SALES_DATE, '%Y-%m') = '2022-03'
order by 1, 2, 3