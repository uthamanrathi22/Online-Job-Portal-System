package com.jobportal.exception;

/**
 * Custom Exception thrown when a requested vacancy ID is not found.
 */
public class VacancyNotFoundException extends Exception {
    public VacancyNotFoundException(String vacancyId) {
        super("VACANCY NOT FOUND: No active vacancy registered with ID '" + vacancyId + "'.");
    }
}
