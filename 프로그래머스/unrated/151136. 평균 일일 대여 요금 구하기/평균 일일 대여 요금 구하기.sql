select distinct round(avg(DAILY_FEE) over()) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = 'SUV'
