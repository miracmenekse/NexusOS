from common.web import call


def place_order(body):
    return call("POST", "http://127.0.0.1:8102/orders", body, caller="gateway/routing.py")


def order_status(body):
    return call("GET", "http://127.0.0.1:8102/orders/last", caller="gateway/routing.py")
