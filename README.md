🚁 SecureDrone - Drone Cyber Security & Data Protection System

SecureDrone is a web-based **Drone Cyber Security and Data Protection System** developed using **Python and Flask**.

The project demonstrates how drone telemetry data can be monitored, encrypted, securely stored, and analyzed for potential cybersecurity threats.

---

📌 Project Overview

Modern drones continuously generate and transmit important information such as:

- 📍 GPS Location
- ⛰️ Altitude
- 🚀 Speed
- 🔋 Battery Level
- 🛰️ GPS Status
- 📡 Communication Status
- 🔐 Security Information

If this information is not properly protected, attackers may attempt to intercept, modify, manipulate, or access sensitive drone data.

**SecureDrone** provides a web-based security dashboard that demonstrates basic cybersecurity mechanisms for drone systems.

The application includes:

- 🔐 Telemetry Data Encryption
- 🛡️ Security Monitoring
- 🚨 Threat Detection
- 📡 Communication Security
- 📋 Security Event Logging
- 🚁 Drone Telemetry Monitoring
- 💾 Secure SQLite Database Storage
- 🔑 Encryption Key Management

---

🎯 Objectives

The main objectives of the SecureDrone project are:

1. To monitor drone telemetry data.
2. To protect sensitive telemetry data using encryption.
3. To securely store telemetry information.
4. To detect and display possible security threats.
5. To monitor drone communication security.
6. To maintain security event logs.
7. To provide a simple web-based cybersecurity dashboard.
8. To demonstrate secure database storage using SQLite.
9. To demonstrate symmetric encryption using Fernet.
10. To provide a foundation for future drone cybersecurity research.

---

🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Backend programming |
| 🌐 Flask | Web application framework |
| HTML5 | Web page structure |
| CSS3 | User interface design |
| 🗄️ SQLite | Database management |
| 🔐 Cryptography | Data encryption |
| 🔑 Fernet | Symmetric encryption |
| 🎨 Jinja2 | Dynamic HTML templates |
| 💻 Git | Version control |
| 🐙 GitHub | Project repository |

---
----
 🏗️ System Architecture

The SecureDrone system follows a simple layered architecture:


                 ┌─────────────────────────┐
                 │       User / Admin      │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │     Flask Web App       │
                 │         app.py          │
                 └────────────┬────────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
     ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
     │   Dashboard  │ │ Drone Monitor│ │ Security     │
     │              │ │              │ │ Alerts       │
     └──────────────┘ └──────────────┘ └──────────────┘
             │                │                │
             └────────────────┼────────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │      Telemetry          │
                 │     telemetry.py        │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │      Encryption         │
                 │     encryption.py       │
                 │        Fernet           │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │       Database          │
                 │     database.py         │
                 │        SQLite           │
                 └─────────────────────────┘
----



---
📂 Project Structure

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

---
📄 File Description

app.py

The main Flask application.

It is responsible for:

Starting the Flask server
Managing application routes
Rendering HTML templates
Loading telemetry information
Displaying security alerts
Displaying encrypted data
Managing dashboard navigation
Main Routes
/
 /dashboard
 /drone-monitor
 /alerts
 /data-protection
 /communication
 /security-logs
database.py

Responsible for SQLite database operations.

It manages:

Database creation
Telemetry storage
Encrypted telemetry retrieval
Security alert storage
Security alert retrieval
Database Tables
drone_telemetry
security_alerts
encryption.py

Responsible for encrypting and decrypting telemetry data.

The project uses:

Fernet Symmetric Encryption

The encryption key is stored in:

data/secret.key
Encryption Process
Drone Telemetry
       ↓
   Encryption
       ↓
Encrypted Data
       ↓
SQLite Database
Decryption Process
SQLite Database
       ↓
Encrypted Data
       ↓
   Decryption
       ↓
Original Telemetry
telemetry.py

Responsible for generating simulated drone telemetry data.

Example telemetry information includes:

Latitude
Longitude
Altitude
Speed
Battery
GPS Status

This allows the project to demonstrate drone monitoring without requiring an actual physical drone.

---
🖥️ Web Application Modules


🏠 1. Dashboard

The Dashboard provides an overview of the SecureDrone system.
It can display:

Drone status
GPS information
Altitude
Speed
Battery level
GPS status
Security status

🚁 2. Drone Monitor

The Drone Monitor displays simulated telemetry information.

Example
Drone ID       : DRN_001
Latitude       : 14.6819
Longitude      : 77.6006
Altitude       : 120 m
Speed          : 35 km/h
Battery        : 82%
GPS Status     : ACTIVE

The telemetry can be generated dynamically using telemetry.py.

🚨 3. Security Alerts

The Security Alerts page displays detected security events.

Example Threats
GPS Spoofing
Unauthorized Access
Communication Interception
Geofence Breach
Low Battery

Each alert contains:

Alert ID
Alert Type
Severity
Drone ID
Description
Status
Timestamp

🔐 4. Data Protection

The Data Protection module demonstrates protection of sensitive drone telemetry.

The system:

Generates telemetry.
Converts telemetry into data.
Encrypts the data.
Stores encrypted information in SQLite.
Retrieves encrypted information.
Decrypts the information when required.
📡 5. Communication Security

The Communication Security page provides information about drone communication.

It monitors parameters such as:

Signal Strength
Encryption
Secure Session
Packet Integrity
Packet Loss
Unknown Packets
Interception Attempts
Security Controls
🔐 Data Encryption
🔑 Authentication
🛡️ Packet Integrity
🚨 Intrusion Detection
📡 Signal Monitoring
📋 6. Security Logs

The Security Logs page displays historical security events.

The logs include:

ID
Time
Drone ID
Threat Type
Severity
Description
Status

This allows administrators to review previous security events.
---
🔐 Security Features

SecureDrone demonstrates several important cybersecurity concepts.

1. Data Encryption

Sensitive telemetry is encrypted before storage.

Plain Telemetry
       ↓
Fernet Encryption
       ↓
Encrypted Data

2. Secure Storage

Encrypted telemetry is stored inside an SQLite database.

SQLite
   ↓
Encrypted Telemetry

3. Authentication Monitoring

The dashboard provides security information regarding authenticated communication.

4. Packet Integrity

The system demonstrates packet integrity verification to identify unauthorized modification.

5. Threat Detection

The project considers possible threats such as:

GPS Spoofing
Man-in-the-Middle Attacks
Packet Injection
Replay Attacks
Signal Jamming
Unauthorized Devices

6. Security Logging

Security-related events are recorded and displayed through the Security Logs module.

🚨 Threats Considered

Threat	Description
GPS Spoofing	Manipulation of GPS information
GPS Jamming	Disruption of GPS signals
Unauthorized Access	Attempted access by an unauthorized user
Packet Injection	Injection of unauthorized network packets
Replay Attack	Reuse of previously captured communication
Man-in-the-Middle	Interception of communication
Signal Jamming	Disruption of communication signals
Geofence Breach	Drone entering a restricted area
---

💾 Database

SecureDrone uses SQLite for data storage.

Database File
data/securedrone.db
Drone Telemetry Table
drone_telemetry
Fields
id
encrypted_data
timestamp
Security Alerts Table
security_alerts
Fields
id
alert_type
severity
drone_id
description
status
timestamp

🔑 Encryption

SecureDrone uses the Python cryptography library and Fernet symmetric encryption.

The encryption key is generated automatically if it does not already exist.

data/secret.key
Encryption Workflow
Telemetry Data
      │
      ▼
Fernet Encryption
      │
      ▼
Encrypted String
      │
      ▼
SQLite Database
Decryption Workflow
SQLite Database
      │
      ▼
Encrypted String
      │
      ▼
Fernet Decryption
      │
      ▼
Telemetry Data

⚙️ Installation
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/SecureDrone.git

Move into the project directory:

cd SecureDrone

🐍 2. Create Virtual Environment

For Windows:

python -m venv venv

Activate the virtual environment:

venv\Scripts\Activate.ps1

If PowerShell blocks activation, run:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Then activate:

venv\Scripts\Activate.ps1

📦 3. Install Dependencies

Run:

pip install -r requirements.txt

If requirements.txt is not available:

pip install flask cryptography

▶️ 4. Run the Application

Start the Flask application:

python app.py

You should see something similar to:

* Running on http://127.0.0.1:5000

Open the browser and visit:

http://127.0.0.1:5000

🖥️ Application Pages

After starting the application, the following pages are available:

Page	URL
Login	/
Dashboard	/dashboard
Drone Monitor	/drone-monitor
Security Alerts	/alerts
Data Protection	/data-protection
Communication	/communication
Security Logs	/security-logs

🔄 Application Workflow

The overall workflow is:

Start Flask Application
          ↓
Generate Drone Telemetry
          ↓
Monitor Telemetry
          ↓
Encrypt Sensitive Data
          ↓
Store Data in SQLite
          ↓
Analyze Security Events
          ↓
Generate Security Alerts
          ↓
Display Information
          ↓
Maintain Security Logs

📊 Example Telemetry

Example simulated telemetry:

Latitude    : 14.6819
Longitude   : 77.6006
Altitude    : 120 m
Speed       : 35 km/h
Battery     : 82%
GPS Status  : ACTIVE

🚨 Example Security Alerts
GPS Spoofing
Severity : HIGH
Drone    : DRN_001
Status   : DETECTED
Unauthorized Access
Severity : HIGH
Drone    : DRN_002
Status   : BLOCKED
Communication Interception
Severity : MEDIUM
Drone    : DRN_003
Status   : MONITORING

🧪 Testing

The application can be tested using the following commands.

Test Database
python database.py

This creates the database and displays security alerts.

Test Encryption
python encryption.py

This demonstrates:

Original Data
      ↓
Encrypted Data
      ↓
Decrypted Data
Test Flask Application
python app.py

Then open:

http://127.0.0.1:5000

🔒 Security Considerations

This project is developed as an educational mini project and prototype.

It demonstrates cybersecurity concepts but is not intended to provide production-grade protection for real-world drone systems.

For a production system, additional mechanisms would be required, including:

Strong user authentication
Role-based access control
Secure key management
TLS communication
Hardware security modules
Secure drone communication protocols
Real intrusion detection
Real-time network packet analysis
Secure firmware
Certificate-based authentication
Audit logging
Cloud security
Secure API authentication

🚀 Future Enhancements
1. Real Drone Integration

Connect the system with an actual drone using technologies such as:

MAVLink
DroneKit
PX4
ArduPilot
2. Real-Time GPS Tracking

Add an interactive map to display the drone's live location.

Possible technologies:

Leaflet.js
OpenStreetMap
Google Maps API
3. Advanced Intrusion Detection

Implement network traffic analysis to detect:

Packet Injection
Replay Attacks
Man-in-the-Middle Attacks
Port Scanning
Unauthorized Devices
4. Machine Learning Threat Detection

Machine learning can be used to classify suspicious telemetry behavior.

Normal Telemetry
       ↓
    ML Model
       ↓
Threat Classification
       ↓
 Security Alert
5. Real-Time Dashboard

Add WebSocket-based live updates for:

GPS
Battery
Speed
Altitude
Signal Strength
Security Alerts
6. Multi-Drone Support

The system can be extended to monitor multiple drones:

DRN_001
DRN_002
DRN_003
DRN_004

🎓 Academic Use

SecureDrone can be used as a B.Tech / Engineering Mini Project demonstrating concepts from:

Cyber Security
Drone Technology
Internet of Things
Network Security
Data Protection
Python Programming
Web Development
Database Management
Cryptography
📚 Learning Outcomes

After completing this project, the following concepts can be understood:

Flask web application development
Python programming
SQLite database operations
Encryption and decryption
Fernet symmetric encryption
HTML and CSS
Jinja2 templates
Telemetry monitoring
Security alert management
Cybersecurity threat concepts
Git and GitHub version control

👨‍💻 Project Information
Category	Details
Project Name	SecureDrone
Project Type	Mini Project
Domain	Drone Cyber Security
Backend	Python + Flask
Database	SQLite
Encryption	Fernet
Frontend	HTML5 + CSS3
Version Control	Git
Repository	GitHub

📜 Disclaimer

SecureDrone is intended for educational and academic purposes.

The telemetry data used by the project may be simulated and does not represent real drone flight data.

The security detection mechanisms are demonstrations of cybersecurity concepts and should not be considered a complete production security solution.

⭐ Conclusion

SecureDrone demonstrates how cybersecurity techniques can be applied to drone systems to protect telemetry and monitor potential security events.

The project combines:

Drone Technology
       +
Cyber Security
       +
Encryption
       +
Database Security
       +
Web Development
       =
   SecureDrone

The system provides a foundation that can be further developed into a real-time drone cybersecurity platform.

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.



