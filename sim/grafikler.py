import numpy as np, wave, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.color": "#dfe7e3",
                     "figure.facecolor": "#fbfcfb", "axes.facecolor": "#fbfcfb"})
YESIL, KOYU, GRI, TURUNCU = "#0e7a5c", "#24413a", "#8fa39b", "#c2671b"

# 1) Verici
d = np.loadtxt("verici.dat", usecols=(0, 1, 3, 5, 7))
t, lfo, ton, kir, uzak = d.T
fig, ax = plt.subplots(2, 1, figsize=(9, 5.2))
m = (t > 1.0) & (t < 1.6)
s = ton > 4.5; i = np.where(~s[:-1] & s[1:])[0]
te, f = t[i][1:], 1 / np.diff(t[i])
k = (te > 1.0) & (te < 1.6)
ax[0].plot(te[k], f[k], color=YESIL, lw=1.6, label="U2 ton frekansı")
ax2 = ax[0].twinx(); ax2.plot(t[m], lfo[m], color=GRI, lw=1, label="U1 çıkışı"); ax2.set_ylabel("U1 (V)"); ax2.grid(False)
ax[0].set_ylabel("Hz"); ax[0].set_title("Verici: U1 tonu 2,1 Hz ile iki frekans arasında kaydırıyor", loc="left")
m2 = (t > 1.200) & (t < 1.208)
ax[1].plot((t[m2] - 1.2) * 1e3, kir[m2], color=KOYU, lw=1.4, label="Kırmızı klips")
ax[1].plot((t[m2] - 1.2) * 1e3, uzak[m2], color=TURUNCU, lw=1.4, ls="--", label="3 km hattın uzak ucu")
ax[1].set_xlabel("ms"); ax[1].set_ylabel("V"); ax[1].legend(loc="upper right", frameon=False)
ax[1].set_title("Hat sinyali: uzak uçta da ≈ 6,2 V tepe-tepe", loc="left")
fig.tight_layout(); fig.savefig("verici.png", dpi=130)

# 2) Alici frekans cevabi
a = np.loadtxt("alici_ac.dat", usecols=(0, 1, 3, 5))
f, o1, inp, pot = a.T
fig, ax = plt.subplots(figsize=(9, 3.6))
ax.semilogx(f, inp, color=GRI, lw=1.4, label="Prob girişi (U1A +)")
ax.semilogx(f, o1, color=KOYU, lw=1.4, label="U1A çıkışı")
ax.semilogx(f, pot, color=YESIL, lw=2, label="U1B çıkışı (LM386'ya giden)")
for x, lbl in [(50, "50 Hz şebeke"), (910, "910 Hz"), (1220, "1220 Hz")]:
    ax.axvline(x, color=TURUNCU if x == 50 else GRI, lw=1, ls=":")
    ax.text(x * 1.05, -112, lbl, fontsize=9, color=TURUNCU if x == 50 else KOYU)
ax.set_xlim(10, 1e5); ax.set_ylim(-120, 10); ax.set_xlabel("Frekans (Hz)"); ax.set_ylabel("dB (1 V damar, 0,15 pF kuplaj)")
ax.legend(loc="upper left", frameon=False, fontsize=9)
ax.set_title("Alıcı frekans cevabı: 1 kHz tonu, 50 Hz'e göre ≈ 87 dB daha güçlü geçiyor", loc="left")
fig.tight_layout(); fig.savefig("alici_ac.png", dpi=130)

# 3) Hoparlor + WAV
durumlar = [("damar_toprak_5cm", "5 cm, damar–toprak"), ("tip_ring_5cm", "5 cm, tip–ring"), ("kablosuz_ugultu", "Kablo yok, sadece şebeke uğultusu")]
fig, ax = plt.subplots(len(durumlar), 1, figsize=(9, 5.6), sharex=True, sharey=True)
for j, (ad, baslik) in enumerate(durumlar):
    d = np.loadtxt(f"{ad}.dat", usecols=(0, 7)); t, ls = d.T
    m = (t > 1.0) & (t < 1.03)
    ax[j].plot((t[m] - 1.0) * 1e3, ls[m], color=YESIL if j < 2 else TURUNCU, lw=1)
    tt = np.arange(0.1, 1.5, 1 / 16000); y = np.interp(tt, t, ls)
    rms = np.sqrt(np.mean(np.interp(np.arange(0.1, 1.5, 1/48000), t, ls) ** 2))
    ax[j].set_title(f"{baslik}: hoparlörde {rms:.2f} V rms", loc="left", fontsize=10)
    ax[j].set_ylabel("V")
    pcm = np.clip(y / 4.5, -1, 1)
    with wave.open(f"{ad}.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000)
        w.writeframes((pcm * 32000).astype("<i2").tobytes())
ax[-1].set_xlabel("ms")
fig.tight_layout(); fig.savefig("hoparlor.png", dpi=130)
print("ok")
