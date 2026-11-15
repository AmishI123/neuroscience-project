// Small, readable charts drawn as SVG from website/assets/results.js. Two colours only:
// sand for the comparison and rust for the thing being tested; every bar carries its own number.
(function (root) {
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const fmt = v => (Math.abs(v) < 1 ? v.toFixed(3).replace(/^0/, '') : String(v));
  const table = (caption, head, rows) => `<div class="sr-only"><table><caption>${esc(caption)}</caption><tr>${head.map(h => `<th>${esc(h)}</th>`).join('')}</tr>${rows.map(r => `<tr>${r.map(c => `<td>${esc(c)}</td>`).join('')}</tr>`).join('')}</table></div>`;
  const frame = (w, h, body, labelText) => `<svg class="chart" viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(labelText)}">${body}</svg>`;

  // Bars in groups: [{label, values:[a, b]}], with two series names.
  function groupedBars({ groups, series, max, min = 0, caption, height = 300, ticks = 4, format = fmt }) {
    const w = 640, h = height, left = 48, right = 12, top = 36, bottom = 52;
    const plotW = w - left - right, plotH = h - top - bottom;
    const y = v => top + plotH - ((v - min) / (max - min)) * plotH;
    const gw = plotW / groups.length, bw = Math.min(64, (gw - 28) / series.length);
    let body = '';
    for (let t = 0; t <= ticks; t++) { const v = min + ((max - min) * t) / ticks; body += `<line class="grid" x1="${left}" x2="${w - right}" y1="${y(v)}" y2="${y(v)}"/><text class="tick" x="${left - 8}" y="${y(v) + 4}" text-anchor="end">${format(v)}</text>`; }
    groups.forEach((g, gi) => {
      const x0 = left + gi * gw + (gw - bw * series.length - 6 * (series.length - 1)) / 2;
      g.values.forEach((v, si) => {
        const x = x0 + si * (bw + 6);
        body += `<rect class="bar s${si}" x="${x}" y="${y(v)}" width="${bw}" height="${y(min) - y(v)}" rx="3"/><text class="val${si ? ' strong' : ''}" x="${x + bw / 2}" y="${y(v) - 8}" text-anchor="middle">${format(v)}</text>`;
      });
      body += `<text class="cat" x="${left + gi * gw + gw / 2}" y="${h - bottom + 22}" text-anchor="middle">${esc(g.label)}</text>`;
    });
    body += series.map((s, si) => `<rect class="bar s${si}" x="${left + si * 210}" y="8" width="14" height="14" rx="2"/><text class="key" x="${left + 20 + si * 210}" y="20">${esc(s)}</text>`).join('');
    return frame(w, h, body, caption) + table(caption, ['', ...series], groups.map(g => [g.label, ...g.values.map(format)]));
  }

  // Fold-by-fold dots against a dashed chance line: rows [{label, values:[...], mean}].
  function foldDots({ rows, caption, min = 0.2, max = 0.8, chance = 0.5, folds = 5 }) {
    const w = 640, rowH = 64, top = 16, left = 150, right = 96, h = top + rows.length * rowH + 44;
    const x = v => left + ((v - min) / (max - min)) * (w - left - right);
    const avg = r => (r.mean != null ? r.mean : r.values.reduce((a, b) => a + b, 0) / r.values.length);
    let body = '';
    for (let v = min; v <= max + 1e-9; v += 0.1) body += `<line class="grid" x1="${x(v)}" x2="${x(v)}" y1="${top}" y2="${h - 40}"/><text class="tick" x="${x(v)}" y="${h - 22}" text-anchor="middle">${fmt(v)}</text>`;
    body += `<line class="chance" x1="${x(chance)}" x2="${x(chance)}" y1="${top}" y2="${h - 40}"/><text class="tick" x="${x(chance)}" y="${h - 4}" text-anchor="middle">0.5 = a coin flip</text><text class="tick" x="${w - 4}" y="${top + 4}" text-anchor="end">average</text>`;
    rows.forEach((r, ri) => {
      const cy = top + 14 + ri * rowH + rowH / 2;
      body += `<text class="cat-l" x="0" y="${cy + 5}">${esc(r.label)}</text><line class="track" x1="${x(Math.min(...r.values))}" x2="${x(Math.max(...r.values))}" y1="${cy}" y2="${cy}"/>`;
      r.values.forEach((v, i) => { body += `<circle class="dot ${r.tone || ''}" cx="${x(v)}" cy="${cy}" r="9"><title>Stretch ${i + 1}: ${fmt(v)}</title></circle><text class="fold" x="${x(v)}" y="${cy + 3.5}" text-anchor="middle">${i + 1}</text>`; });
      body += `<path class="mean" d="M${x(avg(r))} ${cy + 12} l6 9 h-12 z"/><text class="val strong" x="${w - 4}" y="${cy + 5}" text-anchor="end">${fmt(avg(r))}</text>`;
    });
    return frame(w, h, body, caption) + table(caption, ['', ...Array.from({ length: folds }, (_, i) => `Stretch ${i + 1}`), 'Average'], rows.map(r => [r.label, ...r.values.map(fmt), fmt(avg(r))]));
  }

  // One row of bars: [{label, value}], with a reference line (for example zero gain).
  function rowBars({ items, caption, max, height = 240, format = fmt, tone = 's1' }) {
    const w = 640, left = 48, right = 12, top = 24, bottom = 52, plotH = height - top - bottom;
    const gw = (w - left - right) / items.length, bw = Math.min(96, gw - 40);
    const y = v => top + plotH - (v / max) * plotH;
    let body = `<line class="axis" x1="${left}" x2="${w - right}" y1="${y(0)}" y2="${y(0)}"/>`;
    items.forEach((it, i) => {
      const x = left + i * gw + (gw - bw) / 2;
      body += `<rect class="bar ${it.tone || tone}" x="${x}" y="${y(it.value)}" width="${bw}" height="${y(0) - y(it.value)}" rx="3"/><text class="val strong" x="${x + bw / 2}" y="${y(it.value) - 8}" text-anchor="middle">${format(it.value)}</text><text class="cat" x="${x + bw / 2}" y="${height - bottom + 22}" text-anchor="middle">${esc(it.label)}</text>`;
    });
    return frame(w, height, body, caption) + table(caption, ['', 'Value'], items.map(it => [it.label, format(it.value)]));
  }

  // A number line from min to max with labelled marks: how to read a score.
  // marks: [{v, label, tone, below}], ticks: [{v, label}].
  function scale({ min = 0, max = 1, marks, ticks, caption, band }) {
    const w = 640, h = 190, left = 24, right = 24, y0 = 100;
    const x = v => left + ((v - min) / (max - min)) * (w - left - right);
    let body = band ? `<rect class="band" x="${x(band[0])}" y="${y0 - 14}" width="${x(band[1]) - x(band[0])}" height="28" rx="4"/>` : '';
    body += `<line class="axis" x1="${x(min)}" x2="${x(max)}" y1="${y0}" y2="${y0}"/>`;
    ticks.forEach(t => { body += `<line class="grid" x1="${x(t.v)}" x2="${x(t.v)}" y1="${y0 - 8}" y2="${y0 + 8}"/><text class="tick" x="${x(t.v)}" y="${y0 + 72}" text-anchor="${t.v === min ? 'start' : t.v === max ? 'end' : 'middle'}">${esc(t.label)}</text>`; });
    marks.forEach(m => {
      const up = !m.below, ty = up ? y0 - 30 : y0 + 44;
      body += `<line class="lead" x1="${x(m.v)}" x2="${x(m.v)}" y1="${up ? y0 - 22 : y0 + 4}" y2="${up ? y0 - 4 : y0 + 26}"/><circle class="dot ${m.tone || ''}" cx="${x(m.v)}" cy="${y0}" r="8"/><text class="val strong" x="${x(m.v)}" y="${ty}" text-anchor="middle">${esc(m.label)}</text>`;
    });
    return frame(w, h, body, caption) + table(caption, ['', 'Score'], marks.map(m => [m.label, fmt(m.v)]));
  }

  root.PortfolioCharts = { groupedBars, foldDots, rowBars, scale, fmt };
})(window);
