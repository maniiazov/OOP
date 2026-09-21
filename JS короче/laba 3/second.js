function getRange(start, end, step = 1) {
  const result = [];
  for (let i = start; i <= end; i += step) {
    result.push(i);
  }
  return result;
}


function myReverse(str) {
  let reversedStr = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversedStr += str[i];
  }
  return reversedStr;
}


function maskCard(cardNumber, maskSymbol = "X") {
  const strCard = String(cardNumber);
  if (strCard.length <= 10) return strCard;

  const firstDigits = strCard.slice(0, 6);
  const lastDigits = strCard.slice(-4);
  const middleMask = maskSymbol.repeat(strCard.length - 10);

  return firstDigits + middleMask + lastDigits;
}

document.getElementById("res1").innerText = JSON.stringify(getRange(10, 30, 5));
document.getElementById("res2").innerText = myReverse("123456789");
document.getElementById("res3").innerText = maskCard("4815154823541789", "*");


console.log("getRange(1, 10) ->", getRange(1, 10));
console.log("getRange(10, 30, 5) ->", getRange(10, 30, 5));
console.log("myReverse('123456789') ->", myReverse("123456789"));
console.log("maskCard('4815154823541789') ->", maskCard("4815154823541789"));
console.log("maskCard('4815154823541789', '*') ->", maskCard("4815154823541789", "*"));