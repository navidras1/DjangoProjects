
var addToCart = function (productId) {
    const url = `/ecom/addToCart/`;
    const csrfToken = getCookie('csrftoken');

    const qtySelect = document.getElementById('quantity');
    const quantity = qtySelect ? qtySelect.value : 1;

    // Form-encoded body (Django reads from request.POST)
    const body = new URLSearchParams();
    body.append('product_id', productId);
    body.append('quantity', quantity);

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: body.toString(),
    })
    .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
    })
    .then(data => {
        console.log('Success:', data);
        const badge = document.getElementById('cart-qty');

        // if (badge && data.cart_count !== undefined) {
            badge.textContent = data.cart_count;
        // }
        // Update cart badge, show toast, etc.
    })
    .catch(err => {
        console.error('Error:', err);
        alert('Failed to add to cart');
    });
};

function getCookie(name) {
    const cookie = document.cookie
        .split('; ')
        .find(row => row.startsWith(name + '='));
    return cookie ? decodeURIComponent(cookie.split('=')[1]) : null;
}