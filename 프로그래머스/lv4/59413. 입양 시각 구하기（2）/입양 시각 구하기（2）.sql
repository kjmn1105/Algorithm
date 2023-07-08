SET @HOUR = -1;
select (@HOUR := @HOUR +1) as HOUR,
    (select count(*)
     from ANIMAL_OUTS
     where @HOUR = hour(DATETIME)) COUNT
from ANIMAL_OUTS
where @HOUR < 23;
