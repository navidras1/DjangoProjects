document.addEventListener('DOMContentLoaded', () => {
    const cartItems = document.querySelectorAll('.cart-item');

    cartItems.forEach(itemEl => {
        const productId = itemEl.dataset.productId;

        itemEl.querySelectorAll('[data-action]').forEach(btn => {
            btn.addEventListener('click', () => {
                const action = btn.dataset.action;

                if (action === 'remove') {
                    removeFromCart(productId, itemEl);
                } else if (action === 'increase' || action === 'decrease') {
                    changeQuantity(productId, action, itemEl);
                }
            });
        });
    });

    // ✅ Clear Cart handler
    const clearBtn = document.getElementById('clear-cart-btn');
    if (clearBtn) {
        clearBtn.addEventListener('click', () => {
            if (!confirm('Remove all items from your cart?')) return;
            clearCart();
        });
    }
});

function changeQuantity(productId, action, itemEl) {
    const qtyEl = itemEl.querySelector('.cart-item__qty-value');
    let qty = parseInt(qtyEl.textContent, 10);

    qty = action === 'increase' ? qty + 1 : Math.max(1, qty - 1);

    fetch('/cart/update_cart/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ product_id: productId, quantity: qty }),
    })
    .then(res => res.json())
    .then(data => {
        if (!data.success) return;
        window.location.reload();
    })
    .catch(err => console.error(err));
}

function removeFromCart(productId, itemEl) {
    fetch('/cart/delete_cart/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ product_id: productId }),
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            itemEl.remove();
            window.location.reload();
        }
    })
    .catch(err => console.error(err));
}

// ✅ Clear entire cart
function clearCart() {
    fetch('/cart/clear/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
    })
    .then(data => {
        if (data.success) {
            window.location.reload();
        }
    })
    .catch(err => {
        console.error('Clear cart failed:', err);
        alert('Failed to clear cart');
    });
}

function getCookie(name) {
    const cookie = document.cookie
        .split('; ')
        .find(row => row.startsWith(name + '='));
    return cookie ? decodeURIComponent(cookie.split('=')[1]) : null;
}