-- ============================================================================
-- ONLINE JOB PORTAL AND EMPLOYMENT TREND ANALYSIS SYSTEM
-- DATABASE MANAGEMENT SYSTEM SAMPLE DATA (DML)
-- ============================================================================

-- 1. Insert Departments
INSERT INTO departments (dept_id, dept_name) VALUES
('IT', 'Information Technology'),
('CSE', 'Computer Science and Engineering'),
('ECE', 'Electronics and Communication Engineering'),
('MECH', 'Mechanical Engineering'),
('AIDS', 'Artificial Intelligence and Data Science');

-- 2. Insert Companies
INSERT INTO companies (company_id, company_name, industry, location, contact_email) VALUES
('CMP101', 'Google India', 'Product / Internet', 'Bengaluru', 'careers@google.com'),
('CMP102', 'Microsoft IDC', 'Product / Cloud', 'Hyderabad', 'recruitment@microsoft.com'),
('CMP103', 'Amazon Dev Centre', 'E-Commerce / Cloud', 'Chennai', 'jobs@amazon.com'),
('CMP104', 'Tata Consultancy Services', 'IT Services', 'Chennai', 'campus@tcs.com'),
('CMP105', 'Zoho Corporation', 'SaaS Software', 'Tenkasi', 'talent@zohocorp.com'),
('CMP106', 'Bosch Global Software', 'Automotive / Embedded', 'Coimbatore', 'careers@bosch.com');

-- 3. Insert Students (Job Seekers)
INSERT INTO students (student_id, name, dept_id, qualification, cgpa, skills, email) VALUES
('STU001', 'Aarav Sharma', 'IT', 'B.Tech IT', 8.75, 'Java, Python, SQL, Spring Boot', 'aarav.sharma@campus.edu'),
('STU002', 'Diya Patel', 'CSE', 'B.E CSE', 9.20, 'Python, Machine Learning, SQL, C++', 'diya.patel@campus.edu'),
('STU003', 'Rohan Verma', 'ECE', 'B.E ECE', 7.80, 'Embedded C, IoT, Python, MATLAB', 'rohan.verma@campus.edu'),
('STU004', 'Ananya Iyer', 'AIDS', 'B.Tech AIDS', 8.90, 'Python, Data Science, Pandas, PowerBI', 'ananya.iyer@campus.edu'),
('STU005', 'Karthik Raja', 'MECH', 'B.E MECH', 7.45, 'AutoCAD, SolidWorks, Python, ANSYS', 'karthik.raja@campus.edu'),
('STU006', 'Sneha Menon', 'IT', 'B.Tech IT', 8.10, 'Java, React, SQL, HTML/CSS', 'sneha.menon@campus.edu'),
('STU007', 'Vikramaditya Rao', 'CSE', 'B.E CSE', 8.65, 'Java, Spring Boot, Microservices, Docker', 'vikram.rao@campus.edu'),
('STU008', 'Pooja Hegde', 'ECE', 'B.E ECE', 8.05, 'VLSI, Verilog, C, Python', 'pooja.hegde@campus.edu'),
('STU009', 'Naveen Kumar', 'AIDS', 'B.Tech AIDS', 9.05, 'Deep Learning, NLP, Python, PyTorch', 'naveen.kumar@campus.edu'),
('STU010', 'Meera Krishnan', 'IT', 'B.Tech IT', 7.60, 'Python, Django, PostgreSQL, Git', 'meera.krishnan@campus.edu'),
('STU011', 'Arjun Das', 'CSE', 'B.E CSE', 7.95, 'Java, Kotlin, Android, SQLite', 'arjun.das@campus.edu'),
('STU012', 'Harini Sundar', 'AIDS', 'B.Tech AIDS', 8.40, 'Tableau, SQL, Python, Statistics', 'harini.sundar@campus.edu');

-- 4. Insert Job Vacancies
INSERT INTO job_vacancies (vacancy_id, company_id, job_title, min_cgpa, required_skills, location, salary, openings) VALUES
('VAC201', 'CMP101', 'Software Development Engineer', 8.50, 'Java, Data Structures, Algorithms', 'Bengaluru', 1800000, 5),
('VAC202', 'CMP102', 'Cloud Solutions Associate', 8.00, 'Cloud, Python, Linux, Networking', 'Hyderabad', 1500000, 8),
('VAC203', 'CMP103', 'Data Engineer', 8.00, 'Python, SQL, Spark, Big Data', 'Chennai', 1600000, 4),
('VAC204', 'CMP104', 'Systems Engineer', 7.00, 'Java, C++, DBMS, Communication', 'Chennai', 450000, 25),
('VAC205', 'CMP105', 'Product Developer', 7.50, 'Java, C, Web Development, Problem Solving', 'Tenkasi', 850000, 10),
('VAC206', 'CMP106', 'Embedded Software Engineer', 7.50, 'Embedded C, Microcontrollers, RTOS', 'Coimbatore', 700000, 6);

-- 5. Insert Applications
-- Tracking statuses: Applied, Shortlisted, Selected, Rejected
INSERT INTO applications (student_id, vacancy_id, apply_date, status) VALUES
('STU001', 'VAC201', '2026-09-01', 'Selected'),
('STU001', 'VAC205', '2026-09-03', 'Shortlisted'),
('STU002', 'VAC201', '2026-09-01', 'Selected'),
('STU002', 'VAC203', '2026-09-02', 'Shortlisted'),
('STU003', 'VAC206', '2026-09-04', 'Selected'),
('STU003', 'VAC204', '2026-09-05', 'Applied'),
('STU004', 'VAC203', '2026-09-02', 'Selected'),
('STU004', 'VAC202', '2026-09-03', 'Shortlisted'),
('STU005', 'VAC204', '2026-09-06', 'Applied'),
('STU006', 'VAC205', '2026-09-04', 'Selected'),
('STU006', 'VAC204', '2026-09-05', 'Shortlisted'),
('STU007', 'VAC201', '2026-09-01', 'Shortlisted'),
('STU007', 'VAC202', '2026-09-02', 'Selected'),
('STU008', 'VAC206', '2026-09-04', 'Shortlisted'),
('STU008', 'VAC204', '2026-09-05', 'Applied'),
('STU009', 'VAC201', '2026-09-01', 'Rejected'),
('STU009', 'VAC203', '2026-09-02', 'Selected'),
('STU010', 'VAC204', '2026-09-06', 'Selected'),
('STU011', 'VAC205', '2026-09-04', 'Shortlisted'),
('STU012', 'VAC203', '2026-09-03', 'Applied');
