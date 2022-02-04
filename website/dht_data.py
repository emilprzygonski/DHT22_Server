import random
import time

import board
import adafruit_dht


def get_dht_data(state_shared):
    dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
    while True:
        try:

            temp = dhtDevice.temperature
            hum = dhtDevice.humidity

            state_shared.add_data(temp, hum)
            time.sleep(60)
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(0.5)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
