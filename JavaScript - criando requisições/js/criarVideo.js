import { conectaApi } from "./conectaAPI";

const formulario = document.querySelector('[formulario]');

async function criarVideo(evento) {
    evento.preventDefault(); //evitar a ação padrão de recarregar formulario
    const imagem = document.querySelector('[data-imagem]').value;
    const url = document.querySelector('[data-url]').value;
    const titulo = document.querySelector('[data-titulo]').value;
    const descricao = Math.floor(Math.random() *10).toString();

    try{

        await conectaApi.criaVideo(titulo, descricao, url, imagem);

    }
    catch(erro){
        alert(erro);
    }

    

    window.location.href = "../pages/envio-concluido.html";
}

formulario.addEventListener('submit', evento =>  criarVideo(criarVideo));