package com.jobportal.exception;

/**
 * Custom Exception thrown when a student attempts to apply for the same vacancy multiple times.
 * Meets FR4: Prevent duplicate applications by the same student for the same vacancy.
 * Demonstrates Unit 3: User defined Exception, try-catch, throw, throws.
 */
public class DuplicateApplicationException extends Exception {
    private final String studentId;
    private final String vacancyId;

    public DuplicateApplicationException(String studentId, String vacancyId) {
        super(String.format("DUPLICATE APPLICATION BLOCKED: Student '%s' has already applied for Vacancy '%s'!",
                studentId, vacancyId));
        this.studentId = studentId;
        this.vacancyId = vacancyId;
    }

    public String getStudentId() { return studentId; }
    public String getVacancyId() { return vacancyId; }
}
