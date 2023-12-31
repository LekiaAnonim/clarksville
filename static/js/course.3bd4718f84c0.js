let textMenuist = document.querySelectorAll('.menu-card a');
let sidebarMenu = document.querySelector('.sidebar-menu');
let leftArrow = document.querySelector('.collapse-menu svg');

function toggleMenu() {
    textMenuist.forEach((ele) => {
        ele.classList.toggle('disappear');
    })
}

function toggleSidebar() {
    sidebarMenu.classList.toggle('disappear');
    leftArrow.classList.toggle('rotate180');
}