// ヘッダーの切り替え・モバイルメニュー・スクロール表示
(function(){
  var hd=document.querySelector('.hd'),hero=document.querySelector('.hero');
  function onScroll(){
    if(!hd||hd.classList.contains('sub'))return;
    var th=hero?hero.offsetHeight-80:40;
    hd.classList.toggle('solid',window.scrollY>th);
  }
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();

  var bg=document.querySelector('.burger'),mn=document.querySelector('.mnav');
  if(bg&&mn){
    bg.addEventListener('click',function(){
      var o=!mn.classList.contains('open');
      mn.classList.toggle('open',o);bg.classList.toggle('open',o);hd.classList.toggle('menu',o);
      bg.setAttribute('aria-expanded',o?'true':'false');
      document.body.style.overflow=o?'hidden':'';
    });
    mn.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){bg.click();});});
  }

  var els=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:.08});
    els.forEach(function(el){io.observe(el);});
  }else{els.forEach(function(el){el.classList.add('on');});}
})();
