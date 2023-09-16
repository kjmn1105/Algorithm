# desc ONLINE_SALE
select USER_ID, PRODUCT_ID
from ONLINE_SALE
group by USER_ID, PRODUCT_ID
having count(*)>1
order by 1, 2 desc

# select 
#     USER_ID, PRODUCT_ID
# from ONLINE_SALE
# group by USER_ID, PRODUCT_ID
# having count(*) > 1
# order by 1, 2 desc