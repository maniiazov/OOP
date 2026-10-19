(() => {
    'use strict';

    const fullNamePattern = /^[а-яё]+(?:[ -][а-яё]+){1,2}$/i;
    const phonePattern = /^(?:\+7|8)?[\s()-]*\d(?:[\s()-]*\d){9}$/;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    document.querySelectorAll('.oudomania-signup').forEach((form) => {
        const fullName = form.elements.name;
        const phone = form.elements.phone;
        const email = form.elements.email;
        const successMessage = form.querySelector('.signup-success');

        form.addEventListener('submit', (event) => {
            event.preventDefault();
            successMessage.textContent = '';

            fullName.setCustomValidity(fullNamePattern.test(fullName.value.trim()) ? '' : 'Проверьте ФИО.');
            phone.setCustomValidity(phonePattern.test(phone.value.trim()) ? '' : 'Проверьте номер телефона.');
            email.setCustomValidity(emailPattern.test(email.value.trim()) ? '' : 'Проверьте адрес почты.');
            form.classList.add('was-validated');

            if (!form.checkValidity()) {
                form.querySelector(':invalid')?.focus();
                return;
            }

            successMessage.textContent = 'Данные заполнены верно. Спасибо за регистрацию!';
            form.reset();
            form.classList.remove('was-validated');
        });

        form.addEventListener('input', (event) => {
            if (event.target.matches('[name="name"], [name="phone"], [name="email"]')) {
                event.target.setCustomValidity('');
            }
        });
    });
})();
