# VCET Job Portal — Visuals & Diagrams Dashboard

**Academic Project & Multi-Disciplinary Syllabus Implementation**  
- **Subject 1 (25ITT33):** Software Engineering  
- **Subject 2 (25ITT31):** Database Management Systems  
- **Subject 3 (25ITT32):** Java Programming  
- **Subject 4 (25ITC31):** Foundations of Data Science  

---

## Project Structure Overview

```
c:\JOB PORTAL
│
├── run_all.bat                               (MASTER LAUNCHER - Interactive Console Menu)
├── generate_dashboard.py                     (Visuals Scanner & Dashboard Generator)
├── visuals_dashboard.html                    (Interactive Web Dashboard for All Diagrams)
│
├── 1_Software_Engineering/
│   ├── Software_Engineering_Documentation.md  (SRS, Testing, Metrics & Estimation)
│   ├── generate_se_diagrams.py               (Diagram Generation Source Script)
│   ├── use_case_diagram.png                  (Use Case Diagram - Actors & Use Cases)
│   ├── class_diagram.png                     (UML Class Diagram - Object Model)
│   ├── sequence_diagram.png                  (Sequence Diagram - Validation Flow)
│   ├── activity_diagram.png                  (Activity Diagram - End-to-End Workflow)
│   ├── dfd_diagram.png                       (Data Flow Diagram Level 0 Context)
│   ├── architecture_diagram.png              (3-Tier Software Architecture)
│   ├── architecture_and_dfd_diagram.png      (DFD Level 0 & 3-Tier Architecture)
│   └── state_machine_diagram.png             (Application Lifecycle State Diagram)
│
├── 2_Database_Management_System/
│   ├── DBMS_Documentation.md                 (E-R Design, Relational Schema, 3NF, Queries)
│   ├── E_R_Diagram.png                       (Cheney E-R Diagram with Mapping Cardinalities)
│   ├── schema.sql                            (DDL: Tables, Constraints, Views, Triggers)
│   ├── sample_data.sql                       (DML: Rich Seed Data Across Departments)
│   ├── queries.sql                           (Advanced SQL Queries, Joins, Aggregations)
│   ├── dbms_interactive.py                   (Interactive DBMS Console with Manual Input)
│   ├── run_dbms.bat                          (Double-Click Runnable Batch File)
│   ├── dbms_output.txt                       (Captured DBMS Execution Output Text File)
│   └── screenshot_dbms_execution.png         (Screenshot of DBMS Program Execution)
│
├── 3_Java_Programming/
│   ├── Java_Programming_Documentation.md    (OOP Architecture, Generics, Streams)
│   ├── src/com/jobportal/                    (Java Packages: model, exception, service, thread, app)
│   ├── bin/                                  (Compiled Bytecode Classes)
│   ├── run_java.bat                          (Double-Click Runnable Batch File)
│   ├── java_output.txt                       (Captured Java Execution Output Text File)
│   └── screenshot_java_execution.png         (Screenshot of Java Program Execution)
│
└── 4_Foundation_of_Data_Science/
    ├── Data_Science_Documentation.md         (Descriptive Statistics, z-Scores, IQR)
    ├── recruitment_data.csv                  (Dataset for Preprocessing and EDA)
    ├── trend_analysis.py                     (Core Statistics, Wrangling & Plot Engine)
    ├── interactive_ds.py                     (Interactive CLI with Manual Keyboard Input)
    ├── run_datascience.bat                   (Double-Click Runnable Batch File)
    ├── datascience_output.txt                (Captured Data Science Execution Output)
    ├── screenshot_datascience_execution.png  (Screenshot of Data Science Execution)
    └── visualizations/                       (Generated High-Resolution Visual Plots)
        ├── 1_dept_applications_bar.png       (Bar Chart: Department Selections)
        ├── 2_status_distribution_pie.png     (Pie Chart: Application Status Distribution)
        ├── 3_salary_distribution_hist.png    (Histogram: Salary Distribution & KDE)
        ├── 4_cgpa_vs_salary_scatter.png      (Scatter Plot: CGPA vs Offered Salary)
        ├── 5_salary_by_dept_boxplot.png      (Box Plot: Salary Range Across Departments)
        └── 6_correlation_heatmap.png         (Heatmap: Pearson Correlation Matrix)
```

---

## Master Launcher & Visuals Dashboard

### Top-Level Launcher (`run_all.bat`)
Run the master launcher by double-clicking [run_all.bat](file:///C:/JOB%20PORTAL/run_all.bat) at the root of `C:\JOB PORTAL`. It provides a centralized interactive menu:
- **Option 1**: Software Engineering (opens [1_Software_Engineering](file:///C:/JOB%20PORTAL/1_Software_Engineering) and its documentation).
- **Option 2**: Database Management System (runs [run_dbms.bat](file:///C:/JOB%20PORTAL/2_Database_Management_System/run_dbms.bat)).
- **Option 3**: Java Programming (runs [run_java.bat](file:///C:/JOB%20PORTAL/3_Java_Programming/run_java.bat)).
- **Option 4**: Foundation of Data Science (runs [run_datascience.bat](file:///C:/JOB%20PORTAL/4_Foundation_of_Data_Science/run_datascience.bat)).
- **Option 5**: View Visuals & Diagrams Dashboard (scans all 17 visual assets across subfolders, generates/refreshes [visuals_dashboard.html](file:///C:/JOB%20PORTAL/visuals_dashboard.html), and opens it in your default web browser).
- **Option 6**: Exit.

---

## How to Test Each Category Interactively Step-by-Step

### 1. Database Management System (`2_Database_Management_System`)
- **Run File:** Double-click [`run_dbms.bat`](file:///C:/JOB%20PORTAL/2_Database_Management_System/run_dbms.bat)
- **Features Tested via Manual Keyboard Input:**
  - View all tables, vacancies, and application statuses.
  - Add new student profile and post new job vacancy interactively.
  - Test Duplicate Application Prevention (FR4) via manual entry.
  - Update status and verify database audit triggers.
  - Execute arbitrary ad-hoc SQL queries typed from keyboard.
- **Output Artifacts:** [`dbms_output.txt`](file:///C:/JOB%20PORTAL/2_Database_Management_System/dbms_output.txt), [`screenshot_dbms_execution.png`](file:///C:/JOB%20PORTAL/2_Database_Management_System/screenshot_dbms_execution.png), and [`E_R_Diagram.png`](file:///C:/JOB%20PORTAL/2_Database_Management_System/E_R_Diagram.png).

---

### 2. Java Programming (`3_Java_Programming`)
- **Run File:** Double-click [`run_java.bat`](file:///C:/JOB%20PORTAL/3_Java_Programming/run_java.bat)
- **Features Tested via Manual Keyboard Input:**
  - Register student profiles and post vacancies.
  - Apply for vacancies with instant validation:
    - *Eligibility check*: throws `IneligibleStudentException` if CGPA < required.
    - *Duplicate check*: throws `DuplicateApplicationException` if applied before.
  - Generate placement analytics via Java Stream API (`groupingBy`, `counting`).
  - Trigger multithreaded screening worker (`BatchApplicationProcessor`).
- **Output Artifacts:** [`java_output.txt`](file:///C:/JOB%20PORTAL/3_Java_Programming/java_output.txt) and [`screenshot_java_execution.png`](file:///C:/JOB%20PORTAL/3_Java_Programming/screenshot_java_execution.png).

---

### 3. Foundation of Data Science (`4_Foundation_of_Data_Science`)
- **Run File:** Double-click [`run_datascience.bat`](file:///C:/JOB%20PORTAL/4_Foundation_of_Data_Science/run_datascience.bat)
- **Features Tested via Manual Keyboard Input:**
  - Descriptive statistics (Mean, Median, Standard Deviation, Variance, Range).
  - Standard $(z)$ score calculations for candidate salaries and CGPAs.
  - Outlier detection using Tukey's $1.5 \times IQR$ rule.
  - Pivot tables comparing department vs recruitment status.
  - Manual filtering of candidates by department and CGPA.
  - Generate and inspect all 6 Matplotlib & Seaborn plots.
- **Output Artifacts:** [`datascience_output.txt`](file:///C:/JOB%20PORTAL/4_Foundation_of_Data_Science/datascience_output.txt), [`screenshot_datascience_execution.png`](file:///C:/JOB%20PORTAL/4_Foundation_of_Data_Science/screenshot_datascience_execution.png), and [`visualizations/`](file:///C:/JOB%20PORTAL/4_Foundation_of_Data_Science/visualizations).

---

### 4. Software Engineering (`1_Software_Engineering`)
- **Documentation:** [`Software_Engineering_Documentation.md`](file:///C:/JOB%20PORTAL/1_Software_Engineering/Software_Engineering_Documentation.md)
- **Diagrams:**
  - [`use_case_diagram.png`](file:///C:/JOB%20PORTAL/1_Software_Engineering/use_case_diagram.png)
  - [`class_diagram.png`](file:///C:/JOB%20PORTAL/1_Software_Engineering/class_diagram.png)
  - [`sequence_diagram.png`](file:///C:/JOB%20PORTAL/1_Software_Engineering/sequence_diagram.png)
  - [`activity_diagram.png`](file:///C:/JOB%20PORTAL/1_Software_Engineering/activity_diagram.png)
  - [`dfd_diagram.png`](file:///C:/JOB%20PORTAL/1_Software_Engineering/dfd_diagram.png)
  - [`architecture_diagram.png`](file:///C:/JOB%20PORTAL/1_Software_Engineering/architecture_diagram.png)
  - [`architecture_and_dfd_diagram.png`](file:///C:/JOB%20PORTAL/1_Software_Engineering/architecture_and_dfd_diagram.png)
  - [`state_machine_diagram.png`](file:///C:/JOB%20PORTAL/1_Software_Engineering/state_machine_diagram.png)
