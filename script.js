document.addEventListener('DOMContentLoaded', () => {
    // Reveal Animations on Scroll
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, {
        root: null,
        threshold: 0.15, // Trigger when 15% visible
        rootMargin: "0px 0px -50px 0px"
    });

    revealElements.forEach(el => revealObserver.observe(el));

    // Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Parallax Effect for Hero Backgrounds
    const heroVideoContainer = document.querySelector('.hero-video-container');
    if (heroVideoContainer) {
        window.addEventListener('scroll', () => {
            const scrollValue = window.scrollY;
            if (scrollValue < window.innerHeight) {
                // Move container slower than scroll
                heroVideoContainer.style.transform = `translateY(${scrollValue * 0.5}px)`;
            }
        });
    }

    // Hero Video & Image Lazy Loader
    function initializeHeroBackgrounds() {
        // Handle Video (Homepage)
        const heroVideo = document.getElementById('heroVideo');
        const placeholder = document.getElementById('heroPlaceholder');

        if (heroVideo && placeholder) {
            const videoSrc = 'assets/Video.mp4';

            heroVideo.src = videoSrc;
            heroVideo.load();

            // Use 'canplay' to trigger the transition as soon as basic video is ready
            heroVideo.addEventListener('canplay', () => {
                heroVideo.play().then(() => {
                    heroVideo.classList.add('loaded');
                    setTimeout(() => {
                        placeholder.classList.add('hidden');
                    }, 600);
                }).catch(e => console.warn('Autoplay prevented:', e));
            }, { once: true });
        }

        // Handle Images (Other pages)
        const heroImages = document.querySelectorAll('img.hero-bg');
        heroImages.forEach(img => {
            if (img.complete) {
                img.classList.add('loaded');
            } else {
                img.addEventListener('load', () => {
                    img.classList.add('loaded');
                });
            }
        });
    }

    initializeHeroBackgrounds();

    // Mobile Navbar Toggle
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.classList.toggle('no-scroll');
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.classList.remove('no-scroll');
            });
        });
    }

    // Scroll to Top Button
    const scrollToTopBtn = document.getElementById('scrollToTop');
    if (scrollToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                scrollToTopBtn.classList.add('visible');
            } else {
                scrollToTopBtn.classList.remove('visible');
            }
        });

        scrollToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});
