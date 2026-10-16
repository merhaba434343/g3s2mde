VB vcc 0 9
R1t vcc dis1 10k
R2t dis1 tc1 68k
C2t tc1 0 4.7u
C3t cv1 0 10n
XU1t vcc 0 tc1 tc1 cv1 dis1 lfo NE555
R5t lfo cv2 10k
R3t vcc dis2 1k
R4t dis2 tc2 6.8k
C4t tc2 0 100n
XU2t vcc 0 tc2 tc2 cv2 dis2 ton NE555
R6t ton cl 470
D2t cl vcc D1N4148
D3t 0 cl D1N4148
C5t cl kirmizi 1u
Rh1 kirmizi h1 140
Ch1 h1 0 50n
Rh2 h1 h2 140
Ch2 h2 0 50n
Rh3 h2 uzak 140
Ch3 uzak 0 50n
Rkacak uzak 0 100Meg
.model D1N4148 D(Is=2.5n Rs=0.6 N=1.75 Cjo=4p Bv=100)
