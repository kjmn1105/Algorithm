select
    t1.ANIMAL_ID,
    t1.NAME
from ANIMAL_OUTS t1
left join ANIMAL_INS t2 on t1.ANIMAL_ID = t2.ANIMAL_ID
where t1.DATETIME < t2.DATETIME
order by t2.DATETIME