select
    USER_ID,
    NICKNAME,
    concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as 전체주소,
    concat(left(TLNO, 3), '-', substr(TLNO, 4, 4), '-', right(TLNO, 4)) as 전화번호
from USED_GOODS_USER as t1
join USED_GOODS_BOARD as t2
on t1.USER_ID = t2.WRITER_ID
group by USER_ID
having count(USER_ID) >= 3
order by USER_ID desc
