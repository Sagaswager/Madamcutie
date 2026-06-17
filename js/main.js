/**
 * Madamcutie Main JavaScript
 */

function toggleMobileNav() {
    const drawer = document.getElementById('mobile-nav');
    const overlay = document.getElementById('mobile-nav-overlay');
    
    if (drawer && overlay) {
        drawer.classList.toggle('open');
        overlay.classList.toggle('open');
        document.body.style.overflow = drawer.classList.contains('open') ? 'hidden' : '';
    }
}

// Header scroll effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (header) {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
});

document.addEventListener('DOMContentLoaded', () => {
    // Mobile search toggle (if exists)
    const searchTrigger = document.getElementById('search-trigger');
    const searchBar = document.getElementById('search-bar-container');
    
    if (searchTrigger && searchBar) {
        searchTrigger.addEventListener('click', (e) => {
            e.preventDefault();
            searchBar.style.display = searchBar.style.display === 'none' ? 'block' : 'none';
        });
    }

    // Close mobile nav on link click
    const mobileLinks = document.querySelectorAll('.mobile-nav-links a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            const drawer = document.getElementById('mobile-nav');
            if (drawer && drawer.classList.contains('open')) {
                toggleMobileNav();
            }
        });
    });
});
