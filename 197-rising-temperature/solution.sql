SELECT w.id
FROM (SELECT w2.id,
            w2.recordDate,
            lag(w2.recordDate, 1) OVER (ORDER BY w2.recordDate) AS shifted_date,
            w2.temperature,
            lag(w2.temperature, 1) OVER (ORDER BY w2.recordDate) AS shifted_temp
        FROM Weather w2) AS w
WHERE DATEDIFF(day, w.shifted_date, w.recordDate) = 1 and w.temperature > w.shifted_temp;