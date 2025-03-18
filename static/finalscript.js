function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = "";
}

function backspace() {
    let display = document.getElementById('display');
    display.value = display.value.slice(0, -1);
}
