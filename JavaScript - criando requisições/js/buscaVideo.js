import { conectaApi } from "./conectaAPI";
import constroiCard from "./mostra videos";


async function buscarVideo(){

    const dadosDePesquisa = document.querySelector('[data-pesquisa]').value;
    const busca = await conectaApi.buscaVideos(dadosDePesquisa);

    const lista = document.querySelector('[data-lista]');
    // Remove itens filhos até deixar a lista vazia
    while(lista.firstChild){
        lista.removeChild(lista.firstChild);
    }

    busca.forEach(element => lista.appendChild(constroiCard(element.titulo, element.descricao, element.url, element.imagem)));
 
    if(busca.length == 0){
        lista.innerHTML = `<h2 class= "mensagem__titulo" >Nenhum vídeo encontrado</h2>`;
    }
};


const botaoDePesquisa = document.querySelector('[data-pesquisa]');
botaoDePesquisa.addEventListener('click', buscarVideo(evento));