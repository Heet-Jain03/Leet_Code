# Write your MySQL query statement below


SELECT 
Email 
FROM Person 
group by email 
having count(email) > 1