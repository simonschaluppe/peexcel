(() => {
  const versionsUrl = new URL('assets/preset-versions/', document.currentScript.src);

  function initializeCatalog(catalog) {
    catalog.querySelectorAll('[data-in-var]').forEach(label => {
      const link = document.createElement('a');
      link.href = 'glossary.html#in-' + encodeURIComponent(label.dataset.inVar);
      link.textContent = label.textContent;
      label.replaceWith(link);
    });
    const source = catalog.dataset.source;
    const prefix = source.toLowerCase();
    const form = catalog.querySelector('form');
    const query = catalog.querySelector(`#${prefix}-query`);
    const domain = catalog.querySelector(`#${prefix}-domain`);
    const entity = catalog.querySelector(`#${prefix}-entity`);
    const groups = [...catalog.querySelectorAll('.out-domain')];
    const normalize = value => value.toLocaleLowerCase('de').normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    const records = groups.map(group => ({group, rows: [...group.querySelectorAll('tbody tr')].map(row => ({
      row, text: normalize(row.textContent + ' ' + group.dataset.domain + ' ' + group.querySelector('summary').textContent),
    }))}));
    const total = records.reduce((sum, entry) => sum + entry.rows.length, 0);
    function filter() {
      const alternatives = normalize(query.value).split('|').map(term => term.trim().split(/\s+/).filter(Boolean)).filter(terms => terms.length);
      const active = alternatives.length || domain.value !== '*' || entity.value !== '*';
      let count = 0;
      records.forEach(({group, rows}) => {
        let matches = 0;
        rows.forEach(({row, text}) => {
          const visible = (domain.value === '*' || domain.value === group.dataset.domain)
            && (entity.value === '*' || entity.value === row.dataset.entity)
            && (!alternatives.length || alternatives.some(terms => terms.every(term => text.includes(term))));
          row.hidden = !visible;
          if (visible) matches++;
        });
        group.hidden = matches === 0;
        group.open = Boolean(active && matches);
        group.querySelector('.out-domain-count').textContent = `(${matches} / ${rows.length})`;
        count += matches;
      });
      catalog.querySelector(`#${prefix}-count`).textContent = `${count} von ${total} ${catalog.dataset.itemLabel || source + '-Variablen'}`;
      catalog.querySelector(`#${prefix}-empty`).hidden = count !== 0;
    }
    form.addEventListener('submit', event => event.preventDefault());
    form.addEventListener('input', filter);
    form.addEventListener('change', filter);
    form.addEventListener('reset', () => { query.value = ''; domain.value = '*'; entity.value = '*'; filter(); });
    catalog.querySelectorAll('[data-query]').forEach(button => button.addEventListener('click', () => {
      domain.value = '*'; entity.value = '*'; query.value = button.dataset.query; filter();
    }));
    catalog.querySelector(`#${prefix}-expand`).addEventListener('click', () => groups.forEach(group => { if (!group.hidden) group.open = true; }));
    catalog.querySelector(`#${prefix}-collapse`).addEventListener('click', () => groups.forEach(group => { group.open = false; }));
    function revealAnchor() {
      let id;
      try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
      const target = document.getElementById(id);
      if (!target || !catalog.contains(target) || !id.startsWith(`${prefix}-`)) return;
      query.value = ''; domain.value = '*'; entity.value = '*'; filter();
      const group = target.closest('.out-domain');
      if (group) group.open = true;
      target.scrollIntoView({block: 'start'});
    }
    form.hidden = false;
    filter();
    window.addEventListener('hashchange', revealAnchor);
    revealAnchor();
    return () => window.removeEventListener('hashchange', revealAnchor);
  }

  const content = document.getElementById('preset-catalog-content');
  document.querySelectorAll('.schema-catalog').forEach(catalog => {
    if (!content?.contains(catalog)) initializeCatalog(catalog);
  });

  const controls = document.querySelector('[data-preset-versions]');
  if (!controls || !content) return;

  const select = controls.querySelector('select');
  const status = controls.querySelector('[data-preset-version-status]');
  const current = controls.dataset.current;
  const currentHtml = content.innerHTML;
  const available = new Set([...select.options].map(option => option.value));
  let displayed = current;
  let dispose = initializeCatalog(content.querySelector('.schema-catalog'));

  async function showVersion(version) {
    if (!available.has(version) || version === displayed) return;
    select.disabled = true;
    content.setAttribute('aria-busy', 'true');
    status.hidden = true;
    try {
      let html = currentHtml;
      if (version !== current) {
        const response = await fetch(new URL(encodeURIComponent(version) + '.html', versionsUrl));
        if (!response.ok) throw new Error(response.statusText);
        html = await response.text();
      }
      const fragment = document.createElement('template');
      fragment.innerHTML = html;
      const catalog = fragment.content.querySelector('.schema-catalog[data-source="PRESET"]');
      if (!catalog) throw new Error('Preset catalog is missing');

      dispose();
      content.replaceChildren(catalog);
      dispose = initializeCatalog(catalog);
      displayed = version;
      const url = new URL(location.href);
      if (version === current) url.searchParams.delete('version');
      else url.searchParams.set('version', version);
      history.replaceState(history.state, '', url);
    } catch {
      status.textContent = document.documentElement.lang.startsWith('de')
        ? 'Die ausgewählte Version konnte nicht geladen werden.'
        : 'The selected version could not be loaded.';
      status.hidden = false;
    } finally {
      select.value = displayed;
      select.disabled = false;
      content.removeAttribute('aria-busy');
    }
  }

  controls.hidden = select.options.length <= 1;
  select.value = current;
  select.addEventListener('change', () => showVersion(select.value));
  const requested = new URLSearchParams(location.search).get('version');
  if (requested) showVersion(requested);
})();
