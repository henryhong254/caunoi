// Force scroll to top on reload
if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}
window.scrollTo(0, 0);

window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    const progress = document.getElementById('progress');
    if(progress) progress.style.width = scrolled + '%';
    const stickyCta = document.getElementById('abs-bar');
    if (stickyCta) {
        if (!stickyCta.classList.contains('closed')) {
            stickyCta.classList.remove('hidden');
            stickyCta.style.display = 'block';
        } else {
            stickyCta.style.display = 'none';
        }
    }
});

function closeBar() {
    const stickyCta = document.getElementById('abs-bar');
    if(stickyCta) {
        stickyCta.classList.add('closed');
        stickyCta.style.display = 'none';
    }
}

// TYPEWRITER EFFECT
const phrases = [
  "BẠN ĐANG BÁN GÌ?",
  "BẠN GIÚP ĐƯỢC GÌ CHO HỌ?",
  "VÌ SAO PHẢI MUA TỪ BẠN?"
];
let phraseIndex = 0;
let charIndex = phrases[0].length;
let isDeleting = true;
const typewriterElement = document.getElementById('typewriter');

function typeEffect() {
  if (!typewriterElement) return;
  const currentPhrase = phrases[phraseIndex];
  
  if (isDeleting) {
    typewriterElement.textContent = currentPhrase.substring(0, charIndex - 1);
    charIndex--;
  } else {
    typewriterElement.textContent = currentPhrase.substring(0, charIndex + 1);
    charIndex++;
  }
  
  let typeSpeed = isDeleting ? 25 : 50; 
  
  if (!isDeleting && charIndex === currentPhrase.length) {
    typeSpeed = 1500; 
    isDeleting = true;
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    phraseIndex = (phraseIndex + 1) % phrases.length;
    typeSpeed = 300; 
  }
  
  setTimeout(typeEffect, typeSpeed);
}
if(typewriterElement && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    setTimeout(typeEffect, 1200);
}

// Reserve the actual bar height, including mobile safe-area padding.
const ctaBar = document.getElementById('abs-bar');
if (ctaBar) {
  new ResizeObserver(() => {
    document.documentElement.style.setProperty('--sticky-cta-height', `${ctaBar.getBoundingClientRect().height}px`);
  }).observe(ctaBar);
}
