import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from common.web import serve
from gateway.routing import place_order, order_status

serve(8101, {("POST", "/checkout"): place_order, ("GET", "/status"): order_status})
