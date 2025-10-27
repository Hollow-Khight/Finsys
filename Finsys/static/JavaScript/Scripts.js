document.addEventListener('DOMContentLoaded', function() {
    console.log("Finsys: Script JavaScript carregado.");

    var header = document.querySelector('header');
    if (header) {
        setTimeout(function() {
            header.classList.add('loaded');
        }, 100);
    }

    var tituloPagina = document.title;
    if (tituloPagina.includes("Início")) {
        console.log("Página de Início detectada.");

    }
});