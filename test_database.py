from database import (
    create_database,
    add_encrypted_telemetry,
    get_latest_encrypted_data,
    get_latest_decrypted_telemetry
)


print("Creating database...")

create_database()


print("Adding encrypted drone telemetry...")


add_encrypted_telemetry(
    latitude=14.6819,
    longitude=77.6006,
    altitude=120,
    speed=35,
    battery=82,
    gps_status="SECURE"
)


print("\nEncrypted record stored in database:")

encrypted = get_latest_encrypted_data()

print(encrypted)


print("\nDecrypted telemetry:")

decrypted = get_latest_decrypted_telemetry()

print(decrypted)