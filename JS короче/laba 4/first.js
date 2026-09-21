const countDisplay = document.getElementById('count-display');
const btnDecrease = document.getElementById('btn-decrease');
const btnReset = document.getElementById('btn-reset');
const btnIncrease = document.getElementById('btn-increase');

let count = 0;

function updateColor() {
  countDisplay.classList.remove('positive', 'negative', 'zero');

  if (count > 0) {
    countDisplay.classList.add('positive');
  } else if (count < 0) {
    countDisplay.classList.add('negative');
  } else {
    countDisplay.classList.add('zero');
  }
}

btnIncrease.addEventListener('click', function() {
  count++;
  countDisplay.textContent = count;
  updateColor();
});

btnDecrease.addEventListener('click', function() {
  count--;
  countDisplay.textContent = count;
  updateColor();
});

btnReset.addEventListener('click', function() {
  count = 0;
  countDisplay.textContent = count;
  updateColor();
});


function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

const lottoContainer = document.getElementById('lotto-container');
const btnGenerate = document.getElementById('btn-generate');

function generateLottoNumbers() {
  lottoContainer.innerHTML = '';

  let numbers = [];

  while (numbers.length < 6) {
    let randomNumber = getRandomInt(1, 99);
    if (!numbers.includes(randomNumber)) {
      numbers.push(randomNumber);
    }
  }

  for (let i = 0; i < numbers.length; i++) {
    let num = numbers[i];
    let formattedNum = num < 10 ? '0' + num : String(num);

    let ball = document.createElement('div');
    ball.className = 'lotto-ball';
    ball.textContent = formattedNum;

    lottoContainer.appendChild(ball);
  }
}

btnGenerate.addEventListener('click', generateLottoNumbers);