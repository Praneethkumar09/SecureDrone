import random
from database import store_drone_telemetry


# =========================================================
# GENERATE DRONE TELEMETRY
# =========================================================

def generate_telemetry():

    # -----------------------------------------------------
    # SIMULATED DRONE VALUES
    # -----------------------------------------------------

    latitude = round(
        random.uniform(14.60, 14.75),
        6
    )

    longitude = round(
        random.uniform(77.50, 77.70),
        6
    )

    altitude = random.randint(
        80,
        150
    )

    speed = random.randint(
        20,
        60
    )

    battery = random.randint(
        60,
        100
    )


    # -----------------------------------------------------
    # GPS STATUS
    # -----------------------------------------------------

    gps_status = "SECURE"


    # -----------------------------------------------------
    # TELEMETRY DICTIONARY
    # -----------------------------------------------------

    telemetry = {

        "latitude": latitude,

        "longitude": longitude,

        "altitude": altitude,

        "speed": speed,

        "battery": battery,

        "gps_status": gps_status

    }


    # -----------------------------------------------------
    # STORE ENCRYPTED TELEMETRY
    # -----------------------------------------------------

    store_drone_telemetry(

        latitude,
        longitude,
        altitude,
        speed,
        battery,
        gps_status

    )


    # -----------------------------------------------------
    # RETURN TELEMETRY
    # -----------------------------------------------------

    return telemetry


# =========================================================
# TEST TELEMETRY
# =========================================================

if __name__ == "__main__":

    print("\nGenerating drone telemetry...\n")


    telemetry = generate_telemetry()


    print("Drone Telemetry:")

    print(
        f"Latitude   : {telemetry['latitude']}"
    )

    print(
        f"Longitude  : {telemetry['longitude']}"
    )

    print(
        f"Altitude   : {telemetry['altitude']} m"
    )

    print(
        f"Speed      : {telemetry['speed']} km/h"
    )

    print(
        f"Battery    : {telemetry['battery']}%"
    )

    print(
        f"GPS Status : {telemetry['gps_status']}"
    )

    print("\nTelemetry stored successfully.")