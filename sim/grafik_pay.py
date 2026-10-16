import numpy as np, wave, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from testler import calistir
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.color": "#dfe7e3",
                     "figure.facecolor": "#fbfcfb", "axes.facecolor": "#fbfcfb"})
YESIL, KOYU, TURUNCU = "#0e7a5c", "#24413a", "#c2671b"
d = np.load("pay_testi.npy")
fig, ax = plt.subplots(figsize=(9, 3.8))
for v, ad, renk, ls in [(0, "Normal", YESIL, "-"), (1, "Ucuz", KOYU, "--")]:
    m = d[:, 0] == v
    ax.loglog(d[m, 1], d[m, 3], color=renk, lw=2, ls=ls, marker="o", label=f"{ad}: ton")
    ax.loglog(d[m, 1], d[m, 4], color=TURUNCU, lw=1.2, ls=ls, label=f"{ad}: uğultu")
ax.axvline(0.15, color="#8fa39b", ls=":"); ax.text(0.15, 3.6, " 5 cm tahmini", fontsize=9, color=KOYU)
ax.axvline(0.005, color="#8fa39b", ls=":"); ax.text(0.005, 3.6, " 5 cm tip–ring", fontsize=9, color=KOYU)
ax.set_xlabel("Prob ile damar arası kuplaj (pF) — sağa gittikçe prob uzaklaşıyor")
ax.set_ylabel("Hoparlörde V rms"); ax.set_ylim(0.04, 5); ax.invert_xaxis()
ax.legend(frameon=False, fontsize=9, ncol=2, loc="lower left")
ax.set_title("Pay testi: ton, uğultunun üstünde kaldığı sürece cihaz kabloyu bulur", loc="left")
fig.tight_layout(); fig.savefig("pay_testi.png", dpi=130)
# ucuz versiyon sesi
r, tt, y = calistir("ucuz", "0.15p", 9.0, sure=1.5, ad="ucuz_damar_toprak")
yy = np.interp(np.arange(0.15, 1.5, 1/16000), tt, y)
with wave.open("ucuz_damar_toprak_5cm.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000)
    w.writeframes((np.clip(yy / 4.5, -1, 1) * 32000).astype("<i2").tobytes())
print("ok", r)
