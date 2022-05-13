document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('button').onclick = function toggleMenu() {
        const navToggle = document.getElementById('navbar')
        navToggle.classList.toggle('hidden')
    }

    // document.getElementById('delete_button').onclick = function deleteMessage() {
    //     this.parentNode.parentNode.removeChild(this.parentNode)
    // }
})
