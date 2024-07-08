import random
import queue
import uuid
import time

OPERATIONS = ["car registration", "deregister the car", "copy documents"]

queue = queue.Queue()


def generate_request():
    id = str(uuid.uuid1())
    operation = random.choice(OPERATIONS)
    cost = random.randint(1, 100)
    application = {"id": id, "operation": operation, "cost": cost}
    queue.put(application)
    print(f"(+) Application added: {application}\n")


def process_request():
    application = queue.get()
    print(f"(-) Application processed: {application}\n")


print('\nPress "Ctrl + C" to exit ... \n')
while True:
    time.sleep(3)
    for i in range(0, random.randint(0, 3)):
        generate_request()
    if not queue.empty():
        process_request()
    print(f"  >> The queue contains {queue.qsize()} applications\n")
