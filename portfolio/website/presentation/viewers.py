"""Full-screen slide viewer and presenter view (same viewer as the Helper Jobs deck)."""
import html, json

STYLE = """
:root{--bg:#1F1915;--ink:#F3ECE1;--muted:#CDBFA9;--rust:#E3B98F;--bar:rgba(31,25,21,.92)}
*{box-sizing:border-box}html,body{margin:0;height:100%;background:var(--bg);color:var(--ink);font:500 16px/1.4 system-ui,-apple-system,'Segoe UI',sans-serif;overflow:hidden}
.stage{position:fixed;inset:0 0 56px 0;display:flex;align-items:center;justify-content:center;padding:12px}
.stage img{max-width:100%;max-height:100%;object-fit:contain;display:block;box-shadow:0 8px 40px rgba(0,0,0,.45);user-select:none;-webkit-user-drag:none}
body.full .stage{inset:0;padding:0}body.full .stage img{box-shadow:none}
.bar{position:fixed;left:0;right:0;bottom:0;height:56px;background:var(--bar);display:flex;align-items:center;gap:8px;padding:0 12px;transition:opacity .25s}
body.full .bar{opacity:0}body.full.show-bar .bar{opacity:1}
.bar button,.bar a{min-height:44px;min-width:44px;padding:0 14px;border:1px solid #5A4A3E;background:transparent;color:var(--ink);font:inherit;border-radius:6px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;text-decoration:none}
.bar button:hover,.bar a:hover{border-color:var(--rust)}
:focus-visible{outline:3px solid var(--rust);outline-offset:2px}
.count{min-width:72px;text-align:center;color:var(--muted);font-variant-numeric:tabular-nums}
.spacer{flex:1}
.notes{position:fixed;left:0;right:0;bottom:56px;max-height:34vh;overflow:auto;background:#2B231D;border-top:2px solid var(--rust);padding:14px 20px;font:400 18px/1.5 Georgia,serif;display:none}
body.notes-on .notes{display:block}body.notes-on .stage{bottom:calc(56px + 34vh)}
body.full .notes{display:none!important}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.hint{color:var(--muted);font-size:13px}
.bar button,.bar a{white-space:nowrap}.short{display:none}
.bar a .label{display:inline}
@media (max-width:640px){.hint,.label,.bar a .label,#notes-toggle{display:none}.short{display:inline}.count{min-width:52px}.bar button,.bar a{padding:0 8px}.bar{gap:4px}.bar{gap:6px;padding:0 8px}.bar button,.bar a{padding:0 10px}}
"""

SCRIPT = """
(function(){
  var items = ITEMS, i = 0, kind = KIND;
  var img = document.getElementById('view'), count = document.getElementById('count'), live = document.getElementById('live'), notes = document.getElementById('notes');
  var m = /[#&]?(\\d+)$/.exec(location.hash); if (m) i = Math.min(items.length - 1, Math.max(0, +m[1] - 1));
  // Load the neighbours early so moving between pages is instant.
  items.forEach(function(item){ var pre = new Image(); pre.src = item.src; });
  // The presenter window and this one stay on the same slide.
  var channel = ('BroadcastChannel' in window) ? new BroadcastChannel('bb-present') : null, quiet = false;
  if (channel) channel.onmessage = function(e){ if (e.data && typeof e.data.slide === 'number' && e.data.slide !== i) { quiet = true; show(e.data.slide); quiet = false; } if (e.data && e.data.hello) channel.postMessage({slide: i}); };
  function show(n){
    i = Math.min(items.length - 1, Math.max(0, n));
    img.src = items[i].src; img.alt = items[i].alt;
    count.textContent = (i + 1) + ' / ' + items.length;
    live.textContent = kind + ' ' + (i + 1) + ' of ' + items.length + '. ' + items[i].alt;
    history.replaceState(null, '', '#' + (i + 1));
    if (channel && !quiet) channel.postMessage({slide: i});
    document.getElementById('prev').disabled = i === 0; document.getElementById('next').disabled = i === items.length - 1;
  }
  function full(){
    var el = document.documentElement;
    if (!document.fullscreenElement) { (el.requestFullscreen || el.webkitRequestFullscreen || function(){}).call(el); }
    else { (document.exitFullscreen || document.webkitExitFullscreen).call(document); }
  }
  document.addEventListener('fullscreenchange', function(){ document.body.classList.toggle('full', !!document.fullscreenElement); var on = !!document.fullscreenElement; document.getElementById('full-label').textContent = on ? 'Exit full screen' : 'Full screen'; document.getElementById('full-short').textContent = on ? '✕' : '⛶'; document.getElementById('full').setAttribute('aria-label', on ? 'Exit full screen' : 'Full screen'); });
  document.getElementById('prev').onclick = function(){ show(i - 1); };
  document.getElementById('next').onclick = function(){ show(i + 1); };
  document.getElementById('full').onclick = full;
  // Speaker notes open in their own window, for the laptop screen, so they never show on the projector.
  var notesBtn = document.getElementById('notes-toggle');
  if (notesBtn) notesBtn.onclick = function(){ window.open('presenter.html#' + (i + 1), 'bb-presenter', 'width=1280,height=800'); };
  document.addEventListener('keydown', function(e){
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    var k = e.key;
    // Space and Enter on a focused button press that button; they never also move the slides.
    if ((k === ' ' || k === 'Enter') && e.target && e.target.closest && e.target.closest('button, a')) return;
    if (k === 'ArrowRight' || k === 'PageDown' || k === ' ' || k === 'Enter') { e.preventDefault(); show(i + 1); }
    else if (k === 'ArrowLeft' || k === 'PageUp' || k === 'Backspace') { e.preventDefault(); show(i - 1); }
    else if (k === 'Home') { e.preventDefault(); show(0); }
    else if (k === 'End') { e.preventDefault(); show(items.length - 1); }
    else if (k === 'f' || k === 'F') { full(); }
    else if ((k === 'n' || k === 'N') && notesBtn) { notesBtn.click(); }
  });
  // Click the right two thirds to go forward, the left third to go back. Swipe on phones.
  document.querySelector('.stage').addEventListener('click', function(e){ if (e.clientX < innerWidth / 3) show(i - 1); else show(i + 1); });
  var x0 = null; document.addEventListener('touchstart', function(e){ x0 = e.touches[0].clientX; }, {passive: true});
  document.addEventListener('touchend', function(e){ if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1)); x0 = null; });
  // In full screen the bar hides; moving the mouse brings it back for a moment.
  var t = null; document.addEventListener('mousemove', function(){ document.body.classList.add('show-bar'); clearTimeout(t); t = setTimeout(function(){ document.body.classList.remove('show-bar'); }, 1800); });
  window.addEventListener('hashchange', function(){ var h = /#([0-9]+)$/.exec(location.hash); if (h && +h[1] - 1 !== i) show(+h[1] - 1); });
  show(i);
})();
"""

def page(title, kind, items, back, back_label, with_notes, pdf):
    notes_html = ''
    notes_btn = '<button type="button" id="notes-toggle" title="Presenter view with notes, next slide and a timer, in a separate window (N)">Presenter view</button>' if with_notes else ''
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>{title}</title><style>{STYLE}</style></head><body>
<main class="stage" aria-label="{kind}s"><img id="view" src="{items[0]['src']}" alt="{html.escape(items[0]['alt'])}"></main>
{notes_html}
<p class="sr" id="live" aria-live="polite"></p>
<nav class="bar" aria-label="{kind} controls">
<a href="{back}" title="{back_label}"><span class="label">← {back_label}</span><span class="short">All</span></a>
<button type="button" id="prev" aria-label="Previous {kind.lower()}">←</button><span class="count" id="count">1 / {len(items)}</span><button type="button" id="next" aria-label="Next {kind.lower()}">→</button>
<span class="spacer"></span><span class="hint">Arrow keys or tap to move · F for full screen{' · N for presenter view' if with_notes else ''}</span>
{notes_btn}<a href="{pdf}" download title="Download PDF"><span class="label">PDF</span><span class="sr"> download</span>⤓</a>
<button type="button" id="full" title="Full screen (F)" aria-label="Full screen"><span class="label" id="full-label">Full screen</span><span class="short" id="full-short" aria-hidden="true">⛶</span></button>
</nav>
<script>var ITEMS={json.dumps(items)};var KIND={json.dumps(kind)};{SCRIPT}</script>
</body></html>"""


PRESENTER_STYLE = """
:root{--bg:#1F1915;--ink:#F3ECE1;--muted:#CDBFA9;--rust:#E3B98F;--panel:#2B231D}
*{box-sizing:border-box}html,body{margin:0;height:100%;background:var(--bg);color:var(--ink);font:500 16px/1.4 system-ui,-apple-system,'Segoe UI',sans-serif}
.grid{display:grid;grid-template-columns:1.6fr 1fr;grid-template-rows:auto 1fr auto;gap:14px;height:100%;padding:14px}
.now{grid-row:1/3;display:flex;flex-direction:column;gap:8px;min-height:0}.now img{width:100%;height:auto;max-height:62vh;object-fit:contain;background:#000}
.side{display:flex;flex-direction:column;gap:10px;min-height:0}.side img{width:100%;height:auto;opacity:.85;background:#000}
.label{font:600 12px/1 system-ui;letter-spacing:.12em;text-transform:uppercase;color:var(--rust)}
.notes{grid-column:2;grid-row:2;background:var(--panel);border-left:3px solid var(--rust);padding:14px 16px;overflow:auto;font:400 20px/1.5 Georgia,serif}
.controls{grid-column:1/3;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
button{min-height:44px;min-width:44px;padding:0 14px;border:1px solid #5A4A3E;background:transparent;color:var(--ink);font:inherit;border-radius:6px;cursor:pointer}
button:hover{border-color:var(--rust)}:focus-visible{outline:3px solid var(--rust);outline-offset:2px}
.clock{font:600 28px/1 ui-monospace,Menlo,monospace;font-variant-numeric:tabular-nums;margin-left:auto}.count{color:var(--muted);min-width:70px;text-align:center}
.end{color:var(--muted);padding:30px 0;text-align:center}
"""
PRESENTER_SCRIPT = """
(function(){
  var items = ITEMS, i = 0;
  var m = /#([0-9]+)$/.exec(location.hash); if (m) i = Math.min(items.length - 1, Math.max(0, +m[1] - 1));
  var channel = ('BroadcastChannel' in window) ? new BroadcastChannel('bb-present') : null, quiet = false;
  function show(n){
    i = Math.min(items.length - 1, Math.max(0, n));
    document.getElementById('now').src = items[i].src; document.getElementById('now').alt = items[i].alt;
    var next = items[i + 1]; var nextImg = document.getElementById('next-img'); var end = document.getElementById('end');
    if (next) { nextImg.hidden = false; end.hidden = true; nextImg.src = next.src; nextImg.alt = 'Next: ' + next.alt; } else { nextImg.hidden = true; end.hidden = false; }
    document.getElementById('notes').textContent = items[i].notes || 'No notes for this slide.';
    document.getElementById('count').textContent = (i + 1) + ' / ' + items.length;
    history.replaceState(null, '', '#' + (i + 1));
    if (channel && !quiet) channel.postMessage({slide: i});
  }
  if (channel) { channel.onmessage = function(e){ if (e.data && typeof e.data.slide === 'number' && e.data.slide !== i) { quiet = true; show(e.data.slide); quiet = false; } }; channel.postMessage({hello: true}); }
  // A simple talk timer: starts with the first move, or with the Start button.
  var start = null, timer = null;
  function tick(){ var s = Math.floor((Date.now() - start) / 1000); document.getElementById('clock').textContent = String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); }
  function begin(){ if (start === null) { start = Date.now(); timer = setInterval(tick, 500); tick(); document.getElementById('timer').textContent = 'Reset timer'; } }
  document.getElementById('timer').onclick = function(){ if (start === null) begin(); else { clearInterval(timer); start = null; document.getElementById('clock').textContent = '00:00'; this.textContent = 'Start timer'; } };
  document.getElementById('prev').onclick = function(){ begin(); show(i - 1); };
  document.getElementById('next').onclick = function(){ begin(); show(i + 1); };
  document.addEventListener('keydown', function(e){
    if (e.altKey || e.ctrlKey || e.metaKey) return; var k = e.key;
    if ((k === ' ' || k === 'Enter') && e.target && e.target.closest && e.target.closest('button')) return;
    if (k === 'ArrowRight' || k === 'PageDown' || k === ' ' || k === 'Enter') { e.preventDefault(); begin(); show(i + 1); }
    else if (k === 'ArrowLeft' || k === 'PageUp' || k === 'Backspace') { e.preventDefault(); show(i - 1); }
    else if (k === 'Home') { e.preventDefault(); show(0); } else if (k === 'End') { e.preventDefault(); show(items.length - 1); }
  });
  show(i);
})();
"""
def presenter(items):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Brain &amp; Behaviour · Presenter view</title><style>{PRESENTER_STYLE}</style></head><body>
<main class="grid" aria-label="Presenter view">
<section class="now"><span class="label">Now showing</span><img id="now" src="{items[0]['src']}" alt=""></section>
<section class="side"><span class="label">Up next</span><img id="next-img" src="" alt=""><p class="end" id="end" hidden>Last slide. Take questions.</p></section>
<section class="notes" aria-label="Speaker notes"><span class="label" style="display:block;margin-bottom:8px">Your notes (only on this screen)</span><div id="notes"></div></section>
<nav class="controls" aria-label="Slide controls"><button type="button" id="prev" aria-label="Previous slide">←</button><span class="count" id="count">1 / {len(items)}</span><button type="button" id="next" aria-label="Next slide">→</button><button type="button" id="timer">Start timer</button><span class="clock" id="clock" role="timer" aria-label="Time since you started">00:00</span></nav>
</main>
<script>var ITEMS={json.dumps(items)};{PRESENTER_SCRIPT}</script>
</body></html>"""
