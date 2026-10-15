#!/usr/bin/env python3
"""
maak_werkdocumenten.py
Genereert het werkdocument voor les 4 "Berichten aan ouders" (De Speelboom, klas 3MWb):

  Ouderbericht.docx    het werkdocument dat de leerling INLEVERT (wordt in Classroom een Google-document)

Gebruik:  python3 maak_werkdocumenten.py     (vereist python-docx; huisstijl.py en go-dalton-gent.png
          staan ernaast; huisstijl.py heeft hier een extra bouwblok: appvenster)

Waarom geen zip en geen echte app: de les is een afstandsles (thuis, op de Chromebook, zonder leraar) en per les
gebruiken de leerlingen één werkplek naast Classroom en de lespagina (_afspraken/didactiek.md). Het bericht komt
daarom in dit document, in een venster dat eruitziet als "Nieuw bericht" in de (verzonnen) Speelboom-app.
Er wordt niets verstuurd. De teksten om te lezen (het bericht van Kobe, het bericht van Lien, de vertalingen,
de pictogrammen) staan op de lespagina.

LET OP bij aanpassen:
 - Deel 1, rij a en deel 2, rij 1 zijn het uitgewerkte voorbeeld (er is geen leraar die voordoet). Laat ze ingevuld.
 - De feiten van de uitstap (datum, uren, wat de kinderen meegeven) staan ook op de lespagina (de quiz niet,
   wel het bericht van Lien) en in de verbetersleutel van de README. Verander je ze, doe het overal.
 - De punten in deel 5 komen uit lesvoorbereiding.md § 22. Verander je ze, doe het op beide plaatsen.
 - Alle namen en gegevens zijn fictief (dat staat op de lespagina, niet in het werkdocument).
"""
import os
from huisstijl import *

HERE = os.path.dirname(os.path.abspath(__file__))


def ouderbericht():
    doc = nieuw_document()
    kopblok(doc, "OUDERBERICHT", punten=20)

    kader(doc, "De uitstap", [
        ("Wie:", "groep De Eekhoorns, kinderen van 6 tot 9 jaar"),
        ("Wat:", "een uitstap naar het speelbos"),
        ("Wanneer:", "woensdag 18 november 2026. Vertrek om 13.30 uur, terug om 16.30 uur."),
        ("Ophalen:", "vanaf 16.30 uur in De Speelboom"),
        ("Meegeven:", "laarzen, een regenjas en een drinkbus met water"),
        ("Berichtjes:", "De Speelboom stuurt de ouders berichtjes via een eigen app: de Speelboom-app."),
        ("Jouw rol:", "stagiair. Je mentor Lien Verhoeven vraagt jou het bericht aan de ouders te schrijven."),
    ])

    # ---- Deel 1
    deel(doc, 1, "Welk kanaal?")
    tabel(doc, ["Situatie", "Speelboom-app, bellen of gesprek?", "Waarom?"], [
        ("a.  Woensdag 18 november gaan De Eekhoorns naar het speelbos. Alle ouders moeten laarzen meegeven.",
         "Speelboom-app", "praktisch nieuws voor alle ouders"),
        ("b.  Om 15 uur heeft een kind 39 °C koorts. Het moet naar huis.", "", ""),
        ("c.  Een kind heeft vandaag een ander kind gebeten. Je wil dat met de ouders bespreken.", "", ""),
        ("d.  Een papa vraagt met een berichtje in de Speelboom-app of de muts van zijn dochter nog in De Speelboom ligt.", "", ""),
        ("e.  Een mama vraagt je gsm-nummer, zodat ze je via WhatsApp kan sturen.", "", ""),
    ], [7.4, 3.4, BREEDTE - 7.4 - 3.4], invul=(1, 2), rijhoogte=1.5, voorbeeld_rij=1)

    # ---- Deel 2
    deel(doc, 2, "Wat is er mis met het bericht van Kobe?", nieuwe_pagina=True)
    tabel(doc, ["", "Wat is er mis?", "Hoe kan het beter?"], [
        ("1", "Alles in hoofdletters en drie uitroeptekens: dat leest als roepen.", "Begin met een aanspreking: *Beste ouders,*"),
        ("2", "", ""),
        ("3", "", ""),
        ("4", "", ""),
        ("5", "", ""),
    ], [0.8, 8.1, BREEDTE - 0.8 - 8.1], invul=(1, 2), rijhoogte=1.3, voorbeeld_rij=1)

    # ---- Deel 3 (het venster breekt niet: het staat met deel 2 op bladzijde 2)
    deel(doc, 3, "Jouw bericht aan de ouders")
    appvenster(doc, [("① aanspreking", 1.0), ("② wat en wanneer", 2.4), ("③ wat geven de ouders mee?", 1.8),
                     ("④ iets positiefs", 1.4), ("⑤ groet, je naam en wie je bent", 1.8)])

    # ---- Deel 4
    deel(doc, 4, "Voor elke ouder", nieuwe_pagina=True)
    # a: de leerling zoekt de fouten zelf in het infokader op de lespagina (Jonas, 13-10-2026: geef de
    # antwoorden niet zelf). Geen ingevulde rij: er zijn maar twee fouten.
    vraag(doc, "a.  Welke twee fouten maakte Google Vertalen in de zin van Kobe?")
    tabel(doc, ["", "Kobe schreef", "Google Vertalen maakte ervan"], [
        ("1", "", ""),
        ("2", "", ""),
    ], [0.8, 6.2, BREEDTE - 0.8 - 6.2], invul=(1, 2), rijhoogte=1.0)
    vraag(doc, "b.  Schrijf de zin van Kobe opnieuw, zodat Google Vertalen geen fouten meer maakt.")
    tekst(doc, "Tegen half vijf mogen jullie de kapoenen komen oppikken.", cursief=True, na=2)
    antwoordvak(doc, 1.4)
    vraag(doc, "c.  Welke twee pictogrammen zet je bij jouw bericht? Typ de letters.")
    antwoordvak(doc, 1.0)

    # ---- Deel 5: nalezen = de criteria van de beoordeling (lesvoorbereiding § 22)
    deel(doc, 5, "Nalezen")
    # eerst het codewoord van de zelftest (15-10-2026): de lespagina toont het pas als de drie vragen van stap 6
    # juist zijn; zo ziet Jonas wie de zelftest echt maakte (_afspraken/lespagina.md, De laatste stap)
    vraag(doc, "Het codewoord van de zelftest (stap 6 op de lespagina):")
    antwoordvak(doc, 0.9)
    controletabel(doc, [
        ("Deel 1: bij b tot e staat *Speelboom-app*, *bellen* of *gesprek*, met een reden.", 4),
        ("Deel 2: ik vond vier fouten en schreef erbij hoe het beter kan.", 2),
        ("Deel 3: bij Aan staat *Alle ouders van De Eekhoorns*, en ik schreef een duidelijke titel.", 2),
        ("Deel 3: mijn bericht zegt wat, welke dag en hoe laat (in cijfers), en wat de ouders meegeven.", 4),
        ("Deel 3: mijn bericht is kort, positief en beleefd: een aanspreking, overal *jullie*, een groet, "
         "mijn naam en *stagiair*.", 4),
        ("Deel 3: geen hoofdletters, chattaal, dialect of emoji's, en geen andere kinderen bij naam.", 2),
        ("Deel 4: de twee fouten van Google Vertalen, de zin zonder die fouten en twee passende pictogrammen.", 2),
    ])
    vraag(doc, "Waarom vertel je moeilijk nieuws liever niet met een berichtje in de Speelboom-app?")
    antwoordvak(doc, 1.8)

    # ---- Extra
    deel(doc, None, "Extra — niet verplicht")
    vraag(doc, "Een mama antwoordt met een berichtje in de Speelboom-app: “Mijn zoon heeft geen laarzen. Mag hij met sportschoenen komen?” "
               "Schrijf een kort, vriendelijk antwoord.")
    antwoordvak(doc, 2.4)

    doc.save(os.path.join(HERE, "Ouderbericht.docx"))


if __name__ == "__main__":
    ouderbericht()
    print("Gemaakt: Ouderbericht.docx")
