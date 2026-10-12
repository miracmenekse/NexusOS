import random


def charge(body):
    amount = float(body.get("amount", 0))
    # simulated provider: large amounts fail now and then, so the demo has red paths
    ok = amount < 40 or random.random() > 0.5
    return {"ok": ok, "amount": amount}
