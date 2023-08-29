with T2 as (
    select 
        HISTORY_ID, CAR_ID, datediff(END_DATE, START_DATE)+1 as DURATION,
        case 
            when datediff(END_DATE, START_DATE)+1 < 7 then '없음'
            when datediff(END_DATE, START_DATE)+1 >= 90 then '90일 이상'
            when datediff(END_DATE, START_DATE)+1 >= 30 then '30일 이상'
            when datediff(END_DATE, START_DATE)+1 >= 7 then '7일 이상'
        end as DURATION_TYPE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY T2
),

T12 as (
    select CAR_TYPE, HISTORY_ID, DURATION, DAILY_FEE, DURATION_TYPE
    from T2
    join CAR_RENTAL_COMPANY_CAR T1 on T1.CAR_ID = T2.CAR_ID
    where T1.CAR_TYPE='트럭'
)

select 
    HISTORY_ID, 
    round(DURATION * DAILY_FEE * (100 - if(DISCOUNT_RATE, DISCOUNT_RATE, 0))/100) as FEE
from T12
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN T3 on T12.DURATION_TYPE = T3.DURATION_TYPE
where T3.CAR_TYPE = '트럭' or T3.CAR_TYPE is null
order by 2 desc, 1 desc