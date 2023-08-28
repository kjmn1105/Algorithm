with temp as (
    select t1.BOARD_ID
    from USED_GOODS_BOARD t1
    join USED_GOODS_FILE t2 on t1.BOARD_ID = t2.BOARD_ID
    order by VIEWS desc
    limit 1
)
select 
    concat('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
from USED_GOODS_FILE 
where BOARD_ID in (select BOARD_ID from temp)
order by FILE_ID desc