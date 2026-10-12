# Handleiding voor de leraar — Les 4: Berichten aan ouders

**Vak:** Toegepaste Informatica
**Doelgroep:** klas 3MWb — 2de graad Maatschappij en welzijn, dubbele finaliteit
**Lesduur:** 1 × 50 minuten: **0 minuten instructie + 50 minuten keuzewerktijd** (afstandsles)
**Context:** De Speelboom, een fictieve buitenschoolse opvang, met de (verzonnen) Speelboom-app
**Waar:** thuis, alleen, op de eigen Chromebook (geen leraar in het lokaal)
**Lesdag:** maandag 19 oktober 2026, 9de lesuur (15.25–16.15): pedagogische studienamiddag
**Kernleerplandoel:** `BV2_04.01` — digitaal communiceren (toepassen; summatief via het portfolio)
**Opdracht in Classroom:** *Les 4 — Berichten aan ouders*, deadline vrijdag 23 oktober 2026, 20.00 uur

<!-- Beginvragen (stap 1 van CONTEXT.md), beantwoord door Jonas op 12-10-2026:
     klas 3MWb · les 4 van het lessenplan (Berichten aan ouders) · lesdag ma 19-10, 9de uur: de pedagogische
     studienamiddag, maar "De leerlingen hebben zelfstandig werk thuis. Deze les gaat dus toch door op 19 oktober,
     niet 26. De leerlingen werken op hun chromebook." Dus afstandsonderwijs: thuis, alleen, zonder leraar in het
     lokaal · les 3 is gegeven op 12-10 (antwoorden in de app Na de les): lesstart haalt les 3 op ·
     de ouderapp is een venster in het werkdocument, zoals het mailvenster van les 3 (één werkplek, niets
     versturen, geen zip) · lespagina met Stap voor stap / Kort, start in Stap voor stap · AI-hulp: ja, zoals
     les 3 · toestel: Chromebook (thuis). -->

## 1. Inhoud van het pakket

```text
W08 - Les 04 - MW - Berichten aan ouders/
├── index.html              de lespagina: startpagina in beelden · route · één stap · checklist (6 stappen, 17 taken)
├── presentatie.html        10 dia's: de RESERVE (zie hieronder); dia 1 is de vaste startdia
├── css/style.css           lespagina (les 3, met .app, .vert, .pict-rij, .kijkna voor deze les)
├── css/slides.css          dia's
├── js/script.js, js/slides.js   (script.js heeft de knop Kijk na)
├── assets/                 logo's De Speelboom en GO! Dalton Gent, lettertypes (OFL), mascotte, stapjes (22 beelden)
├── werkdocument/
│   ├── Ouderbericht.docx           het werkdocument dat de leerling INLEVERT
│   ├── maak_werkdocumenten.py      maakt het opnieuw (python-docx)
│   ├── huisstijl.py, go-dalton-gent.png   de huisstijl, met een extra bouwblok: appvenster
│   └── maak_stapjes.py             maakt de beelden bij de stapjes opnieuw, uit de pdf van Google Documenten
├── lesvoorbereiding.md     de lesvoorbereiding (28 punten + bronnenonderzoek)
├── dalton-lesfiche.html    de Dalton-lesfiche (instructie 0 + KWT 50): openen, Kopieer de fiche, plakken
├── lesdoelen.json          de doelen voor je jaaroverzicht
├── classroom.json          de opdracht voor de Classroom-koppeling
├── ai-bron.txt             de volledige tekst van de lespagina: de bron van de AI-hulp
└── README.md               deze handleiding
```

**Een afstandsles.** Ma 19-10 is een pedagogische studienamiddag: "De leerlingen hebben zelfstandig werk thuis.
Deze les gaat dus toch door op 19 oktober, niet 26. De leerlingen werken op hun chromebook." (Jonas, 12-10-2026).
Daarom: geen instructie, de lespagina doet alles (de quiz *Weet je het nog?*, het uitgewerkte voorbeeld van Lien,
de ingevulde eerste rijen, de route met minuten). Zes afwijkingen van de gewone les staan bovenaan
`lesvoorbereiding.md`; de belangrijkste:

- **Vast?** = *Toon stapjes* → *AI-hulp* → *Je leraar*: een **privéreactie** bij de opdracht (onder **Privéreacties**
  typen › **Posten**). Dat wijkt af van `_afspraken/klikpaden.md` (thuis is er geen buur en geen leraar).
  `controleer_les.py` laat het toe met `<meta name="afstandsles" content="ja">` (nieuw, zie § 8).
- **Niet klaar?** staat deze keer wel op de lespagina, in stap 6: werk verder tot de deadline.
- **De dia's** (`presentatie.html`) zijn een **reserve**: ze worden op 19-10 niet getoond (de notities van dia 1
  zeggen het). Blijkt op 26-10 dat veel leerlingen de les niet maakten, dan kan je ze in de klas gebruiken
  (les 5 schuift dan op).
- **Eén werkplek**: alles in het werkdocument; de ouderapp is een venster daarin (*Speelboom-app · Nieuw bericht*,
  met Aan en Titel en vijf vakken). Er wordt niets verstuurd, er is geen zip en geen echte vertaalapp: de
  vertalingen staan op de lespagina (Google Vertalen, 12-10-2026).
- **Op de lespagina**: bij elke leestaak eerst het doel (*Zoek vier dingen die …*), de quiz met directe uitleg, zes
  eigen pictogrammen A–F, de knop *Kijk na* in stap 5 en in stap 6 de tekening van de opdracht met **Inleveren** in
  een rood kader (de vraag die in les 3 het vaakst kwam).

### 1b. Hoe de lespagina werkt

- **Startpagina**: *Wat heb je nodig?* in drie beelden (de opdracht, de lespagina, het werkdocument), één zin
  *Je werkt thuis: alles wat je nodig hebt, staat hier*, *Na deze les kan je*, *Vast?* als genummerde rij.
- **Route** links, **één stap** in het midden, **checklist** rechts (17 taken). Op een smal scherm staat alles
  onder elkaar. Op 1280 × 650 staat *Wat moet je doen?* (kop op ± 223 px) in elke stap in beeld zonder scrollen.
- **Stap voor stap / Kort**: de les begint in *Stap voor stap* (`data-modus-start="stap"`).
- **Titel van de pagina**: *Lespagina · Les 4 · …*: zo heet de link in de opdracht.
- **Toestel**: `<meta name="toestel" content="chromebook">`; geen Windows-woorden.
- **AI-hulp**: `data-ai-hulp="aan"` zodra de notebook aan de opdracht hangt (zie hieronder).
- `?leraar` toont screenshot-plaatsen (deze les heeft er geen: de beelden zijn tekeningen en uitsneden van het
  werkdocument).

## 2. Klaarzetten

### Stap 1 — Publiceren via GitHub Pages

Repository [`jonasdaltongent/Ouderbericht-Speelboom`](https://github.com/jonasdaltongent/Ouderbericht-Speelboom), Pages op branch `main`,
map `/ (root)`. De lespagina: <https://jonasdaltongent.github.io/Ouderbericht-Speelboom/>, de dia's:
<https://jonasdaltongent.github.io/Ouderbericht-Speelboom/presentatie.html>. Dat adres staat ook op dia 9, in
`classroom.json` en in `lesdoelen.json`.

### Stap 2 — De opdracht in Classroom, met de koppeling

Als **concept** in [3MWb - Informatica](https://classroom.google.com/c/MjUzNTk0NjYzMTJa), **ingepland**: Classroom publiceert het
zelf op **maandag 19-10-2026 om 8.25 uur**, het eerste lesuur. Dat is een **eenmalige uitzondering** (Jonas,
12-10-2026: "Je mag deze inderdaad vroeger publiceren. Je mag ze eenmalig zelfs al op maandag op het eerste lesuur
publiceren."); de gewone regel (een half uur vóór het lesuur, hier 14.55 uur) staat in `_afspraken/publiceren.md`.
Wil je ze al later of vroeger, dan verandert alleen het tijdstip van het inplannen.

| | Opdracht: **Les 4 — Berichten aan ouders** |
|---|---|
| **Onderwerp** | Module 1 — Organiseren en professioneel communiceren |
| **Bijlage 1** | de link naar de lespagina |
| **Bijlage 2** | `Ouderbericht` (Google-document) — **Een kopie maken voor elke leerling** |
| **Bijlage 3** | de notebook *AI-hulp · Les 4 · Berichten aan ouders* (Gemini Notebook) |
| **Punten** | 20 |
| **Deadline** | vrijdag 23 oktober 2026, 20.00 uur |

```bash
python3 "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/_tools/zet_opdracht_klaar.py" "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/2026-2027/W08 - Les 04 - MW - Berichten aan ouders" --proef
```

Instructietekst (het script vult de deadline in; er is geen e-mailadres nodig):

```text
Je werkt thuis op je Chromebook.
Open de lespagina en werk stap 1 tot 6 af.
Je schrijft alles in je werkdocument Ouderbericht. Je hebt niets anders nodig.

Klik op Inleveren, ten laatste vrijdag 23 oktober 2026 om 20.00 uur.
```

**Wil je ze zelf eerder tonen?** In het concept kan je het inplannen laten staan; klik je zelf op **Toewijzen**,
dan verschijnt de opdracht meteen.

### Stap 3 — Met de hand, als de koppeling niet werkt

1. Upload `werkdocument/Ouderbericht.docx` **in Drive zelf** (**Nieuw** › **Bestand uploaden**, met *Uploads
   converteren* aan).
2. Voeg het in de opdracht toe met **Bijvoegen** › **Drive**, met **Een kopie maken voor elke leerling**
   (alleen vóór je de opdracht post).
3. Voeg de lespagina toe met **Link**.

### De AI-hulp

Zie § AI-hulp onderaan deze stap: de notebook, de bron (`ai-bron.txt`) en de instelling staan volgens
`_afspraken/ai-hulp.md`. (Wordt ingevuld na het klaarzetten.)

### Afvinklijst vóór de les (een afstandsles)

- [ ] De lespagina staat online (HTTP 200) en het adres op dia 9 klopt.
- [ ] De opdracht staat als **concept** klaar in `3MWb - Informatica` met de lespagina, *Ouderbericht* als **kopie per
      leerling** en de notebook; het inplannen staat op ma 19-10 om 8.25 uur (teruggelezen: nog `DRAFT`).
- [ ] **Geen wachtwoord op het bord** of op een dia: de leerlingen zitten thuis en melden zelf aan.
- [ ] **Geen demo-kopie** klaar te zetten: er is geen demo (de dia's worden niet getoond).
- [ ] Je Classroom-meldingen staan aan: de **privéreacties** van leerlingen die vastzitten komen binnen.
- [ ] De Dalton-lesfiche staat in je planner (open `dalton-lesfiche.html`, klik op **Kopieer de fiche**, plak).
- [ ] Zeg het aan de klas in een ander lesuur: de opdracht staat vanaf 8.25 uur klaar (en de deadline is vrijdag).

**Optie:** een **instructiefilmpje van 2 minuten** (jij, schermopname) in de opdracht: de lespagina openen, naar
*Ouderbericht* wisselen, in het venster typen, **Inleveren**. Dat is bouwsteen 3 van *Wijze lessen* (eigen
instructievideo). Niet nodig om de les te geven. Zie `_afspraken/filmpjes-en-schermafbeeldingen.md`.

### 2b. Nagelezen klikpaden

| Handeling | Klikpad / naam | Bron |
|---|---|---|
| Inleveren | **Inleveren** · **Inleveren ongedaan maken** | [Classroom 6020285](https://support.google.com/edu/classroom/answer/6020285?hl=nl&co=GENIE.Platform%3DDesktop) (09-10-2026) |
| Bericht aan de leraar | onder **Privéreacties** typen › **Posten** | Jonas' scherm (09-10-2026), `_afspraken/klikpaden.md` |
| De opdracht (leerling) | in het midden de bijlagen; rechts **Jouw werk** met de eigen kopie en **Inleveren** | demoleerling3 (09-10-2026), `_afspraken/klikpaden.md` |

Er staan geen knopnamen van Documenten of van een app in de stappen: de leerlingen typen alleen in vakken van
hun werkdocument. Nog niet nagelezen op een leerlingenaccount: de naam van de knop in het bevestigingsvenster na
**Inleveren**, en of een leerling met **Inleveren ongedaan maken** opnieuw kan inleveren (de Extra gebruikt het).

## 3. Het verloop van de les

Er is geen les in het lokaal. Dit is wat een leerling thuis doet (50 minuten, volgens de route links):

| Stap | Titel | Min. | Werkdocument | Wat gebeurt er |
|---|---|---|---|---|
| 1 | Start | 5 | kader *De uitstap* | quiz *Weet je het nog?* (3 vragen, direct uitleg), werkdocument openen, kader lezen met een doel |
| 2 | Welk kanaal? | 8 | deel 1 | app, bellen of gesprek bij vier situaties, met een reden (rij a is ingevuld) |
| 3 | Wat is er mis? | 8 | deel 2 | vier fouten in het bericht van Kobe (rij 1 is ingevuld) |
| 4 | Jouw bericht | 15 | deel 3 | het bericht van Lien als voorbeeld; eigen bericht in het venster van de Speelboom-app |
| 5 | Voor elke ouder | 7 | deel 4 | vertalingen lezen, zin in eenvoudige taal, twee pictogrammen, *Kijk na* |
| 6 | Nalezen en inleveren | 7 | deel 5 | criteria aankruisen, slotvraag, **Inleveren** |
| Extra | Antwoord aan een mama | — | *Extra* | telt niet mee; opnieuw inleveren |

**Voor jou, ná de les:** kijk in de opdracht wie ingeleverd heeft en lees de privéreacties; geef één top en één tip
als privéreactie. In de AI-hulp zie je wie een gesprek begon (niet wat gevraagd werd).

## 4. Verbetersleutel

- **Deel 1** (4 punten): b **bellen** (de ouder moet meteen iets doen; een bericht wordt misschien te laat
  gelezen) · c **gesprek** bij het afhalen (bellen mag ook): gevoelig, de ouder moet je kunnen horen en zien en iets
  kunnen vragen · d **app**: een korte, praktische vraag, antwoord in de app · e **app van De Speelboom**: als
  stagiair geef je je eigen gsm-nummer niet; berichten gaan via de opvang.
- **Deel 2** (2 punten), zes mogelijke fouten (vier zijn genoeg): hoofdletters en *!!!* (ingevuld) · geen titel en
  geen naam: de ouders weten niet waarover het gaat en wie het stuurt · negatief (*anders zijn de kleren vuil en da
  is nie onze schuld*) met 😂: klinkt als een verwijt of als uitlachen → zeg wat ze meegeven · dialect en chattaal
  (*da, nie, he, botten, kapoenen, oppikken, amai*): niet elke ouder begrijpt het, een vertaalmachine ook niet ·
  twee kinderen bij naam en iets negatiefs over hen, in een bericht aan **alle** ouders → privacy; praat met hun ouders ·
  informatie ontbreekt: welke woensdag, hoe laat vertrekken jullie, regenjas en drinkbus?
- **Deel 3** (12 punten), een goed bericht (een van vele): *Aan*: Alle ouders van De Eekhoorns · *Titel*: Woensdag 18
  november: uitstap naar het speelbos · *Beste ouders,* / *Woensdag 18 november gaan we met De Eekhoorns naar het
  speelbos. We vertrekken om 13.30 uur en zijn om 16.30 uur terug in De Speelboom.* / *Geven jullie laarzen, een
  regenjas en een drinkbus met water mee?* / *De kinderen kijken er al naar uit!* / *Vriendelijke groeten,* /
  *[voornaam en naam], stagiair in De Speelboom*
- **Deel 4** (2 punten): a *kapoenen* werd *capons*: gecastreerde hanen · *half vijf* werd na het Turks *half
  vier*: een uur te vroeg. b *Om 16.30 uur kunnen jullie je kind ophalen.* (of: *Vanaf 16.30 uur …*) c twee van A–D
  (laars, regenjas, klok, boom); niet E (zwembroek) of F (taart).
- **Deel 5**, slotvraag: in een bericht zie je geen gezicht en hoor je geen stem; de ouder kan niet meteen iets
  vragen; het komt sneller verkeerd over.

Punten (20): deel 1: 4 · deel 2: 2 · deel 3: aan en titel 2, wat/dag/uur/meegeven 4, kort-positief-beleefd 4, geen
hoofdletters/chattaal/dialect/emoji en geen ander kind 2 · deel 4: 2 (`lesvoorbereiding.md` § 22).

### Essentiële fouten — geef hier altijd feedback op

- Bij koorts een bericht in de app in plaats van bellen.
- Andere kinderen bij naam in een bericht aan alle ouders.
- Geen dag of geen uur.
- Hoofdletters, chattaal of emoji's.
- Geen naam onder het bericht.

## 5. Schermafbeeldingen

De beelden bij de stapjes (`assets/stapjes/`, 22 stuks) zijn uitsneden van het werkdocument zoals Google
Documenten het toont (de pdf die Drive van *Ouderbericht* maakt), op ware grootte, met één rood kader (#C5221F,
witte rand erbuiten): `werkdocument/maak_stapjes.py` maakt ze opnieuw. De opdracht in Classroom, de tabbladen van Chrome,
de Speelboom-app en de zes pictogrammen zijn tekeningen in HTML, CSS en SVG (eigen werk, niets van internet).

## 6. Het materiaal opnieuw maken

```bash
cd "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/2026-2027/W08 - Les 04 - MW - Berichten aan ouders/werkdocument" && python3 maak_werkdocumenten.py
```

Verandert het werkdocument, upload dan de nieuwe `.docx` opnieuw en laat `maak_stapjes.py` de beelden maken (uitleg
bovenaan het script). Een concept dat al in Classroom staat: zie `_afspraken/werkdocument-en-bronbestanden.md`
(*Een les aanpassen die al als concept in Classroom staat*).

## 7. Leerplandoelen in je jaaroverzicht

`lesdoelen.json` (klasgroep `3 MW`): `BV2_04.01` kern · `BK2_02.10`, `BV2_02.12`, `BV2_02.07`, `BV2_02.07.02`
ondersteunend · `BV2_04.04` voorbereidend · `BV2_07.03` contextueel. De pre-push hook schrijft ze in
`Leerplandoelen 2026-2027.xlsx`.

## 8. Wat nog moet blijken in de klas

- **Werken ze alleen door?** Komen ze zonder leraar tot en met stap 6, of haken ze af bij stap 4 (15 minuten, het
  eigen bericht)? Hoeveel leerlingen leveren in vóór vrijdag?
- **Vinden ze Inleveren?** Het meest gestelde vraag in les 3 was "Waar moet ik inleveren?". Helpen de quiz in stap 1
  en de tekening in stap 6 (met de knop in een rood kader)? Vragen ze het toch in een privéreactie?
- **Gebruiken ze de AI-hulp of een privéreactie** als ze vastzitten, of zoeken ze niets en geven ze op? (De AI-hulp toont
  wie een gesprek begon; de privéreacties lees je in de opdracht.)
- Werkt de **privéreactie** zoals de klikpaden zeggen (onder **Privéreacties** typen › **Posten**) op het scherm van een
  leerling?
- Lezen ze het **doel vooraf** (*Zoek vier dingen die …*), en vinden ze er ook vier?
- Typen ze netjes in de vakken van het venster *Speelboom-app · Nieuw bericht* (in Google Documenten schuift niets)?
- Begrijpen ze *Kijk na* (stap 5), en zetten ze bij de pictogrammen de juiste letters?
- Klopt de tijd: 50 minuten zonder instructie, met stap 4 van 15 minuten? Hadden velen tijd over voor *Extra*?
  Werkt **Inleveren ongedaan maken** voor opnieuw inleveren?
- **Zijn de dia's nodig?** Blijkt op 26-10 dat veel leerlingen de les niet maakten, geef ze dan in de klas (de dia's
  staan klaar) en schuif les 5 op.
- Een instructiefilmpje van 2 minuten (zie boven): nodig als de eerste stappen veel privéreacties opleveren?
