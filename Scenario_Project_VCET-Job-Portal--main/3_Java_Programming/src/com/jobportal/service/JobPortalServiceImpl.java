package com.jobportal.service;

import com.jobportal.exception.DuplicateApplicationException;
import com.jobportal.exception.IneligibleStudentException;
import com.jobportal.exception.VacancyNotFoundException;
import com.jobportal.model.*;

import java.time.LocalDate;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Service Implementation
 * Demonstrates Unit 3 (Exceptions), Unit 4 (Strings), and Unit 5 (Generics, Collections, Lambdas, Streams)
 */
public class JobPortalServiceImpl implements JobPortalService {
    // Unit 5: Generic Collections
    private final Map<String, Student> students = new LinkedHashMap<>();
    private final Map<String, Company> companies = new LinkedHashMap<>();
    private final Map<String, JobVacancy> vacancies = new LinkedHashMap<>();
    private final List<JobApplication> applications = new ArrayList<>();
    
    // Set to track unique (studentId + "#" + vacancyId) for fast duplicate check (FR4)
    private final Set<String> applicationKeys = new HashSet<>();

    public JobPortalServiceImpl() {
        seedSampleData();
    }

    private void seedSampleData() {
        // Companies
        addCompany(new Company("CMP101", "Google India", "Product / Internet", "Bengaluru", "careers@google.com"));
        addCompany(new Company("CMP102", "Microsoft IDC", "Product / Cloud", "Hyderabad", "recruitment@microsoft.com"));
        addCompany(new Company("CMP103", "Amazon Dev Centre", "E-Commerce / Cloud", "Chennai", "jobs@amazon.com"));
        addCompany(new Company("CMP104", "Tata Consultancy Services", "IT Services", "Chennai", "campus@tcs.com"));
        addCompany(new Company("CMP105", "Zoho Corporation", "SaaS Software", "Tenkasi", "talent@zohocorp.com"));
        addCompany(new Company("CMP106", "Bosch Global Software", "Automotive", "Coimbatore", "careers@bosch.com"));

        // Vacancies
        postJobVacancy(new JobVacancy("VAC201", "CMP101", "Google India", "Software Development Engineer", 8.50, "Java, Data Structures", "Bengaluru", 1800000, 5));
        postJobVacancy(new JobVacancy("VAC202", "CMP102", "Microsoft IDC", "Cloud Solutions Associate", 8.00, "Cloud, Linux, Python", "Hyderabad", 1500000, 8));
        postJobVacancy(new JobVacancy("VAC203", "CMP103", "Amazon Dev Centre", "Data Engineer", 8.00, "Python, SQL, Big Data", "Chennai", 1600000, 4));
        postJobVacancy(new JobVacancy("VAC204", "CMP104", "Tata Consultancy Services", "Systems Engineer", 7.00, "Java, C++, DBMS", "Chennai", 450000, 25));
        postJobVacancy(new JobVacancy("VAC205", "CMP105", "Zoho Corporation", "Product Developer", 7.50, "Java, C, Web Dev", "Tenkasi", 850000, 10));
        postJobVacancy(new JobVacancy("VAC206", "CMP106", "Bosch Global Software", "Embedded Engineer", 7.50, "Embedded C, RTOS", "Coimbatore", 700000, 6));

        // Students
        registerStudent(new Student("STU001", "Aarav Sharma", "aarav.sharma@campus.edu", "IT", "B.Tech IT", 8.75, "Java, Python, SQL, Spring Boot"));
        registerStudent(new Student("STU002", "Diya Patel", "diya.patel@campus.edu", "CSE", "B.E CSE", 9.20, "Python, ML, SQL, C++"));
        registerStudent(new Student("STU003", "Rohan Verma", "rohan.verma@campus.edu", "ECE", "B.E ECE", 7.80, "Embedded C, IoT, Python"));
        registerStudent(new Student("STU004", "Ananya Iyer", "ananya.iyer@campus.edu", "AIDS", "B.Tech AIDS", 8.90, "Python, Data Science, Pandas"));
        registerStudent(new Student("STU005", "Karthik Raja", "karthik.raja@campus.edu", "MECH", "B.E MECH", 7.45, "AutoCAD, SolidWorks, Python"));
        registerStudent(new Student("STU006", "Sneha Menon", "sneha.menon@campus.edu", "IT", "B.Tech IT", 8.10, "Java, React, SQL"));
        registerStudent(new Student("STU007", "Vikramaditya Rao", "vikram.rao@campus.edu", "CSE", "B.E CSE", 8.65, "Java, Spring Boot, Docker"));
        registerStudent(new Student("STU008", "Pooja Hegde", "pooja.hegde@campus.edu", "ECE", "B.E ECE", 8.05, "VLSI, Verilog, C"));
        registerStudent(new Student("STU009", "Naveen Kumar", "naveen.kumar@campus.edu", "AIDS", "B.Tech AIDS", 9.05, "Deep Learning, NLP, Python"));
        registerStudent(new Student("STU010", "Meera Krishnan", "meera.krishnan@campus.edu", "IT", "B.Tech IT", 7.60, "Python, Django, PostgreSQL"));

        // Applications with diverse statuses
        seedApplication("STU001", "VAC201", ApplicationStatus.SELECTED);
        seedApplication("STU001", "VAC205", ApplicationStatus.SHORTLISTED);
        seedApplication("STU002", "VAC201", ApplicationStatus.SELECTED);
        seedApplication("STU003", "VAC206", ApplicationStatus.SELECTED);
        seedApplication("STU004", "VAC203", ApplicationStatus.SELECTED);
        seedApplication("STU005", "VAC204", ApplicationStatus.APPLIED);
        seedApplication("STU006", "VAC205", ApplicationStatus.SELECTED);
        seedApplication("STU007", "VAC202", ApplicationStatus.SELECTED);
        seedApplication("STU008", "VAC206", ApplicationStatus.SHORTLISTED);
        seedApplication("STU009", "VAC201", ApplicationStatus.REJECTED);
        seedApplication("STU009", "VAC203", ApplicationStatus.SELECTED);
        seedApplication("STU010", "VAC204", ApplicationStatus.SELECTED);
    }

    private void seedApplication(String stuId, String vacId, ApplicationStatus status) {
        String key = stuId + "#" + vacId;
        if (!applicationKeys.contains(key)) {
            JobApplication app = new JobApplication(stuId, vacId);
            app.setStatus(status);
            applications.add(app);
            applicationKeys.add(key);
        }
    }

    @Override
    public void registerStudent(Student student) {
        students.put(student.getId(), student);
    }

    @Override
    public Student getStudent(String studentId) {
        return students.get(studentId);
    }

    @Override
    public List<Student> getAllStudents() {
        return new ArrayList<>(students.values());
    }

    @Override
    public void addCompany(Company company) {
        companies.put(company.getCompanyId(), company);
    }

    @Override
    public List<Company> getAllCompanies() {
        return new ArrayList<>(companies.values());
    }

    @Override
    public void postJobVacancy(JobVacancy vacancy) {
        vacancies.put(vacancy.getVacancyId(), vacancy);
    }

    @Override
    public JobVacancy getJobVacancy(String vacancyId) {
        return vacancies.get(vacancyId);
    }

    @Override
    public List<JobVacancy> getAllVacancies() {
        return new ArrayList<>(vacancies.values());
    }

    @Override
    public synchronized JobApplication applyForJob(String studentId, String vacancyId)
            throws DuplicateApplicationException, IneligibleStudentException, VacancyNotFoundException {
        // Verify vacancy existence
        JobVacancy vacancy = vacancies.get(vacancyId);
        if (vacancy == null) {
            throw new VacancyNotFoundException(vacancyId);
        }

        // Verify student existence
        Student student = students.get(studentId);
        if (student == null) {
            throw new IllegalArgumentException("Student ID '" + studentId + "' is not registered in the system.");
        }

        // FR4: Prevent duplicate applications
        String key = studentId + "#" + vacancyId;
        if (applicationKeys.contains(key)) {
            throw new DuplicateApplicationException(studentId, vacancyId);
        }

        // FR3: Check student eligibility (CGPA check)
        if (student.getCgpa() < vacancy.getMinCgpa()) {
            throw new IneligibleStudentException(studentId, student.getCgpa(), vacancy.getMinCgpa());
        }

        // Create and record application
        JobApplication application = new JobApplication(studentId, vacancyId);
        applications.add(application);
        applicationKeys.add(key);
        return application;
    }

    @Override
    public synchronized boolean updateApplicationStatus(int applicationId, ApplicationStatus newStatus) {
        for (JobApplication app : applications) {
            if (app.getApplicationId() == applicationId) {
                app.setStatus(newStatus);
                return true;
            }
        }
        return false;
    }

    @Override
    public List<JobApplication> getAllApplications() {
        return new ArrayList<>(applications);
    }

    @Override
    public List<JobApplication> getApplicationsByStudent(String studentId) {
        // Stream API: Filtering (Unit 5)
        return applications.stream()
                .filter(app -> app.getStudentId().equalsIgnoreCase(studentId))
                .collect(Collectors.toList());
    }

    @Override
    public Map<String, Long> getSelectionCountByDepartment() {
        // Stream API: Filtering, Mapping, and Grouping (Unit 5 & Meets FR6)
        return applications.stream()
                .filter(app -> app.getStatus() == ApplicationStatus.SELECTED)
                .map(app -> students.get(app.getStudentId()))
                .filter(Objects::nonNull)
                .collect(Collectors.groupingBy(Student::getDepartment, Collectors.counting()));
    }

    @Override
    public Map<String, Long> getRecruitmentCountByCompany() {
        // Stream API: Grouping and Counting by Company (Meets FR6)
        return applications.stream()
                .filter(app -> app.getStatus() == ApplicationStatus.SELECTED)
                .map(app -> vacancies.get(app.getVacancyId()))
                .filter(Objects::nonNull)
                .collect(Collectors.groupingBy(JobVacancy::getCompanyName, Collectors.counting()));
    }

    @Override
    public Map<ApplicationStatus, Long> getApplicationStatusDistribution() {
        return applications.stream()
                .collect(Collectors.groupingBy(JobApplication::getStatus, Collectors.counting()));
    }

    @Override
    public List<JobVacancy> getVacanciesSortedBySalary() {
        // Stream API: Sorting with Comparator (Unit 5)
        return vacancies.values().stream()
                .sorted(Comparator.comparingDouble(JobVacancy::getSalary).reversed())
                .collect(Collectors.toList());
    }

    @Override
    public List<Student> getEligibleStudentsForVacancy(String vacancyId) throws VacancyNotFoundException {
        JobVacancy vac = vacancies.get(vacancyId);
        if (vac == null) throw new VacancyNotFoundException(vacancyId);
        return students.values().stream()
                .filter(s -> s.getCgpa() >= vac.getMinCgpa())
                .sorted(Comparator.comparingDouble(Student::getCgpa).reversed())
                .collect(Collectors.toList());
    }

    @Override
    public String generateComprehensiveSummaryReport() {
        // Unit 4: String and StringBuilder Handling
        StringBuilder sb = new StringBuilder();
        sb.append("================================================================================\n");
        sb.append("         ONLINE JOB PORTAL - PLACEMENT CELL SUMMARY REPORT (FR6)\n");
        sb.append("================================================================================\n");
        sb.append(String.format("Total Registered Students : %d\n", students.size()));
        sb.append(String.format("Total Partner Companies   : %d\n", companies.size()));
        sb.append(String.format("Total Job Vacancies Posted: %d\n", vacancies.size()));
        sb.append(String.format("Total Applications Logged : %d\n", applications.size()));

        // Calculate Average Package Offered using Stream API
        double avgSalary = vacancies.values().stream()
                .mapToDouble(JobVacancy::getSalary)
                .average().orElse(0.0);
        sb.append(String.format("Average Annual Package    : INR %,.2f\n\n", avgSalary));

        sb.append("--- DEPARTMENT-WISE SELECTION BREAKDOWN ---\n");
        getSelectionCountByDepartment().forEach((dept, count) ->
                sb.append(String.format("  * Department %-6s: %d Students Selected\n", dept, count)));

        sb.append("\n--- COMPANY-WISE RECRUITMENT COUNTS ---\n");
        getRecruitmentCountByCompany().forEach((comp, count) ->
                sb.append(String.format("  * %-25s: %d Recruits\n", comp, count)));

        sb.append("\n--- APPLICATION STATUS DISTRIBUTION ---\n");
        getApplicationStatusDistribution().forEach((status, count) ->
                sb.append(String.format("  * %-12s: %d\n", status.getLabel(), count)));

        sb.append("================================================================================\n");
        return sb.toString();
    }
}
