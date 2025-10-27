document.addEventListener('DOMContentLoaded', function() {
    console.log("Finsys: Script JavaScript carregado.");

    // Função para aplicar a máscara no CPF (xxx.xxx.xxx-xx)
    function maskCPF(value) {
        // 1. Remove tudo que não for dígito
        value = value.replace(/\D/g, "");
        // 2. Limita a 11 dígitos
        value = value.substring(0, 11);

        // 3. Aplica a máscara: xxx.xxx.xxx-xx
        value = value.replace(/(\d{3})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d)/, "$1.$2");
        value = value.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
        
        return value;
    }

    // Função para aplicar a máscara no Telefone (Ex: (xx) xxxxx-xxxx)
    function maskPhone(value) {
        // 1. Remove tudo que não for dígito
        value = value.replace(/\D/g, "");
        // 2. Limita a 11 dígitos (incluindo o DDD e o 9)
        value = value.substring(0, 11); 

        // 3. Aplica a máscara: (xx) xxxxx-xxxx (para 11 dígitos) ou (xx) xxxx-xxxx (para 10 dígitos)
        value = value.replace(/^(\d{2})(\d)/g, "($1) $2"); 
        
        // Aplica o hífen
        if (value.length === 15) { // Celular com 9º dígito: (xx) 9xxxx-xxxx
            value = value.replace(/(\d{5})(\d)/, "$1-$2");
        } else { // Telefone fixo (ou celular antigo): (xx) xxxx-xxxx
            value = value.replace(/(\d{4})(\d)/, "$1-$2");
        }
        
        return value;
    }

    function attachMaskEvent(id, maskFunction) {
        const input = document.getElementById(id);
        if (input) {
            input.addEventListener('input', (event) => {
                event.target.value = maskFunction(event.target.value);
            });
        }
    }

    attachMaskEvent('cpf', maskCPF);
    attachMaskEvent('telefone', maskPhone);


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