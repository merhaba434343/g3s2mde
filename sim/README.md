# Kablo takip cihazı (bilibili) simülasyonu

ngspice ile verici + 3 km DSL hattı + alıcı prob simülasyonu.

```
ngspice -b verici.cir && python3 analiz_verici.py   # verici frekansları, hat sinyali
ngspice -b alici_ac.cir                             # alıcı frekans cevabı
python3 calistir_tran.py && python3 analiz_alici.py # 3 durumda hoparlör çıkışı
python3 grafikler.py                                # PNG grafikler ve WAV sesler
```

- `modeller.lib`: NE555, TL072 (yarısı), LM386 için davranışsal modeller
- `vericigovde.inc`, `alici_govde.inc`: devreler (şema V-01 ve A-01)
