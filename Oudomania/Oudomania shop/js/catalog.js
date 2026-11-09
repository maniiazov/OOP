(() => {
    'use strict';

    const list = document.querySelector('[data-perfume-list]');
    if (!list) return;

    const storageKey = 'oudomania-perfumes-v1';
    const managerStatus = document.querySelector('[data-catalog-status]');
    const form = document.querySelector('[data-product-form]');
    const editorElement = document.getElementById('productEditorModal');
    const editor = bootstrap.Modal.getOrCreateInstance(editorElement);
    let perfumes = [];

    document.addEventListener('DOMContentLoaded', () => {
        document.querySelector('main h1')?.classList.add('catalog-title-enter');
    });

    const money = (price) => `${new Intl.NumberFormat('ru-RU').format(price)} ₽`;
    const escapeHtml = (value) => String(value).replace(/[&<>"']/g, (char) => ({
        '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[char]);
    const makeId = (brand, name) => `${brand}-${name}`.toLowerCase()
        .replace(/[^a-zа-яё0-9]+/gi, '-')
        .replace(/^-|-$/g, '') || `aroma-${Date.now()}`;

    list.addEventListener('pointerover', (event) => {
        const image = event.target.closest('.card-img-top');
        if (!image || image.contains(event.relatedTarget)) return;
        image.classList.remove('perfume-image-wiggle');
        void image.offsetWidth;
        image.classList.add('perfume-image-wiggle');
    });

    list.addEventListener('click', (event) => {
        const card = event.target.closest('.card');
        if (!card || event.target.closest('[data-product-edit], [data-product-delete]')) return;
        card.classList.remove('perfume-card-tap');
        void card.offsetWidth;
        card.classList.add('perfume-card-tap');
    });

    list.addEventListener('animationend', (event) => {
        event.target.classList.remove('perfume-image-wiggle', 'perfume-card-tap');
    });

    const persist = () => {
        try {
            localStorage.setItem(storageKey, JSON.stringify(perfumes));
            managerStatus.textContent = 'Изменения сохранены в этом браузере.';
        } catch {
            managerStatus.textContent = 'Браузер не разрешил сохранить изменения. Проверьте настройки хранилища.';
        }
    };

    const render = () => {
        list.innerHTML = perfumes.length ? perfumes.map((perfume) => `
            <div class="col">
                <article class="card border-0 shadow-sm h-100">
                    <button class="btn p-0 border-0 bg-transparent" type="button" data-perfume-detail="${escapeHtml(perfume.id)}" aria-label="Подробнее: ${escapeHtml(perfume.name)}">
                        <div class="card-img-wrapper"><img src="${escapeHtml(perfume.image)}" class="card-img-top" alt="${escapeHtml(perfume.brand)} ${escapeHtml(perfume.name)}" loading="lazy"></div>
                    </button>
                    <div class="card-body text-center">
                        <p class="text-uppercase text-muted small mb-1">${escapeHtml(perfume.brand)}</p>
                        <h2 class="h6 text-uppercase mb-2">${escapeHtml(perfume.name)}</h2>
                        <p class="fw-bold mb-3">${money(perfume.price)}</p>
                        <div class="d-flex justify-content-center gap-2 flex-wrap">
                            <button class="btn btn-outline-dark btn-sm text-uppercase" type="button" data-quick-add="${escapeHtml(perfume.id)}">Подробнее</button>
                            <button class="btn btn-outline-secondary btn-sm" type="button" data-product-edit="${escapeHtml(perfume.id)}">Изменить</button>
                            <button class="btn btn-outline-danger btn-sm" type="button" data-product-delete="${escapeHtml(perfume.id)}">Удалить</button>
                        </div>
                    </div>
                </article>
            </div>`).join('') : '<div class="col-12"><p class="text-muted py-5 text-center">В каталоге пока нет ароматов. Добавьте первый товар.</p></div>';

        list.querySelectorAll('.col').forEach((card, index) => {
            card.classList.add('catalog-card-enter');
            card.style.setProperty('--card-order', index);
        });
        document.dispatchEvent(new CustomEvent('oudomania:catalog-ready', { detail: perfumes }));
    };

    const openEditor = (perfume = null) => {
        form.reset();
        form.elements.id.value = perfume?.id || '';
        document.querySelector('[data-editor-title]').textContent = perfume ? 'Изменить аромат' : 'Новый аромат';
        ['brand', 'name', 'price', 'volume', 'gender', 'family', 'notes', 'image', 'description'].forEach((key) => {
            form.elements[key].value = perfume?.[key] ?? '';
        });
        editor.show();
    };

    document.querySelector('[data-product-create]').addEventListener('click', () => openEditor());
    list.addEventListener('click', (event) => {
        const editButton = event.target.closest('[data-product-edit]');
        if (editButton) {
            openEditor(perfumes.find((item) => item.id === editButton.dataset.productEdit));
            return;
        }
        const deleteButton = event.target.closest('[data-product-delete]');
        if (deleteButton) {
            const product = perfumes.find((item) => item.id === deleteButton.dataset.productDelete);
            if (!product || !window.confirm(`Удалить аромат «${product.brand} ${product.name}»?`)) return;
            perfumes = perfumes.filter((item) => item.id !== product.id);
            persist();
            render();
        }
    });

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        if (!form.reportValidity()) return;
        const data = new FormData(form);
        const brand = String(data.get('brand')).trim();
        const name = String(data.get('name')).trim();
        const existingId = String(data.get('id'));
        let id = existingId || makeId(brand, name);
        if (!existingId && perfumes.some((item) => item.id === id)) id = `${id}-${Date.now().toString(36)}`;
        const product = {
            id, brand, name, price: Number(data.get('price')),
            volume: String(data.get('volume')).trim(), gender: String(data.get('gender')).trim(),
            family: String(data.get('family')).trim(), notes: String(data.get('notes')).trim(),
            image: String(data.get('image')).trim(), description: String(data.get('description')).trim()
        };
        if (!Number.isFinite(product.price) || product.price <= 0) return;
        perfumes = existingId
            ? perfumes.map((item) => item.id === existingId ? product : item)
            : [...perfumes, product];
        persist();
        render();
        editor.hide();
    });

    fetch('../data/perfumes.json')
        .then((response) => {
            if (!response.ok) throw new Error('Не удалось загрузить каталог');
            return response.json();
        })
        .then((initialPerfumes) => {
            if (!Array.isArray(initialPerfumes)) throw new Error('Неверный формат каталога');
            try {
                const saved = JSON.parse(localStorage.getItem(storageKey));
                perfumes = Array.isArray(saved) ? saved : initialPerfumes;
            } catch {
                perfumes = initialPerfumes;
            }
            render();
        })
        .catch(() => {
            list.innerHTML = '<p class="text-danger">Не удалось загрузить каталог. Откройте сайт через локальный сервер.</p>';
            managerStatus.textContent = 'Для работы каталога откройте сайт через локальный сервер.';
        });

    const modalElement = document.getElementById('perfumeDetailModal');
    const detailModal = bootstrap.Modal.getOrCreateInstance(modalElement);
    const showDetail = (perfume) => {
        if (!perfume) return;
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
        modalElement.querySelector('[data-detail-add]').dataset.product = JSON.stringify(perfume);
        detailModal.show();
    };

    list.addEventListener('click', (event) => {
        const detailButton = event.target.closest('[data-perfume-detail]');
        const quickAddButton = event.target.closest('[data-quick-add]');
        if (detailButton) showDetail(perfumes.find((item) => item.id === detailButton.dataset.perfumeDetail));
        if (quickAddButton) showDetail(perfumes.find((item) => item.id === quickAddButton.dataset.quickAdd));
    });
})();
