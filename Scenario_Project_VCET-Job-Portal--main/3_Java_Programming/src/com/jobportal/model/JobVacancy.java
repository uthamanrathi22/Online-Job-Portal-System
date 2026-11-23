package com.jobportal.model;

/**
 * Job Vacancy Model
 * Meets FR2: Maintain job vacancy information including job title, eligibility criteria, location, and salary range
 */
public class JobVacancy {
    private String vacancyId;
    private String companyId;
    private String companyName;
    private String jobTitle;
    private double minCgpa;
    private String requiredSkills;
    private String location;
    private double salary;
    private int openings;

    public JobVacancy(String vacancyId, String companyId, String companyName, String jobTitle,
                      double minCgpa, String requiredSkills, String location, double salary, int openings) {
        this.vacancyId = vacancyId;
        this.companyId = companyId;
        this.companyName = companyName;
        this.jobTitle = jobTitle;
        this.minCgpa = minCgpa;
        this.requiredSkills = requiredSkills;
        this.location = location;
        this.salary = salary;
        this.openings = openings;
    }

    public String getVacancyId() { return vacancyId; }
    public String getCompanyId() { return companyId; }
    public String getCompanyName() { return companyName; }
    public String getJobTitle() { return jobTitle; }
    public double getMinCgpa() { return minCgpa; }
    public String getRequiredSkills() { return requiredSkills; }
    public String getLocation() { return location; }
    public double getSalary() { return salary; }
    public int getOpenings() { return openings; }

    @Override
    public String toString() {
        return String.format("Vacancy[ID=%s, Company=%-15s, Title=%-25s, MinCGPA=%.2f, Salary=INR %,.0f, Loc=%s]",
                vacancyId, companyName, jobTitle, minCgpa, salary, location);
    }
}
