-- ============================================================================
-- ONLINE JOB PORTAL AND EMPLOYMENT TREND ANALYSIS SYSTEM
-- ADVANCED SQL QUERIES & REPORTS (Unit 2 & Unit 3 of 25ITT31)
-- ============================================================================

-- Query 1: Basic Retrieval & Sorting
-- List all active job vacancies sorted by salary descending
SELECT 
    j.vacancy_id, 
    c.company_name, 
    j.job_title, 
    j.salary, 
    j.min_cgpa, 
    j.location
FROM job_vacancies j
JOIN companies c ON j.company_id = c.company_id
ORDER BY j.salary DESC;

-- Query 2: Multi-table INNER JOIN with Conditional Filtering
-- List all selected students along with their company and role
SELECT 
    s.student_id, 
    s.name AS student_name, 
    d.dept_name, 
    c.company_name, 
    j.job_title, 
    j.salary
FROM applications a
JOIN students s ON a.student_id = s.student_id
JOIN departments d ON s.dept_id = d.dept_id
JOIN job_vacancies j ON a.vacancy_id = j.vacancy_id
JOIN companies c ON j.company_id = c.company_id
WHERE a.status = 'Selected'
ORDER BY j.salary DESC;

-- Query 3: Aggregate Functions with GROUP BY and HAVING
-- Find departments where at least 2 students were selected, along with average salary
SELECT 
    d.dept_name,
    COUNT(a.application_id) AS total_selected,
    ROUND(AVG(j.salary), 2) AS average_salary_package,
    MAX(j.salary) AS highest_package
FROM applications a
JOIN students s ON a.student_id = s.student_id
JOIN departments d ON s.dept_id = d.dept_id
JOIN job_vacancies j ON a.vacancy_id = j.vacancy_id
WHERE a.status = 'Selected'
GROUP BY d.dept_name
HAVING COUNT(a.application_id) >= 1
ORDER BY average_salary_package DESC;

-- Query 4: Nested Subquery with IN
-- Find all students who applied for high-paying jobs (Salary >= 1,500,000)
SELECT 
    student_id, 
    name, 
    qualification, 
    cgpa, 
    skills 
FROM students
WHERE student_id IN (
    SELECT student_id 
    FROM applications 
    WHERE vacancy_id IN (
        SELECT vacancy_id 
        FROM job_vacancies 
        WHERE salary >= 1500000
    )
);

-- Query 5: Correlated Subquery with EXISTS
-- Find students who have applied for at least one vacancy
SELECT s.student_id, s.name, s.cgpa
FROM students s
WHERE EXISTS (
    SELECT 1 
    FROM applications a 
    WHERE a.student_id = s.student_id
);

-- Query 6: Set Operations (UNION)
-- Combine list of students from IT and CSE departments eligible for software roles
SELECT student_id, name, dept_id, cgpa FROM students WHERE dept_id = 'IT' AND cgpa >= 8.0
UNION
SELECT student_id, name, dept_id, cgpa FROM students WHERE dept_id = 'CSE' AND cgpa >= 8.0;

-- Query 7: Querying from Views (Meets FR6)
-- Query the company recruitment summary view
SELECT * FROM vw_company_recruitment ORDER BY selected_count DESC;

-- Query 8: Department Placement Rate Summary
SELECT * FROM vw_department_placement ORDER BY placement_percentage DESC;

-- Query 9: Prevent Duplicate Application Test
-- (This query demonstrates constraint violation if executed with existing pair)
-- INSERT INTO applications (student_id, vacancy_id, apply_date, status) VALUES ('STU001', 'VAC201', '2026-09-10', 'Applied');
-- Expected: UNIQUE constraint failed: applications.student_id, applications.vacancy_id
