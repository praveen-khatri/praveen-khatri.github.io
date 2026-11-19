/* Accessible progressive enhancement, no libraries or trackers. */
(() => {
  const menu = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('#primary-navigation');
  if (menu && nav) {
    const close = () => { menu.setAttribute('aria-expanded','false'); nav.classList.remove('open'); document.body.classList.remove('menu-open'); };
    menu.addEventListener('click', () => {
      const expanded = menu.getAttribute('aria-expanded') === 'true';
      menu.setAttribute('aria-expanded',String(!expanded)); nav.classList.toggle('open',!expanded);
      document.body.classList.toggle('menu-open',!expanded);
    });
    nav.addEventListener('click', (e) => { if (e.target.closest('a')) close(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
    window.addEventListener('resize', () => { if (window.innerWidth > 820) close(); });
  }
  document.querySelectorAll('[data-year]').forEach(node => { node.textContent = new Date().getFullYear(); });
  const filters = [...document.querySelectorAll('[data-filter]')];
  const items = [...document.querySelectorAll('[data-publication]')];
  const search = document.querySelector('#publication-search');
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-state');
  let selected = 'all';
  function filter() {
    const q = (search?.value || '').trim().toLocaleLowerCase();
    let visible=0;
    items.forEach(item => {
      const type=item.dataset.category||'';
      const matches=(selected==='all'||type===selected) && (!q || item.textContent.toLocaleLowerCase().includes(q));
      item.hidden=!matches; if(matches) visible++;
    });
    if (count) count.textContent = `${visible} ${visible===1?'entry':'entries'} shown`;
    if (empty) empty.classList.toggle('show',visible===0);
  }
  if(items.length){
    filters.forEach(btn=>btn.addEventListener('click',()=>{selected=btn.dataset.filter;filters.forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));filter();}));
    search?.addEventListener('input',filter); filter();
  }
  async function copy(text, button) {
    let success = false;
    try { await navigator.clipboard.writeText(text); success = true; }
    catch(e) { try{const ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.opacity='0';document.body.append(ta);ta.select();success=document.execCommand('copy');ta.remove();}catch(_e){} }
    if (success && button) { const original=button.textContent; button.textContent='Copied!'; setTimeout(()=>{button.textContent=original;},1800); }
  }
  document.addEventListener('click',e=>{
    const button=e.target.closest('[data-copy-citation]');
    if(button){const paper=button.closest('[data-publication]');if(paper) copy(paper.dataset.citation||'',button);}
    const email=e.target.closest('[data-copy-email]');if(email) copy('praveen.khatri@utoronto.ca',email);
  });
})();
