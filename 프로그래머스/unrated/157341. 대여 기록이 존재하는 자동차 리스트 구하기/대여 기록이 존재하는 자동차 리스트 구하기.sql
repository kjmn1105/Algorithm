select
    distinct t1.CAR_ID 
from CAR_RENTAL_COMPANY_CAR t1
join CAR_RENTAL_COMPANY_RENTAL_HISTORY t2 on t1.CAR_ID = t2.CAR_ID
where 
    CAR_TYPE = '세단'
    and left(START_DATE, 7) = '2022-10'
order by 1 desc