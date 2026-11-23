#!/usr/bin/env python3
"""
Online Job Portal and Employment Trend Analysis System
Interactive Data Science Console (Subject Code: 25ITC31)
Supports Step-by-Step Manual Keyboard Input & Trend Analysis
"""

import os
import sys
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "recruitment_data.csv")

# Import functions from trend_analysis
from trend_analysis import (
    load_and_describe_data,
    perform_descriptive_statistics,
    perform_data_cleaning_and_wrangling,
    generate_visualizations,
    run_full_pipeline
)

def manual_filter_candidates(df):
    """Allows user to filter candidates by department and CGPA via keyboard input."""
    print("\n--- [MANUAL INPUT] FILTER CANDIDATES BY CRITERIA ---")
    print(f"Available Departments: {list(df['department'].unique())}")
    dept = input("Enter Department to filter (or press Enter for ALL): ").strip().upper()
    try:
        min_cgpa_str = input("Enter Minimum CGPA (e.g. 8.0, or press Enter for NONE): ").strip()
        min_cgpa = float(min_cgpa_str) if min_cgpa_str else 0.0
    except ValueError:
        print("[ERROR] Invalid CGPA! Using 0.0.")
        min_cgpa = 0.0

    filtered = df.copy()
    if dept:
        filtered = filtered[filtered['department'] == dept]
    if min_cgpa > 0:
        filtered = filtered[filtered['cgpa'] >= min_cgpa]

    print(f"\n[FILTERED RESULTS: {len(filtered)} matching records]")
    cols = ['student_id', 'student_name', 'department', 'cgpa', 'job_title', 'company_name', 'salary', 'status']
    print(filtered[cols].to_string(index=False))

def manual_check_eligibility(df):
    """Allows user to enter a student's CGPA and skills to evaluate eligibility for companies."""
    print("\n--- [MANUAL INPUT] EVALUATE RECRUITMENT ELIGIBILITY ---")
    try:
        cgpa = float(input("Enter Student CGPA (0.0 to 10.0): ").strip())
    except ValueError:
        print("[ERROR] Invalid CGPA.")
        return
    dept = input("Enter Department (IT/CSE/ECE/MECH/AIDS): ").strip().upper()

    print(f"\nChecking eligible job vacancies for CGPA {cgpa:.2f} ({dept})...")
    vacancies = df[['company_name', 'job_title', 'min_cgpa', 'salary', 'location']].drop_duplicates()
    
    eligible = vacancies[vacancies['min_cgpa'] <= cgpa].sort_values(by='salary', ascending=False)
    ineligible = vacancies[vacancies['min_cgpa'] > cgpa]

    print(f"\n[ELIGIBLE OPPORTUNITIES: {len(eligible)} companies]")
    print(eligible.to_string(index=False))

    if len(ineligible) > 0:
        print(f"\n[INELIGIBLE (Requirement > {cgpa:.2f}): {len(ineligible)} companies]")
        print(ineligible[['company_name', 'job_title', 'min_cgpa']].to_string(index=False))

def main_menu():
    df = load_and_describe_data()
    
    while True:
        print("\n" + "=" * 70)
        print("   ONLINE JOB PORTAL - DATA SCIENCE & TREND ANALYSIS CONSOLE (25ITC31)")
        print("=" * 70)
        print(" 1. View Raw Dataset Overview & Data Types [Unit 2]")
        print(" 2. Compute Descriptive Statistics & Standard (z) Scores [Unit 1]")
        print(" 3. Perform Data Cleaning, Duplicate Audit & Outlier Detection [Unit 4]")
        print(" 4. View Department & Company Recruitment Pivot Tables [Unit 3]")
        print(" 5. Generate Matplotlib & Seaborn Visualizations (PNG Charts) [Unit 5]")
        print(" 6. [Manual Input] Filter Candidates by Department and CGPA")
        print(" 7. [Manual Input] Evaluate Eligibility for Job Vacancies")
        print(" 8. Run Full Automated Pipeline & Update 'datascience_output.txt'")
        print(" 0. Exit")
        print("-" * 70)
        
        choice = input("Enter your choice (0-8): ").strip()
        if choice == "1":
            print(f"\nTotal Records: {len(df)}, Features: {len(df.columns)}")
            print("\nDataset Info:")
            print(df.info())
            print("\nFirst 5 Records:")
            print(df[['student_id', 'student_name', 'department', 'cgpa', 'company_name', 'salary', 'status']].head())
        elif choice == "2":
            stats_text, _ = perform_descriptive_statistics(df)
            print("\n" + stats_text)
        elif choice == "3":
            clean_text, _, _ = perform_data_cleaning_and_wrangling(df)
            print("\n" + clean_text)
        elif choice == "4":
            _, p_dept, p_comp = perform_data_cleaning_and_wrangling(df)
            print("\n[PIVOT TABLE: DEPARTMENT vs STATUS]")
            print(p_dept)
            print("\n[PIVOT TABLE: COMPANY PERFORMANCE]")
            print(p_comp.to_string(index=False))
        elif choice == "5":
            print("\nGenerating Matplotlib and Seaborn charts in 'visualizations/' folder...")
            viz_files = generate_visualizations(df)
            print("[SUCCESS] All 6 visualizations generated successfully:")
            for vf in viz_files:
                print(f"  -> {os.path.basename(vf)}")
        elif choice == "6":
            manual_filter_candidates(df)
        elif choice == "7":
            manual_check_eligibility(df)
        elif choice == "8":
            run_full_pipeline()
        elif choice == "0":
            print("\nExiting Data Science Console. Goodbye!\n")
            break
        else:
            print("[ERROR] Invalid choice! Please select 0 to 8.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        run_full_pipeline()
    else:
        main_menu()
