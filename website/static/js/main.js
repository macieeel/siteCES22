document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('button').onclick = function toggleMenu() {
        const navToggle = document.getElementById('navbar')
        navToggle.classList.toggle('hidden')
        console.log('Teste')
    }
})
