import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_er_diagram(output_path):
    fig, ax = plt.subplots(figsize=(18, 12), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Color Palette
    entity_color = '#E3F2FD'     # Light blue
    entity_edge = '#1565C0'      # Deep blue
    rel_color = '#FFF3E0'        # Light orange
    rel_edge = '#E65100'         # Deep orange
    attr_color = '#F3E5F5'       # Light purple
    attr_edge = '#7B1FA2'        # Deep purple
    pk_color = '#E8F5E9'         # Light green
    pk_edge = '#2E7D32'          # Deep green

    # Title
    ax.text(50, 97, "ONLINE JOB PORTAL - ENTITY RELATIONSHIP (E-R) DIAGRAM", 
            ha='center', va='center', fontsize=18, fontweight='bold', color='#0D47A1')
    ax.text(50, 94, "Subject Code: 25ITT31 - Database Management Systems | Cheney Notation (Standard Academic)", 
            ha='center', va='center', fontsize=11, style='italic', color='#455A64')

    # Helper: Entity Box (Rectangle)
    def draw_entity(x, y, w, h, text):
        rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="square,pad=0",
                                      facecolor=entity_color, edgecolor=entity_edge, linewidth=2.2, zorder=3)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=12, fontweight='bold', color='#0D47A1', zorder=4)

    # Helper: Relationship (Diamond)
    def draw_relationship(x, y, size, text):
        half = size / 2
        diamond = patches.Polygon([[x, y + half], [x + size * 0.7, y], [x, y - half], [x - size * 0.7, y]],
                                  closed=True, facecolor=rel_color, edgecolor=rel_edge, linewidth=2, zorder=3)
        ax.add_patch(diamond)
        ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', color='#BF360C', zorder=4)

    # Helper: Attribute (Ellipse)
    def draw_attribute(x, y, rx, ry, text, is_pk=False, is_multivalued=False):
        ec = pk_edge if is_pk else attr_edge
        fc = pk_color if is_pk else attr_color
        lw = 2.0 if is_pk else 1.2
        ellipse = patches.Ellipse((x, y), rx * 2, ry * 2, facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3)
        ax.add_patch(ellipse)
        if is_multivalued:
            ellipse_inner = patches.Ellipse((x, y), rx * 1.7, ry * 1.6, facecolor=fc, edgecolor=ec, linewidth=1.0, zorder=3)
            ax.add_patch(ellipse_inner)
        txt = f"_{text}_" if is_pk else text
        fontw = 'bold' if is_pk else 'normal'
        ax.text(x, y, txt, ha='center', va='center', fontsize=8.5, fontweight=fontw, color='#212121', zorder=4)

    # Helper: Line with optional cardinality label
    def draw_line(p1, p2, label=None, lbl_pos=0.5, offset=(0, 2)):
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#37474F', linewidth=1.5, zorder=2)
        if label:
            lx = p1[0] + (p2[0] - p1[0]) * lbl_pos + offset[0]
            ly = p1[1] + (p2[1] - p1[1]) * lbl_pos + offset[1]
            ax.text(lx, ly, label, ha='center', va='center', fontsize=10, fontweight='bold', 
                    color='#D84315', bbox=dict(boxstyle="round,pad=0.2", facecolor='#FFFDE7', edgecolor='#FFF59D', alpha=0.9), zorder=5)

    # 1. ENTITY COORDINATES
    dept_pos = (15, 60)
    stu_pos = (40, 60)
    app_pos = (65, 60)
    vac_pos = (85, 60)
    comp_pos = (85, 25)

    # DRAW ENTITIES
    draw_entity(dept_pos[0], dept_pos[1], 16, 8, "DEPARTMENT")
    draw_entity(stu_pos[0], stu_pos[1], 16, 8, "STUDENT")
    draw_entity(app_pos[0], app_pos[1], 16, 8, "APPLICATION\n(Associative)")
    draw_entity(vac_pos[0], vac_pos[1], 16, 8, "JOB_VACANCY")
    draw_entity(comp_pos[0], comp_pos[1], 16, 8, "COMPANY")

    # 2. RELATIONSHIPS
    # Student belongs to Department
    draw_relationship(27.5, 60, 8, "BELONGS\nTO")
    draw_line((dept_pos[0] + 8, dept_pos[1]), (27.5 - 5.6, 60), "1", 0.5, (0, 2.5))
    draw_line((27.5 + 5.6, 60), (stu_pos[0] - 8, stu_pos[1]), "N", 0.5, (0, 2.5))

    # Student Applies (Application)
    draw_relationship(52.5, 60, 8, "SUBMITS")
    draw_line((stu_pos[0] + 8, stu_pos[1]), (52.5 - 5.6, 60), "1", 0.5, (0, 2.5))
    draw_line((52.5 + 5.6, 60), (app_pos[0] - 8, app_pos[1]), "N", 0.5, (0, 2.5))

    # Application for Vacancy
    draw_relationship(75, 60, 8, "TARGETS")
    draw_line((app_pos[0] + 8, app_pos[1]), (75 - 5.6, 60), "N", 0.5, (0, 2.5))
    draw_line((75 + 5.6, 60), (vac_pos[0] - 8, vac_pos[1]), "1", 0.5, (0, 2.5))

    # Company Posts Vacancies
    draw_relationship(85, 42.5, 8, "POSTS")
    draw_line((comp_pos[0], comp_pos[1] + 4), (85, 42.5 - 4), "1", 0.5, (2.5, 0))
    draw_line((85, 42.5 + 4), (vac_pos[0], vac_pos[1] - 4), "N", 0.5, (2.5, 0))

    # 3. ATTRIBUTES
    # Department Attributes
    draw_line(dept_pos, (8, 73))
    draw_attribute(8, 73, 5.5, 2.2, "DeptID (PK)", is_pk=True)
    draw_line(dept_pos, (22, 73))
    draw_attribute(22, 73, 5.5, 2.2, "DeptName")

    # Student Attributes
    draw_line(stu_pos, (32, 78))
    draw_attribute(32, 78, 5.5, 2.2, "StudentID (PK)", is_pk=True)
    draw_line(stu_pos, (40, 83))
    draw_attribute(40, 83, 5.0, 2.2, "Name")
    draw_line(stu_pos, (48, 78))
    draw_attribute(48, 78, 5.5, 2.2, "Qualification")
    draw_line(stu_pos, (33, 45))
    draw_attribute(33, 45, 5.0, 2.2, "CGPA")
    draw_line(stu_pos, (45, 45))
    draw_attribute(45, 45, 5.5, 2.2, "Skills", is_multivalued=True)
    draw_line(stu_pos, (52, 48))
    draw_attribute(52, 48, 5.0, 2.2, "Email")

    # Application Attributes
    draw_line(app_pos, (60, 78))
    draw_attribute(60, 78, 6.0, 2.2, "AppID (PK)", is_pk=True)
    draw_line(app_pos, (70, 78))
    draw_attribute(70, 78, 5.5, 2.2, "ApplyDate")
    draw_line(app_pos, (65, 45))
    draw_attribute(65, 45, 5.5, 2.2, "Status")

    # Job Vacancy Attributes
    draw_line(vac_pos, (78, 83))
    draw_attribute(78, 83, 6.0, 2.2, "VacancyID (PK)", is_pk=True)
    draw_line(vac_pos, (88, 83))
    draw_attribute(88, 83, 5.5, 2.2, "JobTitle")
    draw_line(vac_pos, (96, 75))
    draw_attribute(96, 75, 5.0, 2.2, "MinCGPA")
    draw_line(vac_pos, (96, 65))
    draw_attribute(96, 65, 5.5, 2.2, "ReqSkills")
    draw_line(vac_pos, (96, 55))
    draw_attribute(96, 55, 5.0, 2.2, "Salary")
    draw_line(vac_pos, (96, 45))
    draw_attribute(96, 45, 5.0, 2.2, "Openings")
    draw_line(vac_pos, (75, 50))
    draw_attribute(75, 50, 5.0, 2.2, "Location")

    # Company Attributes
    draw_line(comp_pos, (72, 28))
    draw_attribute(72, 28, 6.2, 2.2, "CompanyID (PK)", is_pk=True)
    draw_line(comp_pos, (72, 18))
    draw_attribute(72, 18, 6.0, 2.2, "CompanyName")
    draw_line(comp_pos, (85, 12))
    draw_attribute(85, 12, 5.5, 2.2, "Industry")
    draw_line(comp_pos, (96, 18))
    draw_attribute(96, 18, 5.5, 2.2, "Location")
    draw_line(comp_pos, (96, 28))
    draw_attribute(96, 28, 6.0, 2.2, "ContactEmail")

    # Cardinality & Legend Box
    legend_box = patches.FancyBboxPatch((4, 6), 50, 16, boxstyle="round,pad=0.8",
                                        facecolor='#FAFAFA', edgecolor='#BDBDBD', linewidth=1.5, zorder=2)
    ax.add_patch(legend_box)
    ax.text(6, 20, "E-R NOTATION & INTEGRITY CONSTRAINTS:", fontsize=10, fontweight='bold', color='#263238')
    ax.text(6, 17, "- Primary Keys: Underlined attributes (e.g., StudentID, VacancyID, CompanyID)", fontsize=9, color='#37474F')
    ax.text(6, 14.5, "- Duplicate Prevention (FR4): Enforced via UNIQUE(student_id, vacancy_id) in Application table", fontsize=9, color='#1B5E20', fontweight='bold')
    ax.text(6, 12, "- Status Domain (FR5): CHECK(status IN ('Applied', 'Shortlisted', 'Selected', 'Rejected'))", fontsize=9, color='#B71C1C')
    ax.text(6, 9.5, "- M:N Relationship between Student and Vacancy resolved via Associative Entity 'APPLICATION'", fontsize=9, color='#37474F')
    ax.text(6, 7.2, "- Referential Integrity: ON UPDATE CASCADE, ON DELETE RESTRICT / CASCADE", fontsize=9, color='#37474F')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[SUCCESS] E-R Diagram saved to: {output_path}")

if __name__ == "__main__":
    generate_er_diagram(r"C:\JOB PORTAL\2_Database_Management_System\E_R_Diagram.png")
