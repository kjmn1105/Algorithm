with NOT_AVAILIABLE as (
    select distinct(CAR_ID)
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where 
        datediff('2022-11-01', START_DATE) * datediff('2022-11-01', END_DATE) <= 0
        or datediff('2022-11-30', START_DATE) * datediff('2022-11-30', END_DATE) <= 0
)

select 
    distinct t1.CAR_ID,
    t1.CAR_TYPE, 
    floor(DAILY_FEE * (100 - DISCOUNT_RATE) / 100 * 30) as FEE
from CAR_RENTAL_COMPANY_CAR t1
join CAR_RENTAL_COMPANY_RENTAL_HISTORY t2 on t1.CAR_ID = t2.CAR_ID
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN t3 on t1.CAR_TYPE = t3.CAR_TYPE
where
    t1.CAR_ID not in (select CAR_ID from NOT_AVAILIABLE)
    and DURATION_TYPE = '30일 이상'
    and t1.CAR_TYPE in ('SUV', '세단')
having (FEE >= 500000 and FEE < 2000000)
order by 3 desc, 2, 1 desc
