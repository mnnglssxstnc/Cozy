jQuery(document).ready(function () {
    jQuery(".phone-number").inputmask({
        mask: "+38 (999) 999-99-99",
        greedy: false,
    });
});
const regBut = document.querySelectorAll(".check-form");

regBut.forEach((elem) =>
    elem.addEventListener("click", (event) => {
        //function that prevents the transition to the next action
        event.preventDefault();
        const form = elem.closest(".registration-form");
        elemForCheckCaptcha = form;

        //function to check the correctness of the entered name
        function checkName() {
            let inputName = form.querySelector(".input-name");
            let regexName =
                /^[a-zA-Zа-яА-ЯїЇєЄіІґҐ]{2}[a-zA-Zа-яА-ЯїЇєЄіІґҐ'-]*$/;
            if (inputName.value.trim() == "") {

                inputName.closest('.input-wrapper').querySelector('.error-text').textContent = 'Це поле є обов’язковим для заповнення';

                inputName
                    .closest(".input-wrapper")
                    .querySelector("input")
                    .classList.add("error-box");
            } else if (!regexName.test(inputName.value)) {
               
                        inputName.closest('.input-wrapper').querySelector('.error-text').textContent = "Поле має містити не менше двох літер";
                  
                inputName.closest(".input-wrapper").classList.add("error");
                inputName
                    .closest(".input-wrapper")
                    .querySelector("input")
                    .classList.add("error-box");
            } else {
                inputName
                    .closest(".input-wrapper")
                    .querySelector(".error-text").textContent = "";
                inputName
                    .closest(".input-wrapper")
                    .querySelector("input")
                    .classList.remove("error-box");
            }
            return regexName.test(inputName.value);

        }
        //function to check the correctness of the entered phone number
        function checkPhone() {
            let inputPhone = form.querySelector(".phone-number");
            let regexPhone = /^\+38 \(\d{3}\) \d{3}-\d{2}-\d{2}$/;
            if (inputPhone.value.trim() == "") {

                inputPhone.closest('.input-wrapper').querySelector('.error-text').textContent = 'Це поле є обов’язковим для заповнення';

                inputPhone
                    .closest(".input-wrapper")
                    .querySelector("input")
                    .classList.add("error-box");
            } else if (!regexPhone.test(inputPhone.value)) {
                inputPhone.closest(".input-wrapper").classList.add("error");

                inputPhone.closest('.input-wrapper').querySelector('.error-text').textContent = 'Поле заповнено не коректно';

                inputPhone
                    .closest(".input-wrapper")
                    .querySelector("input")
                    .classList.add("error-box");
            } else {
                inputPhone
                    .closest(".input-wrapper")
                    .querySelector(".error-text").textContent = "";
                inputPhone
                    .closest(".input-wrapper")
                    .querySelector("input")
                    .classList.remove("error-box");
            }
            return regexPhone.test(inputPhone.value);
        }
        function checkPassword() {
            let inputPhone = form.querySelector(".input-password");
            if (inputPhone.value.trim() == "") {

                inputPhone.closest('.input-wrapper').querySelector('.error-text').textContent = 'Це поле є обов’язковим для заповнення';

                inputPhone
                    .closest(".input-wrapper")
                    .querySelector("input")
                    .classList.add("error-box");
            } else {
                inputPhone
                    .closest(".input-wrapper")
                    .querySelector(".error-text").textContent = "";
                inputPhone
                    .closest(".input-wrapper")
                    .querySelector("input")
                    .classList.remove("error-box");
            }
        }

        checkName();
        checkPhone();
        checkPassword();
        //opening a second window after successful validation
        if (checkName() && checkPhone()) {
            window.location.href="page_1_signet.html";
console.log('ppppp');
        }
    })
);
document.addEventListener("DOMContentLoaded", function () {
    let clientInputs = document.querySelectorAll('input[class="input-name"]');
    clientInputs.forEach(function (input) {
        input.addEventListener("input", function () {
            let inputValue = input.value;
            let sanitizedValue = sanitizeInput(inputValue);
            if (inputValue !== sanitizedValue) {
                input.value = sanitizedValue;
            }
        });
    });
    function sanitizeInput(input) {
        let regex = /[^a-zA-Zа-яА-ЯїЇєЄіІґҐ'-]/g;
        return input.replace(regex, "");
    }
});

function openForm(){
    window.location.href="page_1.html";
    console.log('ok');
}

document.querySelectorAll('.open-form').forEach(elem => {
    elem.addEventListener("click", () => {
        window.location.href="page_1.html";

    })
})

document.querySelectorAll('.open-info').forEach(elem => {
    elem.addEventListener("click", () => {
        window.location.href="questions.html";

    })
})