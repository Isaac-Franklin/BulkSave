const opennav = document.querySelector('.opennav')
const closenav = document.querySelector('.closenav')
const navBar = document.querySelector('.respgeneral')


const showMenuBar = () => {
    navBar.style.display = "block";
    closenav.style.display = "block";
    opennav.style.display = "none";
    navBar.classList.add("slidein");
}


const hideMenuBar = () => {
    navBar.style.display = "none";
    closenav.style.display = "none";
    opennav.style.display = "block";
    navBar.classList.add("slideback");
}

opennav.addEventListener("click", showMenuBar)
closenav.addEventListener("click", hideMenuBar)