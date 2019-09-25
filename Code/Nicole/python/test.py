# test.py

import random

neg_num = random.randint(-10, -1)
pos_num = random.randint(1, 10)

count = 0

events = [
    {"text" : "distance loss 1", "distance" : neg_num},
    {"text" : "distance loss 2", "distance" : neg_num},
    {"text" : "distance loss 3", "distance" : neg_num},
    {"text" : "distance gain 1", "distance" : pos_num},
    {"text" : "distance gain 2", "distance" : pos_num},
    {"text" : "distance gain 3", "distance" : pos_num}
    ]
choose_event = random.choice(events)
print(choose_event)
print(choose_event["text"])
print(choose_event["distance"])
count += choose_event["distance"]
# count += events[1]
# print(count)
