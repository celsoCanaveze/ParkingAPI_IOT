import paho.mqtt.client as mqtt
import json

BROKER = "broker.hivemq.com"
TOPIC_STATUS = "mottu/patio/motos"
TOPIC_CMD = "mottu/patio/comandos"

MOTO_ID = "moto-3"
PLACA = "ZZZ-9999"
MODELO = "Honda Biz 125"

estado = {"locked": False}

def publicar_status():
    payload = {
        "id": MOTO_ID,
        "placa": PLACA,
        "modelo": MODELO,
        "status": 2 if estado["locked"] else 0,
        "locked": estado["locked"]
    }
    client.publish(TOPIC_STATUS, json.dumps(payload))
    print("Moto 3 →", payload)

def on_message(client, userdata, msg):
    global estado
    payload = json.loads(msg.payload.decode())
    
    # Comandos só para Moto 3
    if payload.get("id") != MOTO_ID:
        return

    if payload.get("action") == "lock":
        estado["locked"] = True
    elif payload.get("action") == "unlock":
        estado["locked"] = False

    publicar_status()

client = mqtt.Client(client_id="SimMotoLock3", protocol=mqtt.MQTTv311)
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC_CMD)

print("Simulador Trava Moto 3 conectado!")

publicar_status()
client.loop_forever()
