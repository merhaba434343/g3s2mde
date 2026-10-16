* Alici prob (sema A-01)
VBR vb 0 9
R1 vb vref 100k
R2 vref 0 100k
C2 vref 0 10u
* prob ucu: kablodan Ccpl, sebekeden Cmains, ucun kendi kacak kapasitesi 5 pF
Cpst prob 0 5p
Rpl prob 0 1T
C3 prob inp 10n
R3 inp vref 10Meg
XU1 inp inn vb 0 o1 TL071
R4 o1 inn 100k
C9 o1 inn 470p
R5 inn x 1k
C8 x vref 220n
* U1B: 2. dereceden Sallen-Key yuksek geciren, fc ~ 500 Hz
C10 o1 j 10n
C11 j sp 10n
R7 j o2 22k
R8 sp vref 47k
XU1B sp o2 vb 0 o2 TL071
C4 o2 pot 1u
RVR pot 0 10k
XU2 pot 0 vb 0 spk LM386
R6 spk z 10
C6 z 0 47n
C7 spk ls 220u
RLS ls 0 8
