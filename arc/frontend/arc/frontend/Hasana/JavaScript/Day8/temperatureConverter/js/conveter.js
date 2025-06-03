class Converter {
    constructor() {
        this.init();
        this.addListeners();
    }
    resetAll() {
        this.input.value = "";
        this.output.textContent = "Result";
        this.chosenTypes.forEach(select => {
            select.selectedIndex = 0;
        });
    }

    init() {
        this.input = document.querySelector(".converter__io__input>input");
        this.output = document.querySelector(".converter__io__result");
        this.chosenTypes = document.querySelectorAll(
            ".converter__dropdown>select"
        );
        this.reset = document.querySelector(".convert-button__reset>button");
        this.convertBtn = document.querySelector(
            ".convert-button__convert>button"
        );
    }

    addListeners() {
        this.convertBtn.addEventListener("click", () => {
            const inputTemp = parseFloat(this.input.value);
            const inputUnit = this.chosenTypes[0].value.toLowerCase();
            const outputUnit = this.chosenTypes[1].value.toLowerCase();

            if (isNaN(inputTemp)) {
                this.output.textContent = "Not valid input";
                return;
            } else {
                const outputTemp = this.convertTemp(
                    inputUnit,
                    outputUnit,
                    inputTemp
                );
                console.log(outputTemp);
                this.output.textContent = outputTemp.toFixed(2);
            }
        });

        this.reset.addEventListener("click", () => {
            this.resetAll();
        });
    }
    convertTemp(fromTemp, toTemp, inputTemp) {
        if (toTemp === fromTemp) {
            return inputTemp;
        }
        let celsius;

        // Convert input to Celsius
        switch (fromTemp) {
            case "fahrenheit":
                celsius = ((inputTemp - 32) * 5) / 9;
                break;
            case "kelvin":
                celsius = inputTemp - 273.15;
                break;
            case "celsius":
                celsius = inputTemp;
                break;
            default:
                return NaN;
        }

        // Convert Celsius to output unit
        switch (toTemp) {
            case "fahrenheit":
                return (celsius * 9) / 5 + 32;
            case "kelvin":
                return celsius + 273.15;
            case "celsius":
                return celsius;
            default:
                return NaN;
        }
    }
}

const c1 = new Converter();
