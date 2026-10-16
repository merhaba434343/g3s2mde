"""Iki versiyonu ayni kosullarda dener: baglanti sekli, mesafe (kuplaj), pil gerilimi."""
import subprocess, sys, numpy as np
VERSIYON = {
    "tam":  ("vericigovde.inc", "alici_govde.inc"),
    "ucuz": ("ucuz_vericigovde.inc", "ucuz_alici_govde.inc"),
}
def calistir(ver, ccpl, vpil=9.0, ugultu="0.05p", sure=0.6, ad=None):
    vinc, ainc = VERSIYON[ver]
    ad = ad or f"t_{ver}"
    net = open(vinc).read() + "\n" + open(ainc).read()
    net = net.replace("VB vcc 0 9", f"VB vcc 0 {vpil}").replace("VBR vb 0 9", f"VBR vb 0 {vpil}")
    vr = vpil / 2
    cir = f"""* {ad}
.include modeller.lib
{net}
Ccpl uzak prob {ccpl}
Vm m 0 SIN(0 325 50)
Cm m prob {ugultu}
.ic v(vref)={vr} v(inp)={vr} v(inn)={vr} v(x)={vr} v(o1)={vr} v(o2)={vr} v(sp)={vr} v(j)={vr}
.tran 5u {sure} 0 5u uic
.control
run
wrdata {ad}.dat v(ls)
.endc
.end
"""
    open(f"{ad}.cir", "w").write(cir)
    subprocess.run(["ngspice", "-b", f"{ad}.cir"], capture_output=True)
    d = np.loadtxt(f"{ad}.dat"); t, ls = d[:, 0], d[:, 1]
    tt = np.arange(0.15, sure, 1/48000); y = np.interp(tt, t, ls)
    return np.sqrt(np.mean(y**2)), tt, y

if __name__ == "__main__":
    sonuc = {}
    for ver in ["tam", "ucuz"]:
        for ccpl, etiket in [("0.15p", "5 cm damar-toprak"), ("0.005p", "5 cm tip-ring"),
                             ("0.0015p", "tip-ring, 1/3 kuplaj"), ("1e-21", "kablo yok")]:
            for vp in [9.0, 7.0]:
                r, _, _ = calistir(ver, ccpl, vp)
                print(f"{ver:5s} {etiket:22s} pil {vp:.0f} V -> hoparlor {r:5.2f} V rms ({r*r/8*1000:6.1f} mW)", flush=True)
