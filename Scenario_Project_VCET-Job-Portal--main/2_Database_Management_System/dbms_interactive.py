#!/usr/bin/env python3
"""
Online Job Portal and Employment Trend Analysis System
Interactive DBMS Console Application (Subject Code: 25ITT31)
Supports Step-by-Step Manual Keyboard Input and Interactive Testing
"""

import sqlite3
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "job_portal.db")
SCHEMA_FILE = os.path.join(BASE_DIR, "schema.sql")
DATA_FILE = os.path.join(BASE_DIR, "sample_data.sql")
OUTPUT_FILE = os.path.join(BASE_DIR, "dbms_output.txt")

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_database(log_to_file=False):
    """Initializes the database schema and loads sample data."""
    output_lines = []
    output_lines.append("================================================================================")
    output_lines.append("              INITIALIZING JOB PORTAL DATABASE (SQLite RDBMS)")
    output_lines.append("================================================================================")
    
    if os.path.exists(DB_FILE):
        try:
            os.remove(DB_FILE)
            output_lines.append(f"[INFO] Removed existing database: {DB_FILE}")
        except Exception as e:
            output_lines.append(f"[WARN] Could not remove old db: {e}")

    conn = get_connection()
    cursor = conn.cursor()

    # Execute schema.sql
    if os.path.exists(SCHEMA_FILE):
        with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
            schema_script = f.read()
        cursor.executescript(schema_script)
        output_lines.append(f"[SUCCESS] Executed {SCHEMA_FILE}: Tables, Views, Triggers created successfully.")
    else:
        output_lines.append(f"[ERROR] {SCHEMA_FILE} not found!")

    # Execute sample_data.sql
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data_script = f.read()
        cursor.executescript(data_script)
        conn.commit()
        output_lines.append(f"[SUCCESS] Executed {DATA_FILE}: Sample records populated.")
    else:
        output_lines.append(f"[ERROR] {DATA_FILE} not found!")

    # Count records
    for table in ["departments", "students", "companies", "job_vacancies", "applications"]:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        output_lines.append(f"  -> Table '{table}': {count} records loaded.")

    conn.close()
    
    msg = "\n".join(output_lines)
    print(msg)
    if log_to_file:
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n\n")

def display_table(query, title="QUERY RESULTS", log_to_file=False):
    """Executes a query and displays formatted tabular output."""
    conn = get_connection()
    cursor = conn.cursor()
    output_lines = []
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        
        # Calculate column widths
        col_widths = [len(c) for c in columns]
        for row in rows:
            for i, val in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(val if val is not None else "NULL")))
        
        header_sep = "+" + "+".join(["-" * (w + 2) for w in col_widths]) + "+"
        header_str = "|" + "|".join([f" {columns[i].ljust(col_widths[i])} " for i in range(len(columns))]) + "|"
        
        output_lines.append("\n" + "=" * len(header_sep))
        output_lines.append(f" {title.center(len(header_sep) - 2)}")
        output_lines.append("=" * len(header_sep))
        output_lines.append(header_sep)
        output_lines.append(header_str)
        output_lines.append(header_sep)
        
        for row in rows:
            row_str = "|" + "|".join([f" {str(val if val is not None else 'NULL').ljust(col_widths[i])} " for i, val in enumerate(row)]) + "|"
            output_lines.append(row_str)
        
        output_lines.append(header_sep)
        output_lines.append(f"Total Rows: {len(rows)}")
    except Exception as e:
        output_lines.append(f"[ERROR] Query Execution Failed: {e}")
    finally:
        conn.close()

    result_text = "\n".join(output_lines)
    print(result_text)
    if log_to_file:
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(result_text + "\n\n")

def manual_add_student():
    """FR1: Maintain student details via manual keyboard input."""
    print("\n--- [MANUAL INPUT] ADD NEW STUDENT ---")
    student_id = input("Enter Student ID (e.g. STU013): ").strip()
    name = input("Enter Full Name (e.g. Priyan Sharma): ").strip()
    print("Available Depts: IT, CSE, ECE, MECH, AIDS")
    dept_id = input("Enter Department ID: ").strip().upper()
    qualification = input("Enter Qualification (e.g. B.Tech IT): ").strip()
    try:
        cgpa = float(input("Enter CGPA (0.0 - 10.0): ").strip())
    except ValueError:
        print("[ERROR] Invalid CGPA! Must be a numeric value.")
        return
    skills = input("Enter Skills (e.g. Java, Python, SQL): ").strip()
    email = input("Enter Email: ").strip()

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students (student_id, name, dept_id, qualification, cgpa, skills, email)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (student_id, name, dept_id, qualification, cgpa, skills, email))
        conn.commit()
        print(f"[SUCCESS] Student '{name}' ({student_id}) inserted successfully!")
    except Exception as e:
        print(f"[DATABASE ERROR] Failed to insert student: {e}")
    finally:
        conn.close()

def manual_add_vacancy():
    """FR2: Maintain vacancy details via manual keyboard input."""
    print("\n--- [MANUAL INPUT] POST NEW JOB VACANCY ---")
    vacancy_id = input("Enter Vacancy ID (e.g. VAC207): ").strip()
    company_id = input("Enter Company ID (e.g. CMP101): ").strip().upper()
    job_title = input("Enter Job Title (e.g. AI Research Intern): ").strip()
    try:
        min_cgpa = float(input("Enter Min CGPA Requirement: ").strip())
        salary = float(input("Enter Annual Salary (in INR, e.g. 1200000): ").strip())
        openings = int(input("Enter Number of Openings: ").strip())
    except ValueError:
        print("[ERROR] Numeric fields must contain valid numbers!")
        return
    required_skills = input("Enter Required Skills: ").strip()
    location = input("Enter Job Location: ").strip()

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO job_vacancies (vacancy_id, company_id, job_title, min_cgpa, required_skills, location, salary, openings)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (vacancy_id, company_id, job_title, min_cgpa, required_skills, location, salary, openings))
        conn.commit()
        print(f"[SUCCESS] Job Vacancy '{job_title}' ({vacancy_id}) posted successfully!")
    except Exception as e:
        print(f"[DATABASE ERROR] Failed to post vacancy: {e}")
    finally:
        conn.close()

def manual_apply_job():
    """FR3 & FR4: Apply for job vacancy with duplicate application prevention."""
    print("\n--- [MANUAL INPUT] APPLY FOR JOB VACANCY ---")
    student_id = input("Enter Student ID (e.g. STU001): ").strip()
    vacancy_id = input("Enter Vacancy ID (e.g. VAC201): ").strip()

    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Check eligibility first
        cursor.execute("SELECT name, cgpa FROM students WHERE student_id = ?", (student_id,))
        stu = cursor.fetchone()
        if not stu:
            print(f"[ERROR] Student '{student_id}' does not exist!")
            return
        
        cursor.execute("SELECT job_title, min_cgpa FROM job_vacancies WHERE vacancy_id = ?", (vacancy_id,))
        vac = cursor.fetchone()
        if not vac:
            print(f"[ERROR] Vacancy '{vacancy_id}' does not exist!")
            return

        print(f"Candidate: {stu[0]} (CGPA: {stu[1]}), Vacancy: {vac[0]} (Req CGPA: {vac[1]})")
        if stu[1] < vac[1]:
            print(f"[ELIGIBILITY REJECTION] Student CGPA ({stu[1]}) is below minimum requirement ({vac[1]}).")
            return

        # Attempt Insert (Database constraint uq_student_vacancy enforces FR4)
        cursor.execute("""
            INSERT INTO applications (student_id, vacancy_id, apply_date, status)
            VALUES (?, ?, DATE('now'), 'Applied')
        """, (student_id, vacancy_id))
        conn.commit()
        print(f"[SUCCESS] Application submitted successfully for {student_id} -> {vacancy_id} with status 'Applied'!")
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            print(f"\n[DUPLICATE APPLICATION REJECTED] Student '{student_id}' has ALREADY APPLIED for vacancy '{vacancy_id}'!")
            print("  Constraint 'uq_student_vacancy' prevented duplicate submission. (FR4 Satisfied)")
        else:
            print(f"[INTEGRITY ERROR] {e}")
    except Exception as e:
        print(f"[DATABASE ERROR] {e}")
    finally:
        conn.close()

def manual_update_status():
    """FR5: Track and update application status."""
    print("\n--- [MANUAL INPUT] UPDATE APPLICATION STATUS ---")
    try:
        app_id = int(input("Enter Application ID to update: ").strip())
    except ValueError:
        print("[ERROR] Application ID must be an integer!")
        return

    print("Allowed statuses: Applied, Shortlisted, Selected, Rejected")
    new_status = input("Enter New Status: ").strip().capitalize()
    if new_status not in ["Applied", "Shortlisted", "Selected", "Rejected"]:
        print("[ERROR] Invalid status entered!")
        return

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT status FROM applications WHERE application_id = ?", (app_id,))
        row = cursor.fetchone()
        if not row:
            print(f"[ERROR] Application ID {app_id} not found!")
            return
        old_status = row[0]

        cursor.execute("UPDATE applications SET status = ? WHERE application_id = ?", (new_status, app_id))
        conn.commit()
        print(f"[SUCCESS] Status updated: '{old_status}' -> '{new_status}'.")
        print("[TRIGGER FIRED] The database trigger 'trg_audit_application_status' logged this transition.")
    except Exception as e:
        print(f"[DATABASE ERROR] Failed to update status: {e}")
    finally:
        conn.close()

def run_predefined_reports(log_to_file=False):
    """FR6: Generates reports on vacancies, applications, selection counts, and company recruitment."""
    display_table("SELECT * FROM vw_student_applications LIMIT 10", "REPORT 1: RECENT STUDENT APPLICATIONS", log_to_file)
    display_table("SELECT * FROM vw_company_recruitment", "REPORT 2: COMPANY-WISE RECRUITMENT SUMMARY", log_to_file)
    display_table("SELECT * FROM vw_department_placement", "REPORT 3: DEPARTMENT-WISE PLACEMENT SUMMARY", log_to_file)
    display_table("""
        SELECT a.application_id, a.old_status, a.new_status, a.change_timestamp 
        FROM application_audit_log a 
        ORDER BY a.log_id DESC LIMIT 5
    """, "REPORT 4: RECENT AUDIT LOG ENTRIES (TRIGGER VERIFICATION)", log_to_file)

def execute_custom_sql():
    """Allows user to type any SQL query from keyboard and see immediate results."""
    print("\n--- [MANUAL INPUT] EXECUTE AD-HOC SQL QUERY ---")
    print("Type your SQL query (e.g., SELECT * FROM students WHERE cgpa > 8.5):")
    query = input("SQL> ").strip()
    if query:
        display_table(query, title="CUSTOM SQL EXECUTION RESULT")

def run_automated_test_suite():
    """Runs a complete test suite and saves detailed output to dbms_output.txt."""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("================================================================================\n")
        f.write("       ONLINE JOB PORTAL - DATABASE MANAGEMENT SYSTEM EXECUTION OUTPUT\n")
        f.write("       Subject Code: 25ITT31 - Database Management Systems\n")
        f.write("================================================================================\n\n")

    init_database(log_to_file=True)
    display_table("SELECT * FROM students LIMIT 6", "STUDENTS TABLE (FIRST 6 ROWS)", log_to_file=True)
    display_table("SELECT * FROM job_vacancies", "JOB VACANCIES POSTED", log_to_file=True)
    display_table("SELECT * FROM applications LIMIT 10", "ACTIVE APPLICATIONS", log_to_file=True)
    
    # Test FR4: Duplicate application prevention
    print("\n[TEST FR4] Attempting Duplicate Application (STU001 to VAC201)...")
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO applications (student_id, vacancy_id, apply_date, status) VALUES ('STU001', 'VAC201', '2026-09-10', 'Applied')")
        conn.commit()
    except sqlite3.IntegrityError as e:
        dup_msg = f"[TEST FR4 PASSED] Database enforced UNIQUE(student_id, vacancy_id): {e}"
        print(dup_msg)
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(dup_msg + "\n\n")
    finally:
        conn.close()

    run_predefined_reports(log_to_file=True)
    print(f"\n[INFO] Full execution results saved to '{OUTPUT_FILE}'.")

def main_menu():
    if not os.path.exists(DB_FILE):
        init_database(log_to_file=False)

    while True:
        print("\n" + "=" * 65)
        print("   ONLINE JOB PORTAL - INTERACTIVE DBMS CONSOLE (25ITT31)")
        print("=" * 65)
        print(" 1. View All Students (Job Seekers) [FR1]")
        print(" 2. View All Companies & Vacancies [FR2]")
        print(" 3. View All Applications & Recruitment Status [FR5]")
        print(" 4. [Manual Input] Add New Student Profile [FR1]")
        print(" 5. [Manual Input] Post New Job Vacancy [FR2]")
        print(" 6. [Manual Input] Apply for Job (Test Duplicate Check) [FR3, FR4]")
        print(" 7. [Manual Input] Update Application Status [FR5]")
        print(" 8. Generate System Reports & Statistics [FR6]")
        print(" 9. [Manual Input] Execute Custom SQL Query")
        print("10. Reset Database & Reload Sample Records")
        print("11. Run Automated Test Suite & Save Output to Text File")
        print(" 0. Exit")
        print("-" * 65)
        
        choice = input("Enter your choice (0-11): ").strip()
        if choice == "1":
            display_table("SELECT student_id, name, dept_id, qualification, cgpa, skills FROM students", "ALL REGISTERED STUDENTS")
        elif choice == "2":
            display_table("SELECT * FROM job_vacancies", "ALL JOB VACANCIES")
        elif choice == "3":
            display_table("SELECT * FROM vw_student_applications", "ALL JOB APPLICATIONS")
        elif choice == "4":
            manual_add_student()
        elif choice == "5":
            manual_add_vacancy()
        elif choice == "6":
            manual_apply_job()
        elif choice == "7":
            manual_update_status()
        elif choice == "8":
            run_predefined_reports()
        elif choice == "9":
            execute_custom_sql()
        elif choice == "10":
            init_database(log_to_file=False)
        elif choice == "11":
            run_automated_test_suite()
        elif choice == "0":
            print("\nExiting DBMS Console. Goodbye!\n")
            break
        else:
            print("[ERROR] Invalid choice! Please select 0 to 11.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        run_automated_test_suite()
    else:
        main_menu()
