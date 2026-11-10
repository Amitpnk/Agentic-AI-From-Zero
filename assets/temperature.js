// Interactive temperature demo.
// Usage: <div data-temp-demo></div> (add data-themed to follow dark mode)
(function () {
  var PROMPT = 'The best thing about our college canteen is the';
  // Made-up probabilities at temperature = 1
  var BASE = [
    ['chai', 0.40],
    ['samosa', 0.25],
    ['vibe', 0.12],
    ['dosa', 0.10],
    ['WiFi', 0.08],
    ['silence', 0.05]
  ];

  function probsAt(t) {
    if (t <= 0.001) {
      return BASE.map(function (w, i) { return i === 0 ? 1 : 0; });
    }
    var raw = BASE.map(function (w) { return Math.pow(w[1], 1 / t); });
    var sum = raw.reduce(function (a, b) { return a + b; }, 0);
    return raw.map(function (r) { return r / sum; });
  }

  function sample(p) {
    var r = Math.random(), acc = 0;
    for (var i = 0; i < p.length; i++) { acc += p[i]; if (r <= acc) return BASE[i][0]; }
    return BASE[p.length - 1][0];
  }

  function label(t) {
    if (t <= 0.001) return 'T = 0 (always top word)';
    if (t < 0.5) return 'T = ' + t.toFixed(1) + ' (safe, focused)';
    if (t <= 1.1) return 'T = ' + t.toFixed(1) + ' (balanced)';
    return 'T = ' + t.toFixed(1) + ' (creative, risky)';
  }

  function build(el) {
    el.classList.add('td');
    if (el.hasAttribute('data-themed')) el.classList.add('td-themed');
    var rows = BASE.map(function (w) {
      return '<div class="td-row"><span class="td-word">' + w[0] +
        '</span><div class="td-bar"><span></span></div><span class="td-pct"></span></div>';
    }).join('');
    el.innerHTML =
      '<div class="td-prompt">"' + PROMPT + ' <b>___</b>"</div>' +
      '<div class="td-controls"><label for="td-r">Temperature</label>' +
      '<input id="td-r" type="range" min="0" max="2" step="0.1" value="1">' +
      '<span class="td-tval"></span></div>' + rows +
      '<div class="td-actions"><button type="button">Generate 5 answers</button>' +
      '<span class="td-out"></span></div>' +
      '<div class="td-hint">Probabilities are made up for teaching. Slide left: the model plays safe. Slide right: rare words get a chance.</div>';

    var range = el.querySelector('input');
    var tval = el.querySelector('.td-tval');
    var bars = el.querySelectorAll('.td-bar span');
    var pcts = el.querySelectorAll('.td-pct');
    var out = el.querySelector('.td-out');

    function render() {
      var t = parseFloat(range.value);
      var p = probsAt(t);
      tval.textContent = label(t);
      p.forEach(function (v, i) {
        bars[i].style.width = (v * 100).toFixed(1) + '%';
        pcts[i].textContent = Math.round(v * 100) + '%';
      });
      out.textContent = '';
    }
    range.addEventListener('input', render);
    el.querySelector('button').addEventListener('click', function () {
      var p = probsAt(parseFloat(range.value));
      var words = [];
      for (var i = 0; i < 5; i++) words.push(sample(p));
      out.textContent = words.join(', ');
    });
    // Stop reveal.js from treating arrow keys on the slider as slide navigation
    range.addEventListener('keydown', function (e) { e.stopPropagation(); });
    render();
  }

  function init() {
    var els = document.querySelectorAll('[data-temp-demo]');
    for (var i = 0; i < els.length; i++) build(els[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
