(() => {
    'use strict';

    const CART_KEY = 'oudomania-cart';
    const readCart = () => {
        try {
            const saved = JSON.parse(localStorage.getItem(CART_KEY) || '[]');
            return Array.isArray(saved) ? saved : [];
        } catch {
            return [];
        }
    };
    const saveCart = (cart) => localStorage.setItem(CART_KEY, JSON.stringify(cart));
    const formatPrice = (price) => `${new Intl.NumberFormat('ru-RU').format(price)} ₽`;

    function updateCartBadges(cart) {
        const count = cart.reduce((sum, item) => sum + item.quantity, 0);
        document.querySelectorAll('a[href$="cart.html"]').forEach((link) => {
            let badge = link.querySelector('[data-cart-count]');
            if (!badge) {
                badge = document.createElement('span');
                badge.dataset.cartCount = '';
                badge.className = 'badge rounded-pill bg-dark ms-1';
                link.append(badge);
            }
            badge.textContent = count;
            badge.setAttribute('aria-label', `Товаров в корзине: ${count}`);
        });
    }

    function getProduct(button) {
        const card = button.closest('.card');
        if (!card) return null;
        const name = card.querySelector('h5, h6')?.textContent.trim();
        const priceText = card.querySelector('.fw-semibold, .fw-bold')?.textContent || '';
        const price = Number(priceText.replace(/[^\d]/g, ''));
        const image = card.querySelector('img')?.getAttribute('src') || '';
        const brand = card.querySelector('.text-uppercase.text-muted')?.textContent.trim() || '';
        if (!name || !price) return null;
        return { id: `${brand}-${name}`.toLowerCase(), name, brand, price, image, quantity: 1 };
    }

    function renderCart() {
        const container = document.querySelector('[data-cart-items]');
        if (!container) return;
        const cart = readCart();
        const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
        container.innerHTML = cart.length ? cart.map((item) => `
            <article class="d-flex align-items-center gap-3 py-3 border-bottom" data-cart-item="${item.id}">
                ${item.image ? `<img src="${item.image}" alt="" width="72" height="84" class="object-fit-contain bg-light">` : ''}
                <div class="flex-grow-1">
                    <p class="text-muted small mb-1">${item.brand}</p>
                    <h3 class="h6 mb-1">${item.name}</h3>
                    <p class="mb-0">${formatPrice(item.price)}</p>
                </div>
                <div class="d-flex align-items-center gap-2">
                    <button type="button" class="btn btn-sm btn-outline-dark" data-quantity="-1" aria-label="Уменьшить количество">−</button>
                    <span>${item.quantity}</span>
                    <button type="button" class="btn btn-sm btn-outline-dark" data-quantity="1" aria-label="Увеличить количество">+</button>
                </div>
                <button type="button" class="btn btn-sm text-muted" data-remove aria-label="Удалить ${item.name}">Удалить</button>
            </article>`).join('') : '<p class="text-muted py-4 mb-0">Корзина пока пуста. Выберите аромат в каталоге.</p>';
        const totalElement = document.querySelector('[data-cart-total]');
        if (totalElement) totalElement.textContent = formatPrice(total);
        const checkout = document.querySelector('[data-checkout]');
        if (checkout) checkout.hidden = !cart.length;
        updateCartBadges(cart);
    }

    document.addEventListener('click', (event) => {
        const addButton = event.target.closest('[data-cart-add]');
        if (addButton) {
            const product = getProduct(addButton);
            if (!product) return;
            const cart = readCart();
            const existing = cart.find((item) => item.id === product.id);
            if (existing) existing.quantity += 1;
            else cart.push(product);
            saveCart(cart);
            updateCartBadges(cart);
            const original = addButton.textContent;
            addButton.textContent = 'Добавлено ✓';
            window.setTimeout(() => { addButton.textContent = original; }, 1200);
            return;
        }

        const row = event.target.closest('[data-cart-item]');
        if (!row) return;
        const cart = readCart();
        const item = cart.find((entry) => entry.id === row.dataset.cartItem);
        if (!item) return;
        if (event.target.closest('[data-remove]')) {
            saveCart(cart.filter((entry) => entry.id !== item.id));
        } else {
            item.quantity += Number(event.target.closest('[data-quantity]')?.dataset.quantity || 0);
            saveCart(cart.filter((entry) => entry.quantity > 0));
        }
        renderCart();
    });

    renderCart();
})();
