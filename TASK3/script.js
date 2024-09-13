let display = document.getElementById('display');
let buttons = document.querySelectorAll('.button');

let currentNumber = '';
let previousNumber = '';
let operation = '';

buttons.forEach(button => {
    button.addEventListener('click', () => {
        let value = button.textContent;

        if (value === 'C') {
            clear();
        } else if (value === '⌫') {
            backspace();
        } else if (value === '=') {
            calculate();
        } else if (value === '+' || value === '-' || value === '*' || value === '/') {
            setOperation(value);
        } else {
            appendNumber(value);
        }
    });
});

function clear() {
    currentNumber = '';
    previousNumber = '';
    operation = '';
    display.value = '';
}

function backspace() {
    currentNumber = currentNumber.slice(0, -1);
    display.value = currentNumber;
}

function appendNumber(value) {
    currentNumber += value;
    display.value = currentNumber;
}

function setOperation(value) {
    operation = value;
    previousNumber = currentNumber;
    currentNumber = '';
}

function calculate() {
    let result = 0;

    switch (operation) {
        case '+':
            result = parseFloat(previousNumber) + parseFloat(currentNumber);
            break;
        case '-':
            result = parseFloat(previousNumber) - parseFloat(currentNumber);
            break;
        case '*':
            result = parseFloat(previousNumber) * parseFloat(currentNumber);
            break;
        case '/':
            result = parseFloat(previousNumber) / parseFloat(currentNumber);
            break;
    }

    display.value = result;
    currentNumber = result.toString();
    previousNumber = '';
    operation = '';
}