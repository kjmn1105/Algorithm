# select CART_ID
# from (
#     select
#         CART_ID,
#         sum(if(NAME='Milk', 1, 0) + if(NAME='Yogurt', 1, 0)) as MilkandYogurt
#     from CART_PRODUCTS
#     group by CART_ID
#     having MilkandYogurt=2) as t
# order by CART_ID

select distinct(M.CART_ID)
from (select CART_ID from CART_PRODUCTS where NAME='Milk') as M
inner join (select CART_ID from CART_PRODUCTS where NAME='Yogurt') as Y
on M.CART_ID = Y.CART_ID
order by CART_ID