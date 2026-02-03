import json
import random
import time

while True:
    payload = {
        "moisture": random.randint(10, 60)
    }
    print(json.dumps(payload))
    time.sleep(5)
