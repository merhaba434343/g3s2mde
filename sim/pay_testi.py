"""Kuplaj zayifladikca (prob uzaklastikca) tonun ugultuya gore durumu."""
import numpy as np
from testler import calistir
def bant(y, f1, f2, fs=48000):
    X = np.fft.rfft(y); f = np.fft.rfftfreq(len(y), 1/fs)
    return np.sqrt(np.sum(np.abs(X[(f >= f1) & (f <= f2)])**2) * 2) / len(y)
satirlar = []
for ver in ["tam", "ucuz"]:
    for c in [0.15, 0.05, 0.015, 0.005, 0.0015, 0.0005, 0.00015]:
        r, tt, y = calistir(ver, f"{c}p", 9.0, sure=0.6)
        ton = bant(y, 600, 2500); ug = bant(y, 40, 400)
        satirlar.append((ver, c, r, ton, ug))
        print(f"{ver:5s} kuplaj {c:8.5f} pF ({0.15/c:6.0f}x zayif) -> toplam {r:4.2f} V rms, ton bandi {ton:4.2f} V, ugultu bandi {ug:4.2f} V", flush=True)
np.save("pay_testi.npy", np.array([(0 if v=='tam' else 1, c, r, t, u) for v, c, r, t, u in satirlar]))
