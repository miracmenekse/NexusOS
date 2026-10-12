import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from common.web import serve
from orders.handlers.order_handler import create_order, last_order

serve(8102, {("POST", "/orders"): create_order, ("GET", "/orders/last"): last_order})
