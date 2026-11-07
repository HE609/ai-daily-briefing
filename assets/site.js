(() => {
  'use strict';
  const root = document.body.dataset.root || './';
  const $ = (selector) => document.querySelector(selector);
  const grid = $('#report-grid');
  const escapeHTML = (value) => String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));

  if (grid) {
    const search = $('#search');
    const month = $('#month');
    const status = $('#result-count');
    const more = $('#load-more');
    const reset = $('#reset-filters');
    const params = new URLSearchParams(location.search);
    let topic = params.get('topic') || '';
    let limit = 12;
    let reports;
    let searchIndex;
    let searchPromise;
    let revision = 0;
    let timer;
    let searchFailed = false;
    search.value = params.get('q') || '';
    if ([...month.options].some(o => o.value === params.get('month'))) month.value = params.get('month');
    const topics = [...document.querySelectorAll('[data-topic]')];
    if (!topics.some(b => b.dataset.topic === topic)) topic = '';
    const reportPromise = fetch(root + 'data/reports.json').then(response => {
      if (!response.ok) throw new Error('report index unavailable');
      return response.json();
    }).then(data => { reports = data; return data; });

    function setTopic() {
      topics.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.topic === topic)));
    }
    function card(item, query) {
      // Highlight literal matches in escaped text, never interpret search input as HTML.
      const highlight = (text) => {
        if (!query) return escapeHTML(text);
        const lower = text.toLocaleLowerCase();
        const needle = query.toLocaleLowerCase();
        let position = 0;
        let output = '';
        while (position < text.length) {
          const found = lower.indexOf(needle, position);
          if (found < 0) return output + escapeHTML(text.slice(position));
          output += escapeHTML(text.slice(position, found)) + '<mark>' + escapeHTML(text.slice(found, found + query.length)) + '</mark>';
          position = found + query.length;
        }
        return output;
      };
      let excerpt = item.summary;
      if (query && searchIndex && ![item.headline, item.summary].some(x => x.toLocaleLowerCase().includes(query.toLocaleLowerCase()))) {
        const text = searchIndex[item.date] || '';
        const at = text.toLocaleLowerCase().indexOf(query.toLocaleLowerCase());
        if (at >= 0) excerpt = (at > 25 ? '…' : '') + text.slice(Math.max(0, at - 25), at + 120) + '…';
      }
      return `<a class="report-card" href="${root}${escapeHTML(item.url)}"><div class="card-meta"><time datetime="${item.date}">${item.date.replaceAll('-', '.')}</time><span>${item.minutes} 分钟阅读</span></div><h3>${highlight(item.headline)}</h3><p>${highlight(excerpt)}</p><div class="card-bottom"><div class="tags">${item.topics.slice(0,2).map(t => `<span class="tag">${escapeHTML(t)}</span>`).join('')}</div><span class="card-arrow" aria-hidden="true">↗</span></div></a>`;
    }
    async function render() {
      const thisRevision = ++revision;
      const query = search.value.trim();
      try { await reportPromise; }
      catch (_) {
        status.textContent = '归档索引暂时无法加载，已显示的日报仍可阅读。刷新页面可重试。';
        more.hidden = true;
        return;
      }
      if (thisRevision !== revision) return;
      if (query && !searchIndex) {
        status.textContent = '正在加载全文索引…';
        grid.setAttribute('aria-busy', 'true');
        if (!searchPromise) searchPromise = fetch(root + 'data/search.json').then(response => {
          if (!response.ok) throw new Error('search index unavailable');
          return response.json();
        });
        try {
          searchIndex = await searchPromise;
          searchFailed = false;
        } catch (_) {
          searchFailed = true;
          searchPromise = null;
        }
        grid.removeAttribute('aria-busy');
        if (thisRevision !== revision) return;
      }
      const needle = query.toLocaleLowerCase();
      const matches = reports.filter(item =>
        (!month.value || item.date.startsWith(month.value)) &&
        (!topic || item.topics.includes(topic)) &&
        (!needle || (item.date + ' ' + item.headline + ' ' + item.summary + ' ' + (searchIndex?.[item.date] || '')).toLocaleLowerCase().includes(needle))
      );
      grid.innerHTML = matches.slice(0, limit).map(item => card(item, query)).join('');
      status.textContent = `${query || month.value || topic ? '找到' : '共'} ${matches.length} 期日报 · 按日期倒序${searchFailed && query ? '（全文索引加载失败，目前仅搜索标题与摘要；重新搜索可重试）' : ''}`;
      $('#empty-state').hidden = matches.length !== 0;
      more.hidden = matches.length <= limit;
      more.textContent = `继续浏览历史日报 · 还有 ${Math.max(0, matches.length - limit)} 期 ↓`;
      reset.hidden = !(query || month.value || topic);
      setTopic();
      const next = new URLSearchParams();
      if (query) next.set('q', query);
      if (month.value) next.set('month', month.value);
      if (topic) next.set('topic', topic);
      history.replaceState(null, '', location.pathname + (next.size ? '?' + next.toString() : '') + location.hash);
    }
    search.addEventListener('input', () => { limit = 12; clearTimeout(timer); timer = setTimeout(render, 160); });
    month.addEventListener('change', () => { limit = 12; render(); });
    topics.forEach(button => button.addEventListener('click', () => { topic = button.dataset.topic; limit = 12; render(); }));
    reset.addEventListener('click', () => { search.value = ''; month.value = ''; topic = ''; limit = 12; render(); search.focus(); });
    more.addEventListener('click', async () => {
      const previouslyVisible = grid.children.length;
      limit += 12;
      await render();
      grid.children[previouslyVisible]?.focus({preventScroll:true});
    });
    $('#search-form').addEventListener('submit', event => { event.preventDefault(); clearTimeout(timer); limit = 12; render(); });
    document.addEventListener('keydown', event => {
      const editable = event.target.isContentEditable || /INPUT|TEXTAREA|SELECT/.test(event.target.tagName);
      if (event.key === '/' && !editable) { event.preventDefault(); search.focus(); }
      if (event.key === 'Escape' && document.activeElement === search) { search.value = ''; limit = 12; render(); }
    });
    setTopic();
    render();
  }

  const top = $('.back-top');
  const progress = $('.reading-progress');
  function updateScroll() {
    const range = document.documentElement.scrollHeight - innerHeight;
    if (progress) progress.style.width = (range > 0 ? Math.min(100, scrollY / range * 100) : 0) + '%';
    top?.classList.toggle('visible', scrollY > 650);
  }
  window.addEventListener('scroll', updateScroll, {passive:true});
  window.addEventListener('resize', updateScroll, {passive:true});
  top?.addEventListener('click', () => window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'}));
  updateScroll();

  const tocDetails = $('.toc details');
  if (tocDetails && matchMedia('(max-width:760px)').matches) tocDetails.open = false;
  const tocLinks = [...document.querySelectorAll('.toc nav a')];
  if (tocLinks.length && 'IntersectionObserver' in window) {
    const linksByID = new Map(tocLinks.map(a => [decodeURIComponent(a.hash.slice(1)), a]));
    const observer = new IntersectionObserver(entries => {
      const heading = entries.find(entry => entry.isIntersecting);
      if (!heading) return;
      tocLinks.forEach(link => link.classList.remove('active'));
      linksByID.get(heading.target.id)?.classList.add('active');
    }, {rootMargin:'-100px 0px -65% 0px',threshold:0});
    document.querySelectorAll('.prose h2[id],.prose h3[id]').forEach(heading => observer.observe(heading));
  }
  const copy = $('#copy-link');
  copy?.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(location.href.split('#')[0]);
      copy.textContent = '链接已复制 ✓';
      setTimeout(() => { copy.textContent = '复制本期链接 ↗'; }, 2200);
    } catch (_) { copy.textContent = '可从浏览器地址栏复制链接'; }
  });
  if (window.katex) {
    document.querySelectorAll('.arithmatex').forEach(element => {
      const source = element.textContent;
      const displayMode = source.startsWith('\\[');
      const math = source.replace(/^\\[\[(]/, '').replace(/\\[\])]$/, '');
      try { window.katex.render(math, element, {displayMode,throwOnError:false,strict:false,trust:false}); }
      catch (_) { /* Preserve readable TeX if a historical formula is unsupported. */ }
    });
  }
})();
