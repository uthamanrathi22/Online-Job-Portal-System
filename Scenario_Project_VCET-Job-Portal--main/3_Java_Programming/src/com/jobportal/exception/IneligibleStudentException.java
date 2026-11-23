package com.jobportal.exception;

/**
 * Custom Exception thrown when a student does not meet the eligibility criteria for a vacancy.
 * Meets FR3: Allow eligible students to apply for available job vacancies.
 */
public class IneligibleStudentException extends Exception {
    private final String studentId;
    private final double studentCgpa;
    private final double minRequiredCgpa;

    public IneligibleStudentException(String studentId, double studentCgpa, double minRequiredCgpa) {
        super(String.format("ELIGIBILITY CRITERIA NOT MET: Student '%s' has CGPA %.2f, which is below the minimum required CGPA of %.2f!",
                studentId, studentCgpa, minRequiredCgpa));
        this.studentId = studentId;
        this.studentCgpa = studentCgpa;
        this.minRequiredCgpa = minRequiredCgpa;
    }

    public String getStudentId() { return studentId; }
    public double getStudentCgpa() { return studentCgpa; }
    public double getMinRequiredCgpa() { return minRequiredCgpa; }
}
