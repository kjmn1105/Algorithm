select
    t2.USER_ID,
    t2.NICKNAME,
    sum(t1.PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as t1
join USED_GOODS_USER as t2
on t1.WRITER_ID = t2.USER_ID
where STATUS = 'DONE'
group by USER_ID
having TOTAL_SALES >= 700000
order by TOTAL_SALES asc