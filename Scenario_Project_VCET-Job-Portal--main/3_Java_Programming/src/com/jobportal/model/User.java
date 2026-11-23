package com.jobportal.model;

/**
 * Abstract Base Class: User
 * Demonstrates Unit 2: Inheritance, Abstract Classes, and Access Control
 */
public abstract class User {
    protected String id;
    protected String name;
    protected String email;

    public User(String id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public String getEmail() { return email; }

    public abstract String getRole();

    @Override
    public String toString() {
        return "[" + getRole() + "] ID: " + id + ", Name: " + name + ", Email: " + email;
    }
}
