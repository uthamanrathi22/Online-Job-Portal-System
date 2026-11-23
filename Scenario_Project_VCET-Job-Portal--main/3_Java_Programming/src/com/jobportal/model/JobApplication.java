package com.jobportal.model;

import java.time.LocalDate;

/**
 * Job Application Model
 * Meets FR3, FR4, and FR5
 */
public class JobApplication {
    private static int idCounter = 1000;
    private int applicationId;
    private String studentId;
    private String vacancyId;
    private LocalDate applyDate;
    private ApplicationStatus status;

    public JobApplication(String studentId, String vacancyId) {
        this(++idCounter, studentId, vacancyId, LocalDate.now(), ApplicationStatus.APPLIED);
    }

    public JobApplication(int applicationId, String studentId, String vacancyId, LocalDate applyDate, ApplicationStatus status) {
        this.applicationId = applicationId;
        this.studentId = studentId;
        this.vacancyId = vacancyId;
        this.applyDate = applyDate;
        this.status = status;
        if (applicationId >= idCounter) {
            idCounter = applicationId + 1;
        }
    }

    public int getApplicationId() { return applicationId; }
    public String getStudentId() { return studentId; }
    public String getVacancyId() { return vacancyId; }
    public LocalDate getApplyDate() { return applyDate; }
    public ApplicationStatus getStatus() { return status; }
    public void setStatus(ApplicationStatus status) { this.status = status; }

    @Override
    public String toString() {
        return String.format("App[ID=%-4d, Student=%-8s, Vacancy=%-8s, Date=%s, Status=%-11s]",
                applicationId, studentId, vacancyId, applyDate, status.getLabel());
    }
}
