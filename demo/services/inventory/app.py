import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from common.web import serve
from inventory.store.stock import reserve, levels

serve(8103, {("POST", "/reserve"): reserve, ("GET", "/stock"): levels})
