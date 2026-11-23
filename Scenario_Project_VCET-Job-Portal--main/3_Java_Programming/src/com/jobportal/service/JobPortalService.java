package com.jobportal.service;

import com.jobportal.exception.DuplicateApplicationException;
import com.jobportal.exception.IneligibleStudentException;
import com.jobportal.exception.VacancyNotFoundException;
import com.jobportal.model.*;

import java.util.List;
import java.util.Map;

/**
 * Service Interface for Job Portal Operations
 * Demonstrates Unit 2: Interfaces
 */
public interface JobPortalService {
    void registerStudent(Student student);
    Student getStudent(String studentId);
    List<Student> getAllStudents();

    void addCompany(Company company);
    List<Company> getAllCompanies();

    void postJobVacancy(JobVacancy vacancy);
    JobVacancy getJobVacancy(String vacancyId);
    List<JobVacancy> getAllVacancies();

    JobApplication applyForJob(String studentId, String vacancyId)
            throws DuplicateApplicationException, IneligibleStudentException, VacancyNotFoundException;

    boolean updateApplicationStatus(int applicationId, ApplicationStatus newStatus);
    List<JobApplication> getAllApplications();
    List<JobApplication> getApplicationsByStudent(String studentId);

    // Reporting & Analytics using Java Stream API (Unit 5 & Meets FR6)
    Map<String, Long> getSelectionCountByDepartment();
    Map<String, Long> getRecruitmentCountByCompany();
    Map<ApplicationStatus, Long> getApplicationStatusDistribution();
    List<JobVacancy> getVacanciesSortedBySalary();
    List<Student> getEligibleStudentsForVacancy(String vacancyId) throws VacancyNotFoundException;
    String generateComprehensiveSummaryReport();
}
