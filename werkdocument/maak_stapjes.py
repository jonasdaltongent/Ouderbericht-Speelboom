#!/usr/bin/env python3
"""
maak_stapjes.py — de beelden bij de stapjes op de lespagina (assets/stapjes/), uit het werkdocument zelf

Gebruik:  python3 maak_stapjes.py <leeg.pdf>     (vereist PyMuPDF en Pillow)

  leeg.pdf    Ouderbericht zoals Google Documenten het toont: upload Ouderbericht.docx in Drive (het wordt een
              Google-document) en kies Bestand › Downloaden › PDF-document (of Drive API files.export).
              De x in het eerste vak van deel 5 (s6-kruis.png) zet het script zelf in de pdf.

Waarom zo (12-10-2026): de beelden kwamen eerst uit schermafbeeldingen in Chrome. Sinds de nieuwe huisstijl
van het werkdocument maakt dit script ze opnieuw, uit de pdf die Google Documenten zelf maakt (MW les 4: Ouderbericht): dezelfde
letters en vakken die de leerling ziet, op ware grootte (Google Documenten op 100 %), met één rood kader
(#C5221F, witte rand erbuiten). Verandert het werkdocument, draai dan dit script opnieuw.
"""
import os
import sys

import fitz
from PIL import Image, ImageDraw

HIER = os.path.dirname(os.path.abspath(__file__))
UIT = os.path.join(HIER, "..", "assets", "stapjes")
SCHAAL = 2 * 96 / 72          # eerst op dubbele grootte tekenen, dan verkleinen: scherpe letters
ROOD = (197, 34, 31)
VAK = (0xF3, 0xF5, 0xFC)      # HEX_VAK in huisstijl.py
KADER = (0xEE, 0xF0, 0xF9)    # HEX_KADER
VENSTERKOP = (0xE6, 0xF2, 0xEC)   # titelbalk van appvenster


def kleur(fill):
    return tuple(round(c * 255) for c in fill) if fill else None


def vlakken(page, rgb):
    """De gevulde rechthoeken met deze kleur, van boven naar onder en van links naar rechts."""
    uit = []
    for d in page.get_drawings():
        k = kleur(d.get("fill"))
        if k and all(abs(a - b) <= 2 for a, b in zip(k, rgb)):
            uit.append(fitz.Rect(d["rect"]))
    uit.sort(key=lambda r: (round(r.y0), r.x0))
    return uit


def tekst(page, s, nr=0):
    treffers = page.search_for(s)
    if len(treffers) <= nr:
        raise SystemExit(f"'{s}' niet gevonden op bladzijde {page.number + 1}")
    return treffers[nr]


def bladzijde_met(doc, s):
    for p in doc:
        if p.search_for(s):
            return p
    raise SystemExit(f"'{s}' staat in geen enkele bladzijde")


def bewaar(page, naam, uitsnede, kaders=(), boven=None, onder=None):
    """Snijdt uitsnede (in pdf-punten) uit, tekent de rode kaders en bewaart op ware grootte.
    boven/onder: wat boven of onder die hoogte valt, wordt wit (geen halve regels van de buurrij)."""
    uitsnede = fitz.Rect(uitsnede) & page.rect
    pix = page.get_pixmap(matrix=fitz.Matrix(SCHAAL, SCHAAL), clip=uitsnede, alpha=False)
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    d = ImageDraw.Draw(im)
    if boven is not None:
        d.rectangle([0, 0, im.width, (boven - uitsnede.y0) * SCHAAL], fill="white")
    if onder is not None:
        d.rectangle([0, (onder - uitsnede.y0) * SCHAAL, im.width, im.height], fill="white")
    for k in kaders:
        k = fitz.Rect(k)
        box = [(k.x0 - uitsnede.x0) * SCHAAL - 6, (k.y0 - uitsnede.y0) * SCHAAL - 6,
               (k.x1 - uitsnede.x0) * SCHAAL + 6, (k.y1 - uitsnede.y0) * SCHAAL + 6]
        wit = [box[0] - 4, box[1] - 4, box[2] + 4, box[3] + 4]
        d.rounded_rectangle(wit, radius=16, outline=(255, 255, 255), width=4)
        d.rounded_rectangle(box, radius=12, outline=ROOD, width=5)
    im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
    im.save(os.path.join(UIT, naam + ".png"), optimize=True)
    print("gemaakt:", naam + ".png", im.size)


def rand(r, x=8, y=8):
    return fitz.Rect(r.x0 - x, r.y0 - y, r.x1 + x, r.y1 + y)


def band(r, links, rechts):
    """Dezelfde hoogte als r, over de volle breedte van links tot rechts."""
    return fitz.Rect(links, r.y0, rechts, r.y1)


def main(leeg):
    doc = fitz.open(leeg)

    # ---- bladzijde 1: De uitstap, deel 1
    p = bladzijde_met(doc, "De uitstap")
    kader = vlakken(p, KADER)[0]
    wat, wanneer = tekst(p, "Wat:"), tekst(p, "Wanneer:")
    bewaar(p, "s1-de-uitstap", rand(kader, 10, 5),
           [fitz.Rect(kader.x0 + 2, wat.y0 - 1, kader.x1 - 2, wanneer.y1 + 1)], boven=kader.y0 - 1)
    kop1 = tekst(p, "Deel 1")
    vakken = [v for v in vlakken(p, VAK) if v.y0 > kop1.y1]            # rij b tot e, twee vakken per rij
    rij_a = tekst(p, "a.  Woensdag")
    rechts_x = max(v.x1 for v in vakken)
    links_x = tekst(p, "Situatie").x0 - 4
    deel1 = fitz.Rect(links_x, kop1.y0, rechts_x, vakken[-1].y1)
    kopregel = tekst(p, "gesprek?")           # de kop van de tabel heeft twee regels
    bewaar(p, "s2-deel1", rand(deel1), [fitz.Rect(links_x, max(rij_a.y0 - 6, kopregel.y1 + 3), rechts_x, vakken[0].y0)])
    bewaar(p, "s2-kanaal-b", rand(deel1), [vakken[0]])
    bewaar(p, "s2-waarom-b", rand(deel1), [vakken[1]])

    # ---- bladzijde 2: deel 2 en het venster
    p = bladzijde_met(doc, "Deel 2")
    kop2, kop3 = tekst(p, "Deel 2"), tekst(p, "Deel 3")
    d2 = [v for v in vlakken(p, VAK) if kop2.y1 < v.y0 < kop3.y0]        # rij 2 tot 5: twee vakken per rij
    rij1 = tekst(p, "Alles in hoofdletters")
    links, rechts = d2[0].x0 - 36, max(v.x1 for v in d2)
    deel2 = fitz.Rect(links, kop2.y0, rechts, d2[-1].y1)
    bewaar(p, "s3-deel2", rand(deel2), [fitz.Rect(links + 20, rij1.y0 - 6, rechts, d2[0].y0)])
    bewaar(p, "s3-rij2-fout", rand(deel2), [d2[0]])
    bewaar(p, "s3-rij2-beter", rand(deel2), [d2[1]])
    kop = vlakken(p, VENSTERKOP)[0]
    links, rechts = kop.x0, kop.x1
    velden = [v for v in vlakken(p, VAK) if v.y0 >= kop.y1 - 1]          # Aan, Titel, dan de vijf vakken
    rijen = {n: band(v, links, rechts) for n, v in zip(
        ["Aan", "Titel", "aanspreking", "wat", "mee", "positief", "groet"], velden)}
    boven = fitz.Rect(links, kop.y0, rechts, rijen["Titel"].y1)
    bewaar(p, "s4-venster", rand(boven), onder=boven.y1 + 1)
    bewaar(p, "s4-aan", rand(boven), [rijen["Aan"]], onder=boven.y1 + 1)
    bewaar(p, "s4-titel", rand(boven), [rijen["Titel"]], onder=boven.y1 + 1)
    bericht = fitz.Rect(links, rijen["aanspreking"].y0, rechts, rijen["groet"].y1)
    for n in ("aanspreking", "wat", "mee", "positief", "groet"):
        bewaar(p, "s4-" + n, rand(bericht), [rijen[n]], boven=bericht.y0 - 1)

    # ---- bladzijde 3: deel 4 en deel 5
    p = bladzijde_met(doc, "Voor elke ouder")
    kop4, kop5 = tekst(p, "Deel 4"), tekst(p, "Deel 5")
    slot = tekst(p, "Waarom vertel je")
    vakken = vlakken(p, VAK)
    # vraag a is een tabel (twee rijen van twee vakken: Kobe schreef · Google Vertalen maakte ervan), dan b en c
    a1_kobe, a1_vert, a2_kobe, a2_vert, vb, vc = [v for v in vakken if kop4.y1 < v.y0 < kop5.y0]
    code = tekst(p, "Het codewoord")                 # sinds 15-10-2026: deel 5 begint met het codewoord
    antw_code = [v for v in vakken if code.y1 < v.y0 < slot.y0][0]
    vinkjes = [v for v in vakken if antw_code.y1 < v.y0 < slot.y0]
    antw_slot = [v for v in vakken if v.y0 > slot.y1][0]
    links, rechts = vb.x0, vb.x1
    qa, qb, qc = tekst(p, "Welke twee fouten"), tekst(p, "Schrijf de zin van Kobe"), tekst(p, "Welke twee pictogrammen")
    vraag_a = rand(fitz.Rect(links, qa.y0, rechts, a2_vert.y1), 8, 10)
    bewaar(p, "s5-deel4", vraag_a, [a1_kobe])
    bewaar(p, "s5-vertaling", vraag_a, [a1_vert])
    bewaar(p, "s5-zin", rand(fitz.Rect(links, qb.y0, rechts, vb.y1), 8, 10),
           [fitz.Rect(links, qb.y0 - 2, rechts, vb.y1)])
    bewaar(p, "s5-pict", rand(fitz.Rect(links, qc.y0, rechts, vc.y1), 8, 10),
           [fitz.Rect(links, qc.y0 - 2, rechts, vc.y1)])
    bewaar(p, "s6-codewoord", rand(fitz.Rect(links, kop5.y0, rechts, antw_code.y1), 8, 10),
           [fitz.Rect(links, code.y0 - 2, rechts, antw_code.y1)], onder=antw_code.y1 + 4)
    tab5 = fitz.Rect(links, kop5.y0, rechts, vinkjes[-1].y1)
    bewaar(p, "s6-deel5", rand(tab5), onder=vinkjes[-1].y1 + 1)
    bewaar(p, "s6-slotvraag", rand(fitz.Rect(links, slot.y0, rechts, antw_slot.y1), 8, 10),
           [fitz.Rect(links, slot.y0 - 2, rechts, antw_slot.y1)])
    # de x in het eerste vak van deel 5 (alleen in het geheugen, voor s6-kruis.png)
    v = vinkjes[0]
    p.insert_textbox(fitz.Rect(v.x0, v.y0 + (v.height - 14) / 2 - 1, v.x1, v.y1), "x", fontsize=12,
                     fontname="helv", align=1)
    bewaar(p, "s6-kruis", rand(fitz.Rect(links, vinkjes[0].y0, rechts, vinkjes[2].y1), 8, 8), [vinkjes[0]],
           boven=vinkjes[0].y0 - 1, onder=vinkjes[2].y1 + 1)

    # ---- bladzijde 4: Extra
    p = bladzijde_met(doc, "Extra")
    kopx = tekst(p, "Extra")
    vx = [v for v in vlakken(p, VAK) if v.y0 > kopx.y1][0]
    qx = tekst(p, "Een mama antwoordt")
    bewaar(p, "s7-extra", rand(fitz.Rect(links, kopx.y0, rechts, vx.y1), 8, 10),
           [fitz.Rect(links, qx.y0 - 2, rechts, vx.y1)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
