"""Endless demo traffic: a user places random orders through the gateway."""
import os, random, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "services"))
from common.web import call

while True:
    call("POST", "http://127.0.0.1:8101/checkout",
         {"item": random.choice(["book", "pen", "lamp"]), "qty": random.randint(1, 5)}, caller="user")
    time.sleep(random.uniform(0.2, 0.8))
