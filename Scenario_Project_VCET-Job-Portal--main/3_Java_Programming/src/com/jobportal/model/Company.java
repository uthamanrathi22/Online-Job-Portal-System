package com.jobportal.model;

/**
 * Company Model
 * Meets FR2: Maintain company details
 */
public class Company {
    private String companyId;
    private String companyName;
    private String industry;
    private String location;
    private String contactEmail;

    public Company(String companyId, String companyName, String industry, String location, String contactEmail) {
        this.companyId = companyId;
        this.companyName = companyName;
        this.industry = industry;
        this.location = location;
        this.contactEmail = contactEmail;
    }

    public String getCompanyId() { return companyId; }
    public String getCompanyName() { return companyName; }
    public String getIndustry() { return industry; }
    public String getLocation() { return location; }
    public String getContactEmail() { return contactEmail; }

    @Override
    public String toString() {
        return String.format("Company[ID=%s, Name=%-20s, Industry=%-15s, Location=%s]",
                companyId, companyName, industry, location);
    }
}
