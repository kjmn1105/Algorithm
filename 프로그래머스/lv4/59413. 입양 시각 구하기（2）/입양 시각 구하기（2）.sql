# SET @HOUR = -1;
# select (@HOUR := @HOUR +1) as HOUR,
#     (select count(*)
#      from ANIMAL_OUTS
#      where @HOUR = hour(DATETIME)) COUNT
# from ANIMAL_OUTS
# where @HOUR < 23;


with recursive TIME_RANGE as (
    -- anchor 쿼리
    select 0 as hour
    union all
    -- recursive 쿼리
    select hour+1 from TIME_RANGE where hour < 23
)

select T.HOUR, count(A.animal_id) COUNT
from TIME_RANGE T
left join ANIMAL_OUTS A on T.hour = hour(A.datetime)
group by 1