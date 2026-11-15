// More Tabler line icons (MIT licence, https://tabler.io/icons) for the research pages, added to the
// Helper Jobs / Next Step icon set without changing it. Same size, stroke and class as HelperJobsIcons.
(function (root) {
  const extra = {
 "brain": "<path d=\"M15.5 13a3.5 3.5 0 0 0 -3.5 3.5v1a3.5 3.5 0 0 0 7 0v-1.8\" /> <path d=\"M8.5 13a3.5 3.5 0 0 1 3.5 3.5v1a3.5 3.5 0 0 1 -7 0v-1.8\" /> <path d=\"M17.5 16a3.5 3.5 0 0 0 0 -7h-.5\" /> <path d=\"M19 9.3v-2.8a3.5 3.5 0 0 0 -7 0\" /> <path d=\"M6.5 16a3.5 3.5 0 0 1 0 -7h.5\" /> <path d=\"M5 9.3v-2.8a3.5 3.5 0 0 1 7 0v10\" />",
 "chart-bar": "<path d=\"M3 13a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v6a1 1 0 0 1 -1 1h-4a1 1 0 0 1 -1 -1l0 -6\" /> <path d=\"M15 9a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v10a1 1 0 0 1 -1 1h-4a1 1 0 0 1 -1 -1l0 -10\" /> <path d=\"M9 5a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v14a1 1 0 0 1 -1 1h-4a1 1 0 0 1 -1 -1l0 -14\" /> <path d=\"M4 20h14\" />",
 "chart-line": "<path d=\"M4 19l16 0\" /> <path d=\"M4 15l4 -6l4 2l4 -5l4 4\" />",
 "chart-dots": "<path d=\"M3 3v18h18\" /> <path d=\"M7 9a2 2 0 1 0 4 0a2 2 0 1 0 -4 0\" /> <path d=\"M17 7a2 2 0 1 0 4 0a2 2 0 1 0 -4 0\" /> <path d=\"M12 15a2 2 0 1 0 4 0a2 2 0 1 0 -4 0\" /> <path d=\"M10.16 10.62l2.34 2.88\" /> <path d=\"M15.088 13.328l2.837 -4.586\" />",
 "microscope": "<path d=\"M5 21h14\" /> <path d=\"M6 18h2\" /> <path d=\"M7 18v3\" /> <path d=\"M9 11l3 3l6 -6l-3 -3l-6 6\" /> <path d=\"M10.5 12.5l-1.5 1.5\" /> <path d=\"M17 3l3 3\" /> <path d=\"M12 21a6 6 0 0 0 3.715 -10.712\" />",
 "activity": "<path d=\"M3 12h4l3 8l4 -16l3 8h4\" />",
 "wave-sine": "<path d=\"M21 12h-2c-.894 0 -1.662 -.857 -1.761 -2c-.296 -3.45 -.749 -6 -2.749 -6s-2.5 3.582 -2.5 8s-.5 8 -2.5 8s-2.452 -2.547 -2.749 -6c-.1 -1.147 -.867 -2 -1.763 -2h-2\" />",
 "eye-closed": "<path d=\"M21 9c-2.4 2.667 -5.4 4 -9 4c-3.6 0 -6.6 -1.333 -9 -4\" /> <path d=\"M3 15l2.5 -3.8\" /> <path d=\"M21 14.976l-2.492 -3.776\" /> <path d=\"M9 17l.5 -4\" /> <path d=\"M15 17l-.5 -4\" />",
 "run": "<path d=\"M11.007 5a2 2 0 1 0 4 0a2 2 0 1 0 -4 0\" /> <path d=\"M4 17l5 1l.75 -1.5\" /> <path d=\"M15 21v-4l-4 -3l1 -6\" /> <path d=\"M7 12v-3l5 -1l3 3l3 1\" />",
 "flask": "<path d=\"M9 3l6 0\" /> <path d=\"M10 9l4 0\" /> <path d=\"M10 3v6l-4 11a.7 .7 0 0 0 .5 1h11a.7 .7 0 0 0 .5 -1l-4 -11v-6\" />",
 "target": "<path d=\"M11 12a1 1 0 1 0 2 0a1 1 0 1 0 -2 0\" /> <path d=\"M7 12a5 5 0 1 0 10 0a5 5 0 1 0 -10 0\" /> <path d=\"M3 12a9 9 0 1 0 18 0a9 9 0 1 0 -18 0\" />",
 "arrows-shuffle": "<path d=\"M18 4l3 3l-3 3\" /> <path d=\"M18 20l3 -3l-3 -3\" /> <path d=\"M3 7h3a5 5 0 0 1 5 5a5 5 0 0 0 5 5h5\" /> <path d=\"M21 7h-5a4.978 4.978 0 0 0 -3 1m-4 8a4.984 4.984 0 0 1 -3 1h-3\" />",
 "filter": "<path d=\"M4 4h16v2.172a2 2 0 0 1 -.586 1.414l-4.414 4.414v7l-6 2v-8.5l-4.48 -4.928a2 2 0 0 1 -.52 -1.345v-2.227\" />",
 "books": "<path d=\"M5 5a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v14a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1l0 -14\" /> <path d=\"M9 5a1 1 0 0 1 1 -1h2a1 1 0 0 1 1 1v14a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1l0 -14\" /> <path d=\"M5 8h4\" /> <path d=\"M9 16h4\" /> <path d=\"M13.803 4.56l2.184 -.53c.562 -.135 1.133 .19 1.282 .732l3.695 13.418a1.02 1.02 0 0 1 -.634 1.219l-.133 .041l-2.184 .53c-.562 .135 -1.133 -.19 -1.282 -.732l-3.695 -13.418a1.02 1.02 0 0 1 .634 -1.219l.133 -.041\" /> <path d=\"M14 9l4 -1\" /> <path d=\"M16 16l3.923 -.98\" />",
 "route-2": "<path d=\"M3 19a2 2 0 1 0 4 0a2 2 0 0 0 -4 0\" /> <path d=\"M19 7a2 2 0 1 0 0 -4a2 2 0 0 0 0 4\" /> <path d=\"M14 5a2 2 0 0 0 -2 2v10a2 2 0 0 1 -2 2\" />",
 "timeline": "<path d=\"M4 16l6 -7l5 5l5 -6\" /> <path d=\"M14 14a1 1 0 1 0 2 0a1 1 0 1 0 -2 0\" /> <path d=\"M9 9a1 1 0 1 0 2 0a1 1 0 1 0 -2 0\" /> <path d=\"M3 16a1 1 0 1 0 2 0a1 1 0 1 0 -2 0\" /> <path d=\"M19 8a1 1 0 1 0 2 0a1 1 0 1 0 -2 0\" />",
 "alert-triangle": "<path d=\"M12 9v4\" /> <path d=\"M10.363 3.591l-8.106 13.534a1.914 1.914 0 0 0 1.636 2.871h16.214a1.914 1.914 0 0 0 1.636 -2.87l-8.106 -13.536a1.914 1.914 0 0 0 -3.274 0\" /> <path d=\"M12 16h.01\" />",
 "presentation": "<path d=\"M3 4l18 0\" /> <path d=\"M4 4v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-10\" /> <path d=\"M12 16l0 4\" /> <path d=\"M9 20l6 0\" /> <path d=\"M8 12l3 -3l2 2l3 -3\" />",
 "code": "<path d=\"M7 8l-4 4l4 4\" /> <path d=\"M17 8l4 4l-4 4\" /> <path d=\"M14 4l-4 16\" />",
 "player-play": "<path d=\"M7 4v16l13 -8z\" />",
 "file-text": "<path d=\"M14 3v4a1 1 0 0 0 1 1h4\" /> <path d=\"M17 21h-10a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2z\" /> <path d=\"M9 9l1 0\" /> <path d=\"M9 13l6 0\" /> <path d=\"M9 17l6 0\" />"
};
  const base = root.HelperJobsIcons;
  function icon(name, label) {
    if (!extra[name]) return base.icon(name, label);
    return base.icon('star', label).replace(/(<svg[^>]*>).*(<\/svg>)/s, (_, open, close) => open + extra[name] + close);
  }
  root.HelperJobsIcons = { icon, names: [...base.names, ...Object.keys(extra)] };
})(window);
