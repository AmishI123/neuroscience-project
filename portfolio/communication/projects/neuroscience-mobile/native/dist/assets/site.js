// Fills in icons, illustrations and charts on every portfolio page.
(function () {
  const R = window.PortfolioResults, C = window.PortfolioCharts;
  document.querySelectorAll('[data-icon]').forEach(el => { el.innerHTML = window.HelperJobsIcons.icon(el.dataset.icon); });
  document.querySelectorAll('[data-art]').forEach(el => { el.innerHTML = window.HelperJobsArt.draw(el.dataset.art); });
  const pct = v => `+${(v * 100).toFixed(1)}`;
  const charts = {
    'mouse-scores': () => C.groupedBars({
      caption: 'Score for three mice on unseen pictures: guesser A (picture only) and guesser B (picture plus pupil and running).',
      series: ['A · picture only', 'B · picture + state'], max: 0.25, ticks: 5,
      groups: R.mouse.mice.map(m => ({ label: m.id, values: [m.stimulus, m.behavior] }))
    }),
    'mouse-scale': () => {
      const m = R.mouse.mice, avg = k => m.reduce((a, b) => a + b[k], 0) / m.length;
      return C.scale({ caption: 'Score scale from 0 (nothing in common) to 1 (perfect match), with the average score of guesser A and guesser B.', band: [avg('stimulus'), avg('behavior')],
        ticks: [{ v: 0, label: '0 · nothing in common' }, { v: 0.5, label: '0.5' }, { v: 1, label: '1 · perfect match' }],
        marks: [{ v: avg('stimulus'), label: `A · picture only ${C.fmt(+avg('stimulus').toFixed(3))}`, tone: 'soft', below: true }, { v: avg('behavior'), label: `B · plus state ${C.fmt(+avg('behavior').toFixed(3))}` }] });
    },
    'eeg-scale': () => C.scale({ caption: 'Score scale from 0 to 1 where 0.5 is a coin flip, with the EEG results marked.', band: [0.45, 0.55],
      ticks: [{ v: 0, label: '0 · always wrong' }, { v: 0.5, label: '0.5 · coin flip' }, { v: 1, label: '1 · always right' }],
      marks: [{ v: R.eeg.fold_means['pointwise EEG'], label: `Over time ${C.fmt(R.eeg.fold_means['pointwise EEG'])}`, tone: 'soft', below: true }, { v: R.eeg.holdout[0].auc, label: `Last stretch ${C.fmt(R.eeg.holdout[0].auc)}`, tone: 'soft' }, { v: R.eeg.glitches.holdout[0], label: `Glitches trimmed ${C.fmt(R.eeg.glitches.holdout[0])}`, below: true }] }),
    'mouse-gain': () => C.rowBars({
      caption: 'How much knowing the mouse’s state adds, for each mouse.', max: 0.06, height: 220,
      items: R.mouse.mice.map(m => ({ label: m.id, value: m.gain })),
      format: v => (v === 0 ? '0' : `+${v.toFixed(3).replace(/^0/, '')}`)
    }),
    'mouse1-ablation': () => { const f = R.mouse.first_mouse.ablation; return C.rowBars({
      caption: 'First mouse: score with the picture only, plus running, plus pupil, and plus both.', max: 0.2, height: 230,
      items: Object.entries(f).map(([label, value]) => ({ label, value, tone: label.includes('pupil') || label.includes('both') ? 's1' : 's0' })) }); },
    'mouse1-cells': () => { const f = R.mouse.first_mouse; return C.rowBars({
      caption: 'First mouse: average gain for brain cells that follow pupil size and for the rest.', max: 0.08, height: 230,
      items: [{ label: `Follow pupil (${f.follow_pupil_cells.toLocaleString()} cells)`, value: f.follow_pupil_gain }, { label: 'All the rest', value: f.other_gain, tone: 's0' }],
      format: v => `+${v.toFixed(3).replace(/^0/, '')}` }); },
    'mouse1-cell': () => { const b = R.mouse.first_mouse.best_cell; return C.rowBars({
      caption: `Brain cell ${b.id}: score from the picture alone and with the mouse's state added.`, max: 0.5, height: 230,
      items: [{ label: 'Picture only', value: b.picture_only, tone: 's0' }, { label: 'Picture + state', value: b.with_state }] }); },
    'mouse-loo': () => C.rowBars({
      caption: 'Average gain from knowing the mouse’s state, leaving out each mouse in turn.', max: 0.06, height: 220, tone: 's0',
      items: R.mouse.leave_one_out_mean_gain.map(m => ({ label: `Without ${m.omit.toLowerCase()}`, value: m.gain })),
      format: v => `+${v.toFixed(3).replace(/^0/, '')}`
    }),
    'eeg-holdout': () => C.groupedBars({
      caption: 'Score on the last stretch of the recording for each model, as first run and with four glitchy readings trimmed.',
      series: ['As first run', 'Glitches trimmed'], max: 0.8, min: 0, ticks: 4,
      groups: [{ label: 'Now only', values: [R.eeg.holdout[0].auc, R.eeg.glitches.holdout[0]] }, { label: 'Now + a moment ago', values: [R.eeg.holdout[1].auc, R.eeg.glitches.holdout[1]] }]
    }),
    'eeg-folds': () => C.foldDots({
      caption: 'Score on each of five later blocks of the recording; the dashed line is a coin flip.',
      rows: [
        { label: 'Now only', values: R.eeg.folds.pointwise, mean: R.eeg.fold_means['pointwise EEG'] },
        { label: 'Now + a moment ago', values: R.eeg.folds.context, mean: R.eeg.fold_means['EEG + causal temporal context'], tone: 'ink' },
        { label: 'Glitches trimmed', values: R.eeg.glitches.folds.pointwise, mean: R.eeg.glitches.means[0], tone: 'soft' },
        { label: 'With a gap', values: R.eeg.gap_folds.pointwise, mean: R.eeg.gap_means['pointwise EEG'], tone: 'soft' }
      ]
    }),
    'eeg-bands': () => C.foldDots({
      caption: 'Experiment 2: score on five later stretches for raw readings, all four brain-wave rhythms and alpha alone, with a gap of one second; the dashed line is a coin flip.',
      min: 0.2, max: 0.8,
      rows: [
        { label: 'Raw readings', values: R.eeg.bands.with_gap['raw readings'].stretches, mean: R.eeg.bands.with_gap['raw readings'].mean, tone: 'soft' },
        { label: 'All four rhythms', values: R.eeg.bands.with_gap['all four bands'].stretches, mean: R.eeg.bands.with_gap['all four bands'].mean },
        { label: 'Alpha only', values: R.eeg.bands.with_gap['alpha only'].stretches, mean: R.eeg.bands.with_gap['alpha only'].mean, tone: 'ink' }
      ]
    }),
    'eeg-windows': () => C.groupedBars({
      caption: 'How many readings back the model looks: score on the last stretch and average of five stretches.',
      series: ['Last stretch', 'Average of 5 stretches'], max: 0.8, ticks: 4,
      groups: R.eeg.windows.map(w => ({ label: `${w.window} back`, values: [w.holdout, w.blocked] }))
    })
  };
  document.querySelectorAll('[data-chart]').forEach(el => { if (charts[el.dataset.chart]) el.innerHTML = charts[el.dataset.chart](); });
  document.querySelectorAll('[data-num]').forEach(el => {
    const path = el.dataset.num.split('.'); let v = R; for (const p of path) v = v == null ? v : v[p];
    if (typeof v === 'number') el.textContent = el.dataset.fmt === 'gain' ? pct(v) : C.fmt(v);
  });
})();
