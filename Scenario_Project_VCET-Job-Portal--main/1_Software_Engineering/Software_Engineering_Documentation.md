# Category 1: Software Engineering
**Course Code:** 25ITT33 - Software Engineering  
**System:** Online Job Portal and Employment Trend Analysis System  

---

## 1. Syllabus Evaluation & Requirements Categorization

| Unit | Syllabus Topics (25ITT33) | System Implementation & Functional Requirements |
|---|---|---|
| **Unit 1: Software Process** | Nature of Software, Software Process Models (Generic, Prescriptive, Unified, Agile Scrum, XP), Software Myths. | Selected **Agile Scrum Methodology** with 2-week iterations. Dispelled placement automation myths (e.g., "Automated portals increase placement officer workload"). |
| **Unit 2: Requirements Analysis & Specification** | Requirements Engineering (Elicitation, Specification, Validation, Change), Data Modeling, Class-Based Modeling. | Formulated Software Requirements Specification (SRS) for FR1 to FR7. Developed Use Case Specifications, Data Flow Diagrams (DFD Level 0 & 1), and Class-Based Domain Models. |
| **Unit 3: Software Design** | Design Process & Concepts, Architectural Design (3-Tier Style), Interface Design, Component-Level Design, Web-App Design. | Implemented a clean **3-Tier Architecture** (Presentation, Business Logic, Data Persistence). Designed interactive console UX and visualization dashboards. |
| **Unit 4: Software Testing** | Verification & Validation, Unit/Integration/Validation Testing, Black-Box Testing (BVA, Equivalence Partitioning), White-Box Testing (Basis Path, Cyclomatic Complexity). | Built comprehensive test cases for eligibility checking (FR3) and duplicate application blocking (FR4). Calculated Cyclomatic Complexity ($V(G) = 4$) for `applyForJob()` logic. |
| **Unit 5: Project Management & Metrics** | 4P's (People, Product, Process, Project), LOC, Function Point (FP) Analysis, Project Scheduling, COCOMO Cost Modeling, Risk Identification & Management. | Estimated project metrics ($LOC \approx 1,250$, Unadjusted FP = $64$, COCOMO effort = $3.8$ Person-Months). Formulated Risk Management & Mitigation matrix. |

---

## 2. Software Requirements Specification (SRS)

### 2.1 Problem Statement & Scope
Manual record keeping of students, recruiters, and placement drives leads to delays, inaccurate tracking, duplicate applications, and zero visibility into cross-departmental hiring trends. The proposed system replaces manual logbooks with an integrated 3-tier software solution incorporating Java business logic, SQLite relational persistence, and Python data science trend analytics.

### 2.2 Functional Requirements (FR) Traceability Matrix

| Req ID | Functional Requirement Description | Target Category | Implementation Module |
|---|---|---|---|
| **FR1** | Maintain student / job seeker details (ID, name, dept, qualification, skills, CGPA). | Software Engineering / Java / DBMS | `Student.java`, `students` table, `manualRegisterStudent()` |
| **FR2** | Maintain company details and job vacancies (title, eligibility criteria, location, salary). | Software Engineering / Java / DBMS | `Company.java`, `JobVacancy.java`, `job_vacancies` table |
| **FR3** | Allow eligible students to apply for vacancies (CGPA criteria validation). | Java Programming / DBMS | `applyForJob()`, `IneligibleStudentException.java` |
| **FR4** | Prevent duplicate applications by same student for the same vacancy. | DBMS / Java Programming | `uq_student_vacancy` SQL constraint, `DuplicateApplicationException.java` |
| **FR5** | Track recruitment status (Applied, Shortlisted, Selected, Rejected). | Java / DBMS / Data Science | `ApplicationStatus.java`, `application_audit_log` trigger |
| **FR6** | Generate placement reports (vacancies, applications, selection counts, company recruitment). | Java Programming / DBMS | Java 8 Streams (`Collectors.groupingBy`), SQL Views |
| **FR7** | Retrieve data from database, preprocess it, and generate visual charts in Python. | Foundation of Data Science | `trend_analysis.py`, Matplotlib & Seaborn visual plots |

### 2.3 Non-Functional Requirements (NFR)
1. **Performance**: Query response time $< 0.1$ seconds for student and vacancy retrieval.
2. **Data Integrity & Consistency**: Enforce strict relational foreign keys and unique constraints ($O(1)$ duplicate lookup).
3. **Usability**: Interactive CLI menus supporting step-by-step keyboard inputs with descriptive validation messages.
4. **Reliability & Concurrency**: Synchronized multithreaded application screening without race conditions.

---

## 3. Software Design & Architectural Models

### 3.1 3-Tier Architecture
```
+-------------------------------------------------------------------------+
|                        PRESENTATION LAYER                               |
|   - Java Console Application (Interactive Keyboard Input)               |
|   - SQLite DBMS Interactive Tool (Ad-hoc SQL Console)                   |
|   - Data Science Interactive CLI & Matplotlib/Seaborn Dashboards        |
+------------------------------------+------------------------------------+
                                     | Data Exchange
+------------------------------------v------------------------------------+
|                       BUSINESS LOGIC LAYER (Java)                       |
|   - Eligibility Validation Engine (FR3)                                 |
|   - Duplicate Application Prevention Engine (FR4)                       |
|   - Application Lifecycle Transition Engine (FR5)                       |
|   - Multithreaded Batch Screening Worker (Unit 3 Multithreading)        |
|   - Stream API Analytics & Reporting Service (FR6)                      |
+------------------------------------+------------------------------------+
                                     | SQL / CSV Interface
+------------------------------------v------------------------------------+
|                    DATA PERSISTENCE LAYER (DBMS)                        |
|   - Relational Tables (departments, students, companies, vacancies)    |
|   - Table Constraint: UNIQUE(student_id, vacancy_id)                    |
|   - Audit Logging Triggers & Aggregation Views                          |
|   - Preprocessed CSV Data Stores for Python Trend Analysis              |
+-------------------------------------------------------------------------+
```

---

## 4. Software Testing & Quality Assurance

### 4.1 White-Box Testing: Basis Path Testing
**Target Method:** `JobPortalServiceImpl.applyForJob(studentId, vacancyId)`

#### Control Flow Graph (CFG) & Cyclomatic Complexity:
1. Node 1: Check if `vacancyId` exists. (If not, throw `VacancyNotFoundException`)
2. Node 2: Check if `studentId` exists. (If not, throw `IllegalArgumentException`)
3. Node 3: Check if `applicationKeys.contains(key)`. (If true, throw `DuplicateApplicationException`)
4. Node 4: Check if `student.getCgpa() < vacancy.getMinCgpa()`. (If true, throw `IneligibleStudentException`)
5. Node 5: Create and commit `JobApplication` with status `Applied`.

**Cyclomatic Complexity Calculation:**
$$V(G) = P + 1 = 4 \text{ predicate nodes} + 1 = 5 \text{ linearly independent paths}$$

#### Basis Paths:
- **Path 1:** $1 \rightarrow \text{VacancyNotFoundException}$
- **Path 2:** $1 \rightarrow 2 \rightarrow \text{IllegalArgumentException}$
- **Path 3:** $1 \rightarrow 2 \rightarrow 3 \rightarrow \text{DuplicateApplicationException}$ **(FR4 Verified)**
- **Path 4:** $1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow \text{IneligibleStudentException}$ **(FR3 Verified)**
- **Path 5:** $1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5 \rightarrow \text{Success (Application Created)}$

### 4.2 Test Cases Suite (Black-Box & Boundary Value Analysis)

| Test ID | Test Scenario | Input Data | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| **TC-01** | Student Profile Registration | ID: `STU015`, Name: `Priyan`, Dept: `IT`, CGPA: `8.5` | Student added to registry | Student registered successfully | **PASSED** |
| **TC-02** | Vacancy Posting | Company: `CMP101`, Title: `SDE`, Min CGPA: `8.5` | Vacancy published | Vacancy posted in system | **PASSED** |
| **TC-03** | Eligible Application Submission | Student: `STU001` (CGPA 8.75), Vacancy: `VAC201` (Req 8.5) | Application created with status `Applied` | Application #1012 created | **PASSED** |
| **TC-04** | Duplicate Application Prevention (FR4) | Student: `STU001`, Vacancy: `VAC201` (Repeat) | `DuplicateApplicationException` thrown | Blocked with custom exception | **PASSED** |
| **TC-05** | Eligibility Check Failure (FR3) | Student: `STU005` (CGPA 7.45), Vacancy: `VAC201` (Req 8.5) | `IneligibleStudentException` thrown | Blocked with criteria message | **PASSED** |
| **TC-06** | Status Transition (FR5) | App ID: `1001`, New Status: `Selected` | Status updated; audit log triggered | Transition logged to audit table | **PASSED** |
| **TC-07** | Placement Report Generation (FR6) | Stream API grouping by Department | Aggregated counts returned | Accurate counts grouped | **PASSED** |
| **TC-08** | Data Science EDA & Plots (FR7) | Run `trend_analysis.py` | 6 visual PNG charts generated | All 6 charts saved in folder | **PASSED** |

---

## 5. Project Estimation & Metrics (Unit 5)

### 5.1 Function Point (FP) Analysis
- External Inputs (EI): 5 (Student reg, Vacancy post, Apply, Status update, Custom SQL) $\times 4 = 20$
- External Outputs (EO): 4 (Reports, Trend charts, Confirmation receipts) $\times 5 = 20$
- External Inquiries (EQ): 3 (Search vacancies, View status, Candidate filter) $\times 3 = 9$
- Internal Logical Files (ILF): 3 (Students, Vacancies, Applications) $\times 7 = 21$
- External Interface Files (EIF): 1 (Department reference) $\times 5 = 5$
- **Total Unadjusted Function Points (UFP):** $75$
- Adjusted Function Points ($FP = UFP \times [0.65 + 0.01 \times \sum TDI]$) $\approx \mathbf{72.5}$

### 5.2 COCOMO Model (Basic)
Using organic project constants ($a = 2.4, b = 1.05, c = 2.5, d = 0.38$):
- Estimated $KLOC \approx 1.25$
- $\text{Effort} = 2.4 \times (1.25)^{1.05} \approx \mathbf{3.04} \text{ Person-Months}$
- $\text{Development Time} = 2.5 \times (3.04)^{0.38} \approx \mathbf{3.8} \text{ Months}$

---

## 6. Diagrams Generated in This Folder
1. `use_case_diagram.png`: Actors (Student, Recruiter, Placement Officer) and System Boundary.
2. `class_diagram.png`: UML Class Hierarchy, Associations, Encapsulation, and Interfaces.
3. `sequence_diagram.png`: Lifelines, Message Sequence, and Duplicate/Eligibility Validation.
4. `activity_diagram.png`: End-to-end recruitment process workflow.
5. `dfd_diagram.png`: Context Data Flow Diagram (DFD Level 0).
6. `architecture_diagram.png`: 3-Tier Software Architecture (Presentation, Business Logic, Persistence).
7. `architecture_and_dfd_diagram.png`: Combined Context DFD Level 0 and 3-Tier Architectural Style.
8. `state_machine_diagram.png`: State transitions of application lifecycle (`Applied` $\rightarrow$ `Shortlisted` $\rightarrow$ `Selected` / `Rejected`).
