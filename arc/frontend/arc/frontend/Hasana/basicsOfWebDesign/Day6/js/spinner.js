const spinnerButton = document.querySelector("button");
const spinner = document.querySelector(".spinner__button");
const loader = document.querySelector(".spinner__loader");


spinnerButton.addEventListener("click", () => {
    if (spinner.className.includes('spinner__button--active')) {
        spinner.classList.remove('spinner__button--active');
        loader.style.display='none';
        spinnerButton.textContent='Spin Now';
    }
    else{
        spinner.classList.add('spinner__button--active');
        loader.style.display ='block';
        spinnerButton.textContent='Stop!';
    }
});
