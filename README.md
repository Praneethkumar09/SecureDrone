# 🚁 SecureDrone - Drone Cyber Security & Data Protection System

SecureDrone is a web-based **Drone Cyber Security and Data Protection System** developed using Python and Flask.

The project demonstrates how drone telemetry data can be monitored, encrypted, stored securely, and analyzed for potential security threats.

---

## 📌 Project Overview

Drones continuously generate important information such as:

- GPS location
- Altitude
- Speed
- Battery level
- GPS status
- Communication information

If this data is not properly protected, attackers may attempt to intercept, modify, or manipulate it.

**SecureDrone** provides a security monitoring dashboard that demonstrates:

- 🔐 Telemetry data encryption
- 🛡️ Security monitoring
- 🚨 Threat detection
- 📡 Communication security
- 📋 Security event logging
- 🚁 Drone telemetry monitoring
- 💾 Secure database storage

---

## 🎯 Objectives

The main objectives of SecureDrone are:

1. To monitor drone telemetry data.
2. To protect sensitive telemetry using encryption.
3. To detect and display possible security threats.
4. To maintain security event logs.
5. To monitor drone communication security.
6. To provide a simple web-based security dashboard.
7. To demonstrate secure storage using SQLite.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web application framework |
| HTML5 | Web page structure |
| CSS3 | User interface design |
| SQLite | Database |
| Cryptography | Data encryption |
| Fernet | Symmetric encryption |
| Jinja2 | Dynamic HTML templates |

---

## 🏗️ Project Structure

```text
SecureDrone/
│
├── app.py
├── database.py
├── encryption.py
├── telemetry.py
│
├── data/
│   ├── securedrone.db
│   └── secret.key
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── drone_monitor.html
│   ├── alerts.html
│   ├── data_protection.html
│   ├── communication.html
│   └── security_logs.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── README.md
└── .gitignore
