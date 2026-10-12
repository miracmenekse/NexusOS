from common.web import call


def charge(amount):
    return call("POST", "http://127.0.0.1:8104/charge", {"amount": amount},
                caller="orders/clients/payment_client.py")
