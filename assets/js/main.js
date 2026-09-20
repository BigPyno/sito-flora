/* CORAR — interazioni sito vetrina */
(function () {
  "use strict";

  /* Email aziendale: unico punto da modificare ------------------------------ */
  var EMAIL = "corar@corar.it";

  /* Abilita le animazioni solo se lo script viene eseguito */
  document.documentElement.classList.add("js");

  /* Ogni pagina parte dall'alto, anche tornando indietro */
  if ("scrollRestoration" in history) history.scrollRestoration = "manual";

  /* Header: ombra allo scroll ---------------------------------------------- */
  var header = document.querySelector(".site-header");
  var onScroll = function () {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 10);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* Menu mobile ------------------------------------------------------------- */
  var burger = document.querySelector(".burger");
  var nav = document.querySelector(".nav");
  var backdrop = document.querySelector(".nav-backdrop");

  function apriMenu(open) {
    if (!nav || !burger) return;
    nav.classList.toggle("is-open", open);
    burger.classList.toggle("is-open", open);
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    burger.setAttribute("aria-label", open ? "Chiudi il menu" : "Apri il menu");
    document.body.classList.toggle("menu-aperto", open);
    if (backdrop) {
      backdrop.hidden = false;
      backdrop.classList.toggle("is-open", open);
    }
    if (!open) {
      /* richiude anche la tendina Prodotti */
      document.querySelectorAll(".has-drop").forEach(function (d) { d.classList.remove("is-open"); });
    }
  }

  if (burger && nav) {
    burger.addEventListener("click", function () {
      apriMenu(!nav.classList.contains("is-open"));
    });
    /* toccando una voce il menu si chiude e la pagina si apre */
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { apriMenu(false); });
    });
  }
  if (backdrop) backdrop.addEventListener("click", function () { apriMenu(false); });

  /* tornando a schermo largo il menu torna in riga */
  var largo = window.matchMedia("(min-width: 881px)");
  var suLargo = function (e) { if (e.matches) apriMenu(false); };
  if (largo.addEventListener) largo.addEventListener("change", suLargo);
  else if (largo.addListener) largo.addListener(suLargo);

  /* Tendina Prodotti -------------------------------------------------------- */
  var drops = document.querySelectorAll(".has-drop");
  var conHover = window.matchMedia("(hover: hover) and (min-width: 881px)").matches;
  drops.forEach(function (d) {
    var btn = d.querySelector(".drop-toggle");
    if (!btn) return;

    if (conHover) {
      /* Desktop: la tendina si apre al passaggio del mouse,
         il clic porta alla pagina Prodotti. */
      d.addEventListener("mouseenter", function () {
        d.classList.add("is-open"); btn.setAttribute("aria-expanded", "true");
      });
      d.addEventListener("mouseleave", function () {
        d.classList.remove("is-open"); btn.setAttribute("aria-expanded", "false");
      });
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        var primo = d.querySelector(".drop a");
        if (primo) window.location.href = primo.getAttribute("href");
      });
      btn.addEventListener("focus", function () { d.classList.add("is-open"); });
    } else {
      /* Touch e mobile: il clic apre e chiude la tendina. */
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        var open = !d.classList.contains("is-open");
        drops.forEach(function (o) { o.classList.remove("is-open"); });
        d.classList.toggle("is-open", open);
        btn.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }
  });
  document.addEventListener("click", function () {
    drops.forEach(function (d) { d.classList.remove("is-open"); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      drops.forEach(function (d) { d.classList.remove("is-open"); });
      apriMenu(false);
      if (burger) burger.focus();
    }
  });

  /* Animazioni a comparsa --------------------------------------------------- */
  var animati = document.querySelectorAll(".reveal, .zoom");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.14, rootMargin: "0px 0px -8% 0px" });
    animati.forEach(function (el) { io.observe(el); });
  } else {
    animati.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* Invio dei moduli ------------------------------------------------------- */
  /* In produzione il modulo viene inviato alla funzione serverless /api/invia,
     che manda la mail all'azienda. Se l'endpoint non c'e' (sito aperto da file,
     anteprima statica, funzione non ancora configurata) si ricade sul client di
     posta con la richiesta gia' compilata: il visitatore non resta mai a mani vuote. */
  var ENDPOINT = "/api/invia";

  var etichette = {
    nome: "Nome e cognome",
    azienda: "Azienda",
    email: "Email",
    telefono: "Telefono",
    oggetto: "Oggetto",
    messaggio: "Messaggio"
  };

  function corpoMail(dati, tipo) {
    var righe = [];
    Object.keys(etichette).forEach(function (k) {
      var v = (dati[k] || "").trim();
      if (v) righe.push(etichette[k] + ": " + v);
    });
    righe.push("");
    righe.push("Consenso al trattamento dei dati: sì (Privacy Policy del sito CORAR).");
    righe.push("Richiesta inviata dal sito — " + tipo);
    return righe.join("\n");
  }

  function apriClientMail(dati, tipo) {
    window.location.href = "mailto:" + EMAIL +
      "?subject=" + encodeURIComponent(tipo) +
      "&body=" + encodeURIComponent(corpoMail(dati, tipo));
  }

  document.querySelectorAll("form[data-mail]").forEach(function (form) {
    var msg = form.querySelector(".form-msg");
    var btn = form.querySelector("button[type=submit]");
    var tipo = form.dataset.mail || "Richiesta dal sito";
    form.setAttribute("novalidate", "novalidate");

    function stato(testo, classe) {
      if (!msg) return;
      msg.textContent = testo;
      msg.className = "form-msg" + (classe ? " " + classe : "");
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      stato("");

      if (!form.checkValidity()) {
        var primo = form.querySelector(":invalid");
        if (primo) primo.focus();
        stato("Controlla i campi obbligatori: nome, email e consenso privacy.", "ko");
        return;
      }

      var dati = {};
      new FormData(form).forEach(function (v, k) { dati[k] = v.toString(); });

      /* trappola antispam: se il campo nascosto è pieno, fingiamo l'invio */
      if ((dati.website || "").trim()) { stato("Richiesta inviata.", "ok"); form.reset(); return; }
      delete dati.website;
      dati.tipo = tipo;

      /* aperto da file:// non c'è nessun endpoint: si va diretti alla mail */
      if (window.location.protocol === "file:") { apriClientMail(dati, tipo); 
        stato("Si sta aprendo il tuo programma di posta con la richiesta già compilata.", "ok"); return; }

      if (btn) { btn.disabled = true; }
      stato("Invio in corso…");

      fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dati)
      }).then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.json().catch(function () { return {}; });
      }).then(function () {
        form.reset();
        stato("Richiesta inviata: ti risponderemo al più presto.", "ok");
      }).catch(function () {
        apriClientMail(dati, tipo);
        stato("Si sta aprendo il tuo programma di posta con la richiesta già compilata: premi Invia per completare.", "ok");
      }).then(function () {
        if (btn) btn.disabled = false;
      });
    });
  });

  /* Anno corrente nel footer ------------------------------------------------ */
  document.querySelectorAll("[data-anno]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
