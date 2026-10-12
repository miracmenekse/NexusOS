import time

from common.web import fail

_FULL = {"book": 50, "pen": 200, "lamp": 3}
_stock = dict(_FULL)
_t = time.time()


def reserve(body):
    global _t
    if time.time() - _t > 20:   # demo: refill every 20 s so red paths come and go
        _stock.update(_FULL); _t = time.time()
    item, qty = body.get("item"), int(body.get("qty", 1))
    if _stock.get(item, 0) < qty:
        return fail("stok yetersiz", item=item, istenen=qty, kalan=_stock.get(item, 0))
    _stock[item] -= qty
    return {"ok": True, "left": _stock[item]}


def levels(body):
    return _stock
