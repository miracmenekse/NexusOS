from orders.model.order import Order
from orders.clients.inventory_client import reserve
from orders.clients.payment_client import charge

_last = {}


def create_order(body):
    order = Order(body.get("item", "book"), int(body.get("qty", 1)))
    stock = reserve(order.item, order.qty)
    if not stock.get("ok"):
        return {"status": "out_of_stock"}
    pay = charge(order.total())
    _last.update(order.to_dict(), paid=pay.get("ok", False))
    return {"status": "paid" if pay.get("ok") else "payment_failed", "order": _last}


def last_order(body):
    return _last
