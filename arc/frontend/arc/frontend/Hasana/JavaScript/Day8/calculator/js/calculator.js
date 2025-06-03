const keys = document.querySelectorAll(".calculator__key");
const inputDisplay = document.querySelector(".calculator__input");
const allClear = document.querySelector(".calculator__key--ac");
const answer = document.querySelector(".calculator__answer")

let inputText = "";

keys.forEach((key) => {
    key.addEventListener("click", () => {
        const keyText = key.textContent.trim();
        if (key.textContent == "AC") {
            inputText=""
            answer.textContent=""
        }
        else if(key.textContent=="DEL"){
           inputText= inputText.slice(0, -1);
           answer.textContent=""
        } 
        else if(!(key.textContent=="=")){
            inputText += keyText;
        }
        else{
            answer.textContent=inputText
        }
        inputDisplay.textContent = inputText;
    });
});


inputDisplay.textContent = "";
