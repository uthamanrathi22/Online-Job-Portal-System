package com.jobportal.thread;

import com.jobportal.model.ApplicationStatus;
import com.jobportal.model.JobApplication;
import com.jobportal.service.JobPortalService;

import java.util.List;

/**
 * Multithreaded Application Processor
 * Demonstrates Unit 3: Multithreaded Programming, Thread Creation, Synchronization
 * Simulates background screening of applications by placement cell automation.
 */
public class BatchApplicationProcessor extends Thread {
    private final JobPortalService service;
    private final String targetStatus;

    public BatchApplicationProcessor(JobPortalService service, String threadName, String targetStatus) {
        super(threadName);
        this.service = service;
        this.targetStatus = targetStatus;
    }

    @Override
    public void run() {
        System.out.printf("[%s] Background Screening Thread started (Target Action: %s)...\n",
                getName(), targetStatus);

        List<JobApplication> apps = service.getAllApplications();
        int processed = 0;

        for (JobApplication app : apps) {
            if (app.getStatus() == ApplicationStatus.APPLIED) {
                try {
                    Thread.sleep(80); // Simulate background verification latency
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }

                // Synchronized status transition
                synchronized (service) {
                    service.updateApplicationStatus(app.getApplicationId(), ApplicationStatus.SHORTLISTED);
                    processed++;
                    System.out.printf("  [%s] Processed App ID #%d (Student: %s) -> SHORTLISTED\n",
                            getName(), app.getApplicationId(), app.getStudentId());
                }
            }
        }

        System.out.printf("[%s] Background Screening completed. Total processed: %d applications.\n",
                getName(), processed);
    }
}
