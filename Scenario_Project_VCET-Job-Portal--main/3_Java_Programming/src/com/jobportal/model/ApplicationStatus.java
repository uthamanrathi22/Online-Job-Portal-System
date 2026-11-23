package com.jobportal.model;

/**
 * Application Status Enum
 * Meets FR5: Track application status (Applied, Shortlisted, Selected, Rejected)
 */
public enum ApplicationStatus {
    APPLIED("Applied"),
    SHORTLISTED("Shortlisted"),
    SELECTED("Selected"),
    REJECTED("Rejected");

    private final String label;

    ApplicationStatus(String label) {
        this.label = label;
    }

    public String getLabel() {
        return label;
    }

    public static ApplicationStatus fromString(String text) {
        for (ApplicationStatus status : ApplicationStatus.values()) {
            if (status.label.equalsIgnoreCase(text) || status.name().equalsIgnoreCase(text)) {
                return status;
            }
        }
        throw new IllegalArgumentException("Unknown Application Status: " + text);
    }
}
