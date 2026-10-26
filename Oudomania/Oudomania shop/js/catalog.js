(() => {
    'use strict';

    const list = document.querySelector('[data-perfume-list]');
    if (!list) return;

    const money = (price) => `${new Intl.NumberFormat('ru-RU').format(price)} ₽`;
    const escapeHtml = (value) => String(value).replace(/[&<>"']/g, (char) => ({
        '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[char]);

    fetch('../data/perfumes.json')
        .then((response) => {
            if (!response.ok) throw new Error('Не удалось загрузить каталог');
            return response.json();
        })
        .then((perfumes) => {
            if (!Array.isArray(perfumes)) throw new Error('Неверный формат каталога');
            list.innerHTML = perfumes.map((perfume) => `
                <div class="col">
                    <article class="card border-0 shadow-sm h-100">
                        <button class="btn p-0 border-0 bg-transparent" type="button" data-perfume-detail="${escapeHtml(perfume.id)}" aria-label="Подробнее: ${escapeHtml(perfume.name)}">
                            <div class="card-img-wrapper"><img src="${escapeHtml(perfume.image)}" class="card-img-top" alt="${escapeHtml(perfume.brand)} ${escapeHtml(perfume.name)}" loading="lazy"></div>
                        </button>
                        <div class="card-body text-center">
                            <p class="text-uppercase text-muted small mb-1">${escapeHtml(perfume.brand)}</p>
                            <h2 class="h6 text-uppercase mb-2">${escapeHtml(perfume.name)}</h2>
                            <p class="fw-bold mb-3">${money(perfume.price)}</p>
                            <button class="btn btn-outline-dark btn-sm text-uppercase" type="button" data-quick-add="${escapeHtml(perfume.id)}">Подробнее</button>
                        </div>
                    </article>
                </div>`).join('');

            document.dispatchEvent(new CustomEvent('oudomania:catalog-ready', { detail: perfumes }));
        })
        .catch(() => {
            list.innerHTML = '<p class="text-danger">Не удалось загрузить каталог. Откройте сайт через локальный сервер.</p>';
        });

    document.addEventListener('oudomania:catalog-ready', (event) => {
        const perfumes = event.detail;
        const modalElement = document.getElementById('perfumeDetailModal');
        const modal = bootstrap.Modal.getOrCreateInstance(modalElement);
        const showDetail = (perfume) => {
            modalElement.querySelector('[data-detail-brand]').textContent = perfume.brand;
            modalElement.querySelector('[data-detail-name]').textContent = perfume.name;
            modalElement.querySelector('[data-detail-price]').textContent = money(perfume.price);
            modalElement.querySelector('[data-detail-description]').textContent = perfume.description;
            modalElement.querySelector('[data-detail-volume]').textContent = perfume.volume;
            modalElement.querySelector('[data-detail-gender]').textContent = perfume.gender;
            modalElement.querySelector('[data-detail-family]').textContent = perfume.family;
            modalElement.querySelector('[data-detail-notes]').textContent = perfume.notes;
            const image = modalElement.querySelector('[data-detail-image]');
            image.src = perfume.image;
            image.alt = `${perfume.brand} ${perfume.name}`;
            const addButton = modalElement.querySelector('[data-detail-add]');
            addButton.dataset.product = JSON.stringify(perfume);
            modal.show();
        };

        list.addEventListener('click', (clickEvent) => {
            const detailButton = clickEvent.target.closest('[data-perfume-detail]');
            if (detailButton) showDetail(perfumes.find((item) => item.id === detailButton.dataset.perfumeDetail));
            const addButton = clickEvent.target.closest('[data-quick-add]');
            if (addButton) showDetail(perfumes.find((item) => item.id === addButton.dataset.quickAdd));
        });
    });
})();
