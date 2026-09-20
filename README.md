# Sito vetrina CORAR S.r.l.

Sito statico generato da uno script Python, con una funzione serverless per l'invio
dei moduli. Nessun CMS: i contenuti si modificano nel generatore e si rigenerano.

## Struttura

```
build.py                      generatore: da qui escono tutte le pagine
sito/                         output pubblicato (rigenerato da build.py)
  index.html  prodotti.html  contatti.html  catalogo.html  privacy.html  cookie.html
  prodotti/*.html             le cinque pagine categoria
  assets/css/style.css        design system e layout
  assets/js/main.js           menu, tendina, animazioni, invio moduli
  assets/img/  assets/icons/  immagini e icone
netlify/functions/invia.mjs   riceve i moduli e manda la mail all'azienda
netlify.toml                  build, redirect /api/*, header di cache e sicurezza
```

## Modificare il sito

I contenuti stanno quasi tutti in `build.py`: recapiti in cima al file, categorie
e sottofamiglie nella lista `CATS`, settori in `SETTORI`, marchi in `BRANDS`.

```bash
python3 build.py     # riscrive tutto sito/
git add -A && git commit -m "…" && git push
```

Il push fa partire il deploy su Netlify. **Non modificare i file dentro `sito/` a mano**:
al primo `build.py` verrebbero sovrascritti.

## Variabili d'ambiente (Netlify → Site settings → Environment variables)

| Variabile | Valore |
|---|---|
| `RESEND_API_KEY` | chiave API di [Resend](https://resend.com) |
| `MAIL_TO` | `corar@corar.it` |
| `MAIL_FROM` | mittente verificato, es. `Sito CORAR <sito@corar.it>` |

Per spedire da un indirizzo `@corar.it` il dominio va verificato su Resend aggiungendo
i record **SPF** e **DKIM** al DNS. Finché non è fatto, si usa un mittente di test:
la risposta arriva comunque all'azienda perché il `reply-to` è l'email del visitatore.

## Come funzionano i moduli

`assets/js/main.js` invia il modulo a `/api/invia` (la funzione serverless).
Se l'endpoint non risponde — sito aperto da file, anteprima statica, variabili non
ancora impostate — ricade automaticamente sul client di posta con la richiesta già
compilata. Il visitatore non resta mai bloccato.

C'è una trappola antispam: un campo nascosto che solo i bot compilano. Se arriva
pieno la richiesta viene scartata silenziosamente.

## Da fare quando serve

- **Registro delle richieste catalogo**: oggi la richiesta arriva solo via mail.
  Per tenerne traccia servono Netlify Blobs o un foglio esterno.
- **PDF del catalogo**: non è nel repo, per scelta. Il brief vieta il download
  diretto: va inviato dall'azienda o servito con un link firmato a scadenza.
- **Segnaposto da sostituire**: la prima foto della sezione storia (lo sticker) —
  si cambia in `build.py`, lista `foto` dentro `home()`; icone dei settori
  aeronautico e ferroviario; testi di Privacy e Cookie Policy.
