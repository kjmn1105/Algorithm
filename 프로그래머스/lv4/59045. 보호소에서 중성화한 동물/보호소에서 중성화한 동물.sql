select t1.ANIMAL_ID, t1.ANIMAL_TYPE, t1.NAME
from ANIMAL_INS t1
join ANIMAL_OUTS t2 on t1.ANIMAL_ID = t2.ANIMAL_ID
where SEX_UPON_INTAKE like 'Intact%' and SEX_UPON_OUTCOME not like 'Intact%'
order by 1