from PIL import Image, ImageDraw, ImageFont
import os

def render_terminal_image(text_lines, title, output_png, max_lines=45, width=1280):
    """
    Renders an authentic, high-res dark terminal window screenshot.
    """
    line_height = 22
    top_bar_height = 45
    padding = 25
    
    total_height = top_bar_height + (min(len(text_lines), max_lines) * line_height) + (padding * 2)
    img = Image.new('RGB', (width, total_height), color='#1E1E1E')
    draw = ImageDraw.Draw(img)

    # Title bar background
    draw.rectangle([0, 0, width, top_bar_height], fill='#2D2D2D')
    draw.line([0, top_bar_height, width, top_bar_height], fill='#3C3C3C', width=1)

    # Window controls (red, yellow, green dots)
    dot_radius = 6
    draw.ellipse([20, 16, 20 + dot_radius*2, 16 + dot_radius*2], fill='#FF5F56')
    draw.ellipse([40, 16, 40 + dot_radius*2, 16 + dot_radius*2], fill='#FFBD2E')
    draw.ellipse([60, 16, 60 + dot_radius*2, 16 + dot_radius*2], fill='#27C93F')

    # Load font
    font = None
    bold_font = None
    title_font = None
    try:
        font = ImageFont.truetype("consola.ttf", 15)
        bold_font = ImageFont.truetype("consolab.ttf", 15)
        title_font = ImageFont.truetype("segoeui.ttf", 13)
    except:
        font = ImageFont.load_default()
        bold_font = font
        title_font = font

    # Draw Title Bar Text
    draw.text((width // 2, 22), title, fill='#CCCCCC', font=title_font, anchor='mm')

    # Render lines
    y = top_bar_height + padding
    for i, line in enumerate(text_lines[:max_lines]):
        # Syntax highlighting logic for console output
        color = '#D4D4D4'  # default light gray
        if "===" in line or "---" in line or "+" in line:
            color = '#569CD6'  # blue accent
        elif "[SUCCESS]" in line or "[PASSED]" in line or "Selected" in line:
            color = '#4EC9B0'  # green/teal
        elif "[ERROR]" in line or "[REJECTED]" in line or "Failed" in line or "Rejected" in line:
            color = '#F44747'  # red
        elif "[INFO]" in line or "REPORT" in line or "TABLE" in line:
            color = '#DCDCAA'  # yellow/gold
        elif "|" in line:
            color = '#CE9178'  # light salmon for table data

        draw.text((padding, y), line, fill=color, font=font)
        y += line_height

    img.save(output_png, quality=95)
    print(f"[SUCCESS] Terminal screenshot rendered: {output_png}")

if __name__ == "__main__":
    dbms_output_path = r"C:\JOB PORTAL\2_Database_Management_System\dbms_output.txt"
    if os.path.exists(dbms_output_path):
        with open(dbms_output_path, "r", encoding="utf-8") as f:
            lines = [line.rstrip() for line in f.readlines()]
        render_terminal_image(
            lines[:45], 
            "Command Prompt - run_dbms.bat (Interactive SQLite RDBMS Console)", 
            r"C:\JOB PORTAL\2_Database_Management_System\screenshot_dbms_execution.png"
        )
