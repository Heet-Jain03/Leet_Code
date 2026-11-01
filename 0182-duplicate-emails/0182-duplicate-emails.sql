# Write your MySQL query statement below


SELECT 
Email 
FROM person 
group by email 
having count(email) > 1