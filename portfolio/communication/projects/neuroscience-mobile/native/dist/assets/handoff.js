// Handoff pages: answers and essay edits are kept in this browser only (nothing is sent anywhere),
// with live word counts, and buttons to copy or download everything as a text file.
(function () {
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private window: fine, nothing is kept */ } }
  };
  const fields = [...document.querySelectorAll('[data-save]')];
  fields.forEach(el => {
    const saved = store.get('n2ns:' + el.dataset.save);
    if (saved !== null) el.value = saved;
    el.addEventListener('input', () => { store.set('n2ns:' + el.dataset.save, el.value); count(); status('Saved in this browser'); });
  });
  const grow = el => { if (el.tagName === 'TEXTAREA') { el.style.height = 'auto'; el.style.height = el.scrollHeight + 4 + 'px'; } };
  fields.forEach(el => { grow(el); el.addEventListener('input', () => grow(el)); });
  const words = t => (t.trim().match(/\S+/g) || []).length;
  function count() {
    document.querySelectorAll('[data-words-for]').forEach(out => {
      const el = document.getElementById(out.dataset.wordsFor), limit = +out.dataset.limit || 0, n = words(el.value);
      const slot = (el.value.match(/\[[^\]]+\]/g) || []).length;
      out.textContent = `${n} words${limit ? ` of ${limit}` : ''}${slot ? ` · ${slot} part${slot > 1 ? 's' : ''} in [brackets] still to write` : ''}`;
      out.classList.toggle('over', limit && n > limit);
    });
  }
  function status(msg) { document.querySelectorAll('[data-status]').forEach(s => { s.textContent = msg; }); }
  function text() {
    return fields.map(el => {
      const label = el.dataset.label || el.dataset.save;
      return `${label}\n${'-'.repeat(Math.min(label.length, 60))}\n${el.value.trim() || '(not filled in yet)'}\n`;
    }).join('\n');
  }
  document.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(text()); status('Copied. Paste it into a message or document.'); }
    catch (e) { status('Copy did not work here. Use Download instead.'); }
  }));
  document.querySelectorAll('[data-download]').forEach(b => b.addEventListener('click', () => {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text()], { type: 'text/plain' }));
    a.download = b.dataset.download; document.body.appendChild(a); a.click(); a.remove();
    status('Downloaded. Send the file back, or keep it.');
  }));
  document.querySelectorAll('[data-reset]').forEach(b => b.addEventListener('click', () => {
    fields.forEach(el => { el.value = el.defaultValue; store.set('n2ns:' + el.dataset.save, el.value); });
    count(); status('Back to the original draft.');
  }));
  // Keep the typeset draft in step with the edit box.
  const escapeHtml = x => x.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  function renderRead() {
    document.querySelectorAll('[data-read]').forEach(art => {
      const box = document.querySelector('.essay-box textarea'); if (!box) return;
      const chapters = JSON.parse(art.dataset.chapters || '[]'), tags = JSON.parse(art.dataset.tags || '{}');
      art.innerHTML = box.value.trim().split(/\n\s*\n/).map((para, i) => {
        const lines = para.split('\n'), title = lines.length > 1 ? lines[0] : '', text = lines.length > 1 ? lines.slice(1).join(' ') : para;
        const tag = tags[chapters[i]];
        const body = escapeHtml(text).replace(/\[([^\]]+)\]/g, (_, m) => `<mark class="slot"><b>Your part</b> ${m}</mark>`);
        const aside = tag ? `<p class="essay-tag"><span>${window.HelperJobsIcons.icon(tag[0])}</span>${tag[1]}</p>` : '<p class="essay-tag"></p>';
        return `<div class="essay-row">${aside}<div>${title ? `<h3>${escapeHtml(title)}</h3>` : ''}<p>${body}</p></div></div>`;
      }).join('');
    });
  }
  fields.forEach(el => el.addEventListener('input', renderRead));
  document.querySelectorAll('[data-reset]').forEach(b => b.addEventListener('click', renderRead));
  renderRead();
  count();
})();
