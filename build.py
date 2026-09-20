# -*- coding: utf-8 -*-
"""Generatore statico del sito vetrina CORAR."""
import os, html, pathlib

OUT = pathlib.Path(__file__).parent / "sito"
EMAIL = "corar@corar.it"
TEL = "080 532 9208"
TEL_HREF = "+39080532 9208".replace(" ", "")
IND1 = "Via dei Falegnami n. 2"
IND2 = "70026 Modugno (BA)"
WA = "https://wa.me/39080532 9208".replace(" ", "")

AR = ('<svg class="ar" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
      'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
      '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>')

CATS = [
    dict(slug="tubi-oleodinamici", nome="Tubi oleodinamici",
         breve="Tubi per alta e bassa pressione, spiralati, termoplastici e in acciaio, con ghiere, codoli e protezioni per il montaggio completo della linea.",
         hero="Tubi flessibili e rigidi per ogni linea oleodinamica, dalla bassa pressione alle applicazioni spiralate ad alta portata, con tutta la raccorderia a pressare necessaria a chiudere l'assemblaggio in casa.",
         intro=("La famiglia dei tubi oleodinamici è il cuore dell'assortimento CORAR: gomma sintetica con trecce "
                "d'acciaio, versioni compact a raggio di curvatura ridotto, spiralati per le pressioni più elevate, "
                "termoplastici e PTFE per le applicazioni speciali. A magazzino trovi anche il tubo di acciaio per "
                "impianti, le protezioni e tutta la raccorderia a pressare, così da preparare la linea completa "
                "senza passare da più fornitori."),
         sub=[("Alta pressione in gomma", None, ["Tubo 1SN / R1AT e 2SN / R2AT", "Tubo compact 1SC, 2SC e PREMIER"]),
              ("Spiralati", None, ["Tubo spiralato 4SP / 4SH", "4SH COMPACT e R15"]),
              ("Termoplastici e speciali", None, ["Tubo R7 termoplastico", "Tubo per idropulitrice", "Tubo alta temperatura e PTFE"]),
              ("Aspirazione e bassa pressione", None, ["Tubo di aspirazione R4", "Tubo bassa pressione R6", "Tubo carburante"]),
              ("Tubo di acciaio e protezioni", None, ["Tubo di acciaio per impianti oleodinamici", "Protezioni per tubo"]),
              ("Raccordi a pressare", None, ["Ghiere a pressare e fascette stringitubo", "Codoli a pressare e giunzioni tubo/tubo", "Flange, semiflange e guarnizioni"])]),
    dict(slug="nipples-e-adattatori", nome="Nipples e adattatori",
         breve="Nippleria e adattatori in tutte le principali filettature, per collegare fra loro standard diversi senza compromessi di tenuta.",
         hero="Nippleria e adattatori per collegare filettature GAS, JIC, metriche, ORFS e DIN, con le combinazioni di passaggio più richieste sempre disponibili a magazzino.",
         intro=("Quando due componenti parlano standard diversi, serve il pezzo giusto e serve subito. CORAR tiene a "
                "magazzino la nippleria nelle filettature più diffuse e una gamma completa di adattatori di passaggio, "
                "comprese le rondelle di tenuta e gli occhi nelle versioni con tubo corto e lungo."),
         sub=[("Filettature", None, ["GAS - BSPP 60° + rondelle", "JIC 74°", "Metrica 60° + rondelle", "ORFS"]),
              ("Nippleria DIN", None, ["Nippleria DIN nelle misure di serie"]),
              ("Adattatori di passaggio", None, ["GAS/JIC e GAS/METRICO", "GAS/ORFS e GAS/DIN", "GAS/Flange SAE e JIC/ORFS"]),
              ("Occhi", None, ["Occhi GAS e metrici", "Occhi con tubi corti e lunghi"])]),
    dict(slug="innesti-rapidi", nome="Innesti rapidi",
         breve="Innesti a valvola, a faccia piana e per idropulitrice, con i relativi tappi di protezione.",
         hero="Innesti rapidi per collegare e scollegare le linee in sicurezza, nelle versioni a valvola, a faccia piana e dedicate all'idropulitrice.",
         intro=("Gli innesti rapidi sono il punto in cui l'impianto viene aperto e richiuso ogni giorno: per questo "
                "contano la tenuta, la facilità di aggancio e la protezione dalle impurità. La gamma comprende le "
                "versioni a valvola, quelle a faccia piana per i circuiti dove la pulizia è critica, le esecuzioni "
                "per idropulitrice e i tappi di protezione dedicati."),
         sub=[("Innesti a valvola", None, ["Serie a valvola nelle misure di serie"]),
              ("Innesti a faccia piana", None, ["Esecuzione flat face, a ridotta perdita di fluido"]),
              ("Innesti per idropulitrice", None, ["Innesti e accessori dedicati al lavaggio in pressione"]),
              ("Accessori", None, ["Tappi per innesti rapidi", "Giunti girevoli"])]),
    dict(slug="componenti-oleodinamici", nome="Componenti oleodinamici",
         breve="Distributori, pompe, motori orbitali, valvole, strumenti di controllo pressione e accessori per il serbatoio.",
         hero="Distributori, pompe, motori, valvole e strumentazione: i componenti che governano portata, pressione e movimento dell'impianto.",
         intro=("Oltre alla linea, CORAR segue l'impianto nel suo insieme. In questa famiglia rientrano i distributori, "
                "le pompe ad ingranaggi e i moltiplicatori di giri, i motori orbitali e idraulici, l'intera gamma "
                "delle valvole di controllo, gli strumenti per la lettura della pressione e gli accessori per il "
                "serbatoio e lo scambio termico."),
         sub=[("Distributori", None, ["Distributori monoblocco", "Distributori rotativi", "Distributori con regolatore di flusso"]),
              ("Pompe e trasmissione", None, ["Pompe ad ingranaggi gruppo 1 e accessori", "Moltiplicatori di giri"]),
              ("Motori", None, ["Motori orbitali serie OP, OR e OM", "Motori idraulici serie MM"]),
              ("Valvole", None, ["Valvole di blocco e unidirezionali", "Regolatori di flusso, anche prioritari", "Valvole di massima pressione e overcenter"]),
              ("Controllo pressione", None, ["Manometri", "Tubi capillari e raccorderia", "Nippleria per controllo pressione"]),
              ("Serbatoio e scambio termico", None, ["Filtri olio, tappi livello e sfiato", "Scambiatori aria/olio e accessori", "Deviatori, rubinetti e collari fermatubo"])]),
    dict(slug="guarnizioni", nome="Guarnizioni",
         breve="Guarnizioni e raschiatori per cilindri, anelli di tenuta e O-ring in corda metrica e in pollici.",
         hero="Guarnizioni, raschiatori, anelli di tenuta e O-ring per la manutenzione e la revisione dei cilindri oleodinamici.",
         intro=("La tenuta è ciò che tiene in piedi tutto il resto. CORAR gestisce un assortimento ampio di "
                "guarnizioni per cilindri nelle serie più diffuse, raschiatori, anelli di tenuta e O-ring sia in "
                "corda metrica sia in pollici, per rimettere in servizio un cilindro senza attese."),
         sub=[("Guarnizioni per cilindri", None, ["Serie TTI, TTU, TTS e TSE", "Serie TPM, PDE, TDE e PSE", "Serie GIR, GER, TTQ e TTW"]),
              ("Raschiatori", None, ["Serie GHK", "Serie GHP", "Serie GPA"]),
              ("Anelli di tenuta", None, ["Serie AGI", "Serie AGE"]),
              ("O-ring", None, ["O-ring con corda in pollici", "O-ring con corda metrica"])]),
]

SETTORI = [("1-05.svg", "Agricolo"), ("1-06.svg", "Industriale"), ("1-07.svg", "Eolico"),
           ("1-08.svg", "Nautico"), ("1-09.svg", "Automotive")]

BRANDS = [("omt", "OMT Group"), ("op", "O+P"), ("meta", "Meta Hydraulic"),
          ("marchesini", "Marchesini Group"), ("guarnitec", "Guarnitec"),
          ("vitillo", "Vitillo"), ("stauff", "Stauff"), ("stucchi", "Stucchi")]


def head(titolo, descr, p=""):
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titolo}</title>
<meta name="description" content="{descr}">
<meta property="og:title" content="{titolo}">
<meta property="og:description" content="{descr}">
<meta property="og:type" content="website">
<link rel="icon" href="{p}assets/img/logo-corar.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/style.css">
</head>
<body>
"""


def header(active, p=""):
    def cur(name):
        return ' aria-current="page"' if active == name else ""
    voci = "".join(
        f'<a href="{p}prodotti/{c["slug"]}.html">{c["nome"]}</a>' for c in CATS)
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="{p}index.html" aria-label="CORAR - home">
      <img src="{p}assets/img/logo-corar.png" alt="CORAR - Componenti oleodinamici" width="240" height="51">
    </a>
    <button class="burger" type="button" aria-label="Apri il menu" aria-expanded="false"><span></span></button>
    <nav class="nav" aria-label="Menu principale">
      <a href="{p}index.html"{cur('home')}>Home</a>
      <div class="has-drop">
        <button class="drop-toggle" type="button" aria-expanded="false">Prodotti
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"
               stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="drop">
          <a href="{p}prodotti.html"><strong>Tutte le categorie</strong></a>
          {voci}
        </div>
      </div>
      <a href="{p}contatti.html"{cur('contatti')}>Contatti</a>
      <div class="nav-contatti">
        <a href="tel:{TEL_HREF}"><img src="{p}assets/icons/1-15.svg" alt="" width="18" height="18">Chiama</a>
        <a href="mailto:{EMAIL}"><img src="{p}assets/icons/1-16.svg" alt="" width="18" height="18">Email</a>
      </div>
    </nav>
  </div>
</header>
<div class="nav-backdrop" hidden></div>
"""


def footer(p=""):
    voci = "".join(f'<li><a href="{p}prodotti/{c["slug"]}.html">{c["nome"]}</a></li>' for c in CATS)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img class="footer-logo" src="{p}assets/img/logo-corar-bianco.png" alt="CORAR" width="168" height="36">
        <p class="footer-about">Componenti oleodinamici di qualità per l'industria, l'agricoltura e la
          movimentazione. Affidabilità, competenza e passione dal 1990.</p>
      </div>
      <div>
        <h5>Prodotti</h5>
        <ul>{voci}</ul>
      </div>
      <div>
        <h5>Navigazione</h5>
        <ul>
          <li><a href="{p}index.html">Home</a></li>
          <li><a href="{p}prodotti.html">Prodotti</a></li>
          <li><a href="{p}catalogo.html">Richiedi il catalogo</a></li>
          <li><a href="{p}contatti.html">Contatti</a></li>
        </ul>
      </div>
      <div>
        <h5>Contatti</h5>
        <ul class="footer-cont">
          <li><img src="{p}assets/icons/1-15.svg" alt=""><a href="tel:{TEL_HREF}">{TEL}</a></li>
          <li><img src="{p}assets/icons/1-16.svg" alt=""><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><img src="{p}assets/icons/1-17.svg" alt=""><span>{IND1}<br>{IND2}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-anno>2026</span> CORAR S.r.l. — Tutti i diritti riservati</span>
      <nav>
        <a href="{p}privacy.html">Privacy Policy</a>
        <a href="{p}cookie.html">Cookie Policy</a>
      </nav>
    </div>
  </div>
</footer>
<script src="{p}assets/js/main.js"></script>
</body>
</html>
"""


def form_catalogo(p="", chiaro=False):
    """Modulo richiesta catalogo: invia una mail, non scarica nulla."""
    return f"""<form data-mail="Richiesta catalogo CORAR" novalidate>
    <div class="hp" aria-hidden="true">
      <label>Non compilare questo campo
        <input name="website" type="text" tabindex="-1" autocomplete="off">
      </label>
    </div>
  <div class="form-grid">
    <div class="field"><label for="c-nome">Nome e cognome *</label>
      <input id="c-nome" name="nome" type="text" required autocomplete="name" placeholder="Mario Rossi"></div>
    <div class="field"><label for="c-azienda">Azienda</label>
      <input id="c-azienda" name="azienda" type="text" autocomplete="organization" placeholder="Ragione sociale"></div>
    <div class="field"><label for="c-email">Email *</label>
      <input id="c-email" name="email" type="email" required autocomplete="email" placeholder="nome@azienda.it"></div>
    <div class="field"><label for="c-tel">Telefono</label>
      <input id="c-tel" name="telefono" type="tel" autocomplete="tel" placeholder="080 000 0000"></div>
    <div class="field field--full"><label for="c-msg">Messaggio (facoltativo)</label>
      <textarea id="c-msg" name="messaggio" rows="3" placeholder="Di quali categorie hai bisogno?"></textarea></div>
    <div class="field field--full">
      <label class="consenso"><input type="checkbox" name="privacy" required>
        <span>Ho letto la <a href="{p}privacy.html">Privacy Policy</a> e acconsento al trattamento dei dati per essere ricontattato. *</span>
      </label>
    </div>
    <div class="field field--full">
      <button class="btn btn--rosso btn--full" type="submit">Invia la richiesta {AR}</button>
    </div>
  </div>
  <p class="form-msg" role="status"></p>
</form>"""


def sezione_catalogo(p="", chiaro=False):
    cls = "section catalogo catalogo--chiaro" if chiaro else "section catalogo"
    return f"""<section class="{cls}" id="catalogo">
  <div class="wrap catalogo-grid">
    <div class="book reveal">
      <img src="{p}assets/img/catalogo-cover.webp" alt="Copertina del catalogo prodotti CORAR"
           width="700" height="860" loading="lazy">
    </div>
    <div class="reveal" data-delay="1">
      <p class="kicker {'kicker--blu' if chiaro else 'kicker--chiaro'}">Catalogo CORAR</p>
      <h2>Richiedi il catalogo completo</h2>
      <p>Compila il modulo e il nostro ufficio ti invierà il catalogo con tutte le categorie di prodotto,
        le schede tecniche e le misure disponibili a magazzino.</p>
      {form_catalogo(p, chiaro)}
    </div>
  </div>
</section>"""


def fascia_vantaggi(p=""):
    v = [("1-10.svg", "Magazzino sempre fornito", "Oltre 500 m² di disponibilità a magazzino per migliaia di prodotti sempre pronti alla spedizione."),
         ("1-14.svg", "Qualità garantita", "Solo prodotti dei migliori marchi del settore oleodinamico, selezionati e testati."),
         ("1-12.svg", "Supporto tecnico", "Consulenza specializzata per individuare il componente più adatto all'applicazione."),
         ("1-11.svg", "Spedizioni rapide", "Consegne in tutta Italia ed Europa, sicure e puntuali, con i migliori corrieri.")]
    cards = "".join(
        f'<div class="vantaggio reveal" data-delay="{i}"><img src="{p}assets/icons/{ic}" alt="" width="42" height="42" loading="lazy">'
        f'<strong>{t}</strong><p>{d}</p></div>' for i, (ic, t, d) in enumerate(v))
    return f'<section class="section section--grigio"><div class="wrap vantaggi">{cards}</div></section>'


# --------------------------------------------------------------------------- HOME
def home():
    stats = [("1-01.svg", "30+", "Anni di esperienza"), ("1-02.svg", "10.000+", "Prodotti disponibili"),
             ("1-03.svg", "500 m²", "Magazzino fornito"), ("1-04.svg", "Spedizioni", "in tutta Italia")]
    stats_html = "".join(
        f'<div class="stat zoom" data-delay="{i}"><img src="assets/icons/{ic}" alt="" width="46" height="46">'
        f'<strong>{n}</strong><span>{t}</span></div>' for i, (ic, n, t) in enumerate(stats))

    brands_html = "".join(
        f'<span class="brand"><img src="assets/img/brand-{sl}.webp" alt="{n}" loading="lazy" height="46"></span>'
        for sl, n in BRANDS * 2)

    timeline = [("1990", "Nasce CORAR con l'obiettivo di fornire componenti oleodinamici di qualità."),
                ("2000", "Crescita e ampliamento del magazzino per soddisfare le nuove richieste del mercato."),
                ("2010", "Innovazione e nuove partnership con i migliori marchi del settore."),
                ("Oggi", "Terza generazione e uno sguardo rivolto al futuro, con la stessa passione di sempre.")]
    tl_html = "".join(
        f'<div class="tl-item reveal" data-delay="{i}"><strong>{a}</strong><p>{t}</p></div>'
        for i, (a, t) in enumerate(timeline))
    # Le quattro foto seguono l'ordine della timeline qui sotto: 1990, 2000, 2010, Oggi.
    # Per sostituire lo sticker con una foto vera basta cambiare il primo file di questa lista.
    foto = [("storia-1990.webp", "Gli inizi di CORAR"),
            ("storia-2000.webp", "Il magazzino CORAR"),
            ("storia-2010.webp", "Tubi oleodinamici pronti alla spedizione"),
            ("storia-oggi.webp", "La sede CORAR a Modugno")]
    foto_html = "".join(
        f'<div class="foto-st reveal" data-delay="{i}">'
        f'<img src="assets/img/{f}" alt="{a}" width="560" height="700" loading="lazy"></div>'
        for i, (f, a) in enumerate(foto))

    settori_html = "".join(
        f'<div class="settore reveal" data-delay="{i%4}"><img src="assets/icons/{ic}" alt="" width="54" height="54" loading="lazy">'
        f'<span>{n}</span></div>' for i, (ic, n) in enumerate(SETTORI))
    settori_html += '<div class="settore settore--altri reveal" data-delay="1"><span>E molti<br>altri settori</span></div>'

    def cat_card(c, big=False):
        cls = "cat cat--big" if big else "cat"
        return f"""<a class="{cls} reveal" href="prodotti/{c['slug']}.html">
      <div class="cat-body"><h3>{c['nome']}</h3><span class="link-rosso">Scopri di più {AR}</span></div>
      <div class="cat-img"><img src="assets/img/{c['slug']}.webp" alt="{c['nome']} CORAR" loading="lazy"></div>
    </a>"""

    cat_html = cat_card(CATS[0], True) + "".join(cat_card(c) for c in CATS[1:])

    plus = [("1-10.svg", "Magazzino sempre fornito", "Oltre 500 m² di disponibilità a magazzino per migliaia di prodotti sempre pronti."),
            ("1-11.svg", "Spedizioni veloci", "Collaboriamo con i migliori corrieri per consegne rapide in tutta Italia ed Europa."),
            ("1-12.svg", "Supporto tecnico", "Il nostro team è sempre disponibile per consulenze e assistenza dedicata."),
            ("1-13.svg", "Esperienza consolidata", "Da oltre trent'anni al fianco di aziende e professionisti dell'oleodinamica.")]
    # Le icone sono già nel rosso del marchio (#e20613): nessun filtro, nessuna approssimazione.
    plus_html = "".join(
        f'<div class="plus reveal" data-delay="{i}">'
        f'<img src="assets/icons/{ic}" alt="" width="80" height="80" loading="lazy">'
        f'<strong>{t}</strong><p>{d}</p></div>' for i, (ic, t, d) in enumerate(plus))

    return (head("CORAR S.r.l. | Componenti oleodinamici per ogni settore industriale",
                 "CORAR fornisce tubi oleodinamici, nipples e adattatori, innesti rapidi, componenti e guarnizioni. "
                 "Oltre 30 anni di esperienza, magazzino fornito e spedizioni in tutta Italia.")
            + header("home") + f"""
<main>
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="kicker">Componenti oleodinamici dal 1990</p>
        <h1>Componenti oleodinamici per ogni settore industriale</h1>
        <p class="lead">Da oltre trent'anni CORAR fornisce componenti oleodinamici, assistenza tecnica e soluzioni
          affidabili per impianti e applicazioni industriali. Tubi, raccordi, innesti rapidi, componenti e
          guarnizioni: un'ampia gamma, supporto tecnico e spedizioni in tutta Italia.</p>
        <div class="hero-actions">
          <a class="btn btn--rosso" href="catalogo.html">Richiedi il catalogo {AR}</a>
          <a class="btn btn--chiaro" href="contatti.html">Contattaci</a>
        </div>
      </div>
      <div class="hero-media">
        <span class="hero-arc" aria-hidden="true"></span>
        <div class="hero-disc zoom">
          <img src="assets/img/hero-tubi.webp" alt="Tubi oleodinamici con raccordi CORAR" width="1000" height="1000" fetchpriority="high">
        </div>
        <span class="hero-dot" aria-hidden="true"></span>
      </div>
    </div>
  </section>

  <div class="wrap stats-wrap">
    <div class="stats">{stats_html}</div>
  </div>

  <section class="brands">
    <div class="wrap"><p class="brands-title">Trattiamo i migliori marchi</p></div>
    <div class="marquee"><div class="marquee-track">{brands_html}</div></div>
  </section>

  <section class="section section--grigio" id="storia">
    <div class="wrap storia-grid">
      <div class="reveal">
        <p class="kicker">La nostra storia</p>
        <h2>Oltre trent'anni di crescita e passione</h2>
        <p>CORAR S.r.l. è un'azienda familiare che opera da oltre trent'anni nella commercializzazione di componenti
          oleodinamici. La famiglia Dell'Acqua, titolare e amministratrice dell'azienda, è giunta alla terza
          generazione con la stessa passione per il lavoro e la stessa correttezza di sempre.</p>
        <p>Investiamo costantemente in risorse e nella formazione del nostro team per garantire competenza tecnica,
          affidabilità e un supporto sempre più vicino alle esigenze dei clienti.</p>
      </div>
      <div>
        <div class="storia-foto">{foto_html}</div>
        <div class="timeline">{tl_html}</div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head center reveal">
        <p class="kicker">I settori che serviamo</p>
        <h2>Soluzioni affidabili per ogni settore</h2>
      </div>
      <div class="wrap settori" style="width:100%">{settori_html}</div>
    </div>
  </section>

  <section class="section section--grigio">
    <div class="wrap">
      <div class="section-head center reveal">
        <p class="kicker">Le nostre categorie di prodotto</p>
        <h2>Un'ampia gamma di componenti oleodinamici</h2>
      </div>
      <div class="cat-grid">{cat_html}</div>
    </div>
  </section>

  <section class="section dark">
    <div class="wrap dark-grid">
      <div class="dark-title reveal">
        <p class="kicker">Perché scegliere</p>
        <img src="assets/img/logo-corar-bianco.png" alt="CORAR" width="260" height="56">
        <i></i>
      </div>
      {plus_html}
    </div>
  </section>

  {sezione_catalogo()}
</main>
""" + footer())


# ----------------------------------------------------------------------- PRODOTTI
def prodotti():
    def card(c, big=False):
        return f"""<a class="{'cat cat--big' if big else 'cat'} reveal" href="prodotti/{c['slug']}.html">
      <div class="cat-body"><h3>{c['nome']}</h3><span class="link-rosso">Scopri i prodotti {AR}</span></div>
      <div class="cat-img"><img src="assets/img/{c['slug']}.webp" alt="{c['nome']} CORAR" loading="lazy"></div>
    </a>"""
    cards = card(CATS[0], True) + "".join(card(c) for c in CATS[1:])

    punti = [("1-01.svg", "Prodotti selezionati<br>dei migliori marchi"),
             ("1-11.svg", "Disponibilità<br>e spedizioni rapide"),
             ("1-12.svg", "Supporto tecnico<br>specializzato")]
    punti_html = "".join(
        f'<div class="hero-point"><img src="assets/icons/{ic}" alt="" width="34" height="34"><span>{t}</span></div>'
        for ic, t in punti)

    return (head("Prodotti | CORAR S.r.l. — Componenti oleodinamici",
                 "Tutte le categorie di componenti oleodinamici CORAR: tubi, nipples e adattatori, innesti rapidi, "
                 "componenti oleodinamici e guarnizioni.")
            + header("prodotti") + f"""
<main>
  <section class="p-hero">
    <div class="wrap p-hero-grid">
      <div>
        <p class="kicker">I nostri prodotti</p>
        <h1>Una gamma completa di componenti oleodinamici</h1>
        <p class="lead">Soluzioni affidabili e di qualità per garantire massima efficienza, sicurezza e continuità
          operativa in ogni settore industriale.</p>
        <div class="hero-points">{punti_html}</div>
      </div>
      <div class="hero-media">
        <div class="hero-disc zoom">
          <img src="assets/img/nipples-e-adattatori.webp" alt="Nipples e adattatori CORAR" width="760" height="350">
        </div>
        <span class="hero-dot" aria-hidden="true"></span>
      </div>
    </div>
  </section>

  <section class="section section--grigio">
    <div class="wrap">
      <div class="section-head center reveal">
        <p class="kicker">Categorie prodotto</p>
        <h2>Scopri tutte le nostre categorie</h2>
        <p>Una gamma completa di componenti oleodinamici per ogni esigenza applicativa.
          Seleziona la categoria di tuo interesse per vedere le principali sottofamiglie.</p>
      </div>
      <div class="cat-grid">{cards}</div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="nota reveal">
        <div class="nota-testo">
          <img src="assets/icons/1-12.svg" alt="" width="44" height="44" loading="lazy">
          <div>
            <h3>Non trovi quello che cerchi?</h3>
            <p>Contattaci per ricevere assistenza nella scelta del componente più adatto alle tue esigenze:
              il nostro team è a tua disposizione.</p>
          </div>
        </div>
        <a class="btn btn--outline" href="contatti.html">Richiedi informazioni {AR}</a>
      </div>
    </div>
  </section>

  {fascia_vantaggi()}
</main>
""" + footer())


# ------------------------------------------------------------------ PAGINA CATEGORIA
def categoria(c):
    p = "../"
    altre = [x for x in CATS if x["slug"] != c["slug"]]
    altre_html = "".join(
        f'<a class="altra reveal" data-delay="{i}" href="{x["slug"]}.html">'
        f'<img src="{p}assets/img/{x["slug"]}.webp" alt="{x["nome"]}" loading="lazy">'
        f'<strong>{x["nome"]}</strong><span class="link-rosso" style="color:var(--blu)">Vedi la categoria {AR}</span></a>'
        for i, x in enumerate(altre))

    sub_html = "".join(
        '<div class="sotto reveal" data-delay="%d"><h4>%s</h4><ul>%s</ul></div>' % (
            i % 3, t, "".join(f"<li>{v}</li>" for v in voci))
        for i, (t, _, voci) in enumerate(c["sub"]))

    return (head(f'{c["nome"]} | CORAR S.r.l.', c["breve"], p)
            + header("prodotti", p) + f"""
<main>
  <section class="p-hero">
    <div class="wrap">
      <p class="breadcrumb"><a href="{p}index.html">Home</a><span>/</span><a href="{p}prodotti.html">Prodotti</a><span>/</span>{c['nome']}</p>
    </div>
    <div class="wrap p-hero-grid">
      <div>
        <p class="kicker">Categoria prodotto</p>
        <h1>{c['nome']}</h1>
        <p class="lead">{c['hero']}</p>
      </div>
      <div class="p-hero-img zoom">
        <img src="{p}assets/img/{c['slug']}.webp" alt="{c['nome']} CORAR" width="900" height="650">
      </div>
    </div>
  </section>

  <section class="section section--grigio">
    <div class="wrap">
      <div class="section-head reveal">
        <p class="kicker">La categoria in breve</p>
        <h2>{c['nome']}: cosa trovi a magazzino</h2>
        <p>{c['intro']}</p>
      </div>
      <div class="sotto-grid">{sub_html}</div>
      <p class="small reveal" style="margin-top:26px;color:var(--testo-soft)">
        Misure, codici e dati tecnici completi sono riportati nel catalogo CORAR:
        <a href="{p}catalogo.html" style="color:var(--blu);font-weight:500">richiedilo compilando il modulo</a>.
      </p>
    </div>
  </section>

  <section class="specialisti">
    <div class="wrap">
      <p class="kicker kicker--chiaro reveal">Hai un progetto in corso?</p>
      <h2 class="reveal">Parla con i nostri specialisti</h2>
      <p class="reveal">Ti aiutiamo a trovare la soluzione più adatta alle tue esigenze, con un servizio rapido
        e una consulenza personalizzata.</p>
      <p class="reveal" style="margin:0">
        <a class="btn btn--rosso" href="{p}contatti.html">Richiedi informazioni {AR}</a>
      </p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head center reveal">
        <p class="kicker">Continua a esplorare</p>
        <h2>Le altre categorie</h2>
      </div>
      <div class="altre">{altre_html}</div>
      <p class="center reveal" style="margin:36px 0 0">
        <a class="btn btn--outline" href="{p}catalogo.html">Richiedi il catalogo completo {AR}</a>
      </p>
    </div>
  </section>
</main>
""" + footer(p))


# ----------------------------------------------------------------------- CONTATTI
def contatti():
    cont = [("1-15.svg", "Telefono", f'<a href="tel:{TEL_HREF}">{TEL}</a>'),
            ("1-16.svg", "Email", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
            ("1-17.svg", "Indirizzo", f"<p>{IND1}<br>{IND2}</p>"),
            ("1-18.svg", "WhatsApp", f'<a href="{WA}">Scrivici su WhatsApp</a>')]
    cont_html = "".join(
        f'<div class="contatto zoom" data-delay="{i}"><img src="assets/icons/{ic}" alt="" width="40" height="40">'
        f'<div><span>{t}</span>{v}</div></div>' for i, (ic, t, v) in enumerate(cont))

    return (head("Contatti | CORAR S.r.l. — Componenti oleodinamici",
                 f"Contatta CORAR S.r.l. — {IND1}, {IND2}. Telefono {TEL}, email {EMAIL}.")
            + header("contatti") + f"""
<main>
  <section class="p-hero">
    <div class="wrap">
      <p class="kicker reveal">Contatti</p>
      <h1 class="reveal">Siamo a tua disposizione</h1>
      <p class="lead reveal">Contattaci per ricevere informazioni, richiedere un preventivo o il nostro catalogo.
        Il nostro team è pronto ad aiutarti a trovare la soluzione più adatta alle tue esigenze.</p>
    </div>
  </section>

  <section style="padding-bottom:clamp(50px,6vw,80px)">
    <div class="wrap">
      <div class="contatti-card">{cont_html}</div>
    </div>
  </section>

  <section class="section section--grigio">
    <div class="wrap mappa-grid">
      <div class="reveal">
        <p class="kicker">Dove siamo</p>
        <h2>Vieni a trovarci</h2>
        <p>La nostra sede si trova a Modugno (BA), facilmente raggiungibile dalle principali vie di comunicazione.</p>
        <a class="btn btn--chiaro" href="https://www.google.com/maps/search/?api=1&amp;query={IND1.replace(' ', '+')}+{IND2.replace(' ', '+')}"
           target="_blank" rel="noopener">Indicazioni stradali {AR}</a>
      </div>
      <div class="mappa reveal" data-delay="1">
        <iframe title="Mappa della sede CORAR a Modugno" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps?q={IND1.replace(' ', '+')},+{IND2.replace(' ', '+')}&amp;output=embed"></iframe>
      </div>
    </div>
  </section>

  {sezione_catalogo("", chiaro=True)}
  {fascia_vantaggi()}
</main>
""" + footer())


# ----------------------------------------------------------------------- CATALOGO
def catalogo():
    return (head("Richiedi il catalogo | CORAR S.r.l.",
                 "Richiedi il catalogo completo dei componenti oleodinamici CORAR: compila il modulo e l'ufficio "
                 "ti invierà il catalogo via email.")
            + header("catalogo") + f"""
<main>
  <section class="p-hero" style="padding-bottom:0">
    <div class="wrap" style="max-width:760px;text-align:center">
      <p class="kicker reveal">Catalogo CORAR</p>
      <h1 class="reveal">Il catalogo completo, su richiesta</h1>
      <p class="lead reveal" style="margin-inline:auto">Il catalogo raccoglie tutte le famiglie di prodotto, le misure
        e i dati tecnici. Compila il modulo: la richiesta arriva direttamente all'ufficio CORAR, che provvederà
        a inviarti il catalogo.</p>
    </div>
  </section>

  {sezione_catalogo("", chiaro=True)}
  {fascia_vantaggi()}
</main>
""" + footer())


# ------------------------------------------------------------------------- LEGALI
def legale(titolo, intro):
    return (head(f"{titolo} | CORAR S.r.l.", intro)
            + header("") + f"""
<main>
  <section class="section">
    <div class="wrap" style="max-width:820px">
      <p class="kicker">Informativa</p>
      <h1 style="margin-bottom:22px">{titolo}</h1>
      <p class="lead">{intro}</p>
      <div class="nota" style="margin-top:34px">
        <div class="nota-testo">
          <img src="assets/icons/1-16.svg" alt="" width="44" height="44">
          <div>
            <h3>Testo da fornire</h3>
            <p>Questa pagina è predisposta graficamente ma il testo dell'informativa deve essere fornito
              dall'azienda o dal consulente privacy, con titolare del trattamento, finalità, base giuridica,
              tempi di conservazione e diritti dell'interessato.</p>
          </div>
        </div>
        <a class="btn btn--outline" href="contatti.html">Contatti {AR}</a>
      </div>
    </div>
  </section>
</main>
""" + footer())


def write(path, content):
    f = OUT / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content, encoding="utf-8")
    print("scritto", path, len(content))


if __name__ == "__main__":
    write("index.html", home())
    write("prodotti.html", prodotti())
    write("contatti.html", contatti())
    write("catalogo.html", catalogo())
    write("privacy.html", legale("Privacy Policy",
          "Informativa sul trattamento dei dati personali raccolti tramite i moduli di contatto e di richiesta catalogo del sito CORAR."))
    write("cookie.html", legale("Cookie Policy",
          "Informativa sui cookie tecnici e di terze parti utilizzati dal sito CORAR, inclusa la mappa incorporata di Google Maps."))
    for c in CATS:
        write(f"prodotti/{c['slug']}.html", categoria(c))
