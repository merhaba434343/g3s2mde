import numpy as np
d = np.loadtxt('verici.dat', usecols=(0,1,3,5,7,9))
t, lfo, ton, kir, uzak, cv2 = d.T
m = t > 0.5
t, lfo, ton, kir, uzak, cv2 = t[m], lfo[m], ton[m], kir[m], uzak[m], cv2[m]
def yukselen(x, tt, alt, ust):
    # histerezisli kenar tespiti
    out, durum = [], x[0] > ust
    for xi, ti in zip(x, tt):
        if not durum and xi > ust: out.append(ti); durum = True
        elif durum and xi < alt: durum = False
    return np.array(out)
e = yukselen(lfo, t, 2, 6)
p = np.diff(e)
print(f"U1 titresim: periyot {p.mean()*1e3:.0f} ms -> {1/p.mean():.2f} Hz ({len(p)} periyot)")
e2 = yukselen(ton, t, 2, 6)
f2 = 1/np.diff(e2)
print(f"U2 ton: min {f2.min():.0f} Hz, max {f2.max():.0f} Hz, ort {f2.mean():.0f} Hz")
print(f"U2 CV araligi: {cv2.min():.2f} .. {cv2.max():.2f} V")
def ptp(x, n=4000):
    return np.median([np.ptp(x[i:i+n]) for i in range(0, len(x)-n, n)])
print(f"U2 cikis tepe-tepe:       {ptp(ton):.2f} V")
print(f"Kirmizi klips tepe-tepe:  {ptp(kir):.2f} V")
print(f"3 km uzak uc tepe-tepe:   {ptp(uzak):.2f} V")
np.save('verici_ozet.npy', np.array([1/p.mean(), f2.min(), f2.max(), ptp(ton), ptp(kir), ptp(uzak)]))
