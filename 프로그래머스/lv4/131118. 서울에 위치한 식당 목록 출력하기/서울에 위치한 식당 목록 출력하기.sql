select 
    t1.REST_ID,
    REST_NAME,
    FOOD_TYPE,
    FAVORITES,
    ADDRESS,
    round(avg(REVIEW_SCORE), 2) as SCORE
from 
    REST_INFO t1
    join REST_REVIEW t2 on t1.REST_ID = t2.REST_ID
where ADDRESS like '서울%'
group by REST_ID
order by SCORE desc, FAVORITES desc