import subprocess
# durum adi: (kablo kuplaj, aciklama)
durumlar = {
    "damar_toprak_5cm": "0.15p",   # ~5 cm, damar-toprak baglantisi
    "tip_ring_5cm":     "0.005p",  # bukumlu cift ~30 dB iptal
    "kablosuz_ugultu":  "1e-21",   # sadece sebeke ugultusu
}
for ad, c in durumlar.items():
    net = f"""* {ad}
.include modeller.lib
.include vericigovde.inc
.include alici_govde.inc
Ccpl uzak prob {c}
* yakindaki 230 V sebeke hattindan uca kacak (varsayim 0,05 pF)
Vm m 0 SIN(0 325 50)
Cm m prob 0.05p
.ic v(vref)=4.5 v(inp)=4.5 v(inn)=4.5 v(x)=4.5 v(o1)=4.5 v(o2)=4.5 v(sp)=4.5 v(j)=4.5
.tran 5u 1.5 0 5u uic
.control
run
wrdata {ad}.dat v(uzak) v(inp) v(o1) v(ls)
.endc
.end
"""
    open(f"{ad}.cir", "w").write(net)
    r = subprocess.run(["ngspice", "-b", f"{ad}.cir"], capture_output=True, text=True)
    print(ad, "tamam" if "rror" not in r.stdout + r.stderr else (r.stdout + r.stderr)[-800:])
