// Research pictures drawn with the same helpers and classes as Helper Jobs' art.js
// (cream cards with a rust top edge, dotted lines, peach faces, Tabler line icons). Adds to HelperJobsArt.
(function (root) {
  const icons = root.HelperJobsIcons;
  const glyph = (name, x, y, size, cls = 'sp-glyph') => {
    const body = icons.icon(name).replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '');
    return `<g class="${cls}" transform="translate(${x} ${y}) scale(${size / 24})">${body}</g>`;
  };
  const card = (x, y, w, h, rot, inner, top = true) => `<g transform="translate(${x} ${y}) rotate(${rot})"><rect class="sp-card" width="${w}" height="${h}" rx="3"/>${top ? `<rect class="sp-top" width="${w}" height="5"/>` : ''}${inner}</g>`;
  const line = d => `<path class="sp-line" d="${d}"/>`;
  const tick = (x, y) => `<circle class="sp-tick-bg" cx="${x}" cy="${y}" r="10"/><path class="sp-tick" d="M${x - 4.5} ${y}l3 3 6 -6"/>`;
  const svg = (label, body, w = 320, h = 220) => `<svg class="spot-art" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label}">${body}</svg>`;
  const trace = (x, y, w, amp, seed, cls = 'sp-glyph-ink') => {
    let d = `M${x} ${y}`;
    for (let i = 1; i <= 22; i++) d += ` L${(x + (w * i) / 22).toFixed(1)} ${(y + Math.sin(i * 1.7 + seed) * amp * (0.4 + ((i * 7 + seed * 3) % 5) / 6)).toFixed(1)}`;
    return `<path class="${cls}" d="${d}"/>`;
  };
  const mouse = (x, y, s = 1) => `<g transform="translate(${x} ${y}) scale(${s})"><path class="sp-glyph-ink" d="M-30 6 C -48 10, -52 -6, -66 2"/><ellipse class="sp-face" cx="0" cy="0" rx="32" ry="20"/><circle class="sp-face-soft" cx="20" cy="-18" r="10"/><circle class="sp-face" cx="30" cy="-4" r="14"/><circle class="sp-badge" cx="36" cy="-7" r="3"/><circle class="sp-medal" cx="44" cy="-1" r="2.4"/></g>`;
  const head = (x, y) => `<g transform="translate(${x} ${y})"><ellipse class="sp-face" cx="0" cy="0" rx="50" ry="60"/>${[[-30, -38], [-11, -50], [11, -50], [30, -38], [-40, -14], [40, -14], [-44, 12], [44, 12], [-32, 34], [32, 34], [-13, 47], [13, 47], [-18, -20], [18, -20]].map(([a, b]) => `<circle class="sp-badge" cx="${a}" cy="${b}" r="4.5"/>`).join('')}</g>`;

  const STEPS = [
    ['users', 'Real life', 'Same words land one', 'moment, not the next'],
    ['eye', 'Understand', 'Mouse: state changes', 'what the brain sees'],
    ['activity', 'Measure', 'EEG: readable once,', 'then it drifts'],
    ['heart-handshake', 'Design', 'Ask, don’t guess.', 'One small step.'],
    ['flask', 'Test', 'Do the apps help?', 'More studies, papers']
  ];
  const stepCard = (i, x, y, w, h, rot) => { const [ic, t, a, b] = STEPS[i]; return card(x, y, w, h, rot, `<circle class="sp-face-soft" cx="22" cy="28" r="12"/><text class="sp-num" x="22" y="32" text-anchor="middle">${i + 1}</text>${glyph(ic, w - 44, 14, 28)}<text class="sp-title" x="14" y="${h - 50}">${t}</text><text class="sp-small" x="14" y="${h - 30}">${a}</text><text class="sp-small" x="14" y="${h - 15}">${b}</text>`); };
  function loopArt(tall) {
    if (!tall) {
      let b = '';
      for (let i = 0; i < 5; i++) b += stepCard(i, 14 + i * 190, 26 + (i % 2) * 10, 160, 150, i % 2 ? 2 : -2);
      for (let i = 0; i < 4; i++) { const x = 176 + i * 190; b += line(`M${x} 104 L${x + 24} 104`) + `<path class="sp-arrow" d="M${x + 20} 98l7 6-7 6"/>`; }
      b += line('M854 196 C 854 262, 760 270, 480 270 C 200 270, 94 262, 94 196') + '<path class="sp-arrow" d="M88 204l6-9 6 9"/><text class="sp-return" x="480" y="292" text-anchor="middle">AND BACK TO REAL LIFE</text>';
      return svg('The loop: real life raises a question; understand it in a mouse; measure it in a person; design apps from what held up; test them, and go back to real life.', b, 970, 300);
    }
    let b = '';
    for (let i = 0; i < 5; i++) b += stepCard(i, 14 + (i % 2) * 16, 12 + i * 132, 250, 108, i % 2 ? 1.5 : -1.5);
    for (let i = 0; i < 4; i++) { const y = 122 + i * 132; b += line(`M140 ${y} L140 ${y + 18}`) + `<path class="sp-arrow" d="M134 ${y + 14}l6 7 6-7"/>`; }
    b += line('M282 600 C 306 560, 306 110, 282 66') + '<path class="sp-arrow" d="M290 74l-8-8 -1 11"/><text class="sp-return" x="328" y="340" text-anchor="middle" transform="rotate(90 328 340)">AND BACK TO REAL LIFE</text>';
    return svg('The loop: real life, understand, measure, design, test, and back to real life.', b, 344, 672);
  }

  const pictures = {
    loop: () => loopArt(false),
    loopTall: () => loopArt(true),
    mouseStudy: () => svg('A picture and the mouse’s pupil and running speed go into a model that predicts each neuron.', `
      ${card(10, 22, 128, 104, -3, `<rect class="sp-screen" x="12" y="18" width="104" height="62" rx="2"/><path class="sp-medal" d="M18 76 L46 40 L64 62 L78 50 L110 76 Z"/><circle class="sp-face" cx="96" cy="32" r="7"/><rect class="sp-bar-soft" x="12" y="88" width="70" height="7"/>`)}
      ${card(14, 138, 124, 70, 2, `${glyph('eye', 14, 22, 26)}${glyph('walk', 50, 22, 26)}<rect class="sp-bar" x="86" y="28" width="26" height="7"/><rect class="sp-bar-soft" x="86" y="42" width="20" height="6"/>`)}
      ${line('M140 76 C 160 84, 164 102, 180 108')}${line('M140 170 C 160 160, 164 126, 180 118')}
      <circle class="sp-badge" cx="208" cy="112" r="26"/>${glyph('chart-dots', 194, 98, 28, 'sp-glyph-light')}
      ${line('M236 112 C 248 112, 250 110, 258 110')}
      ${card(256, 44, 56, 140, 2, `${trace(6, 34, 44, 5, 1)}${trace(6, 64, 44, 5, 3)}${trace(6, 94, 44, 6, 5, 'sp-arrow')}${tick(28, 120)}`)}`),
    eegStudy: () => svg('Fourteen sensors on the head record signals over time; the model guesses eyes open or closed.', `
      ${head(70, 108)}
      ${line('M124 96 C 142 88, 148 88, 160 86')}
      ${card(156, 22, 154, 118, 2, `${trace(12, 34, 130, 6, 1)}${trace(12, 58, 130, 6, 2)}${trace(12, 84, 130, 8, 6, 'sp-arrow')}<rect class="sp-bar-soft" x="12" y="100" width="80" height="6"/>`)}
      ${card(162, 154, 68, 54, -3, `${glyph('eye', 22, 16, 24)}`)}${card(242, 154, 68, 54, 3, `${glyph('eye-closed', 22, 16, 24)}`)}`),
    controls: () => svg('Three checks: shuffled answers, a gap in time and leaving one animal out.', `
      ${card(14, 30, 92, 124, -3, `${glyph('arrows-shuffle', 28, 22, 36)}<rect class="sp-bar" x="14" y="74" width="62" height="7"/><rect class="sp-bar-soft" x="14" y="88" width="48" height="6"/>`)}
      ${card(114, 22, 92, 124, 2, `${glyph('timeline', 28, 22, 36)}<rect class="sp-bar" x="14" y="74" width="56" height="7"/><rect class="sp-bar-soft" x="14" y="88" width="62" height="6"/>`)}
      ${card(214, 34, 92, 124, -2, `${glyph('users', 28, 22, 36)}<rect class="sp-bar" x="14" y="74" width="60" height="7"/><rect class="sp-bar-soft" x="14" y="88" width="44" height="6"/>`)}
      ${line('M60 172 C 110 198, 210 198, 262 174')}`),
    plan: () => svg('Five experiment cards; two are ready to run.', `
      ${[0, 1, 2, 3, 4].map(i => card(12 + i * 60, 34 + (i % 2) * 20, 70, 124, i % 2 ? 3 : -3, `<circle class="${i === 1 || i === 3 ? 'sp-medal' : 'sp-face-soft'}" cx="35" cy="36" r="16"/><text class="sp-num" x="35" y="40" text-anchor="middle"${i === 1 || i === 3 ? ' style="fill:#FBF6EE"' : ''}>${i + 1}</text><rect class="sp-bar-soft" x="12" y="68" width="46" height="6"/><rect class="sp-bar-soft" x="12" y="82" width="36" height="6"/>`)).join('')}`, 320, 200),
    eegHero: () => svg('A head with fourteen sensors, and two cards: eyes open and eyes closed.', `
      ${head(86, 112)}${line('M140 92 C 162 82, 176 70, 196 64')}${line('M140 132 C 162 142, 176 154, 196 160')}
      ${card(194, 26, 106, 76, 3, `${glyph('eye', 37, 18, 32)}<rect class="sp-bar-soft" x="22" y="58" width="62" height="6"/>`)}
      ${card(194, 122, 106, 76, -3, `${glyph('eye-closed', 37, 18, 32)}<rect class="sp-bar-soft" x="22" y="58" width="62" height="6"/>`)}`),
    mouseHero: () => svg('A mouse runs on a wheel while it watches a picture.', `
      ${card(16, 26, 140, 100, -3, `<rect class="sp-screen" x="12" y="18" width="116" height="66" rx="2"/><path class="sp-medal" d="M20 80 L52 42 L72 66 L88 52 L122 80 Z"/><circle class="sp-face" cx="108" cy="32" r="7"/>`)}
      ${line('M156 92 C 176 98, 180 110, 190 116')}
      <circle class="sp-line" cx="236" cy="150" r="52"/>${mouse(236, 134, 1)}`, 320, 220)
  };
  const base = root.HelperJobsArt;
  root.HelperJobsArt = { draw: name => (pictures[name] ? pictures[name]() : base.draw(name)), names: [...base.names, ...Object.keys(pictures)] };
})(window);
