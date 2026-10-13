SELECT e.name AS employee
FROM Employee e
JOIN Employee m
    ON e.managerid = m.id
WHERE e.salary > m.salary;