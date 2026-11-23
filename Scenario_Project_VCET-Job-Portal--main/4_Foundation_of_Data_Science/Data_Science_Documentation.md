# Category 4: Foundation of Data Science
**Course Code:** 25ITC31 - Foundations of Data Science  
**System:** Online Job Portal and Employment Trend Analysis System  

---

## 1. Syllabus Evaluation & Requirements Mapping

| Unit | Syllabus Topics (25ITC31) | System Implementation & Functional Requirements |
|---|---|---|
| **Unit 1: Data Science Fundamentals & Data Description** | Data types, variables, tables and graphs, averages (mean, median, mode), variability (variance, standard deviation, IQR), normal distributions, standard $(z)$ scores. | Evaluated numerical metrics on placement packages and student CGPAs. Calculated descriptive statistics and standardized $(z)$ scores ($z = \frac{x - \mu}{\sigma}$) to detect abnormal salaries and profile deviations. |
| **Unit 2: Python Foundations for Data Analysis** | Python fundamentals, data structures (lists, dicts), file handling, reading/writing CSV files, importing modules. | Built modular analytics scripts (`trend_analysis.py`, `interactive_ds.py`) loading and persisting `recruitment_data.csv`. |
| **Unit 3: Data Wrangling** | NumPy arrays, Pandas Series & DataFrames, indexing, aggregations, combining datasets, pivot tables. | Utilized Pandas for multi-column slicing and grouping. Created multi-dimensional pivot tables analyzing Department vs Status and Company vs Recruits. |
| **Unit 4: Data Cleaning & Transformation Techniques** | Data quality, handling missing values, duplicate detection and removal, type conversion, outlier identification (IQR), filtering and sorting. | Implemented automated audits for duplicate application pairs (FR4), verified zero missing values, and calculated Tukey's IQR fences ($Q_1 - 1.5 \times IQR$ and $Q_3 + 1.5 \times IQR$) to categorize salary tiers. |
| **Unit 5: Exploratory Data Analysis (EDA) & Visualization Techniques** | Principles of visualization, Matplotlib (line, bar, pie, histogram, scatter), Seaborn (box plots, heat maps, pair plots), correlation analysis. | Generated 6 publication-ready visual charts in `visualizations/`: Bar chart, Pie chart, Histogram with KDE, Scatter plot with regression line, Box plot, and Correlation Heatmap. (Meets FR7). |

---

## 2. Statistical Findings & Analytical Insights

### Summary Metrics:
- **Student CGPA Distribution**: Mean = $8.384$, Median = $8.525$, Standard Deviation = $0.598$, Range = $[7.20 - 9.20]$.
- **Salary Package Distribution**: Mean = INR $1,125,000$, Median = INR $1,175,000$, IQR = INR $1,087,500$.
- **Standard $(z)$ Scores**: Top tier packages (Google INR 18 LPA) scored $z = +1.216$, indicating high placement performance relative to the campus mean.
- **Correlation**: Strong positive correlation ($r = 0.658$) observed between student CGPA and offered salary package.

### Generated Visualizations (Saved in `visualizations/`):
1. `1_dept_applications_bar.png`: Department-wise Applications vs Placed Count (Bar Chart).
2. `2_status_distribution_pie.png`: Recruitment Status Distribution (Pie Chart).
3. `3_salary_distribution_hist.png`: Salary Package Distribution with Kernel Density Estimation (Histogram).
4. `4_cgpa_vs_salary_scatter.png`: Student CGPA vs Offered Salary with Regression Trendline (Scatter Plot).
5. `5_salary_by_dept_boxplot.png`: Salary Spread across Academic Departments (Box Plot).
6. `6_correlation_heatmap.png`: Pearson Correlation Heatmap across numeric features.

---

## 3. How to Run the Program

1. **Interactive Manual Keyboard Mode (`run_datascience.bat`)**:
   - Double-click `run_datascience.bat` in this folder.
   - Use menu options (1 to 8) to inspect data, compute z-scores, view pivot tables, filter candidates by department/CGPA via keyboard input, and regenerate plots.
2. **Automated Verification Mode**:
   ```cmd
   python trend_analysis.py
   ```
   This regenerates all 6 charts in `visualizations/` and updates `datascience_output.txt`.

---

## 4. Folder Artifacts Checklist
- [x] `recruitment_data.csv`: Preprocessed recruitment and application dataset.
- [x] `trend_analysis.py`: Core descriptive statistics and visualization engine.
- [x] `interactive_ds.py`: Interactive CLI supporting step-by-step manual keyboard input.
- [x] `visualizations/`: Directory with all 6 generated high-resolution PNG charts.
- [x] `run_datascience.bat`: Double-clickable runnable batch script.
- [x] `datascience_output.txt`: Statistical calculations, z-scores, and pivot tables.
- [x] `screenshot_datascience_execution.png`: Screenshot of Data Science program execution.
- [x] `Data_Science_Documentation.md`: Comprehensive documentation.
