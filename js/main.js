// ==========================================================================
// MADAMCUTIE GENERAL UI & INTERACTIONS
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
    // 1. Sticky Header Control
    const header = document.querySelector('.header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // 2. Mobile Drawer Navigation Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-toggle');
    const drawerCloseBtn = document.querySelector('.drawer-close-btn');
    const mobileNavDrawer = document.getElementById('mobile-nav-drawer');
    const overlay = document.getElementById('mobile-nav-overlay');

    function toggleDrawer(isOpen) {
        if (isOpen) {
            mobileNavDrawer.classList.add('open');
            overlay.classList.add('open');
            document.body.style.overflow = 'hidden'; // Stop background scrolling
        } else {
            mobileNavDrawer.classList.remove('open');
            overlay.classList.remove('open');
            document.body.style.overflow = '';
        }
    }

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', () => toggleDrawer(true));
    if (drawerCloseBtn) drawerCloseBtn.addEventListener('click', () => toggleDrawer(false));
    if (overlay) overlay.addEventListener('click', () => toggleDrawer(false));

    // 3. Newsletter Subscription Feedback
    const footerNewsletter = document.querySelector('.footer-col form');
    if (footerNewsletter) {
        footerNewsletter.addEventListener('submit', (e) => {
            e.preventDefault();
            const input = footerNewsletter.querySelector('input[type="email"]');
            if (input && input.value.trim() !== '') {
                showModalAlert('Thank You!', `You have successfully subscribed to our newsletter with email: <strong>${input.value}</strong>. Get ready for exclusive updates.`, 'success');
                input.value = '';
            }
        });
    }

    // 4. Modal Alert Dialog Utility (replaces default alert for aesthetics)
    window.showModalAlert = function(title, message, type = 'info') {
        const existing = document.getElementById('custom-alert-modal');
        if (existing) existing.remove();

        const modal = document.createElement('div');
        modal.id = 'custom-alert-modal';
        modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(17,17,17,0.8);
            z-index: 99999;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            font-family: 'Plus Jakarta Sans', sans-serif;
        `;

        const accentColor = type === 'success' ? '#2e8b57' : (type === 'error' ? '#b22222' : '#c5a880');

        modal.innerHTML = `
            <div style="background-color: #ffffff; width: 100%; max-width: 450px; padding: 40px var(--spacing-lg); text-align: center; border: 1px solid ${accentColor}; box-shadow: 0 20px 50px rgba(0,0,0,0.3); transform: scale(0.9); transition: all 0.3s ease;">
                <h3 style="font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 15px; color: #111111;">${title}</h3>
                <p style="font-size: 0.95rem; color: #666666; margin-bottom: 25px; line-height: 1.6;">${message}</p>
                <button class="btn btn-primary" id="custom-alert-close-btn" style="width: 100%;">CONTINUE</button>
            </div>
        `;

        document.body.appendChild(modal);
        
        // Trigger scale animation
        setTimeout(() => {
            modal.firstElementChild.style.transform = 'scale(1)';
        }, 50);

        const closeBtn = modal.querySelector('#custom-alert-close-btn');
        closeBtn.addEventListener('click', () => {
            modal.firstElementChild.style.transform = 'scale(0.9)';
            modal.style.opacity = '0';
            setTimeout(() => modal.remove(), 250);
        });
    };
});

// Helper function to format price currency
function formatPrice(number) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(number);
}
