* Ucuz verici: tek CD4093
VB vcc 0 9
* U1A: titresim osilatoru (~10 Hz)
XA vcc t1 vcc 0 lfo NAND4093
R1u lfo t1 1.2Meg
C1u t1 0 100n
* U1B: ton osilatoru (~1 kHz), lfo yuksekken calisir
XB lfo t2 vcc 0 tonr NAND4093
R2u tonr t2 120k
C2u t2 0 10n
* U1C, U1D: paralel tampon (evirici)
XC tonr tonr vcc 0 cikis NAND4093
XD tonr tonr vcc 0 cikis NAND4093
R3u cikis cl 470
D1u cl vcc D1N4148
D2u 0 cl D1N4148
C3u cl kirmizi 1u
Rh1 kirmizi h1 140
Ch1 h1 0 50n
Rh2 h1 h2 140
Ch2 h2 0 50n
Rh3 h2 uzak 140
Ch3 uzak 0 50n
Rkacak uzak 0 100Meg
.model D1N4148 D(Is=2.5n Rs=0.6 N=1.75 Cjo=4p Bv=100)
