

# select 
#     MEMBER_NAME,
#     REVIEW_TEXT,
#     date_format(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
# from MEMBER_PROFILE t1
# join REST_REVIEW t2 on t1.MEMBER_ID = t2.MEMBER_ID
# where (t1.MEMBER_ID) in (select MEMBER_ID from temp having max(CNT))
# order by 3, 2

with temp1 as (
    select MEMBER_ID, count(*) REVIEW_COUNT
    from REST_REVIEW
    group by MEMBER_ID    
)

select
    MEMBER_NAME,
    REVIEW_TEXT,
    date_format(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE t1
join REST_REVIEW t2 on t1.MEMBER_ID = t2.MEMBER_ID
where t2.MEMBER_ID in (
    select MEMBER_ID
    from temp1
    where REVIEW_COUNT = (select max(REVIEW_COUNT) from temp1)
)
order by 3, 2