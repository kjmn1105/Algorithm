with step_1 as (
select 
    month(START_DATE) MONTH, CAR_ID,
    count(*) over(partition by month(START_DATE), CAR_ID) RECORDS,
    count(*) over (partition by CAR_ID) RECORDS_SUM
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE between '2022-08-01' and '2022-10-31'
order by 1, 2 desc
)

select 
    distinct MONTH, CAR_ID, 
    RECORDS
from step_1
where RECORDS_SUM >= 5