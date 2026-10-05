/* Shared behaviour: language (EN/HI), theme, expand/collapse all.
   Language choice is stored under 'ks_lang' and is shared with the Karma Siddhant page. */
(function(){
  var d=document.documentElement;
  function getLang(){try{var l=localStorage.getItem('ks_lang');if(l)return l}catch(e){}return (navigator.language||'').indexOf('hi')===0?'hi':'en'}
  function setLang(l){d.lang=l;try{localStorage.setItem('ks_lang',l)}catch(e){}
    document.querySelectorAll('[data-l]').forEach(function(b){b.classList.toggle('on',b.dataset.l===l)});
    var t=document.querySelector('title');if(t){var x=t.dataset[l];if(x)document.title=x}}
  d.lang=getLang();
  document.addEventListener('DOMContentLoaded',function(){
    setLang(d.lang);
    document.querySelectorAll('[data-l]').forEach(function(b){b.onclick=function(){setLang(b.dataset.l)}});
    var th=document.getElementById('bTheme');
    if(th)th.onclick=function(){var dark=d.dataset.theme?d.dataset.theme==='dark':matchMedia('(prefers-color-scheme:dark)').matches;d.dataset.theme=dark?'light':'dark'};
    var ex=document.getElementById('bExpand');
    if(ex){var open=true;ex.onclick=function(){open=!open;document.querySelectorAll('details.ex').forEach(function(x){x.open=open});
      ex.querySelector('.en').textContent=open?'Collapse all':'Expand all';ex.querySelector('.hi').textContent=open?'सब समेटें':'सब खोलें'}}
  });
})();
