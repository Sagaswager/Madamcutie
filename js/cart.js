// ==========================================================================
// SHOPPING CART STATE & LOGIC
// ==========================================================================

// Retrieve the cart from localStorage
function getCart() {
    const cart = localStorage.getItem('madamcutie_cart');
    return cart ? JSON.parse(cart) : [];
}

// Save the cart to localStorage and update indicators
function saveCart(cart) {
    localStorage.setItem('madamcutie_cart', JSON.stringify(cart));
    updateHeaderCartCount();
    // Dispatch a custom event to notify other scripts of cart changes
    window.dispatchEvent(new CustomEvent('cartUpdated', { detail: cart }));
}

// Add a product to the cart
function addToCart(productId, name, price, image, size = 'M', color = 'Alabaster', qty = 1) {
    const cart = getCart();
    
    // Check if the product already exists with the same options (size and color)
    const existingIndex = cart.findIndex(item => 
        item.id === productId && 
        item.size === size && 
        item.color === color
    );
    
    if (existingIndex > -1) {
        // Increment quantity
        cart[existingIndex].quantity += qty;
    } else {
        // Add new item
        cart.push({
            id: productId,
            name: name,
            price: price,
            image: image,
            size: size,
            color: color,
            quantity: qty
        });
    }
    
    saveCart(cart);
    showMiniCartNotification(name, image);
}

// Update the quantity of a specific item in the cart
function updateCartQty(productId, size, color, qty) {
    let cart = getCart();
    const index = cart.findIndex(item => 
        item.id === productId && 
        item.size === size && 
        item.color === color
    );
    
    if (index > -1) {
        if (qty <= 0) {
            // Remove item if quantity set to 0
            cart.splice(index, 1);
        } else {
            cart[index].quantity = qty;
        }
        saveCart(cart);
    }
}

// Remove an item from the cart
function removeFromCart(productId, size, color) {
    let cart = getCart();
    cart = cart.filter(item => 
        !(item.id === productId && item.size === size && item.color === color)
    );
    saveCart(cart);
}

// Clear the entire cart
function clearCart() {
    saveCart([]);
}

// Calculate total cart items count
function getCartCount() {
    const cart = getCart();
    return cart.reduce((total, item) => total + item.quantity, 0);
}

// Calculate grand total price
function getCartTotal() {
    const cart = getCart();
    return cart.reduce((total, item) => total + (item.price * item.quantity), 0);
}

// Update the cart count badge in the header
function updateHeaderCartCount() {
    const badges = document.querySelectorAll('.cart-count');
    const count = getCartCount();
    
    badges.forEach(badge => {
        badge.textContent = count;
        if (count === 0) {
            badge.style.display = 'none';
        } else {
            badge.style.display = 'flex';
        }
    });
}

// Show a temporary visual notification when an item is added
function showMiniCartNotification(name, image) {
    // Check if notification elements already exist, remove if so
    const existing = document.getElementById('mini-cart-notification');
    if (existing) existing.remove();
    
    const notification = document.createElement('div');
    notification.id = 'mini-cart-notification';
    notification.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #111111;
        color: #ffffff;
        border: 1px solid #c5a880;
        padding: 15px 25px;
        z-index: 9999;
        display: flex;
        align-items: center;
        gap: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transform: translateY(100px);
        opacity: 0;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        font-family: 'Plus Jakarta Sans', sans-serif;
    `;
    
    notification.innerHTML = `
        <div style="width: 40px; height: 50px; overflow:hidden;">
            <img src="${image}" style="width:100%; height:100%; object-fit:cover;" />
        </div>
        <div>
            <p style="font-size: 0.7rem; color: #c5a880; text-transform: uppercase; letter-spacing: 0.1em; font-weight:700;">Added to Bag</p>
            <p style="font-size: 0.85rem; font-weight:500;">${name}</p>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Trigger animation
    setTimeout(() => {
        notification.style.transform = 'translateY(0)';
        notification.style.opacity = '1';
    }, 50);
    
    // Dismiss after 3.5 seconds
    setTimeout(() => {
        notification.style.transform = 'translateY(100px)';
        notification.style.opacity = '0';
        setTimeout(() => notification.remove(), 400);
    }, 3500);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    updateHeaderCartCount();
});
