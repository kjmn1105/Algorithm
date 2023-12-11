SELECT flavor
FROM (
    SELECT * FROM first_half
    UNION ALL
    SELECT * FROM july
) as temp
GROUP BY 1
ORDER BY SUM(total_order) desc
LIMIT 3
