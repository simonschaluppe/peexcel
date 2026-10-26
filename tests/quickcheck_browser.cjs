/* Real-browser POC acceptance and reproducible desktop/mobile-emulation timing.
 * PLAYWRIGHT_MODULE may point at an installed Playwright package.
 * CHROME_EXECUTABLE may select the locally installed browser.
 * node tests/quickcheck_browser.cjs path/to/index.html output-directory
 */
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const assert = require('node:assert/strict');

(async()=>{
 const url=/^https?:/.test(process.argv[2])?process.argv[2]:pathToFileURL(path.resolve(process.argv[2])).href;
 const out=path.resolve(process.argv[3]);
 fs.mkdirSync(out,{recursive:true});
 const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_EXECUTABLE});
 const results=[];
 try {
  for(const mobile of [false,true]){
   const context=await browser.newContext({viewport:mobile?{width:390,height:844}:{width:1440,height:1000},isMobile:mobile,hasTouch:mobile,deviceScaleFactor:1});
   const page=await context.newPage(), errors=[], requests=[];
   page.on('pageerror',e=>errors.push(e.message));
   page.on('request',r=>{if(/^https?:/.test(r.url())&&r.url()!==url)requests.push(r.url());});
   const start=performance.now();
   await page.goto(url);
   await page.evaluate(()=>window.quickCheck.ready);
   const loadMs=performance.now()-start;
   const result=await page.evaluate(async()=>{
    const q=window.quickCheck,n=q.dataset.scenarios.length,scenarios=q.dataset.scenarios;
    const assert=(ok,msg)=>{if(!ok)throw Error(msg);};
    assert(n>0,'No scenarios');
    assert(document.querySelectorAll('#choices input').length<=80,'Unbounded DOM');
    const s=scenarios[0], f={geometry:new Set([s.filters.geometry]),pv:new Set([s.filters.pv])};
    const expected=scenarios.filter(x=>x.filters.geometry===s.filters.geometry&&x.filters.pv===s.filters.pv);
    assert(q.filtered('',f).length===expected.length,'AND filter');
    const pv=[...new Set(scenarios.map(x=>x.filters.pv))].slice(0,2);
    assert(q.filtered('',{pv:new Set(pv)}).length===scenarios.filter(x=>pv.includes(x.filters.pv)).length,'OR filter');
    assert(q.filtered('not-a-scenario-XYZ').length===0,'Search');
    const before=[...q.selection];q.filters.geometry.add(s.filters.geometry);q.refreshFilters();
    assert(JSON.stringify([...q.selection])===JSON.stringify(before),'Filter changed selection');
    q.filters.geometry.clear();q.refreshFilters();
    await q.whenIdle();
    assert(q.addMatches()===true,'Bulk selection failed');
    await q.whenIdle();
    assert(q.selection.size===n,'Selection is capped');
    assert(document.querySelectorAll('#selected li').length<=80,'Unbounded selection DOM');
    const sampleTimes=[];
    for(let i=0;i<100;i++){const t=performance.now();q.filtered('',f);sampleTimes.push(performance.now()-t);}
    sampleTimes.sort((a,b)=>a-b);
    const renderMs={};
    for(const count of [...new Set([1,5,10,20,21,100,n])]){
     if(count>n)continue;
     q.selection.clear();scenarios.slice(0,count).forEach(s=>q.selection.add(s.id));
     const times=[];
     for(let repeat=0;repeat<1;repeat++){const t=performance.now();await q.update();times.push(performance.now()-t);}
     renderMs[count]=times;
    }
    assert(Object.keys(q.dataset.analysis).length===5,'Missing analysis charts');
    for(const key of Object.keys(q.dataset.analysis)){
     const fig=q.composeAnalysis(key,scenarios,800);
     assert(fig.data.reduce((n,t)=>n+t.x.length,0)===n,'Missing analysis scenarios: '+key);
     await Plotly.react(document.getElementById('analysis'),fig.data,fig.layout);
    }
    const C=q.dataset.columns, raw=s.values.slice();
    const adjusted=q.contextValues(s,{bgf:2000,gf:1000,renovation:50});
    const density=-Math.min(raw[C.cfd_fPE]*(raw[C.cfd_A]/(2+raw[C.cfd_dx])-raw[C.cfd_EUI]),raw[C.cfd_cutoff]);
    assert(Math.abs(adjusted.values[C.context_factor_density]-density)<1e-10,'Density');
    assert(adjusted.values[C.PEI_cf_renovation]===raw[C.cfr_budget]/2,'Renovation');
    assert(JSON.stringify(s.values)===JSON.stringify(raw),'Mutated originals');
    assert(adjusted.values[C.GWP_lc_total]===raw[C.GWP_lc_total],'Changed THG');
    for(const invalid of [{bgf:0,gf:10},{bgf:10},{renovation:101},{renovation:NaN}]){
     let failed=false;try{q.contextValues(s,invalid);}catch(e){failed=true;}assert(failed,'Invalid context accepted');
    }
    const pe=q.compose('pe',[s],800);
    for(const t of pe.data.filter(t=>t.meta))assert(t.y[0]===Math.abs(s.values[t.meta.column]),'PE rendering differs from Python absolute convention');
    q.selection.clear();q.dataset.defaults.forEach(i=>q.selection.add(i));await q.update();
    return {scenarios:n,initializationMs:q.initializationMs,filterMedianMs:sampleTimes[50],filterP95Ms:sampleTimes[95],renderMs,
     heap:performance.memory?{used:performance.memory.usedJSHeapSize,total:performance.memory.totalJSHeapSize}:null,
     userAgent:navigator.userAgent,contextSample:adjusted.values};
   });
   assert.deepEqual(errors,[]);assert.deepEqual(requests,[],'External network required');
   await page.screenshot({path:path.join(out,mobile?'mobile.png':'desktop.png'),fullPage:true});
   results.push({profile:mobile?'mobile viewport emulation (desktop CPU)':'desktop',loadMs,...result});
   await context.close();
  }
  fs.writeFileSync(path.join(out,'browser-performance.json'),JSON.stringify({url,browser:browser.version(),results},null,2));
  console.log(JSON.stringify(results.map(({contextSample,...r})=>r),null,2));
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
