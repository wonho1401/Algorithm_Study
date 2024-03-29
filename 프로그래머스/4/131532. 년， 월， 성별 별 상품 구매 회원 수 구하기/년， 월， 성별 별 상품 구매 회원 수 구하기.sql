-- 코드를 입력하세요
SELECT YEAR(s.SALES_DATE) as YEAR, MONTH(s.SALES_DATE) as MONTH, u.GENDER as GENDER, COUNT(DISTINCT(s.USER_ID)) as USERS
FROM ONLINE_SALE as s
LEFT JOIN USER_INFO as u 
ON s.USER_ID = u.USER_ID
WHERE u.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER