const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')

//Display Mobile Menu
const mobileMenu = () => {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
}

menu.addEventListener('click', mobileMenu);

function searchItem() {
    let input = document.getElementById('searchbar').value;
    input = input.tolowercase();
    return input
}