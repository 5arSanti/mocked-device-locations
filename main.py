import json
from datetime import datetime, timedelta
import os

def generar_json(user_email, fecha_inicio_str, horas, intervalo_minutos, archivo_salida, lat, long):
    fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d %H:%M:%S")

    total_registros = int((horas * 60) / intervalo_minutos)

    base_objeto = {
        "location": {
            "current": {
                "mocked": False,
                "timestamp": 1750111430899,
                "extras": {"meanCn0": 0, "maxCn0": 0, "satellites": 0},
                "coords": {
                    "speed": 0, "heading": 0, "altitude": 5, "accuracy": 5,
                    "longitude": long, "latitude": lat
                }
            },
            "hasPermission": True,
            "watchId": 1020,
            "watch": {
                "mocked": False,
                "timestamp": 1750111431900,
                "extras": {"meanCn0": 0, "maxCn0": 0, "satellites": 0},
                "coords": {
                    "speed": 0, "heading": 0, "altitude": 5, "accuracy": 5,
                    "longitude": long, "latitude": lat
                }
            }
        },
        "device": {
            "device": {
                "uniqueId": "283273b50bc32373", "brand": "google", "manufacturer": "Google",
                "model": "sdk_gphone64_x86_64", "systemName": "Android", "systemVersion": "16",
                "appVersion": "1.0", "buildNumber": "1", "deviceType": "Handset",
                "isEmulator": True, "isTablet": False
            },
            "battery": {"level": 1, "isCharging": False},
            "memory": {"total": 2067259392, "used": 202770432, "free": 4129697792},
            "storage": {"total": 6815870976, "free": 4129697792},
            "orientation": {"isLandscape": False, "isPortrait": True}
        },
        "sensors": {
            "accelerometer": {"x": 0, "y": 9.776321411132812, "z": 0.812345027923584},
            "gyroscope": {"x": 0, "y": 0, "z": 0},
            "magnetometer": {"x": 0, "y": 9.875, "z": -47.75}
        },
        "userName": user_email,
        "timestamps": {
            "createdAt": ""
        }
    }

    registros = {"deviceLocations": []}
    for i in range(total_registros):
        objeto = json.loads(json.dumps(base_objeto))
        fecha_actual = fecha_inicio + timedelta(minutes=i * intervalo_minutos)
        objeto["timestamps"]["createdAt"] = fecha_actual.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        registros["deviceLocations"].append(objeto)

    ruta_archivo = os.path.abspath(archivo_salida)
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(registros, f, indent=2, ensure_ascii=False)
    
    print(f"Archivo '{ruta_archivo}' generado con {len(registros['deviceLocations'])} registros.")

generar_json(
    user_email="vigilancia-153@davivienda.com", 
    fecha_inicio_str="2025-08-10 23:00:00", 
    horas=10, 
    intervalo_minutos=5,
    archivo_salida="results.json",
    lat=4.634213,
    long=-74.113820
)
