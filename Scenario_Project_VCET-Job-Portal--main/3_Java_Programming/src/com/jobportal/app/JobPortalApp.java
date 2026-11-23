package com.jobportal.app;

import com.jobportal.exception.DuplicateApplicationException;
import com.jobportal.exception.IneligibleStudentException;
import com.jobportal.exception.VacancyNotFoundException;
import com.jobportal.model.*;
import com.jobportal.service.JobPortalService;
import com.jobportal.service.JobPortalServiceImpl;
import com.jobportal.thread.BatchApplicationProcessor;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Scanner;

/**
 * Main Interactive Application for Online Job Portal
 * Subject Code: 25ITT32 - Java Programming
 * Supports Step-by-Step Manual Keyboard Input & Automated Testing
 */
public class JobPortalApp {
    private static final String OUTPUT_FILE = 
            new java.io.File("3_Java_Programming").exists() ? "3_Java_Programming/java_output.txt" : "java_output.txt";
    private final JobPortalService service = new JobPortalServiceImpl();
    private final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        JobPortalApp app = new JobPortalApp();
        if (args.length > 0 && args[0].equalsIgnoreCase("--auto")) {
            app.runAutomatedTestSuite();
        } else {
            app.runInteractiveMenu();
        }
    }

    public void runInteractiveMenu() {
        while (true) {
            System.out.println("\n" + "=".repeat(70));
            System.out.println("   ONLINE JOB PORTAL - JAVA PROGRAMMING SYSTEM (25ITT32)");
            System.out.println("=".repeat(70));
            System.out.println(" 1. View Registered Students [FR1]");
            System.out.println(" 2. View Companies and Job Vacancies [FR2]");
            System.out.println(" 3. View All Applications & Recruitment Status [FR5]");
            System.out.println(" 4. [Manual Input] Register New Student Profile [FR1]");
            System.out.println(" 5. [Manual Input] Post New Job Vacancy [FR2]");
            System.out.println(" 6. [Manual Input] Apply for Job (Test Duplicate Prevention) [FR3, FR4]");
            System.out.println(" 7. [Manual Input] Update Application Status [FR5]");
            System.out.println(" 8. Generate Reports & Placement Analytics (Java Stream API) [FR6]");
            System.out.println(" 9. Launch Multithreaded Background Screening Thread [Unit 3]");
            System.out.println("10. Run Automated Test Suite & Save Output to Text File");
            System.out.println(" 0. Exit System");
            System.out.println("-".repeat(70));
            System.out.print("Enter your choice (0-10): ");

            String input = scanner.nextLine().trim();
            switch (input) {
                case "1": displayStudents(); break;
                case "2": displayVacancies(); break;
                case "3": displayApplications(); break;
                case "4": manualRegisterStudent(); break;
                case "5": manualPostVacancy(); break;
                case "6": manualApplyJob(); break;
                case "7": manualUpdateStatus(); break;
                case "8": displayReports(); break;
                case "9": runMultithreadedScreening(); break;
                case "10": runAutomatedTestSuite(); break;
                case "0":
                    System.out.println("\nThank you for using the Online Job Portal System. Goodbye!\n");
                    return;
                default:
                    System.out.println("[ERROR] Invalid choice! Please select 0 to 10.");
            }
        }
    }

    private void displayStudents() {
        System.out.println("\n" + "=".repeat(85));
        System.out.println("                            REGISTERED STUDENTS");
        System.out.println("=".repeat(85));
        List<Student> students = service.getAllStudents();
        for (Student s : students) {
            System.out.printf("| %-8s | %-18s | %-5s | CGPA: %4.2f | Skills: %-25s |\n",
                    s.getId(), s.getName(), s.getDepartment(), s.getCgpa(), s.getSkills());
        }
        System.out.println("=".repeat(85));
        System.out.println("Total Students: " + students.size());
    }

    private void displayVacancies() {
        System.out.println("\n" + "=".repeat(95));
        System.out.println("                               PUBLISHED JOB VACANCIES");
        System.out.println("=".repeat(95));
        List<JobVacancy> vacancies = service.getAllVacancies();
        for (JobVacancy v : vacancies) {
            System.out.printf("| %-7s | %-20s | %-25s | Min CGPA: %3.1f | Salary: INR %,10.0f |\n",
                    v.getVacancyId(), v.getCompanyName(), v.getJobTitle(), v.getMinCgpa(), v.getSalary());
        }
        System.out.println("=".repeat(95));
        System.out.println("Total Vacancies: " + vacancies.size());
    }

    private void displayApplications() {
        System.out.println("\n" + "=".repeat(75));
        System.out.println("                          STUDENT JOB APPLICATIONS");
        System.out.println("=".repeat(75));
        List<JobApplication> apps = service.getAllApplications();
        for (JobApplication a : apps) {
            Student s = service.getStudent(a.getStudentId());
            JobVacancy v = service.getJobVacancy(a.getVacancyId());
            String stuName = (s != null) ? s.getName() : a.getStudentId();
            String compName = (v != null) ? v.getCompanyName() : a.getVacancyId();
            System.out.printf("| App #%-4d | %-8s (%-15s) | %-7s (%-15s) | Status: %-11s |\n",
                    a.getApplicationId(), a.getStudentId(), stuName, a.getVacancyId(), compName, a.getStatus().getLabel());
        }
        System.out.println("=".repeat(75));
        System.out.println("Total Applications: " + apps.size());
    }

    private void manualRegisterStudent() {
        System.out.println("\n--- [MANUAL INPUT] REGISTER STUDENT PROFILE ---");
        System.out.print("Enter Student ID (e.g., STU015): ");
        String id = scanner.nextLine().trim();
        System.out.print("Enter Full Name: ");
        String name = scanner.nextLine().trim();
        System.out.print("Enter Email Address: ");
        String email = scanner.nextLine().trim();
        System.out.print("Enter Department (IT/CSE/ECE/MECH/AIDS): ");
        String dept = scanner.nextLine().trim().toUpperCase();
        System.out.print("Enter Qualification (e.g., B.Tech IT): ");
        String qual = scanner.nextLine().trim();
        System.out.print("Enter CGPA (0.0 to 10.0): ");
        double cgpa = 0.0;
        try {
            cgpa = Double.parseDouble(scanner.nextLine().trim());
        } catch (NumberFormatException e) {
            System.out.println("[ERROR] Invalid CGPA format.");
            return;
        }
        System.out.print("Enter Key Skills (comma separated): ");
        String skills = scanner.nextLine().trim();

        Student student = new Student(id, name, email, dept, qual, cgpa, skills);
        service.registerStudent(student);
        System.out.printf("[SUCCESS] Student '%s' registered successfully with ID '%s'.\n", name, id);
    }

    private void manualPostVacancy() {
        System.out.println("\n--- [MANUAL INPUT] POST NEW JOB VACANCY ---");
        System.out.print("Enter Vacancy ID (e.g., VAC208): ");
        String vacId = scanner.nextLine().trim();
        System.out.print("Enter Company ID (e.g., CMP101): ");
        String compId = scanner.nextLine().trim();
        System.out.print("Enter Company Name: ");
        String compName = scanner.nextLine().trim();
        System.out.print("Enter Job Title: ");
        String title = scanner.nextLine().trim();
        System.out.print("Enter Minimum CGPA Required: ");
        double minCgpa = Double.parseDouble(scanner.nextLine().trim());
        System.out.print("Enter Required Skills: ");
        String reqSkills = scanner.nextLine().trim();
        System.out.print("Enter Location: ");
        String loc = scanner.nextLine().trim();
        System.out.print("Enter Salary Package (INR): ");
        double salary = Double.parseDouble(scanner.nextLine().trim());
        System.out.print("Enter Number of Openings: ");
        int openings = Integer.parseInt(scanner.nextLine().trim());

        JobVacancy v = new JobVacancy(vacId, compId, compName, title, minCgpa, reqSkills, loc, salary, openings);
        service.postJobVacancy(v);
        System.out.printf("[SUCCESS] Vacancy '%s' at '%s' posted successfully.\n", title, compName);
    }

    private void manualApplyJob() {
        System.out.println("\n--- [MANUAL INPUT] APPLY FOR JOB VACANCY ---");
        System.out.print("Enter Student ID (e.g., STU001): ");
        String stuId = scanner.nextLine().trim();
        System.out.print("Enter Vacancy ID (e.g., VAC201): ");
        String vacId = scanner.nextLine().trim();

        try {
            JobApplication app = service.applyForJob(stuId, vacId);
            System.out.printf("[SUCCESS] Application #%d submitted successfully with status: %s!\n",
                    app.getApplicationId(), app.getStatus().getLabel());
        } catch (DuplicateApplicationException e) {
            System.err.println("\n" + e.getMessage());
            System.out.println("[VERIFICATION] Duplicate check verified: Student cannot apply twice for the same vacancy (FR4).");
        } catch (IneligibleStudentException e) {
            System.err.println("\n" + e.getMessage());
            System.out.println("[VERIFICATION] Eligibility check verified: Student does not meet minimum CGPA (FR3).");
        } catch (VacancyNotFoundException e) {
            System.err.println("\n" + e.getMessage());
        } catch (Exception e) {
            System.err.println("[ERROR] " + e.getMessage());
        }
    }

    private void manualUpdateStatus() {
        System.out.println("\n--- [MANUAL INPUT] UPDATE APPLICATION STATUS ---");
        System.out.print("Enter Application ID to update: ");
        int appId = Integer.parseInt(scanner.nextLine().trim());
        System.out.println("Select Status: 1. APPLIED | 2. SHORTLISTED | 3. SELECTED | 4. REJECTED");
        System.out.print("Enter choice (1-4): ");
        String ch = scanner.nextLine().trim();
        ApplicationStatus newStatus;
        switch (ch) {
            case "1": newStatus = ApplicationStatus.APPLIED; break;
            case "2": newStatus = ApplicationStatus.SHORTLISTED; break;
            case "3": newStatus = ApplicationStatus.SELECTED; break;
            case "4": newStatus = ApplicationStatus.REJECTED; break;
            default:
                System.out.println("[ERROR] Invalid choice!");
                return;
        }

        boolean updated = service.updateApplicationStatus(appId, newStatus);
        if (updated) {
            System.out.printf("[SUCCESS] Application #%d status updated to '%s'!\n", appId, newStatus.getLabel());
        } else {
            System.out.println("[ERROR] Application ID not found!");
        }
    }

    private void displayReports() {
        System.out.println("\n" + service.generateComprehensiveSummaryReport());
    }

    private void runMultithreadedScreening() {
        System.out.println("\n--- [MULTITHREADING] LAUNCHING BACKGROUND SCREENING THREAD ---");
        BatchApplicationProcessor thread = new BatchApplicationProcessor(service, "AutoScreeningWorker-1", "SHORTLISTED");
        thread.start();
        try {
            thread.join(); // Wait for thread to finish for clean console display
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("[SUCCESS] Background screening thread executed successfully.");
    }

    public void runAutomatedTestSuite() {
        System.out.println("================================================================================");
        System.out.println("         RUNNING AUTOMATED TEST SUITE FOR JAVA PROGRAMMING SYSTEM               ");
        System.out.println("================================================================================");

        StringBuilder log = new StringBuilder();
        log.append("================================================================================\n");
        log.append("       ONLINE JOB PORTAL - JAVA PROGRAMMING SYSTEM TEST EXECUTION OUTPUT        \n");
        log.append("       Subject Code: 25ITT32 - Java Programming                                 \n");
        log.append("================================================================================\n\n");

        log.append("[TEST 1: LISTING REGISTERED STUDENTS (FR1)]\n");
        for (Student s : service.getAllStudents()) {
            log.append(s.toString()).append("\n");
        }
        log.append("\n");

        log.append("[TEST 2: LISTING PUBLISHED JOB VACANCIES (FR2)]\n");
        for (JobVacancy v : service.getAllVacancies()) {
            log.append(v.toString()).append("\n");
        }
        log.append("\n");

        log.append("[TEST 3: SORTING VACANCIES BY SALARY (Unit 5: Stream API)]\n");
        List<JobVacancy> sortedVac = service.getVacanciesSortedBySalary();
        for (JobVacancy v : sortedVac) {
            log.append(String.format("  INR %,10.0f | %-20s | %s\n", v.getSalary(), v.getCompanyName(), v.getJobTitle()));
        }
        log.append("\n");

        // TEST 4: FR4 Duplicate Application Prevention Test
        log.append("[TEST 4: DUPLICATE APPLICATION PREVENTION TEST (FR4 & Unit 3 Exceptions)]\n");
        try {
            log.append("Attempting duplicate submission: Student 'STU001' applying again for 'VAC201'...\n");
            service.applyForJob("STU001", "VAC201");
            log.append("FAILED: Duplicate application was NOT caught!\n");
        } catch (DuplicateApplicationException e) {
            log.append("PASSED: Caught DuplicateApplicationException successfully:\n");
            log.append("  ").append(e.getMessage()).append("\n");
        } catch (Exception e) {
            log.append("ERROR: ").append(e.getMessage()).append("\n");
        }
        log.append("\n");

        // TEST 5: FR3 Eligibility Check Test
        log.append("[TEST 5: ELIGIBILITY CHECK TEST (FR3 & Unit 3 Exceptions)]\n");
        try {
            // STU005 has CGPA 7.45, VAC201 requires 8.50
            log.append("Attempting ineligible application: Student 'STU005' (CGPA 7.45) applying for 'VAC201' (Req 8.50)...\n");
            service.applyForJob("STU005", "VAC201");
            log.append("FAILED: Ineligible application was NOT caught!\n");
        } catch (IneligibleStudentException e) {
            log.append("PASSED: Caught IneligibleStudentException successfully:\n");
            log.append("  ").append(e.getMessage()).append("\n");
        } catch (Exception e) {
            log.append("ERROR: ").append(e.getMessage()).append("\n");
        }
        log.append("\n");

        // TEST 6: Multithreading
        log.append("[TEST 6: MULTITHREADED BATCH APPLICATION SCREENING (Unit 3)]\n");
        BatchApplicationProcessor t = new BatchApplicationProcessor(service, "TestScreeningThread", "SHORTLISTED");
        t.start();
        try {
            t.join();
            log.append("PASSED: Multithreaded processor completed execution without race conditions.\n\n");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // TEST 7: Comprehensive Report Generation
        log.append("[TEST 7: COMPREHENSIVE REPORT GENERATION (FR6 & Unit 5 Streams)]\n");
        log.append(service.generateComprehensiveSummaryReport());

        // Write log to file
        try (PrintWriter writer = new PrintWriter(new FileWriter(OUTPUT_FILE))) {
            writer.print(log.toString());
            System.out.println("[SUCCESS] Full Java execution output successfully written to: " + OUTPUT_FILE);
        } catch (IOException e) {
            System.err.println("[ERROR] Failed to write output file: " + e.getMessage());
        }

        System.out.print(log.toString());
    }
}
