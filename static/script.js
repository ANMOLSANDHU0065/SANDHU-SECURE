// SANDHU JI


const container =
document.querySelector('.container');

const registerBtn =
document.querySelector('.register-btn');

const loginBtn =
document.querySelector('.login-btn');

registerBtn.addEventListener('click', () => {

    container.classList.add('active');
// SANDHU JI
});

loginBtn.addEventListener('click', () => {

    container.classList.remove('active');

});

// =======================
// ACTIVE FORM
// =======================

const activeForm =
document.body.getAttribute("data-form");

if(activeForm === "register"){

    container.classList.add("active");

}

// =======================
// LOGIN TIMER
// =======================
// SANDHU JI
function startLoginTimer(){

    const timer =
    document.getElementById("timer");

    let timeLeft = 59;

    let countdown = setInterval(() => {

        if(timeLeft <= 0){

            clearInterval(countdown);

            timer.innerHTML =
            "OTP Expired ❌";

        }else{

            timer.innerHTML =
            "OTP Expires In : "
            + timeLeft + "s";

        }

        timeLeft--;

    },1000);

}
// SANDHU JI
// =======================
// REGISTER TIMER
// =======================

function startRegisterTimer(){

    const timer =
    document.getElementById("timer2");

    let timeLeft = 59;

    let countdown = setInterval(() => {

        if(timeLeft <= 0){

            clearInterval(countdown);

            timer.innerHTML =
            "OTP Expired ❌";

        }else{

            timer.innerHTML =
            "OTP Expires In : "
            + timeLeft + "s";

        }
        // SANDHU JI

        timeLeft--;

    },1000);

}

// =======================
// ONLY CORRECT TIMER
// =======================

const fullText =
document.body.innerText;

if(fullText.includes("Login OTP Sent")){

    startLoginTimer();

}

if(fullText.includes("Register OTP Sent")){

    startRegisterTimer();

}


// SANDHU JI