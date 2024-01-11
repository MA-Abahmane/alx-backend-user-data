# Personal Data Cheatsheet

## 1. What Is PII, non-PII, and Personal Data?

### PII (Personally Identifiable Information):
**PII** refers to information that can be used to identify an individual. This includes:
- Full name
- Social Security number
- Address
- Phone number
- Email address
- Financial information
- Biometric data

### non-PII (Non-Personally Identifiable Information):
Non-PII is data that cannot be used on its own to identify a specific individual. Examples include:
- Age
- Gender
- ZIP code
- Browser history
- IP address (in some cases)

### Personal Data:
Personal data is a broader term that encompasses both PII and non-PII. It includes any information related to an identified or identifiable individual.

---

## 2. Logging Documentation

### Logging Basics:
Logging involves recording information about events in a system to analyze and debug. Key components:
- Log messages: Information, warnings, errors, and debugging details.
- Log levels: Different severity levels for messages (e.g., INFO, WARN, ERROR).
- Log context: Additional details like timestamps, source, and user information.

### Importance of Logging:
- Debugging and troubleshooting.
- Monitoring system behavior.
- Security audits.
- Performance analysis.

---

## 3. Bcrypt Package

### Bcrypt Overview:
Bcrypt is a password-hashing function designed to store passwords securely. Features:
- Key stretching: Slows down brute-force attacks.
- Salted hashes: Adds randomness to each password hash.
- Adaptive hashing: Can be adjusted for increased security.

### Implementation in Programming:
Example usage in Python:
```python
import bcrypt

password = "securepassword"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
```

---

## 4. Logging to Files, Setting Levels, and Formatting

### Logging to Files:
Configure logging to save output to a file:
```python
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)
```

### Setting Log Levels:
Adjust log levels based on severity:
```python
logging.debug("Debugging information")
logging.info("Informational message")
logging.warning("Warning message")
logging.error("Error occurred")
logging.critical("Critical error")
```

### Formatting Log Messages:
Customize log message format:
```python
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
```

---

**Note:** Always handle personal data with care, following privacy regulations and best practices.
