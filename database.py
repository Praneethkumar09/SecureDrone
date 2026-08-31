import sqlite3
from datetime import datetime

from encryption import encrypt_data, decrypt_data


DATABASE_NAME = "data/securedrone.db"


# =========================================================
# CREATE DATABASE
# =========================================================

def create_database():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    # -----------------------------------------------------
    # DRONE TELEMETRY TABLE
    # -----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drone_telemetry (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            encrypted_data TEXT NOT NULL,

            timestamp TEXT NOT NULL

        )
    """)


    # -----------------------------------------------------
    # SECURITY ALERTS TABLE
    # -----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS security_alerts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            alert_type TEXT NOT NULL,

            severity TEXT NOT NULL,

            drone_id TEXT NOT NULL,

            description TEXT NOT NULL,

            status TEXT NOT NULL,

            timestamp TEXT NOT NULL

        )
    """)


    conn.commit()


    # -----------------------------------------------------
    # ADD SAMPLE ALERTS
    # -----------------------------------------------------

    cursor.execute(
        "SELECT COUNT(*) FROM security_alerts"
    )

    count = cursor.fetchone()[0]


    if count == 0:

        sample_alerts = [

            (
                "GPS Spoofing",
                "HIGH",
                "DRN_001",
                "Abnormal GPS coordinates detected.",
                "DETECTED",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),

            (
                "Unauthorized Access",
                "HIGH",
                "DRN_002",
                "Unauthorized login attempt blocked.",
                "BLOCKED",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),

            (
                "Communication Interception",
                "MEDIUM",
                "DRN_003",
                "Unusual communication traffic detected.",
                "MONITORING",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),

            (
                "Geofence Breach",
                "MEDIUM",
                "DRN_004",
                "Drone entered restricted geographical area.",
                "ALERTED",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),

            (
                "Low Battery",
                "LOW",
                "DRN_005",
                "Drone battery level is below safe threshold.",
                "WARNING",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

        ]


        cursor.executemany(
            """
            INSERT INTO security_alerts
            (
                alert_type,
                severity,
                drone_id,
                description,
                status,
                timestamp
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            sample_alerts
        )


        conn.commit()


    conn.close()



# =========================================================
# STORE DRONE TELEMETRY
# =========================================================

def store_drone_telemetry(
    latitude,
    longitude,
    altitude,
    speed,
    battery,
    gps_status
):

    telemetry = {

        "latitude": latitude,

        "longitude": longitude,

        "altitude": altitude,

        "speed": speed,

        "battery": battery,

        "gps_status": gps_status

    }


    encrypted = encrypt_data(
        str(telemetry)
    )


    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO drone_telemetry
        (
            encrypted_data,
            timestamp
        )
        VALUES (?, ?)
        """,
        (
            encrypted,
            timestamp
        )
    )


    conn.commit()

    conn.close()



# =========================================================
# GET LATEST DECRYPTED TELEMETRY
# =========================================================

def get_latest_decrypted_telemetry():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT id, encrypted_data, timestamp
        FROM drone_telemetry
        ORDER BY id DESC
        LIMIT 1
        """
    )


    row = cursor.fetchone()

    conn.close()


    if not row:

        return None


    record_id = row[0]

    encrypted_data = row[1]

    timestamp = row[2]


    decrypted = decrypt_data(
        encrypted_data
    )


    # Convert dictionary string back to dictionary
    import ast

    telemetry = ast.literal_eval(
        decrypted
    )


    telemetry["id"] = record_id

    telemetry["timestamp"] = timestamp


    return telemetry



# =========================================================
# GET LATEST ENCRYPTED DATA
# =========================================================

def get_latest_encrypted_data():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT id, encrypted_data, timestamp
        FROM drone_telemetry
        ORDER BY id DESC
        LIMIT 1
        """
    )


    row = cursor.fetchone()

    conn.close()


    return row



# =========================================================
# GET SECURITY ALERTS
# =========================================================

def get_alerts():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT
            id,
            alert_type,
            severity,
            drone_id,
            description,
            status,
            timestamp

        FROM security_alerts

        ORDER BY id DESC
        """
    )


    rows = cursor.fetchall()

    conn.close()


    alerts = []


    for row in rows:

        alerts.append({

            "id": row[0],

            "alert_type": row[1],

            "severity": row[2],

            "drone_id": row[3],

            "description": row[4],

            "status": row[5],

            "timestamp": row[6]

        })


    return alerts



# =========================================================
# ADD SECURITY ALERT
# =========================================================

def add_alert(
    alert_type,
    severity,
    drone_id,
    description,
    status
):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    cursor.execute(
        """
        INSERT INTO security_alerts
        (
            alert_type,
            severity,
            drone_id,
            description,
            status,
            timestamp
        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,

        (
            alert_type,
            severity,
            drone_id,
            description,
            status,
            timestamp
        )
    )


    conn.commit()

    conn.close()



# =========================================================
# TEST DATABASE
# =========================================================

if __name__ == "__main__":

    create_database()

    print("SecureDrone database created successfully.")

    print("\nSecurity Alerts:")

    for alert in get_alerts():

        print(alert)