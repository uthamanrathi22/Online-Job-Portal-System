# Category 2: Database Management System (DBMS)
**Course Code:** 25ITT31 - Database Management Systems  
**System:** Online Job Portal and Employment Trend Analysis System  

---

## 1. Syllabus Evaluation & Requirements Mapping

| Unit | Syllabus Topics (25ITT31) | System Implementation & Functional Requirements |
|---|---|---|
| **Unit 1: Database Systems and Design** | Purpose of Database Systems, Architecture, Data Models, E-R Model, Complex & Multivalued Attributes, Mapping Cardinalities, E-R Diagrams, Relational Schema, Keys. | Designed Cheney E-R Diagram and Relational Schema connecting `STUDENT`, `COMPANY`, `JOB_VACANCY`, `APPLICATION`, and `DEPARTMENT`. Addressed manual record-keeping bottlenecks. |
| **Unit 2: SQL** | Data types, DDL, DML, Basic Queries, Set Operations, Null Values, Aggregate Functions, Nested Sub-queries, Joins, Views, Integrity Constraints, Triggers. | Implemented `schema.sql`, `sample_data.sql`, and `queries.sql`. Built views (`vw_student_applications`, `vw_company_recruitment`, `vw_department_placement`) and audit triggers (`trg_audit_application_status`). |
| **Unit 3: Normalization & Query Optimization** | Functional Dependencies, Armstrong's Axioms, Normal Forms (1NF, 2NF, 3NF, BCNF), Indexing, B+ Tree concepts. | Normalized relational relations to 3NF/BCNF eliminating redundancy, insertion, update, and deletion anomalies. Created secondary B-Tree indexes on foreign keys. |
| **Unit 4: Transaction Management** | ACID Properties, Concurrency Control, Serializability, Logging. | Enforced atomicity and consistency during job application submission and status updates. |
| **Unit 5: NoSQL Databases** | Document, Key-Value, Column, Graph Databases, CAP Theorem. | Documented contrast between ACID relational model and distributed NoSQL options for recruitment analytics. |

---

## 2. Relational Schema & 3NF Normalization

### Relational Tables:
1. **`departments`** (`dept_id` [PK], `dept_name`)
   - Functional Dependency: $dept\_id \rightarrow dept\_name$
   - In BCNF / 3NF since determinant is superkey.
2. **`students`** (`student_id` [PK], `name`, `dept_id` [FK], `qualification`, `cgpa`, `skills`, `email` [UNIQUE])
   - Functional Dependencies: $student\_id \rightarrow name, dept\_id, qualification, cgpa, skills, email$
   - $email \rightarrow student\_id$
   - In 3NF / BCNF.
3. **`companies`** (`company_id` [PK], `company_name` [UNIQUE], `industry`, `location`, `contact_email`)
   - Functional Dependencies: $company\_id \rightarrow company\_name, industry, location, contact\_email$
   - In 3NF / BCNF.
4. **`job_vacancies`** (`vacancy_id` [PK], `company_id` [FK], `job_title`, `min_cgpa`, `required_skills`, `location`, `salary`, `openings`)
   - Functional Dependencies: $vacancy\_id \rightarrow company\_id, job\_title, min\_cgpa, required\_skills, location, salary, openings$
   - In 3NF / BCNF.
5. **`applications`** (`application_id` [PK], `student_id` [FK], `vacancy_id` [FK], `apply_date`, `status`, `UNIQUE(student_id, vacancy_id)`)
   - Functional Dependencies: $application\_id \rightarrow student\_id, vacancy\_id, apply\_date, status$
   - $(student\_id, vacancy\_id) \rightarrow application\_id, apply\_date, status$
   - In 3NF / BCNF.

### Critical Constraints Addressing Requirements:
- **FR4: Prevent Duplicate Applications**: Enforced via table-level constraint:
  ```sql
  CONSTRAINT uq_student_vacancy UNIQUE (student_id, vacancy_id)
  ```
- **FR5: Track Application Status**: Enforced via CHECK constraint:
  ```sql
  CHECK (status IN ('Applied', 'Shortlisted', 'Selected', 'Rejected'))
  ```

---

## 3. How to Run the Program

1. **Interactive Manual Keyboard Mode (`run_dbms.bat`)**:
   - Double-click `run_dbms.bat` in this folder.
   - Choose menu options (1 through 11) to add students, post vacancies, apply for jobs, update statuses, or execute ad-hoc SQL queries typed from your keyboard.
2. **Automated Verification Mode**:
   ```cmd
   python dbms_interactive.py --auto
   ```
   This regenerates `job_portal.db` and writes full query outputs to `dbms_output.txt`.

---

## 4. Folder Artifacts Checklist
- [x] `E_R_Diagram.png`: Publication-grade Entity-Relationship Diagram.
- [x] `schema.sql`: DDL tables, views, indexes, and triggers.
- [x] `sample_data.sql`: DML seed script.
- [x] `queries.sql`: Advanced SQL analytical queries.
- [x] `dbms_interactive.py`: Python CLI supporting step-by-step manual keyboard input.
- [x] `run_dbms.bat`: Double-clickable runnable batch script.
- [x] `dbms_output.txt`: Execution output text file.
- [x] `screenshot_dbms_execution.png`: Screenshot of DBMS execution.
