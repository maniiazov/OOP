const users = [
  { login: "alex", password: "123", name: "Алексей" },
  { login: "ivan", password: "qwerty", name: "Иван" },
  { login: "mariya", password: "pass123", name: "Мария" },
  { login: "admin", password: "adminpass", name: "Администратор" },
  { login: "olga", password: "789", name: "Ольга" },
  { login: "sergey", password: "password", name: "Сергей" }
];

const authForm = document.getElementById('authForm');
const loginInput = document.getElementById('login');
const passwordInput = document.getElementById('password');
const resultMessage = document.getElementById('resultMessage');

authForm.addEventListener('submit', function(event) {
  event.preventDefault();

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