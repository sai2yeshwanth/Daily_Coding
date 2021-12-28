let colorPickerContainerElement = document.getElementById("colorPickerContainer");
let colorpickerHexCodeElement = document.getElementById("selectedColorHexCode");

function changeBgToGreayAndUpdateText() {
    colorPickerContainerElement.style.backgroundColor = "#e0e0e0";
    colorpickerHexCodeElement.textContent = "#e0e0e0";
}

function changeBgToGreenAndUpdateText() {
    colorPickerContainerElement.style.backgroundColor = "#6fcf97";
    colorpickerHexCodeElement.textContent = "#6fcf97";
}

function changeBgToBlueAndUpdateText() {
    colorPickerContainerElement.style.backgroundColor = "#56ccf2";
    colorpickerHexCodeElement.textContent = "#5ccf2";
}

function changeBgToPurpleAndUpdateText() {
    colorPickerContainerElement.style.backgroundColor = "#bb6bd9";
    colorpickerHexCodeElement.textContent = "#bb6bd9";
}
