# Category 3: Java Programming
**Course Code:** 25ITT32 - Java Programming  
**System:** Online Job Portal and Employment Trend Analysis System  

---

## 1. Syllabus Evaluation & Requirements Mapping

| Unit | Syllabus Topics (25ITT32) | System Implementation & Functional Requirements |
|---|---|---|
| **Unit 1: Introduction to Java** | Data types, arrays, control statements, class fundamentals, constructors, method overloading, access control, console I/O (`Scanner`). | Created core entity classes (`Student`, `Company`, `JobVacancy`, `JobApplication`) with overloaded constructors and encapsulation. Handled console I/O in `JobPortalApp`. |
| **Unit 2: Inheritance, Packages, Interfaces** | Super keyword, method overriding, dynamic method dispatch, abstract classes, packages, interfaces. | Built modular package structure (`com.jobportal.model`, `service`, `exception`, `thread`, `app`). Defined abstract class `User` extended by `Student`. Defined `JobPortalService` interface. |
| **Unit 3: Exception Handling & Multithreading** | Try-catch, throw, throws, finally, custom user-defined exceptions, Java thread model, synchronization. | Defined custom exceptions: `DuplicateApplicationException` (Meets FR4) and `IneligibleStudentException` (Meets FR3). Implemented `BatchApplicationProcessor` thread with synchronized blocks for concurrency. |
| **Unit 4: String Handling & Database Connection** | String operations, `StringBuilder`, data conversion, persistence mechanisms. | Formatted multi-line reports using `StringBuilder`. Clean data exchange between Java objects and persistent records. |
| **Unit 5: Generics, Collections, Lambdas & Streams** | Generic classes, Collections framework (`List`, `Map`, `Set`), Lambdas, Stream API (filtering, mapping, sorting, collectors, reduction). | Used `Map<String, Student>` and `Set<String>` for $O(1)$ duplicate checking. Applied Java Streams for filtering eligible applicants, sorting vacancies by package, and grouping recruitment by company & department. |

---

## 2. Object-Oriented Architecture & Design Patterns

### Class Hierarchy & Components:
```
com.jobportal
├── model
│   ├── User.java                (Abstract Base Class)
│   ├── Student.java             (Extends User - FR1)
│   ├── Company.java             (FR2)
│   ├── JobVacancy.java          (FR2)
│   ├── JobApplication.java      (FR3, FR4, FR5)
│   └── ApplicationStatus.java   (Enum: APPLIED, SHORTLISTED, SELECTED, REJECTED)
├── exception
│   ├── DuplicateApplicationException.java (FR4 duplicate prevention)
│   ├── IneligibleStudentException.java    (FR3 eligibility check)
│   └── VacancyNotFoundException.java
├── service
│   ├── JobPortalService.java       (Interface)
│   └── JobPortalServiceImpl.java   (Implementation with Collections & Streams)
├── thread
│   └── BatchApplicationProcessor.java (Unit 3 Multithreading & Synchronization)
└── app
    └── JobPortalApp.java           (Interactive Console CLI & Automated Test Suite)
```

### Key Technical Implementations:

1. **FR4 - Duplicate Application Prevention**:
   ```java
   String key = studentId + "#" + vacancyId;
   if (applicationKeys.contains(key)) {
       throw new DuplicateApplicationException(studentId, vacancyId);
   }
   ```

2. **FR3 - Eligibility Verification**:
   ```java
   if (student.getCgpa() < vacancy.getMinCgpa()) {
       throw new IneligibleStudentException(studentId, student.getCgpa(), vacancy.getMinCgpa());
   }
   ```

3. **FR6 - Placement Analytics using Stream API**:
   ```java
   // Department-wise Selection Breakdown
   Map<String, Long> deptRecruitment = applications.stream()
       .filter(app -> app.getStatus() == ApplicationStatus.SELECTED)
       .map(app -> students.get(app.getStudentId()))
       .filter(Objects::nonNull)
       .collect(Collectors.groupingBy(Student::getDepartment, Collectors.counting()));
   ```

---

## 3. How to Run the Program

1. **Interactive Manual Keyboard Mode (`run_java.bat`)**:
   - Double-click `run_java.bat` in this folder.
   - The script will automatically compile any modified `.java` files and launch the interactive console.
   - Follow the keyboard prompts (1 to 10) to manually register students, post vacancies, test duplicate applications, and run background threads.
2. **Automated Verification Mode**:
   ```cmd
   java -cp bin com.jobportal.app.JobPortalApp --auto
   ```
   This executes all unit tests, verifies exceptions, and generates `java_output.txt`.

---

## 4. Folder Artifacts Checklist
- [x] `src/com/jobportal/...`: Full Java source code (models, service, exceptions, threads, app).
- [x] `bin/`: Compiled bytecode classes.
- [x] `run_java.bat`: Double-clickable runnable batch script.
- [x] `java_output.txt`: Execution output text file.
- [x] `screenshot_java_execution.png`: Screenshot of Java program execution.
- [x] `Java_Programming_Documentation.md`: Comprehensive documentation.
