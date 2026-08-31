from flask import Flask, render_template, redirect, url_for

from database import (
    create_database,
    get_latest_decrypted_telemetry,
    get_latest_encrypted_data,
    get_alerts
)

# If telemetry.py exists, this will generate live simulated telemetry
try:
    from telemetry import generate_telemetry
except ImportError:
    generate_telemetry = None


# =========================================================
# FLASK APPLICATION
# =========================================================

app = Flask(__name__)


# =========================================================
# CREATE DATABASE
# =========================================================

create_database()


# =========================================================
# HOME / LOGIN
# =========================================================

@app.route("/")
def home():

    return render_template("login.html")


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    telemetry = get_latest_decrypted_telemetry()

    return render_template(
        "dashboard.html",
        telemetry=telemetry
    )


# =========================================================
# DRONE MONITOR
# =========================================================

@app.route("/drone-monitor")
def drone_monitor():

    # Use live simulated telemetry if telemetry.py exists
    if generate_telemetry:

        telemetry = generate_telemetry()

    else:

        telemetry = get_latest_decrypted_telemetry()


    return render_template(
        "drone_monitor.html",
        telemetry=telemetry
    )


# =========================================================
# SECURITY ALERTS
# =========================================================

@app.route("/alerts")
def alerts():

    alerts_data = get_alerts()

    return render_template(
        "alerts.html",
        alerts=alerts_data
    )


# =========================================================
# DATA PROTECTION
# =========================================================

@app.route("/data-protection")
def data_protection():

    encrypted_record = get_latest_encrypted_data()

    telemetry = get_latest_decrypted_telemetry()

    encrypted_data = None
    timestamp = None
    record_id = None


    if encrypted_record:

        record_id = encrypted_record[0]

        encrypted_data = encrypted_record[1]

        timestamp = encrypted_record[2]


    return render_template(
        "data_protection.html",

        encrypted_data=encrypted_data,

        telemetry=telemetry,

        timestamp=timestamp,

        record_id=record_id
    )


# =========================================================
# COMMUNICATION SECURITY
# =========================================================

@app.route("/communication")
def communication():

    return render_template(
        "communication.html"
    )


# =========================================================
# SECURITY LOGS
# =========================================================

@app.route("/security-logs")
def security_logs():

    alerts_data = get_alerts()

    return render_template(
        "security_logs.html",
        alerts=alerts_data
    )


# =========================================================
# OLD URL - DRONE MONITOR
# =========================================================

@app.route("/drone_monitor")
def drone_monitor_old():

    return redirect(
        url_for("drone_monitor")
    )


# =========================================================
# OLD URL - SECURITY LOGS
# =========================================================

@app.route("/security_logs")
def security_logs_old():

    return redirect(
        url_for("security_logs")
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )