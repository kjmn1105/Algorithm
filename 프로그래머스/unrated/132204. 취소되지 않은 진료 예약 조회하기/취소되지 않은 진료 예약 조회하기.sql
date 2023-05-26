select
    APNT_NO,
    t2.PT_NAME,
    t2.PT_NO,
    t1.MCDP_CD,
    t3.DR_NAME,
    APNT_YMD
from
    APPOINTMENT t1
    join PATIENT t2 on t1.PT_NO = t2.PT_NO
    join DOCTOR t3 on t1.MDDR_ID = t3.DR_ID
where
    left(APNT_YMD, 10) = '2022-04-13' 
    and t1.MCDP_CD = 'CS' 
    and APNT_CNCL_YN = 'N'
order by APNT_YMD