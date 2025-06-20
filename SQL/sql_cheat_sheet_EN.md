# SQL Cheat Sheet for Interviews

This document summarizes the most common SQL commands typically asked in job interviews. Each section includes basic syntax and a short example.

## Creating and Modifying Tables

- **CREATE TABLE**: creates a new table.
  ```sql
  CREATE TABLE employees (
      id INT PRIMARY KEY,
      name VARCHAR(100),
      salary DECIMAL(10,2)
  );
  ```
- **ALTER TABLE**: changes the structure of an existing table.
  ```sql
  ALTER TABLE employees ADD COLUMN department VARCHAR(50);
  ```
- **DROP TABLE**: removes a table and its contents entirely.
  ```sql
  DROP TABLE employees;
  ```

## Data Manipulation

- **INSERT INTO**: adds rows to a table.
  ```sql
  INSERT INTO employees (id, name, salary)
  VALUES (1, 'Ana', 45000.00);
  ```

- **INSERT INTO ... SELECT**: copies data from another table.
  ```sql
  INSERT INTO employees_history
  SELECT * FROM employees;
  ```

- **UPDATE**: updates existing values.
  ```sql
  UPDATE employees
  SET salary = 48000.00
  WHERE id = 1;
  ```

- **DELETE**: deletes rows based on a condition.
  ```sql
  DELETE FROM employees WHERE id = 1;
  ```

## Basic Queries

- **SELECT**: retrieves data from one or more tables.
  ```sql
  SELECT name, salary
  FROM employees;
  ```
- **WHERE**: filters results.
  ```sql
  SELECT *
  FROM employees
  WHERE salary > 50000.00;
  ```
- **ORDER BY**: sorts the results.
  ```sql
  SELECT name, salary
  FROM employees
  ORDER BY salary DESC;
  ```

## Advanced Filtering and Conditionals

- **LIKE (wildcards)**: searches for matches using `%` or `_`.
  ```sql
  SELECT name FROM employees
  WHERE name LIKE 'A%';
  ```
- **IN**: specifies a list of allowed values.
  ```sql
  SELECT * FROM employees
  WHERE department IN ('Sales', 'Marketing');
  ```
- **BETWEEN**: filters an inclusive range.
  ```sql
  SELECT * FROM employees
  WHERE salary BETWEEN 30000 AND 60000;
  ```
- **EXISTS**: checks for the existence of rows in a subquery.
  ```sql
  SELECT name FROM employees e
  WHERE EXISTS (SELECT 1 FROM departments d WHERE d.id = e.dep_id);
  ```
- **CASE**: applies conditional logic inside a query.
  ```sql
  SELECT name,
         CASE WHEN salary > 50000 THEN 'High' ELSE 'Medium' END AS salary_range
  FROM employees;
  ```

## Aggregation and Grouping

- **GROUP BY**: groups data for aggregate functions.
  ```sql
  SELECT department, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department;
  ```
- **HAVING**: filters resulting groups.
  ```sql
  SELECT department, COUNT(*) AS total
  FROM employees
  GROUP BY department
  HAVING COUNT(*) > 5;
  ```

## Joins

- **INNER JOIN**: returns rows that match in both tables.
  ```sql
  SELECT e.name, d.name AS dep_name
  FROM employees e
  INNER JOIN departments d ON e.dep_id = d.id;
  ```
- **LEFT JOIN**: returns all rows from the left table and matching rows from the right.
  ```sql
  SELECT e.name, d.name AS dep_name
  FROM employees e
  LEFT JOIN departments d ON e.dep_id = d.id;
  ```
- **UNION**: combines results from two queries.
  ```sql
  SELECT name FROM employees_archive
  UNION
  SELECT name FROM former_employees;
  ```

## Other Useful Statements

- **CREATE VIEW**: defines a view to simplify complex queries.
  ```sql
  CREATE VIEW view_employees AS
  SELECT name, salary
  FROM employees
  WHERE salary > 40000;
  ```
- **CREATE INDEX**: optimizes data search.
  ```sql
  CREATE INDEX idx_salary ON employees(salary);
  ```

## Window Functions

- **ROW_NUMBER**: assigns a sequential number within a group.
  ```sql
  SELECT name,
         ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS pos
  FROM employees;
  ```
- **RANK**: calculates the rank leaving gaps for ties.
  ```sql
  SELECT name,
         RANK() OVER (ORDER BY salary DESC) AS rank
  FROM employees;
  ```
- **LAG**: accesses the previous row in the set.
  ```sql
  SELECT name, salary,
         LAG(salary) OVER (ORDER BY salary) AS previous_salary
  FROM employees;
  ```

This cheat sheet is intended as a quick review of essential commands. Practicing their use with real examples will help you be ready for the interview.
