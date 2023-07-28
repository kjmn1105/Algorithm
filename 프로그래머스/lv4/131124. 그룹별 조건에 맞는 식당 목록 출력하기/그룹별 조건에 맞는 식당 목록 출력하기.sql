with STEP_1 as (
select MEMBER_ID, count(*) REVIEW_CNT
from REST_REVIEW
group by MEMBER_ID
)

select MEMBER_ID
from STEP_1
where REVIEW_CNT = (select max(REVIEW_CNT) from STEP_1)


# select MEMBER_NAME, REVIEW_TEXT, left(REVIEW_DATE, 10) REVIEW_DATE
# from MEMBER_PROFILE M, REST_REVIEW R
# where M.MEMBER_ID = R.MEMBER_ID and M.MEMBER_ID in (
#     select MEMBER_ID
#     from member_review_cnt T1
#     where REVIEW_CNT = (select max(REVIEW_CNT) from member_review_cnt T2)
#     )
# order by 3, 2