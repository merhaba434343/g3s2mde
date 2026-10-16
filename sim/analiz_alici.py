import numpy as np
for ad in ["damar_toprak_5cm", "tip_ring_5cm", "kablosuz_ugultu"]:
    d = np.loadtxt(f"{ad}.dat", usecols=(0,1,3,5,7))
    t, uzak, inp, o1, ls = d.T
    m = t > 0.1
    # duzgun ornekleme
    tt = np.arange(0.1, 1.5, 1/48000)
    lsr = np.interp(tt, t, ls); inr = np.interp(tt, t, inp); o1r = np.interp(tt, t, o1)
    inr -= inr.mean(); o1r -= o1r.mean()
    def bant(x, f1, f2):
        X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1/48000)
        return np.sqrt(np.sum(np.abs(X[(f>=f1)&(f<=f2)])**2)*2)/len(x)
    print(f"{ad:18s} giris 1kHz bandi {bant(inr,600,2000)*1e3:7.3f} mVrms | 50Hz {bant(inr,45,55)*1e3:7.3f} mVrms"
          f" | U1 cikis 1k {bant(o1r,600,2000):6.3f} V, 50Hz {bant(o1r,45,55):6.3f} V"
          f" | hoparlor {np.sqrt(np.mean(lsr**2)):5.2f} Vrms = {np.mean(lsr**2)/8*1000:6.1f} mW")
