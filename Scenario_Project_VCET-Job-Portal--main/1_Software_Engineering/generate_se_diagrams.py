#!/usr/bin/env python3
"""
Online Job Portal and Employment Trend Analysis System
Software Engineering Diagrams Generator (Subject Code: 25ITT33)
Generates: Use Case, Class, Sequence, Activity, DFD, Architecture, and State Diagrams
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def draw_use_case_diagram():
    fig, ax = plt.subplots(figsize=(16, 11), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "USE CASE DIAGRAM: ONLINE JOB PORTAL", ha='center', fontsize=18, fontweight='bold', color='#1A237E')
    ax.text(50, 94, "Subject Code: 25ITT33 - Software Engineering (Unit 2: Requirements Modeling)", ha='center', fontsize=11, color='#546E7A')

    # System Boundary Box
    system_box = patches.FancyBboxPatch((28, 5), 44, 85, boxstyle="round,pad=0.5",
                                        facecolor='#FAFAFA', edgecolor='#1565C0', linewidth=2.5, linestyle='--')
    ax.add_patch(system_box)
    ax.text(50, 87, "System Boundary: Job Portal System", ha='center', fontsize=13, fontweight='bold', color='#0D47A1')

    # Use Cases (Ovals)
    use_cases = [
        (50, 78, "Register Profile\n& Skills (FR1)", "#E8F5E9", "#2E7D32"),
        (50, 67, "View & Search\nJob Vacancies (FR2)", "#E3F2FD", "#1565C0"),
        (50, 56, "Apply for Vacancy\n(Duplicate Check FR3/4)", "#FFF3E0", "#E65100"),
        (50, 45, "Track Application\nStatus (FR5)", "#F3E5F5", "#7B1FA2"),
        (50, 34, "Post Vacancies &\nShortlist (FR2/5)", "#EDE7F6", "#512DA8"),
        (50, 23, "Generate Placement\nReports (FR6)", "#E0F2F1", "#00796B"),
        (50, 12, "Analyze Recruitment\nTrends (FR7)", "#FBE9E7", "#D84315"),
    ]

    for x, y, label, fc, ec in use_cases:
        ellipse = patches.Ellipse((x, y), 26, 7.5, facecolor=fc, edgecolor=ec, linewidth=1.8, zorder=3)
        ax.add_patch(ellipse)
        ax.text(x, y, label, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#263238', zorder=4)

    # Helper: Draw Actor
    def draw_actor(x, y, label, color):
        # Head
        ax.add_patch(patches.Circle((x, y + 4), 2.2, facecolor='#FFFFFF', edgecolor=color, linewidth=2, zorder=4))
        # Body
        ax.plot([x, x], [y + 1.8, y - 4], color=color, linewidth=2.5, zorder=4)
        # Arms
        ax.plot([x - 3.5, x + 3.5], [y - 0.5, y - 0.5], color=color, linewidth=2.5, zorder=4)
        # Legs
        ax.plot([x, x - 3], [y - 4, y - 9], color=color, linewidth=2.5, zorder=4)
        ax.plot([x, x + 3], [y - 4, y - 9], color=color, linewidth=2.5, zorder=4)
        # Label
        ax.text(x, y - 12.5, label, ha='center', va='center', fontsize=11, fontweight='bold', color=color, zorder=4)

    # Actors
    draw_actor(12, 65, "Student /\nJob Seeker", "#0277BD")
    draw_actor(88, 65, "Company\nRecruiter", "#D84315")
    draw_actor(88, 25, "Placement Cell\nOfficer / Admin", "#2E7D32")

    # Connectors
    # Student connections
    ax.plot([14, 37], [66, 78], color='#37474F', linewidth=1.5)
    ax.plot([14, 37], [63, 67], color='#37474F', linewidth=1.5)
    ax.plot([14, 37], [60, 56], color='#37474F', linewidth=1.5)
    ax.plot([14, 37], [57, 45], color='#37474F', linewidth=1.5)

    # Recruiter connections
    ax.plot([86, 63], [66, 34], color='#37474F', linewidth=1.5)
    ax.plot([86, 63], [63, 45], color='#37474F', linewidth=1.5)

    # Placement Cell connections
    ax.plot([86, 63], [28, 45], color='#37474F', linewidth=1.5)
    ax.plot([86, 63], [25, 23], color='#37474F', linewidth=1.5)
    ax.plot([86, 63], [22, 12], color='#37474F', linewidth=1.5)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "use_case_diagram.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"[SAVED] {path}")

def draw_class_diagram():
    fig, ax = plt.subplots(figsize=(18, 12), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "CLASS DIAGRAM: OBJECT-ORIENTED DOMAIN MODEL", ha='center', fontsize=18, fontweight='bold', color='#1A237E')
    ax.text(50, 94, "Subject Code: 25ITT33 - Software Engineering (Unit 2 & 3) | 25ITT32 - Java Architecture", ha='center', fontsize=11, color='#546E7A')

    def draw_uml_class(x, y, w, h, title, attributes, methods, is_abstract=False):
        # Outer box
        rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0",
                                      facecolor='#FAFAFA', edgecolor='#1565C0', linewidth=2, zorder=3)
        ax.add_patch(rect)
        
        # Header banner
        header_h = 3.8
        header = patches.Rectangle((x - w/2, y + h/2 - header_h), w, header_h,
                                   facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=1, zorder=4)
        ax.add_patch(header)
        prefix = "<<abstract>>\n" if is_abstract else ""
        ax.text(x, y + h/2 - header_h/2, prefix + title, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0D47A1', zorder=5)

        # Dividers
        split_y = y + h/2 - header_h - (len(attributes) * 1.8 + 1)
        ax.plot([x - w/2, x + w/2], [split_y, split_y], color='#1565C0', linewidth=1.2, zorder=4)

        # Attributes
        ay = y + h/2 - header_h - 1.5
        for attr in attributes:
            ax.text(x - w/2 + 1, ay, attr, ha='left', va='center', fontsize=8, color='#263238', zorder=5)
            ay -= 1.8

        # Methods
        my = split_y - 1.5
        for m in methods:
            ax.text(x - w/2 + 1, my, m, ha='left', va='center', fontsize=8, color='#004D40', zorder=5)
            my -= 1.8

    # Classes
    # 1. User (Abstract)
    draw_uml_class(20, 78, 26, 17, "User", 
                   ["# id: String", "# name: String", "# email: String"],
                   ["+ getId(): String", "+ getName(): String", "+ getEmail(): String", "+ getRole(): String*"],
                   is_abstract=True)

    # 2. Student
    draw_uml_class(20, 45, 28, 23, "Student",
                   ["- department: String", "- qualification: String", "- cgpa: double", "- skills: String"],
                   ["+ getDepartment(): String", "+ getCgpa(): double", "+ getSkills(): String", "+ getRole(): String", "+ toString(): String"],
                   is_abstract=False)

    # 3. Company
    draw_uml_class(50, 78, 26, 18, "Company",
                   ["- companyId: String", "- companyName: String", "- industry: String", "- location: String", "- contactEmail: String"],
                   ["+ getCompanyId(): String", "+ getCompanyName(): String", "+ getLocation(): String"],
                   is_abstract=False)

    # 4. JobVacancy
    draw_uml_class(50, 45, 28, 23, "JobVacancy",
                   ["- vacancyId: String", "- companyId: String", "- jobTitle: String", "- minCgpa: double", "- requiredSkills: String", "- salary: double", "- openings: int"],
                   ["+ getVacancyId(): String", "+ getJobTitle(): String", "+ getMinCgpa(): double", "+ getSalary(): double"],
                   is_abstract=False)

    # 5. JobApplication
    draw_uml_class(82, 45, 28, 23, "JobApplication",
                   ["- applicationId: int", "- studentId: String", "- vacancyId: String", "- applyDate: LocalDate", "- status: ApplicationStatus"],
                   ["+ getApplicationId(): int", "+ getStudentId(): String", "+ getVacancyId(): String", "+ getStatus(): ApplicationStatus", "+ setStatus(status): void"],
                   is_abstract=False)

    # 6. Service Interface
    draw_uml_class(82, 80, 30, 16, "<<interface>>\nJobPortalService",
                   ["-- Contracts --"],
                   ["+ registerStudent(s): void", "+ postJobVacancy(v): void", "+ applyForJob(stu, vac): App", "+ getSelectionSummary(): Map"],
                   is_abstract=True)

    # Arrows
    # Inheritance: Student -> User (Generalization)
    ax.annotate("", xy=(20, 69.5), xytext=(20, 56.5),
                arrowprops=dict(facecolor='white', edgecolor='#1565C0', shrink=0.05, width=1.5, headwidth=10))

    # Association: Company -> Vacancy (1 to N)
    ax.plot([50, 50], [69, 56.5], color='#37474F', linewidth=1.5)
    ax.text(51.5, 66, "1", fontsize=10, fontweight='bold', color='#D84315')
    ax.text(51.5, 58, "*", fontsize=10, fontweight='bold', color='#D84315')

    # Association: Student -> JobApplication
    ax.plot([34, 68], [45, 45], color='#37474F', linewidth=1.5)
    ax.text(35, 46.5, "1", fontsize=10, fontweight='bold', color='#D84315')
    ax.text(66, 46.5, "*", fontsize=10, fontweight='bold', color='#D84315')

    # Association: Vacancy -> JobApplication
    ax.plot([64, 68], [40, 40], color='#37474F', linewidth=1.5)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "class_diagram.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"[SAVED] {path}")

def draw_sequence_diagram():
    fig, ax = plt.subplots(figsize=(17, 11), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "SEQUENCE DIAGRAM: JOB APPLICATION & DUPLICATE VALIDATION", ha='center', fontsize=18, fontweight='bold', color='#1A237E')
    ax.text(50, 94, "Subject Code: 25ITT33 - Software Engineering (Unit 3: Behavioral Design)", ha='center', fontsize=11, color='#546E7A')

    # Lifelines
    lifelines = [
        (15, ":Student\n(Job Seeker)"),
        (38, ":PortalController\n(Presentation)"),
        (62, ":JobPortalService\n(Business Logic)"),
        (85, ":Database / DAO\n(Persistence)")
    ]

    for x, label in lifelines:
        box = patches.FancyBboxPatch((x - 9, 84), 18, 6, boxstyle="round,pad=0.2",
                                     facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=1.8, zorder=3)
        ax.add_patch(box)
        ax.text(x, 87, label, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0D47A1', zorder=4)
        ax.plot([x, x], [84, 8], color='#90A4AE', linestyle='--', linewidth=1.5, zorder=2)

    # Helper: Message arrow
    def draw_msg(x1, x2, y, label, is_return=False, is_error=False):
        style = '--' if is_return else '-'
        color = '#D32F2F' if is_error else ('#00796B' if is_return else '#263238')
        ax.annotate("", xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="->", linestyle=style, color=color, linewidth=1.6))
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, y + 1.5, label, ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=color)

    # Sequence steps
    draw_msg(15, 38, 77, "1: applyForJob(studentId, vacancyId)")
    draw_msg(38, 62, 71, "2: validateEligibility(studentId, vacancyId)")
    draw_msg(62, 85, 65, "3: checkDuplicate(studentId, vacancyId)")
    draw_msg(85, 62, 59, "4: recordNotFound (OK to proceed)", is_return=True)
    draw_msg(62, 62, 53, "5: verifyCGPA >= minCgpa (Passed)")
    draw_msg(62, 85, 47, "6: insertApplication(studentId, vacancyId, 'Applied')")
    draw_msg(85, 62, 41, "7: commitSuccess (AppID: 1012)", is_return=True)
    draw_msg(62, 38, 35, "8: return ApplicationReceipt", is_return=True)
    draw_msg(38, 15, 29, "9: displayConfirmation(AppID #1012)", is_return=True)

    # Alternative / Error path box
    alt_box = patches.FancyBboxPatch((8, 10), 84, 15, boxstyle="round,pad=0.2",
                                     facecolor='#FFEBEE', edgecolor='#E53935', linewidth=1.5, linestyle=':')
    ax.add_patch(alt_box)
    ax.text(10, 23, "[ALT] Duplicate Application Attempt (FR4)", fontsize=9.5, fontweight='bold', color='#C62828')
    draw_msg(62, 38, 18, "throws DuplicateApplicationException(studentId, vacancyId)", is_return=True, is_error=True)
    draw_msg(38, 15, 12, "displayError('Duplicate Application Blocked')", is_return=True, is_error=True)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "sequence_diagram.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"[SAVED] {path}")

def draw_activity_diagram():
    fig, ax = plt.subplots(figsize=(15, 12), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "ACTIVITY DIAGRAM: RECRUITMENT WORKFLOW (FR1 - FR7)", ha='center', fontsize=18, fontweight='bold', color='#1A237E')
    ax.text(50, 94, "Subject Code: 25ITT33 - Software Engineering (Unit 2 & Unit 3)", ha='center', fontsize=11, color='#546E7A')

    # Start Node
    ax.add_patch(patches.Circle((50, 89), 2.2, facecolor='black', edgecolor='black', zorder=3))
    ax.annotate("", xy=(50, 83), xytext=(50, 86.8), arrowprops=dict(arrowstyle="->", linewidth=1.8))

    # Helper: Action state
    def draw_action(x, y, text, w=28, h=5.5):
        rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.4",
                                      facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=1.8, zorder=3)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold', color='#1B5E20', zorder=4)

    # Helper: Decision diamond
    def draw_decision(x, y, text):
        diamond = patches.Polygon([[x, y + 3.5], [x + 5, y], [x, y - 3.5], [x - 5, y]],
                                  facecolor='#FFF9C4', edgecolor='#F57F17', linewidth=1.8, zorder=3)
        ax.add_patch(diamond)
        ax.text(x, y, text, ha='center', va='center', fontsize=8, fontweight='bold', color='#E65100', zorder=4)

    draw_action(50, 80, "Student / Recruiter Logs In")
    ax.annotate("", xy=(50, 73.5), xytext=(50, 77.2), arrowprops=dict(arrowstyle="->", linewidth=1.8))

    draw_action(50, 71, "Select Vacancy & Submit Application")
    ax.annotate("", xy=(50, 64.5), xytext=(50, 68.2), arrowprops=dict(arrowstyle="->", linewidth=1.8))

    # Decision: Duplicate check
    draw_decision(50, 61, "Duplicate?")
    # Yes -> Reject
    ax.annotate("", xy=(80, 61), xytext=(55, 61), arrowprops=dict(arrowstyle="->", linewidth=1.8))
    ax.text(67, 62.5, "[Yes: FR4]", fontsize=9, fontweight='bold', color='#C62828')
    draw_action(80, 52, "Block Duplicate\n(Throw Exception)", w=20, h=5.5)
    ax.annotate("", xy=(80, 55), xytext=(80, 61), arrowprops=dict(arrowstyle="->", linewidth=1.8))

    # No -> Check CGPA
    ax.annotate("", xy=(50, 52.5), xytext=(50, 57.5), arrowprops=dict(arrowstyle="->", linewidth=1.8))
    ax.text(51.5, 55, "[No]", fontsize=9, fontweight='bold', color='#2E7D32')

    draw_decision(50, 49, "Eligible?")
    # No -> Reject
    ax.annotate("", xy=(20, 49), xytext=(45, 49), arrowprops=dict(arrowstyle="->", linewidth=1.8))
    ax.text(32, 50.5, "[No: FR3]", fontsize=9, fontweight='bold', color='#C62828')
    draw_action(20, 40, "Reject: CGPA Below Min", w=20, h=5.5)
    ax.annotate("", xy=(20, 43), xytext=(20, 49), arrowprops=dict(arrowstyle="->", linewidth=1.8))

    # Yes -> Save Application
    ax.annotate("", xy=(50, 40.5), xytext=(50, 45.5), arrowprops=dict(arrowstyle="->", linewidth=1.8))
    ax.text(51.5, 43, "[Yes]", fontsize=9, fontweight='bold', color='#2E7D32')

    draw_action(50, 38, "Record Status: 'Applied'")
    ax.annotate("", xy=(50, 31.5), xytext=(50, 35.2), arrowprops=dict(arrowstyle="->", linewidth=1.8))

    draw_action(50, 29, "Recruiter Reviews & Updates Status\n(Shortlisted / Selected / Rejected)")
    ax.annotate("", xy=(50, 22.5), xytext=(50, 26.2), arrowprops=dict(arrowstyle="->", linewidth=1.8))

    draw_action(50, 20, "Generate Reports & Python EDA Visualizations\n(Placement Rate, Salary Trends FR6/7)", w=34)
    ax.annotate("", xy=(50, 13.5), xytext=(50, 17.2), arrowprops=dict(arrowstyle="->", linewidth=1.8))

    # End Node
    ax.add_patch(patches.Circle((50, 10), 2.8, facecolor='none', edgecolor='#1565C0', linewidth=2, zorder=3))
    ax.add_patch(patches.Circle((50, 10), 1.8, facecolor='#1565C0', edgecolor='#1565C0', zorder=4))

    # Connect rejections to end node
    ax.plot([80, 80, 53], [49, 10, 10], color='#C62828', linestyle='--', linewidth=1.5)
    ax.plot([20, 20, 47], [37, 10, 10], color='#C62828', linestyle='--', linewidth=1.5)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "activity_diagram.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"[SAVED] {path}")

def draw_dfd_and_architecture():
    # 1. DFD Level 0 Context & Level 1 DFD
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 13), dpi=300)
    for ax in [ax1, ax2]:
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 50)
        ax.axis('off')

    # Top: Level 0 DFD
    ax1.text(50, 47, "DATA FLOW DIAGRAM (DFD) - LEVEL 0 (CONTEXT DIAGRAM)", ha='center', fontsize=14, fontweight='bold', color='#1A237E')
    # Entities
    def draw_ext_entity(ax, x, y, text):
        ax.add_patch(patches.Rectangle((x - 8, y - 5), 16, 10, facecolor='#E3F2FD', edgecolor='#0D47A1', linewidth=2, zorder=3))
        ax.text(x, y, text, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#0D47A1', zorder=4)

    draw_ext_entity(ax1, 15, 25, "Student /\nJob Seeker")
    draw_ext_entity(ax1, 85, 35, "Company\nRecruiter")
    draw_ext_entity(ax1, 85, 15, "Placement\nOfficer")

    # Central Process
    ax1.add_patch(patches.Circle((50, 25), 11, facecolor='#FFF3E0', edgecolor='#E65100', linewidth=2.2, zorder=3))
    ax1.text(50, 27, "0.0\nJOB PORTAL &\nTREND ANALYSIS\nSYSTEM", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#BF360C', zorder=4)

    # Flows
    ax1.annotate("", xy=(39, 28), xytext=(23, 28), arrowprops=dict(arrowstyle="->", linewidth=1.6))
    ax1.text(31, 30, "Profile & Applications", fontsize=8, fontweight='bold')
    ax1.annotate("", xy=(23, 22), xytext=(39, 22), arrowprops=dict(arrowstyle="->", linewidth=1.6))
    ax1.text(31, 23.5, "Status & Job Listings", fontsize=8, fontweight='bold', color='#00796B')

    ax1.annotate("", xy=(61, 28), xytext=(77, 35), arrowprops=dict(arrowstyle="->", linewidth=1.6))
    ax1.text(69, 33, "Job Vacancies", fontsize=8, fontweight='bold')

    ax1.annotate("", xy=(77, 15), xytext=(61, 22), arrowprops=dict(arrowstyle="->", linewidth=1.6))
    ax1.text(69, 17, "Placement Analytics", fontsize=8, fontweight='bold', color='#00796B')

    # Bottom: 3-Tier Architecture Diagram
    ax2.text(50, 47, "3-TIER SOFTWARE ARCHITECTURAL DESIGN (Unit 3)", ha='center', fontsize=14, fontweight='bold', color='#1A237E')
    
    # Tier 1
    ax2.add_patch(patches.FancyBboxPatch((5, 10), 26, 28, boxstyle="round,pad=0.3", facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=2))
    ax2.text(18, 34, "PRESENTATION TIER", ha='center', fontsize=11, fontweight='bold', color='#1B5E20')
    ax2.text(18, 27, "- Java Console CLI\n- Interactive DBMS Tool\n- Data Science Dashboards\n- Keyboard Input Forms", fontsize=9, color='#263238')

    # Tier 2
    ax2.add_patch(patches.FancyBboxPatch((37, 10), 26, 28, boxstyle="round,pad=0.3", facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=2))
    ax2.text(50, 34, "BUSINESS LOGIC TIER", ha='center', fontsize=11, fontweight='bold', color='#0D47A1')
    ax2.text(50, 26, "- Eligibility Validator (FR3)\n- Duplicate Checker (FR4)\n- Application Lifecycle (FR5)\n- Multithreaded Engine\n- Stream Analytics (FR6)", fontsize=9, color='#263238')

    # Tier 3
    ax2.add_patch(patches.FancyBboxPatch((69, 10), 26, 28, boxstyle="round,pad=0.3", facecolor='#FFF3E0', edgecolor='#E65100', linewidth=2))
    ax2.text(82, 34, "DATA PERSISTENCE TIER", ha='center', fontsize=11, fontweight='bold', color='#BF360C')
    ax2.text(82, 26, "- SQLite RDBMS Tables\n- Unique Index (FR4)\n- Audit Log Triggers\n- Preprocessed CSV Data\n- Foreign Key Integrity", fontsize=9, color='#263238')

    # Inter-tier arrows
    ax2.annotate("", xy=(37, 24), xytext=(31, 24), arrowprops=dict(arrowstyle="<->", linewidth=2, color='#37474F'))
    ax2.annotate("", xy=(69, 24), xytext=(63, 24), arrowprops=dict(arrowstyle="<->", linewidth=2, color='#37474F'))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "architecture_and_dfd_diagram.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"[SAVED] {path}")

def draw_state_machine_diagram():
    fig, ax = plt.subplots(figsize=(15, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')

    ax.text(50, 56, "STATE MACHINE DIAGRAM: APPLICATION LIFECYCLE (FR5)", ha='center', fontsize=17, fontweight='bold', color='#1A237E')
    ax.text(50, 52, "Subject Code: 25ITT33 - Software Engineering (Unit 3: Design Models)", ha='center', fontsize=10.5, color='#546E7A')

    # Helper: State
    def draw_state(x, y, name, w=20, h=7):
        rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.5",
                                      facecolor='#EDE7F6', edgecolor='#512DA8', linewidth=2, zorder=3)
        ax.add_patch(rect)
        ax.text(x, y, name, ha='center', va='center', fontsize=11, fontweight='bold', color='#311B92', zorder=4)

    # Initial state
    ax.add_patch(patches.Circle((10, 30), 2.5, facecolor='black', edgecolor='black', zorder=3))
    ax.annotate("", xy=(20, 30), xytext=(12.5, 30), arrowprops=dict(arrowstyle="->", linewidth=2))
    ax.text(16, 32.5, "apply()", fontsize=9, fontweight='bold')

    draw_state(30, 30, "APPLIED\n[Status ID: 1]")
    draw_state(56, 30, "SHORTLISTED\n[Status ID: 2]")
    draw_state(85, 42, "SELECTED\n[Final / Hired]", w=20, h=8)
    draw_state(85, 18, "REJECTED\n[Closed]", w=20, h=8)

    # Transitions
    ax.annotate("", xy=(46, 30), xytext=(40, 30), arrowprops=dict(arrowstyle="->", linewidth=1.8))
    ax.text(48, 32.5, "screen()", fontsize=9, fontweight='bold')

    ax.annotate("", xy=(75, 42), xytext=(66, 32), arrowprops=dict(arrowstyle="->", linewidth=1.8, color='#2E7D32'))
    ax.text(70, 40, "interviewPass()", fontsize=9, fontweight='bold', color='#2E7D32')

    ax.annotate("", xy=(75, 18), xytext=(66, 28), arrowprops=dict(arrowstyle="->", linewidth=1.8, color='#C62828'))
    ax.text(70, 21, "interviewFail()", fontsize=9, fontweight='bold', color='#C62828')

    # Direct rejection from applied
    ax.annotate("", xy=(75, 15), xytext=(35, 26), arrowprops=dict(arrowstyle="->", linestyle='--', linewidth=1.5, color='#C62828'))
    ax.text(50, 17, "resumeRejection()", fontsize=8.5, fontweight='bold', color='#C62828')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "state_machine_diagram.png")
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"[SAVED] {path}")

if __name__ == "__main__":
    draw_use_case_diagram()
    draw_class_diagram()
    draw_sequence_diagram()
    draw_activity_diagram()
    draw_dfd_and_architecture()
    draw_state_machine_diagram()
