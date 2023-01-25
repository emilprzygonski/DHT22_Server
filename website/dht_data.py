import random
import time


def get_dht_data(state_shared):
    while True:
        temp = round(random.uniform(20, 30), 1)

        hum = round(random.uniform(40,    60), 1)
        state_shared.add_data(temp, hum)

        time.sleep(1)
