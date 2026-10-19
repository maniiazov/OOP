const users = [
  { login: "alex", password: "123", name: "Алексей" },
  { login: "ivan", password: "qwerty", name: "Иван" },
  { login: "mariya", password: "pass123", name: "Мария" },
  { login: "admin", password: "adminpass", name: "Администратор" },
  { login: "olga", password: "789", name: "Ольга" },
  { login: "sergey", password: "password", name: "Сергей" }
];

const authForm = document.getElementById('authForm');
const fullNameInput = document.getElementById('fullName');
const phoneInput = document.getElementById('phone');
const emailInput = document.getElementById('email');
const loginInput = document.getElementById('login');
const passwordInput = document.getElementById('password');
const resultMessage = document.getElementById('resultMessage');

const fullNamePattern = /^[А-ЯЁ][а-яё]+(?:[- ][А-ЯЁ][а-яё]+){1,2}$/i;
const phonePattern = /^\+?\d[\d\s()-]{8,18}\d$/;
const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

authForm.addEventListener('submit', function(event) {
  event.preventDefault();

  const fullName = fullNameInput.value.trim();
  const phone = phoneInput.value.trim();
  const email = emailInput.value.trim();

  if (!fullNamePattern.test(fullName)) {
    resultMessage.textContent = 'Введите ФИО: имя, фамилию и (при необходимости) отчество.';
    resultMessage.className = 'error';
    fullNameInput.focus();
    return;
  }

  if (!phonePattern.test(phone)) {
    resultMessage.textContent = 'Введите корректный номер телефона.';
    resultMessage.className = 'error';
    phoneInput.focus();
    return;
  }

  if (!emailPattern.test(email)) {
    resultMessage.textContent = 'Введите корректный адрес электронной почты.';
    resultMessage.className = 'error';
    emailInput.focus();
    return;
  }

  const userLogin = loginInput.value;
  const userPassword = passwordInput.value;

  const foundUser = users.find(function(user) {
    return user.login === userLogin && user.password === userPassword;
  });

  if (foundUser) {
    resultMessage.textContent = `Добро пожаловать, ${foundUser.name}!`;
    resultMessage.className = 'success';
  } else {
    resultMessage.textContent = 'Ошибка: неверный логин или пароль.';
    resultMessage.className = 'error';
  }
});
