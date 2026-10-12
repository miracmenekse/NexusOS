from common.web import call


def reserve(item, qty):
    return call("POST", "http://127.0.0.1:8103/reserve", {"item": item, "qty": qty},
                caller="orders/clients/inventory_client.py")
