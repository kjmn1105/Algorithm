select
    USER_ID,
    NICKNAME,
    concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) 전체주소,
    concat(left(TLNO, 3), '-', substr(TLNO, 4, 4), '-', right(TLNO, 4)) TLNO
from USED_GOODS_USER
where USER_ID in (
    select WRITER_ID
    from USED_GOODS_BOARD
    group by WRITER_ID
    having count(*) >= 3
)
order by 1 desc









# select
#     USER_ID,
#     NICKNAME,
#     concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as 전체주소,
#     concat(left(TLNO, 3), '-', substr(TLNO, 4, 4), '-', right(TLNO, 4)) as 전화번호
# from USED_GOODS_USER as t1
# join USED_GOODS_BOARD as t2
# on t1.USER_ID = t2.WRITER_ID
# group by USER_ID
# having count(USER_ID) >= 3
# order by USER_ID desc