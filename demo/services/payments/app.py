import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from common.web import serve
from payments.provider.card import charge

serve(8104, {("POST", "/charge"): charge})
