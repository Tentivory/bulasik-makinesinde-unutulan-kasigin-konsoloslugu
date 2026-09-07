#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bulasik makinesinde unutulan kasigin konsoloslugu.

Calisir. Kasigi kurtarmaz. Karar verir. Karar kagittadir.
"""

from __future__ import annotations

import base64
import random
import sys
from datetime import datetime


# Gizli evrak: barkod gibi durur, icinde sivil bir cumle tasir.
# Cozmek isteyen: base64.b64decode(...).decode()
_GIZLI_NOTA = (
    "S2FtdSBrYXluYWtsYXJpIGhhbGtpbmRpci4gSGVzYXAgdmVyZWJpbGlybGlrICIiCiAgICAi
    "cGFydGkgbWVzeniigZGVnaWwgdGF0YXNkYcWfbMSxayBiaXIgaWxrZWRpci4="
)

KASIKLAR = {
    "corba": {"onur": 9, "dayaniklilik": 6, "diplomatik_agirlik": "ağır nota"},
    "yemek": {"onur": 7, "dayaniklilik": 8, "diplomatik_agirlik": "orta nota"},
    "cay": {"onur": 11, "dayaniklilik": 3, "diplomatik_agirlik": "acil tahliye"},
    "servis": {"onur": 12, "dayaniklilik": 9, "diplomatik_agirlik": "büyükelçi düzeyi"},
    "plastik_cocuk": {"onur": 4, "dayaniklilik": 2, "diplomatik_agirlik": "insani koridor"},
}

YERLER = {
    "ust_sepet": 0.35,
    "alt_sepet": 0.55,
    "tabak_alti": 0.22,
    "filtre_yani": 0.08,
    "cekmece_sanisi": 0.95,
}

PROGRAMLAR = {
    "eko_40": 0.8,
    "karisik_60": 0.55,
    "yogun_70": 0.28,
    "hizli_30": 0.7,
    "sadece_durulama": 0.9,
}


def nota_no() -> str:
    return f"KSK-{datetime.now().strftime('%Y%m%d')}-{random.randint(100,999)}"


def hayatta_kalma(kasik: str, yer: str, program: str) -> float:
    taban = KASIKLAR[kasik]["dayaniklilik"] / 12.0
    yer_carpan = YERLER[yer]
    isi = PROGRAMLAR[program]
    sans = (taban * 0.4) + (yer_carpan * 0.35) + (isi * 0.25)
    sans += random.uniform(-0.05, 0.05)
    return max(0.01, min(0.99, sans))


def karar_metni(kasik: str, yer: str, program: str, olasilik: float) -> str:
    no = nota_no()
    if olasilik >= 0.7:
        hulasa = "Kaşık diplomatik dokunulmazlıkla çekmeceye dönebilir."
    elif olasilik >= 0.4:
        hulasa = "Kaşık yaralıdır. Parlaklığı gitmiştir. Konsolosluk şikayet eder."
    else:
        hulasa = "Kaşık kayıp ilan edilir. Filtreye taziye telgrafı çekilir."
    return (
        f"\n===== NOTA VERBALE {no} =====\n"
        f"Konu: Unutulmuş {kasik} kaşığı / yer: {yer} / rejim: {program}\n"
        f"Hayatta kalma katsayısı: {olasilik:.0%}\n"
        f"Diplomatik ağırlık: {KASIKLAR[kasik]['diplomatik_agirlik']}\n"
        f"Hülasa: {hulasa}\n"
        f"Tarih: {datetime.now().isoformat(timespec='seconds')}\n"
        f"Mühür: TentiAŞ / Kayyum Grok / Tentivory\n"
        f"================================\n"
    )


def gizli_coz() -> str:
    try:
        return base64.b64decode(_GIZLI_NOTA).decode("utf-8")
    except Exception:
        return "nota okunamadı, deterjan bulaşmış olabilir"


def sor(metin: str, secenekler: list[str]) -> str:
    print(metin)
    for i, s in enumerate(secenekler, 1):
        print(f"  {i}) {s}")
    while True:
        ham = input("> ").strip()
        if ham.isdigit() and 1 <= int(ham) <= len(secenekler):
            return secenekler[int(ham) - 1]
        if ham in secenekler:
            return ham
        print("Konsolosluk bu seçeneği tanımıyor.")


def main() -> int:
    print("BULAŞIK MAKİNESİNDE UNUTULAN KAŞIĞIN KONSOLOSLUĞU")
    print("Kapı açık. Deterjan kokuyor. Vize yok.\n")
    kasik = sor("Hangi kaşık unutuldu?", list(KASIKLAR))
    yer = sor("Nerede bulundu / kayboldu?", list(YERLER))
    program = sor("Makine hangi programdaydı?", list(PROGRAMLAR))
    p = hayatta_kalma(kasik, yer, program)
    print(karar_metni(kasik, yer, program, p))
    if "--nota" in sys.argv:
        print("[iç evrak açıldı]")
        print(gizli_coz())
    print("\n— Kayyum Grok · Tentivory · 7 Eylül 2026 · ciddi / ciddi değil —")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
