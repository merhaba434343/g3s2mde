* Ucuz alici: TL071 + LM386, ayri filtre kati yok
VBR vb 0 9
R1 vb vref 100k
R2 vref 0 100k
C2 vref 0 10u
Cpst prob 0 5p
Rpl prob 0 1T
C3 prob inp 10n
R3 inp vref 10Meg
XU1 inp inn vb 0 o1 TL071
R4 o1 inn 100k
R5 inn x 1k
C8 x vref 220n
* C4 kucuk secildi: VR1 ile birlikte 1,6 kHz yuksek geciren (50 Hz'i bastirir)
C4 o1 pot 10n
RVR pot 0 10k
XU2 pot 0 vb 0 spk LM386
R6 spk z 10
C6 z 0 47n
C7 spk ls 220u
RLS ls 0 8
