/**
 * Invio dei moduli del sito CORAR.
 *
 * Riceve il JSON dei form (contatti e richiesta catalogo), controlla i dati
 * e inoltra la richiesta all'indirizzo dell'azienda tramite Resend.
 *
 * Variabili d'ambiente da impostare su Netlify (Site settings → Environment variables):
 *   RESEND_API_KEY   chiave API di Resend
 *   MAIL_TO          destinatario, es. corar@corar.it
 *   MAIL_FROM        mittente verificato su Resend, es. "Sito CORAR <sito@corar.it>"
 */

const ETICHETTE = {
  nome: "Nome e cognome",
  azienda: "Azienda",
  email: "Email",
  telefono: "Telefono",
  oggetto: "Oggetto",
  messaggio: "Messaggio",
};

const LIMITI = { nome: 120, azienda: 160, email: 200, telefono: 40, oggetto: 160, messaggio: 4000 };

const json = (dati, status = 200) =>
  new Response(JSON.stringify(dati), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });

const pulisci = (v, max) => String(v ?? "").replace(/\s+/g, " ").trim().slice(0, max);
const emailValida = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);

export default async (req) => {
  if (req.method !== "POST") return json({ errore: "Metodo non consentito" }, 405);

  let corpo;
  try {
    corpo = await req.json();
  } catch {
    return json({ errore: "Richiesta non valida" }, 400);
  }

  // Trappola antispam: il campo è nascosto, un umano non lo compila mai.
  // Rispondiamo ok per non far capire al bot che è stato scartato.
  if (pulisci(corpo.website, 200)) return json({ ok: true });

  const dati = {};
  for (const campo of Object.keys(ETICHETTE)) dati[campo] = pulisci(corpo[campo], LIMITI[campo]);

  if (!dati.nome || !emailValida(dati.email)) {
    return json({ errore: "Nome ed email sono obbligatori" }, 422);
  }
  if (!corpo.privacy) {
    return json({ errore: "Manca il consenso al trattamento dei dati" }, 422);
  }

  const tipo = pulisci(corpo.tipo, 120) || "Richiesta dal sito";
  const destinatario = process.env.MAIL_TO;
  const mittente = process.env.MAIL_FROM;
  const chiave = process.env.RESEND_API_KEY;

  if (!chiave || !destinatario || !mittente) {
    console.error("Configurazione incompleta: controlla RESEND_API_KEY, MAIL_TO, MAIL_FROM");
    return json({ errore: "Servizio di invio non configurato" }, 500);
  }

  const righe = Object.entries(ETICHETTE)
    .filter(([campo]) => dati[campo])
    .map(([campo, etichetta]) => `${etichetta}: ${dati[campo]}`);
  righe.push("", "Consenso al trattamento dei dati: sì (Privacy Policy del sito CORAR).", `Origine: ${tipo}`);

  const risposta = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${chiave}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: mittente,
      to: [destinatario],
      reply_to: dati.email,
      subject: `${tipo} — ${dati.nome}${dati.azienda ? " (" + dati.azienda + ")" : ""}`,
      text: righe.join("\n"),
    }),
  });

  if (!risposta.ok) {
    console.error("Resend ha risposto", risposta.status, await risposta.text());
    return json({ errore: "Invio non riuscito" }, 502);
  }

  return json({ ok: true });
};
