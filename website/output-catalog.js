(() => {
  document.querySelectorAll('.schema-catalog').forEach(catalog => {
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
  });
})();
