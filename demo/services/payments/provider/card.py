import random

from common.web import fail


def charge(body):
    amount = float(body.get("amount", 0))
    # simulated provider: large amounts fail now and then, so the demo has red paths
    if amount >= 40 and random.random() < 0.5:
        return fail("sağlayıcı ödemeyi reddetti", amount=amount)
    return {"ok": True, "amount": amount}
