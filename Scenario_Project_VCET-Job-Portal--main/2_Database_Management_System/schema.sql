-- ============================================================================
-- ONLINE JOB PORTAL AND EMPLOYMENT TREND ANALYSIS SYSTEM
-- DATABASE MANAGEMENT SYSTEM SCHEMA (DDL)
-- Subject Code: 25ITT31 - Database Management Systems
-- ============================================================================

-- Drop existing tables to ensure clean setup
DROP TABLE IF EXISTS application_audit_log;
DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS job_vacancies;
DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS departments;

-- 1. Departments Table
CREATE TABLE departments (
    dept_id VARCHAR(10) PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE
);

-- 2. Students Table (Job Seekers)
-- Meets FR1: Maintain student details including ID, name, department, qualification, skills
CREATE TABLE students (
    student_id VARCHAR(15) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept_id VARCHAR(10) NOT NULL,
    qualification VARCHAR(50) NOT NULL,
    cgpa REAL NOT NULL CHECK(cgpa >= 0.0 AND cgpa <= 10.0),
    skills TEXT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- 3. Companies Table
-- Meets FR2: Maintain company details
CREATE TABLE companies (
    company_id VARCHAR(15) PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL UNIQUE,
    industry VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL
);

-- 4. Job Vacancies Table
-- Meets FR2: Maintain job vacancy information (job title, eligibility criteria, location, salary range)
CREATE TABLE job_vacancies (
    vacancy_id VARCHAR(15) PRIMARY KEY,
    company_id VARCHAR(15) NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    min_cgpa REAL NOT NULL CHECK(min_cgpa >= 0.0 AND min_cgpa <= 10.0),
    required_skills TEXT NOT NULL,
    location VARCHAR(100) NOT NULL,
    salary REAL NOT NULL CHECK(salary > 0),
    openings INT NOT NULL CHECK(openings > 0),
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- 5. Applications Table
-- Meets FR3: Allow eligible students to apply
-- Meets FR4: Prevent duplicate applications via UNIQUE(student_id, vacancy_id)
-- Meets FR5: Track application status (Applied, Shortlisted, Selected, Rejected)
CREATE TABLE applications (
    application_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id VARCHAR(15) NOT NULL,
    vacancy_id VARCHAR(15) NOT NULL,
    apply_date TEXT NOT NULL DEFAULT (CURRENT_DATE),
    status VARCHAR(20) NOT NULL DEFAULT 'Applied' CHECK(status IN ('Applied', 'Shortlisted', 'Selected', 'Rejected')),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (vacancy_id) REFERENCES job_vacancies(vacancy_id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT uq_student_vacancy UNIQUE (student_id, vacancy_id)
);

-- 6. Application Audit Log Table (Tracking status transitions)
CREATE TABLE application_audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id INT NOT NULL,
    student_id VARCHAR(15) NOT NULL,
    vacancy_id VARCHAR(15) NOT NULL,
    old_status VARCHAR(20),
    new_status VARCHAR(20),
    change_timestamp TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP)
);

-- ============================================================================
-- INDEXES FOR QUERY OPTIMIZATION (Unit 3)
-- ============================================================================
CREATE INDEX idx_student_dept ON students(dept_id);
CREATE INDEX idx_vacancy_company ON job_vacancies(company_id);
CREATE INDEX idx_app_student ON applications(student_id);
CREATE INDEX idx_app_vacancy ON applications(vacancy_id);
CREATE INDEX idx_app_status ON applications(status);

-- ============================================================================
-- VIEWS FOR REPORTING (Unit 2 & Meets FR6)
-- ============================================================================

-- View 1: Detailed Application View
CREATE VIEW vw_student_applications AS
SELECT 
    a.application_id,
    s.student_id,
    s.name AS student_name,
    d.dept_name,
    s.cgpa,
    c.company_name,
    j.job_title,
    j.salary,
    a.apply_date,
    a.status
FROM applications a
JOIN students s ON a.student_id = s.student_id
JOIN departments d ON s.dept_id = d.dept_id
JOIN job_vacancies j ON a.vacancy_id = j.vacancy_id
JOIN companies c ON j.company_id = c.company_id;

-- View 2: Company-wise Recruitment Summary
CREATE VIEW vw_company_recruitment AS
SELECT 
    c.company_id,
    c.company_name,
    COUNT(DISTINCT j.vacancy_id) AS total_vacancies_posted,
    COUNT(a.application_id) AS total_applicants,
    SUM(CASE WHEN a.status = 'Selected' THEN 1 ELSE 0 END) AS selected_count,
    ROUND(AVG(j.salary), 2) AS avg_package_offered
FROM companies c
LEFT JOIN job_vacancies j ON c.company_id = j.company_id
LEFT JOIN applications a ON j.vacancy_id = a.vacancy_id
GROUP BY c.company_id, c.company_name;

-- View 3: Department-wise Placement Statistics
CREATE VIEW vw_department_placement AS
SELECT 
    d.dept_id,
    d.dept_name,
    COUNT(DISTINCT s.student_id) AS total_students,
    COUNT(DISTINCT CASE WHEN a.status = 'Selected' THEN s.student_id END) AS placed_students,
    ROUND(
        (COUNT(DISTINCT CASE WHEN a.status = 'Selected' THEN s.student_id END) * 100.0) / 
        COUNT(DISTINCT s.student_id), 2
    ) AS placement_percentage
FROM departments d
LEFT JOIN students s ON d.dept_id = s.dept_id
LEFT JOIN applications a ON s.student_id = a.student_id
GROUP BY d.dept_id, d.dept_name;

-- ============================================================================
-- TRIGGERS (Unit 2: Integrity & Audit)
-- ============================================================================

-- Trigger 1: Record status change in audit log
CREATE TRIGGER trg_audit_application_status
AFTER UPDATE OF status ON applications
BEGIN
    INSERT INTO application_audit_log (application_id, student_id, vacancy_id, old_status, new_status, change_timestamp)
    VALUES (OLD.application_id, OLD.student_id, OLD.vacancy_id, OLD.status, NEW.status, CURRENT_TIMESTAMP);
END;

-- Trigger 2: Log newly created application
CREATE TRIGGER trg_audit_application_insert
AFTER INSERT ON applications
BEGIN
    INSERT INTO application_audit_log (application_id, student_id, vacancy_id, old_status, new_status, change_timestamp)
    VALUES (NEW.application_id, NEW.student_id, NEW.vacancy_id, 'None', NEW.status, CURRENT_TIMESTAMP);
END;
