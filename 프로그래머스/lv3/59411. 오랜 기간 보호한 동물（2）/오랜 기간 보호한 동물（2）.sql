select 
    t1.ANIMAL_ID,
    t1.NAME
from ANIMAL_OUTS t1
inner join ANIMAL_INS t2 on t1.ANIMAL_ID = t2.ANIMAL_ID
order by t2.DATETIME-t1.DATETIME
limit 2