"""Bir servisi çalıştırır, kodu değişince yeniden başlatır (Ç1 K4/K5: kaydet → servis yeni kodla → şehir "düzeldi mi" der).

    python3 calistir.py inventory      (run.sh her servis için bunu kullanır)
"""
import os, signal, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))


def imza(svc):   # mtimes of the service's own code and the shared helpers
    return sorted((p, os.path.getmtime(p)) for d in (svc, "common") for p in _py(os.path.join(HERE, d)))


def _py(d):
    for root, _, fs in os.walk(d):
        yield from (os.path.join(root, f) for f in fs if f.endswith(".py"))


if __name__ == "__main__":
    svc = sys.argv[1]
    signal.signal(signal.SIGTERM, lambda *a: sys.exit(0))   # run.sh's Ctrl+C: stop the service too (finally below)
    while True:
        son, p = imza(svc), subprocess.Popen([sys.executable, os.path.join(svc, "app.py")], cwd=HERE)
        try:
            while imza(svc) == son and p.poll() is None:
                time.sleep(0.5)
        finally:
            p.terminate(); p.wait()
        if p.returncode not in (0, -15):   # crashed (e.g. syntax error while editing): wait for the next save
            print(f"{svc} durdu ({p.returncode}); kod değişince yeniden denenecek", file=sys.stderr)
            while imza(svc) == son: time.sleep(0.5)
        time.sleep(0.3)   # let the old process free the port
