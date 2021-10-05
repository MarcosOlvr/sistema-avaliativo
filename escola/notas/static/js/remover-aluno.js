let btn_rm = document.querySelector("#remover_aluno");
    let editar_remover = document.querySelector(".options");
    let confirmar = document.querySelector("#delete-button-div");
    let cancelar = document.querySelector("#cancelar-delete-div");

    let text_confirm = document.querySelector("#texto-confirm");

    btn_rm.addEventListener('click', function(){
        text_confirm.innerHTML = `Tem certeza que quer deletar as informações do aluno?`;
        // ESCONDER BOTÃO DE REMOVER E EDITAR      
        editar_remover.style.display = 'none';
        //
        confirmar.style.display = 'flex';
        cancelar.style.display = 'flex';
    });
    cancelar.addEventListener('click', function(){
        text_confirm.innerHTML = '';
        //
        editar_remover.style.display = 'flex';
        //
        confirmar.style.display = 'none';
        cancelar.style.display = 'none';
    });