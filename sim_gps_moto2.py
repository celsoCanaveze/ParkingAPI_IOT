import paho.mqtt.client as mqtt
import json
import random
import time

BROKER = "broker.hivemq.com"
TOPIC_STATUS = "mottu/patio/motos"

ID = "moto-simulada-02"
PLACA = "BRA-5678"
MODELO = "Yamaha Factor 150"

def publicar():
    payload = {
        "id": ID,
        "placa": PLACA,
        "modelo": MODELO,
        "status": 0, # PRONTA
        "lat": -23.55 + random.uniform(-0.005, 0.005),
        "lon": -46.63 + random.uniform(-0.005, 0.005)
    }
    client.publish(TOPIC_STATUS, json.dumps(payload))
    print("Moto 2 →", payload)

client = mqtt.Client(client_id="SimMotoGPS", protocol=mqtt.MQTTv311)
client.connect(BROKER, 1883, 60)

print("Simulador GPS Moto 2 conectado!")
while True:
    publicar()
    time.sleep(5)
