package com.jobportal.model;

import java.util.Objects;

/**
 * Student Model
 * Meets FR1: Maintain student details including ID, name, department, qualification, and skills
 * Demonstrates Unit 1 (Constructors, Overloading, Encapsulation) and Unit 2 (Inheritance from User)
 */
public class Student extends User {
    private String department;
    private String qualification;
    private double cgpa;
    private String skills;

    public Student(String studentId, String name, String email, String department, String qualification, double cgpa, String skills) {
        super(studentId, name, email);
        this.department = department;
        this.qualification = qualification;
        this.cgpa = cgpa;
        this.skills = skills;
    }

    // Overloaded Constructor
    public Student(String studentId, String name, String email, String department, double cgpa) {
        this(studentId, name, email, department, "B.Tech", cgpa, "Java, Python");
    }

    public String getDepartment() { return department; }
    public void setDepartment(String department) { this.department = department; }

    public String getQualification() { return qualification; }
    public void setQualification(String qualification) { this.qualification = qualification; }

    public double getCgpa() { return cgpa; }
    public void setCgpa(double cgpa) { this.cgpa = cgpa; }

    public String getSkills() { return skills; }
    public void setSkills(String skills) { this.skills = skills; }

    @Override
    public String getRole() {
        return "Student / Job Seeker";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return Objects.equals(id, student.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    @Override
    public String toString() {
        return String.format("Student[ID=%s, Name=%-18s, Dept=%-5s, CGPA=%.2f, Skills=%s]",
                id, name, department, cgpa, skills);
    }
}
