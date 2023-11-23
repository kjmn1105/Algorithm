select 
    MEMBER_ID, 
    MEMBER_NAME, 
    GENDER, 
    date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where 
    month(DATE_OF_BIRTH) = 03 and
    gender = 'W' and
    TLNO is not NULL
order by 1