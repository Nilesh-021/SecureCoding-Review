# Secure Coding Review

## CodeAlpha Cyber Security Internship - Task 3

## 1. Project Overview

This project demonstrates a secure coding review of a Python application.

The original application was manually inspected to identify common security weaknesses. A secure version was then developed with appropriate remediation.

## 2. Programming Language

- Python
- SQLite

## 3. Security Findings

### Finding 1: SQL Injection Risk

**Severity:** High

**Issue:**

The vulnerable application directly inserted user input into SQL queries.

**Risk:**

Untrusted input could alter the intended SQL query.

**Remediation:**

Parameterized SQL queries were implemented using placeholders.

---

### Finding 2: Weak Password Hashing

**Severity:** High

**Issue:**

The vulnerable application used MD5 to hash passwords.

**Risk:**

MD5 is not appropriate for password storage.

**Remediation:**

PBKDF2-HMAC-SHA256 with a random salt was implemented for password hashing.

---

### Finding 3: Missing Input Validation

**Severity:** Medium

**Issue:**

The vulnerable application did not properly validate username and password input.

**Risk:**

Unexpected or invalid input could be accepted by the application.

**Remediation:**

Input validation was added for username length and minimum password length.

## 4. Vulnerability Comparison

| Security Issue | Vulnerable Version | Secure Version |
|---|---|---|
| SQL Injection | Direct SQL string construction | Parameterized queries |
| Password Hashing | MD5 | PBKDF2-HMAC-SHA256 + Salt |
| Input Validation | Missing | Implemented |

## 5. Secure Coding Recommendations

1. Never concatenate untrusted input directly into SQL queries.
2. Use parameterized queries.
3. Use appropriate password hashing methods with unique salts.
4. Validate and constrain user input.
5. Review code regularly for security weaknesses.
6. Follow secure coding practices throughout development.

## 6. Conclusion

The security review identified multiple weaknesses in the original application.

The secure version addresses the identified issues using parameterized SQL queries, stronger password hashing, random salts, and input validation.

This project demonstrates the importance of security-focused code review and secure coding practices.