#!/usr/bin/env python3
"""
VCET Job Portal — Visuals & Diagrams Dashboard Generator
Produces a refined, minimal, premium light-themed visual dashboard (visuals_dashboard.html).
Features concise single-sentence descriptions, single 'View Image' action, hidden technical filenames,
and an elegant distraction-free lightbox viewer with zoom, pan, and fullscreen support.
"""

import os
import sys
import glob
import json
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_HTML = os.path.join(BASE_DIR, "visuals_dashboard.html")

# Preserved asset metadata with refined single-sentence descriptions (8-15 words)
METADATA = {
    "activity_diagram.png": {
        "title": "Activity Diagram: Recruitment Workflow",
        "module": "Software Engineering",
        "code": "25ITT33",
        "category": "se",
        "short_desc": "Shows how candidates apply, pass eligibility checks, and move through recruitment.",
        "full_desc": "End-to-end recruitment process workflow showing student login, vacancy selection, duplicate check gate (FR4), eligibility check gate (FR3), review stages, and reporting."
    },
    "architecture_diagram.png": {
        "title": "3-Tier Software Architecture",
        "module": "Software Engineering",
        "code": "25ITT33",
        "category": "se",
        "short_desc": "Explains how presentation, business logic, and database persistence layers interact.",
        "full_desc": "Architectural design showing bidirectional communication between presentation, business logic, and persistence tiers."
    },
    "dfd_diagram.png": {
        "title": "Data Flow Diagram: Level 0 Context",
        "module": "Software Engineering",
        "code": "25ITT33",
        "category": "se",
        "short_desc": "Shows external data flows between students, recruiters, and placement officers.",
        "full_desc": "Context-level DFD modeling process 0.0 with external entities and data flows without internal data stores."
    },
    "class_diagram.png": {
        "title": "UML Class Diagram: Domain Model",
        "module": "Software Engineering",
        "code": "25ITT33",
        "category": "se",
        "short_desc": "Shows the main system classes, their attributes, and their relationships.",
        "full_desc": "Detailed object-oriented class hierarchy showing abstract User class, Student, Company, JobVacancy, JobApplication, and JobPortalService interface contracts."
    },
    "sequence_diagram.png": {
        "title": "Sequence Diagram: Application Flow",
        "module": "Software Engineering",
        "code": "25ITT33",
        "category": "se",
        "short_desc": "Shows how users and system components interact during an application.",
        "full_desc": "Step-by-step lifelines illustrating student application submission, database duplicate check verification, CGPA qualification check, and exception handling paths."
    },
    "state_machine_diagram.png": {
        "title": "State Machine Diagram: Application Lifecycle",
        "module": "Software Engineering",
        "code": "25ITT33",
        "category": "se",
        "short_desc": "Explains how a job application's status changes during recruitment.",
        "full_desc": "State transition lifecycle for candidate job applications from initial 'Applied' status to 'Shortlisted', followed by final 'Selected' or 'Rejected' outcomes (FR5)."
    },
    "use_case_diagram.png": {
        "title": "Use Case Diagram: System Boundary",
        "module": "Software Engineering",
        "code": "25ITT33",
        "category": "se",
        "short_desc": "Shows how students, recruiters, and placement officers use the portal.",
        "full_desc": "System boundary modeling interactions between external actors (Student, Recruiter, Placement Cell Officer) and core functional use cases (FR1 through FR7)."
    },
    "E_R_Diagram.png": {
        "title": "Cheney E-R Diagram: Database Model",
        "module": "DBMS & E-R",
        "code": "25ITT31",
        "category": "dbms",
        "short_desc": "Shows database entities, attributes, and relationships used in the system.",
        "full_desc": "Entity-Relationship model with mapping cardinalities (1:N, M:N), primary keys, foreign keys, and associative entity 'APPLICATION' enforcing duplicate prevention (FR4)."
    },
    "screenshot_dbms_execution.png": {
        "title": "DBMS Execution Output",
        "module": "DBMS & E-R",
        "code": "25ITT31",
        "category": "dbms",
        "short_desc": "Displays database queries and their results during system execution.",
        "full_desc": "Command prompt screenshot of the interactive SQLite console displaying table views, manual keyboard entries, UNIQUE constraint enforcement, and trigger audit logs."
    },
    "screenshot_java_execution.png": {
        "title": "Java SE 17 Program Execution",
        "module": "Java SE 17",
        "code": "25ITT32",
        "category": "java",
        "short_desc": "Demonstrates object-oriented business logic, multithreading, and stream reports in Java.",
        "full_desc": "Console execution screenshot showing OOP architecture, DuplicateApplicationException and IneligibleStudentException handling, multithreading, and Stream API reports."
    },
    "screenshot_datascience_execution.png": {
        "title": "Data Science Execution Output",
        "module": "Data Science & EDA",
        "code": "25ITC31",
        "category": "ds",
        "short_desc": "Shows descriptive statistics, z-score calculations, and pivot table analysis output.",
        "full_desc": "Terminal screenshot displaying descriptive statistics, standard (z) score calculations, IQR outlier detection, pivot tables, and visualization export logs."
    },
    "1_dept_applications_bar.png": {
        "title": "Department Applications vs Selections",
        "module": "Data Science & EDA",
        "code": "25ITC31",
        "category": "ds",
        "short_desc": "Compares student applications and successful selections across departments.",
        "full_desc": "Comparative bar chart highlighting total student applications vs placed recruits across academic departments (IT, CSE, AIDS, ECE, MECH)."
    },
    "2_status_distribution_pie.png": {
        "title": "Recruitment Status Distribution",
        "module": "Data Science & EDA",
        "code": "25ITC31",
        "category": "ds",
        "short_desc": "Compares the proportions of applied, shortlisted, selected, and rejected applications.",
        "full_desc": "Proportional pie chart displaying overall breakdown of application statuses: Selected (green), Shortlisted (blue), Applied (yellow), and Rejected (red)."
    },
    "3_salary_distribution_hist.png": {
        "title": "Salary Distribution Chart",
        "module": "Data Science & EDA",
        "code": "25ITC31",
        "category": "ds",
        "short_desc": "Shows how offered salary packages are distributed among candidates.",
        "full_desc": "Histogram with Kernel Density Estimation (KDE) curve analyzing compensation distribution in Lakhs per Annum (LPA) across participating companies."
    },
    "4_cgpa_vs_salary_scatter.png": {
        "title": "Student CGPA vs Offered Package",
        "module": "Data Science & EDA",
        "code": "25ITC31",
        "category": "ds",
        "short_desc": "Illustrates the correlation between academic CGPA and offered salary package.",
        "full_desc": "Scatter plot with dashed regression line demonstrating strong positive correlation (r = 0.658) between academic CGPA and offered salary package."
    },
    "5_salary_by_dept_boxplot.png": {
        "title": "Department-wise Salary Variation",
        "module": "Data Science & EDA",
        "code": "25ITC31",
        "category": "ds",
        "short_desc": "Shows salary package spreads and median variations across academic departments.",
        "full_desc": "Box plot with jittered strip points illustrating median salaries, interquartile ranges (IQR), and package spreads across departments."
    },
    "6_correlation_heatmap.png": {
        "title": "Recruitment Feature Correlation Matrix",
        "module": "Data Science & EDA",
        "code": "25ITC31",
        "category": "ds",
        "short_desc": "Displays correlation coefficients between CGPA, requirements, salary, and selection status.",
        "full_desc": "Seaborn Pearson correlation heatmap showing correlation coefficients between CGPA, minimum eligibility requirements, salary, and selection status."
    }
}

def scan_images():
    """Scans all supported image files across subfolders."""
    extensions = ('*.png', '*.jpg', '*.jpeg', '*.webp')
    found_files = []
    
    subfolders = [
        "1_Software_Engineering",
        "2_Database_Management_System",
        "3_Java_Programming",
        "4_Foundation_of_Data_Science"
    ]
    
    for sub in subfolders:
        sub_path = os.path.join(BASE_DIR, sub)
        if not os.path.exists(sub_path):
            continue
        for ext in extensions:
            pattern = os.path.join(sub_path, "**", ext)
            for f in glob.glob(pattern, recursive=True):
                # Avoid duplicate composite if individual diagrams exist
                if os.path.basename(f) == "architecture_and_dfd_diagram.png":
                    continue
                found_files.append(f)
                
    return found_files

def generate_dashboard():
    print(f"[INFO] Scanning visual assets in {BASE_DIR}...")
    image_paths = scan_images()
    print(f"[INFO] Found {len(image_paths)} visual asset(s).")
    
    cards_data = []
    counts = {"all": 0, "se": 0, "dbms": 0, "java": 0, "ds": 0}
    
    for full_path in sorted(image_paths):
        filename = os.path.basename(full_path)
        rel_path = os.path.relpath(full_path, BASE_DIR).replace("\\", "/")
        
        # Match metadata or auto-infer
        if filename in METADATA:
            info = METADATA[filename]
            title = info["title"]
            module = info["module"]
            code = info["code"]
            cat = info["category"]
            short_desc = info["short_desc"]
            full_desc = info["full_desc"]
        else:
            if "Software_Engineering" in rel_path:
                module = "Software Engineering"
                code = "25ITT33"
                cat = "se"
            elif "Database_Management" in rel_path:
                module = "DBMS & E-R"
                code = "25ITT31"
                cat = "dbms"
            elif "Java_Programming" in rel_path:
                module = "Java SE 17"
                code = "25ITT32"
                cat = "java"
            elif "Data_Science" in rel_path:
                module = "Data Science & EDA"
                code = "25ITC31"
                cat = "ds"
            else:
                module = "General Project"
                code = "Core"
                cat = "all"
                
            clean_name = os.path.splitext(filename)[0].replace("_", " ").title()
            title = clean_name
            short_desc = f"Visual artifact demonstrating {title.lower()}."
            full_desc = f"Visual artifact file in {module}."
            
        counts["all"] += 1
        if cat in counts:
            counts[cat] += 1
            
        cards_data.append({
            "filename": filename,
            "rel_path": rel_path,
            "title": title,
            "module": module,
            "code": code,
            "category": cat,
            "short_desc": short_desc,
            "full_desc": full_desc
        })

    # Robust JSON serialization
    cards_json = json.dumps(cards_data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VCET Job Portal — Visuals &amp; Diagrams Dashboard</title>
    <style>
        :root {{
            --bg-page: #F8FAFC;
            --bg-surface: #FFFFFF;
            --bg-subtle: #F1F5F9;
            --border-light: #E2E8F0;
            --border-hover: #CBD5E1;
            
            --text-heading: #0F172A;
            --text-body: #334155;
            --text-muted: #64748B;
            --text-subtle: #94A3B8;

            --primary: #4F46E5;
            --primary-hover: #4338CA;
            --primary-subtle: #EEF2FF;
            --primary-border: #C7D2FE;

            --shadow-card: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05);
            --shadow-hover: 0 10px 25px -4px rgba(15, 23, 42, 0.08), 0 4px 6px -2px rgba(15, 23, 42, 0.03);
            --shadow-modal: 0 25px 50px -12px rgba(0, 0, 0, 0.6);

            --radius-sm: 6px;
            --radius-md: 10px;
            --radius-lg: 14px;
            --radius-full: 9999px;

            --transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-page);
            color: var(--text-body);
            line-height: 1.5;
            -webkit-font-smoothing: antialiased;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}

        /* Navigation Bar */
        .navbar {{
            background: rgba(255, 255, 255, 0.94);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-light);
            position: sticky;
            top: 0;
            z-index: 100;
            height: 60px;
            display: flex;
            align-items: center;
        }}

        .navbar-container {{
            max-width: 1320px;
            margin: 0 auto;
            width: 100%;
            padding: 0 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            cursor: pointer;
        }}

        .brand-icon {{
            width: 32px;
            height: 32px;
            background: var(--primary);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #FFFFFF;
            font-weight: 800;
            font-size: 0.95rem;
            box-shadow: 0 2px 6px rgba(79, 70, 229, 0.3);
        }}

        .brand-title {{
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-heading);
            letter-spacing: -0.015em;
        }}

        .navbar-right {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .stat-badge {{
            font-size: 0.8rem;
            color: var(--text-muted);
            background: var(--bg-subtle);
            border: 1px solid var(--border-light);
            padding: 4px 12px;
            border-radius: var(--radius-full);
            font-weight: 500;
        }}

        .stat-badge strong {{
            color: var(--text-heading);
        }}

        /* Main Container */
        .main-container {{
            max-width: 1320px;
            margin: 0 auto;
            width: 100%;
            padding: 36px 24px 60px;
            flex-grow: 1;
        }}

        /* Hero Section */
        .hero {{
            margin-bottom: 24px;
        }}

        .hero-title {{
            font-size: 2.1rem;
            font-weight: 800;
            letter-spacing: -0.025em;
            color: var(--text-heading);
            margin-bottom: 6px;
        }}

        .hero-subtitle {{
            font-size: 1.02rem;
            color: var(--text-muted);
            line-height: 1.5;
        }}

        /* Compact Visual Summary Metric Strip */
        .summary-strip {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 12px;
            margin-bottom: 28px;
        }}

        .summary-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-light);
            border-radius: var(--radius-md);
            padding: 14px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-card);
            transition: var(--transition);
            cursor: pointer;
            user-select: none;
        }}

        .summary-card:hover {{
            border-color: var(--primary);
            transform: translateY(-2px);
            box-shadow: var(--shadow-hover);
        }}

        .summary-label {{
            font-size: 0.76rem;
            text-transform: uppercase;
            font-weight: 600;
            letter-spacing: 0.04em;
            color: var(--text-muted);
            margin-bottom: 3px;
        }}

        .summary-val {{
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--text-heading);
            line-height: 1;
        }}

        .summary-icon {{
            font-size: 1.3rem;
            opacity: 0.85;
        }}

        /* Filter Controls & Search */
        .controls-bar {{
            background: var(--bg-surface);
            border: 1px solid var(--border-light);
            border-radius: var(--radius-lg);
            padding: 10px 16px;
            margin-bottom: 24px;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            gap: 14px;
            box-shadow: var(--shadow-card);
        }}

        .filter-tabs {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            align-items: center;
        }}

        .filter-tab {{
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-muted);
            padding: 6px 14px;
            border-radius: var(--radius-full);
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}

        .filter-tab:hover {{
            background: var(--bg-subtle);
            color: var(--text-heading);
        }}

        .filter-tab.active {{
            background: var(--primary);
            color: #FFFFFF;
        }}

        .tab-count {{
            background: rgba(0, 0, 0, 0.08);
            padding: 1px 6px;
            border-radius: var(--radius-full);
            font-size: 0.74rem;
        }}

        .filter-tab.active .tab-count {{
            background: rgba(255, 255, 255, 0.22);
            color: #FFFFFF;
        }}

        .search-wrap {{
            position: relative;
            min-width: 250px;
        }}

        .search-icon {{
            position: absolute;
            left: 11px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-subtle);
            font-size: 0.9rem;
            pointer-events: none;
        }}

        .search-input {{
            width: 100%;
            background: var(--bg-subtle);
            border: 1px solid transparent;
            color: var(--text-heading);
            padding: 7px 32px 7px 32px;
            border-radius: var(--radius-md);
            font-size: 0.86rem;
            outline: none;
            transition: var(--transition);
        }}

        .search-input:focus {{
            background: #FFFFFF;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.12);
        }}

        .clear-search {{
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            background: transparent;
            border: none;
            color: var(--text-subtle);
            cursor: pointer;
            font-size: 0.85rem;
            display: none;
        }}

        .clear-search:hover {{
            color: var(--text-heading);
        }}

        /* Active Results Count */
        .results-info {{
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 18px;
            padding: 0 2px;
            font-weight: 500;
        }}

        /* Gallery Grid */
        .gallery-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 20px;
        }}

        /* Gallery Card */
        .visual-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-light);
            border-radius: var(--radius-lg);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: var(--transition);
            box-shadow: var(--shadow-card);
        }}

        .visual-card:hover {{
            transform: translateY(-3px);
            border-color: var(--border-hover);
            box-shadow: var(--shadow-hover);
        }}

        /* Clean Top Image Preview */
        .card-preview {{
            background: #F8FAFC;
            border-bottom: 1px solid var(--border-light);
            height: 210px;
            position: relative;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }}

        .card-preview img {{
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        .visual-card:hover .card-preview img {{
            transform: scale(1.02);
        }}

        /* Card Content Area */
        .card-body {{
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}

        .card-category-subtle {{
            font-size: 0.72rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--primary);
            margin-bottom: 6px;
        }}

        .card-title {{
            font-size: 1.02rem;
            font-weight: 700;
            color: var(--text-heading);
            margin-bottom: 6px;
            line-height: 1.35;
        }}

        /* Refined 1-Sentence Description */
        .card-description {{
            font-size: 0.86rem;
            color: var(--text-muted);
            line-height: 1.45;
            margin-bottom: 18px;
        }}

        /* Bottom Action Button */
        .card-action {{
            margin-top: auto;
            display: flex;
            align-items: center;
        }}

        .btn-view {{
            width: 100%;
            background: #FFFFFF;
            border: 1px solid var(--border-light);
            color: var(--text-heading);
            font-weight: 600;
            font-size: 0.86rem;
            padding: 9px 16px;
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: var(--transition);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }}

        .btn-view:hover {{
            background: var(--primary);
            color: #FFFFFF;
            border-color: var(--primary);
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
        }}

        /* Empty State */
        .empty-state {{
            grid-column: 1 / -1;
            background: var(--bg-surface);
            border: 1px dashed var(--border-light);
            border-radius: var(--radius-lg);
            padding: 50px 20px;
            text-align: center;
            color: var(--text-muted);
        }}

        .empty-state h3 {{
            font-size: 1.15rem;
            color: var(--text-heading);
            margin-bottom: 6px;
        }}

        .btn-reset {{
            background: var(--primary);
            color: #FFFFFF;
            border: none;
            padding: 7px 16px;
            border-radius: var(--radius-md);
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            margin-top: 14px;
        }}

        /* Lightbox Modal */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(15, 23, 42, 0.82);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            z-index: 1000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
            opacity: 0;
            transition: opacity 0.2s ease-out;
        }}

        .modal-overlay.active {{
            display: flex;
            opacity: 1;
        }}

        .modal-dialog {{
            background: #0B0F19;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            width: 95vw;
            max-width: 1260px;
            height: 92vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: var(--shadow-modal);
            transform: scale(0.98);
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        .modal-overlay.active .modal-dialog {{
            transform: scale(1);
        }}

        /* Modal Toolbar */
        .modal-toolbar {{
            background: #111827;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding: 12px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-shrink: 0;
        }}

        .modal-toolbar-left {{
            display: flex;
            align-items: center;
            gap: 12px;
            min-width: 0;
        }}

        .modal-title {{
            font-size: 1.05rem;
            font-weight: 700;
            color: #FFFFFF;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}

        .modal-counter {{
            font-size: 0.8rem;
            color: #94A3B8;
            background: rgba(255, 255, 255, 0.08);
            padding: 2px 8px;
            border-radius: var(--radius-full);
            white-space: nowrap;
        }}

        .modal-toolbar-right {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-shrink: 0;
        }}

        .icon-btn {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.06);
            color: #E2E8F0;
            width: 32px;
            height: 32px;
            border-radius: var(--radius-sm);
            font-size: 0.95rem;
            cursor: pointer;
            transition: var(--transition);
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}

        .icon-btn:hover {{
            background: rgba(255, 255, 255, 0.18);
            color: #FFFFFF;
        }}

        .zoom-label {{
            font-size: 0.78rem;
            font-family: monospace;
            color: #94A3B8;
            padding: 0 6px;
            min-width: 44px;
            text-align: center;
            user-select: none;
        }}

        .icon-btn.btn-close {{
            background: rgba(239, 68, 68, 0.2);
            border-color: rgba(239, 68, 68, 0.4);
            color: #FCA5A5;
            margin-left: 6px;
        }}

        .icon-btn.btn-close:hover {{
            background: #EF4444;
            color: #FFFFFF;
        }}

        /* Modal Image Viewport */
        .modal-viewport {{
            flex-grow: 1;
            position: relative;
            background: #080C16;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            user-select: none;
            cursor: default;
        }}

        .modal-viewport.can-pan {{
            cursor: grab;
        }}

        .modal-viewport.grabbing {{
            cursor: grabbing;
        }}

        .modal-img-wrap {{
            position: absolute;
            display: flex;
            align-items: center;
            justify-content: center;
            transform-origin: center center;
            will-change: transform;
        }}

        .modal-img {{
            max-width: 90vw;
            max-height: 72vh;
            object-fit: contain;
            border-radius: 4px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            pointer-events: none;
        }}

        /* Navigation Arrows */
        .nav-arrow {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 40px;
            height: 40px;
            background: rgba(17, 24, 39, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #FFFFFF;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
            cursor: pointer;
            transition: var(--transition);
            z-index: 10;
        }}

        .nav-arrow:hover {{
            background: var(--primary);
            border-color: var(--primary);
            transform: translateY(-50%) scale(1.08);
        }}

        .nav-arrow.prev {{ left: 16px; }}
        .nav-arrow.next {{ right: 16px; }}

        /* Modal Footer */
        .modal-footer {{
            background: #111827;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding: 12px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-shrink: 0;
            font-size: 0.86rem;
            color: #CBD5E1;
        }}

        .modal-desc {{
            color: #E2E8F0;
            line-height: 1.4;
        }}

        /* Responsive Breakpoints */
        @media (max-width: 1024px) {{
            .gallery-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
            .summary-strip {{
                grid-template-columns: repeat(3, 1fr);
            }}
        }}

        @media (max-width: 768px) {{
            .navbar-container {{
                padding: 0 16px;
            }}
            .main-container {{
                padding: 24px 16px 40px;
            }}
            .hero-title {{
                font-size: 1.7rem;
            }}
            .summary-strip {{
                grid-template-columns: repeat(2, 1fr);
            }}
            .controls-bar {{
                flex-direction: column;
                align-items: stretch;
            }}
            .search-wrap {{
                width: 100%;
                min-width: 0;
            }}
            .gallery-grid {{
                grid-template-columns: 1fr;
            }}
            .modal-dialog {{
                width: 100vw;
                height: 100vh;
                border-radius: 0;
            }}
            .modal-footer {{
                padding: 10px 16px;
                font-size: 0.8rem;
            }}
        }}
    </style>
</head>
<body>

    <!-- Header / Navbar -->
    <header class="navbar">
        <div class="navbar-container">
            <div class="brand" onclick="resetFilters()">
                <div class="brand-icon">V</div>
                <div class="brand-title">VCET Job Portal</div>
            </div>
            <div class="navbar-right">
                <span class="stat-badge">Total Visuals: <strong>{counts['all']}</strong></span>
            </div>
        </div>
    </header>

    <main class="main-container">
        <!-- Hero Section -->
        <section class="hero">
            <h1 class="hero-title">VCET Job Portal</h1>
            <p class="hero-subtitle">System architecture, UML diagrams, database models, and employment analytics.</p>
        </section>

        <!-- Compact Summary KPI Strip -->
        <section class="summary-strip">
            <div class="summary-card" onclick="filterCategory('all')">
                <div>
                    <div class="summary-label">Total Visuals</div>
                    <div class="summary-val">{counts['all']}</div>
                </div>
                <div class="summary-icon">📁</div>
            </div>
            <div class="summary-card" onclick="filterCategory('se')">
                <div>
                    <div class="summary-label">Software Engineering</div>
                    <div class="summary-val">{counts['se']}</div>
                </div>
                <div class="summary-icon">📐</div>
            </div>
            <div class="summary-card" onclick="filterCategory('dbms')">
                <div>
                    <div class="summary-label">DBMS &amp; E-R</div>
                    <div class="summary-val">{counts['dbms']}</div>
                </div>
                <div class="summary-icon">🗄️</div>
            </div>
            <div class="summary-card" onclick="filterCategory('java')">
                <div>
                    <div class="summary-label">Java SE 17</div>
                    <div class="summary-val">{counts['java']}</div>
                </div>
                <div class="summary-icon">☕</div>
            </div>
            <div class="summary-card" onclick="filterCategory('ds')">
                <div>
                    <div class="summary-label">Data Science &amp; EDA</div>
                    <div class="summary-val">{counts['ds']}</div>
                </div>
                <div class="summary-icon">📊</div>
            </div>
        </section>

        <!-- Filter Controls & Search -->
        <section class="controls-bar">
            <div class="filter-tabs">
                <button class="filter-tab active" data-filter="all" onclick="filterCategory('all')">
                    All Visuals <span class="tab-count">{counts['all']}</span>
                </button>
                <button class="filter-tab" data-filter="se" onclick="filterCategory('se')">
                    Software Engineering <span class="tab-count">{counts['se']}</span>
                </button>
                <button class="filter-tab" data-filter="dbms" onclick="filterCategory('dbms')">
                    DBMS &amp; E-R <span class="tab-count">{counts['dbms']}</span>
                </button>
                <button class="filter-tab" data-filter="java" onclick="filterCategory('java')">
                    Java SE 17 <span class="tab-count">{counts['java']}</span>
                </button>
                <button class="filter-tab" data-filter="ds" onclick="filterCategory('ds')">
                    Data Science &amp; EDA <span class="tab-count">{counts['ds']}</span>
                </button>
            </div>

            <div class="search-wrap">
                <span class="search-icon">🔍</span>
                <input type="text" id="searchInput" class="search-input" placeholder="Search visuals..." oninput="handleSearch()">
                <button id="clearSearchBtn" class="clear-search" onclick="clearSearch()" title="Clear">✕</button>
            </div>
        </section>

        <!-- Results Info Bar -->
        <div class="results-info" id="resultsCount">
            Showing {counts['all']} of {counts['all']} visuals
        </div>

        <!-- Gallery Grid -->
        <div class="gallery-grid" id="galleryGrid">
"""

    # Render Cards: Top image preview, middle title & short description, bottom View Image button
    for idx, card in enumerate(cards_data):
        html_content += f"""
            <div class="visual-card" data-category="{card['category']}" data-id="{idx}">
                <div class="card-preview" onclick="openModalByIdx({idx})">
                    <img src="{card['rel_path']}" alt="{card['title']}" loading="lazy">
                </div>
                <div class="card-body">
                    <span class="card-category-subtle">{card['module']}</span>
                    <h3 class="card-title">{card['title']}</h3>
                    <p class="card-description">{card['short_desc']}</p>
                    <div class="card-action">
                        <button class="btn-view" onclick="openModalByIdx({idx})" type="button">
                            View Image
                        </button>
                    </div>
                </div>
            </div>
"""

    html_content += f"""
            <!-- Empty State -->
            <div class="empty-state" id="emptyState" style="display: none;">
                <h3>No Matching Visuals Found</h3>
                <p>No diagrams or charts match your current search.</p>
                <button class="btn-reset" onclick="resetFilters()">Reset Filters</button>
            </div>
        </div>
    </main>

    <!-- Modal Lightbox -->
    <div class="modal-overlay" id="imageModal" onclick="handleOverlayClick(event)">
        <div class="modal-dialog" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
            
            <!-- Modal Toolbar -->
            <div class="modal-toolbar">
                <div class="modal-toolbar-left">
                    <h2 class="modal-title" id="modalTitle">Title</h2>
                    <span class="modal-counter" id="modalCounter">1 of {counts['all']}</span>
                </div>
                
                <div class="modal-toolbar-right">
                    <button class="icon-btn" onclick="zoomOut()" title="Zoom Out (-)">−</button>
                    <span class="zoom-label" id="zoomLevel">100%</span>
                    <button class="icon-btn" onclick="zoomIn()" title="Zoom In (+)">+</button>
                    <button class="icon-btn" onclick="resetZoom()" title="Reset / Fit (0)">⟲</button>
                    <button class="icon-btn" onclick="toggleFullscreen()" title="Fullscreen (F)">⛶</button>
                    <button class="icon-btn btn-close" onclick="closeModal()" title="Close (ESC)">✕</button>
                </div>
            </div>

            <!-- Modal Viewport -->
            <div class="modal-viewport" id="modalViewport" onwheel="handleWheel(event)" onmousedown="startDrag(event)">
                <button class="nav-arrow prev" onclick="navigatePrev(event)" title="Previous (←)">❮</button>
                
                <div class="modal-img-wrap" id="imgContainer">
                    <img class="modal-img" id="modalImg" src="" alt="Full View">
                </div>
                
                <button class="nav-arrow next" onclick="navigateNext(event)" title="Next (→)">❯</button>
            </div>

            <!-- Modal Footer -->
            <div class="modal-footer">
                <div class="modal-desc" id="modalDescription">Description</div>
                <div style="font-size: 0.78rem; color: #64748B;">VCET Placement System</div>
            </div>

        </div>
    </div>

    <!-- Client Script -->
    <script>
        const cardsData = {cards_json};
        
        let currentFilter = 'all';
        let searchQuery = '';
        let visibleIndices = [];
        let activeVisiblePos = 0;
        
        // Zoom & Pan State
        let zoomScale = 1.0;
        let panX = 0;
        let panY = 0;
        let isDragging = false;
        let dragStartX = 0;
        let dragStartY = 0;
        let lastPanX = 0;
        let lastPanY = 0;

        function updateVisibleIndices() {{
            visibleIndices = [];
            cardsData.forEach((item, idx) => {{
                const matchesCat = (currentFilter === 'all' || item.category === currentFilter);
                const query = searchQuery.toLowerCase().trim();
                const matchesSearch = !query || 
                    item.title.toLowerCase().includes(query) || 
                    item.short_desc.toLowerCase().includes(query) || 
                    item.module.toLowerCase().includes(query);

                if (matchesCat && matchesSearch) {{
                    visibleIndices.push(idx);
                }}
            }});
        }}

        function filterCategory(cat) {{
            currentFilter = cat;
            document.querySelectorAll('.filter-tab').forEach(btn => {{
                if (btn.getAttribute('data-filter') === cat) {{
                    btn.classList.add('active');
                }} else {{
                    btn.classList.remove('active');
                }}
            }});
            applyFilters();
        }}

        function handleSearch() {{
            const val = document.getElementById('searchInput').value;
            searchQuery = val;
            document.getElementById('clearSearchBtn').style.display = val.length > 0 ? 'block' : 'none';
            applyFilters();
        }}

        function clearSearch() {{
            document.getElementById('searchInput').value = '';
            searchQuery = '';
            document.getElementById('clearSearchBtn').style.display = 'none';
            applyFilters();
        }}

        function resetFilters() {{
            clearSearch();
            filterCategory('all');
        }}

        function applyFilters() {{
            updateVisibleIndices();
            const cards = document.querySelectorAll('.visual-card');
            
            cards.forEach((card, idx) => {{
                if (visibleIndices.includes(idx)) {{
                    card.style.display = 'flex';
                }} else {{
                    card.style.display = 'none';
                }}
            }});

            const emptyState = document.getElementById('emptyState');
            if (visibleIndices.length === 0) {{
                emptyState.style.display = 'block';
            }} else {{
                emptyState.style.display = 'none';
            }}

            const resultsCount = document.getElementById('resultsCount');
            resultsCount.innerText = `Showing ${{visibleIndices.length}} of ${{cardsData.length}} visuals`;
        }}

        function openModalByIdx(idx) {{
            const pos = visibleIndices.indexOf(idx);
            activeVisiblePos = (pos !== -1) ? pos : 0;
            renderModalContent();
            
            const modal = document.getElementById('imageModal');
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
            resetZoom();
        }}

        function renderModalContent() {{
            if (visibleIndices.length === 0) return;
            const cardIdx = visibleIndices[activeVisiblePos];
            const item = cardsData[cardIdx];

            document.getElementById('modalTitle').innerText = item.title;
            document.getElementById('modalCounter').innerText = `${{activeVisiblePos + 1}} of ${{visibleIndices.length}}`;
            document.getElementById('modalDescription').innerText = item.short_desc;

            const img = document.getElementById('modalImg');
            img.src = item.rel_path;
        }}

        function closeModal() {{
            const modal = document.getElementById('imageModal');
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
            resetZoom();
        }}

        function handleOverlayClick(e) {{
            if (e.target.id === 'imageModal') {{
                closeModal();
            }}
        }}

        function navigateNext(e) {{
            if (e) e.stopPropagation();
            if (visibleIndices.length <= 1) return;
            activeVisiblePos = (activeVisiblePos + 1) % visibleIndices.length;
            renderModalContent();
            resetZoom();
        }}

        function navigatePrev(e) {{
            if (e) e.stopPropagation();
            if (visibleIndices.length <= 1) return;
            activeVisiblePos = (activeVisiblePos - 1 + visibleIndices.length) % visibleIndices.length;
            renderModalContent();
            resetZoom();
        }}

        function applyTransform() {{
            const container = document.getElementById('imgContainer');
            container.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{zoomScale}})`;
            document.getElementById('zoomLevel').innerText = `${{Math.round(zoomScale * 100)}}%`;
            
            const viewport = document.getElementById('modalViewport');
            if (zoomScale > 1.05) {{
                viewport.classList.add('can-pan');
            }} else {{
                viewport.classList.remove('can-pan');
            }}
        }}

        function zoomIn() {{
            if (zoomScale < 4.0) {{
                zoomScale = Math.min(4.0, zoomScale + 0.25);
                applyTransform();
            }}
        }}

        function zoomOut() {{
            if (zoomScale > 0.5) {{
                zoomScale = Math.max(0.5, zoomScale - 0.25);
                if (zoomScale <= 1.0) {{
                    panX = 0;
                    panY = 0;
                }}
                applyTransform();
            }}
        }}

        function resetZoom() {{
            zoomScale = 1.0;
            panX = 0;
            panY = 0;
            applyTransform();
        }}

        function handleWheel(e) {{
            e.preventDefault();
            if (e.deltaY < 0) {{
                zoomIn();
            }} else {{
                zoomOut();
            }}
        }}

        function startDrag(e) {{
            if (zoomScale <= 1.0) return;
            if (e.target.closest('.nav-arrow') || e.target.closest('.icon-btn')) return;
            isDragging = true;
            dragStartX = e.clientX;
            dragStartY = e.clientY;
            lastPanX = panX;
            lastPanY = panY;
            document.getElementById('modalViewport').classList.add('grabbing');
            
            window.addEventListener('mousemove', onDragMove);
            window.addEventListener('mouseup', stopDrag);
        }}

        function onDragMove(e) {{
            if (!isDragging) return;
            panX = lastPanX + (e.clientX - dragStartX);
            panY = lastPanY + (e.clientY - dragStartY);
            applyTransform();
        }}

        function stopDrag() {{
            isDragging = false;
            document.getElementById('modalViewport').classList.remove('grabbing');
            window.removeEventListener('mousemove', onDragMove);
            window.removeEventListener('mouseup', stopDrag);
        }}

        function toggleFullscreen() {{
            const elem = document.querySelector('.modal-dialog');
            if (!document.fullscreenElement) {{
                if (elem.requestFullscreen) elem.requestFullscreen();
            }} else {{
                if (document.exitFullscreen) document.exitFullscreen();
            }}
        }}

        // Keyboard Shortcuts
        document.addEventListener('keydown', (e) => {{
            const modal = document.getElementById('imageModal');
            const isModalOpen = modal.classList.contains('active');

            if (isModalOpen) {{
                if (e.key === 'Escape') closeModal();
                if (e.key === 'ArrowRight') navigateNext(e);
                if (e.key === 'ArrowLeft') navigatePrev(e);
                if (e.key === '+' || e.key === '=') zoomIn();
                if (e.key === '-' || e.key === '_') zoomOut();
                if (e.key === '0') resetZoom();
                if (e.key === 'f' || e.key === 'F') toggleFullscreen();
            }} else {{
                if ((e.key === '/' || (e.ctrlKey && e.key === 'k')) && document.activeElement.id !== 'searchInput') {{
                    e.preventDefault();
                    document.getElementById('searchInput').focus();
                }}
            }}
        }});

        // Double-click to toggle zoom
        document.getElementById('modalViewport').addEventListener('dblclick', (e) => {{
            if (e.target.closest('.nav-arrow')) return;
            if (zoomScale > 1.1) {{
                resetZoom();
            }} else {{
                zoomScale = 2.0;
                applyTransform();
            }}
        }});

        updateVisibleIndices();
    </script>
</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"[SUCCESS] Refined VCET Job Portal Dashboard generated: {OUTPUT_HTML}")
    return OUTPUT_HTML

if __name__ == "__main__":
    generate_dashboard()
