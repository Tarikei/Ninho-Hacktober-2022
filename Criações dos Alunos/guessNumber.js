let bot = Math.floor(Math.random() * 11);
let num = 0

do {
    num = parseFloat(prompt("Estou pensando em um numero de 0 a 10...\nConsegue adivinhar?"));
    if (num !== bot) {
        alert("Errou! Tente novamente!");
    }
} while (num !== bot);

alert(`Parabéns você acertou! Eu estava pensando no número ${bot}`);
