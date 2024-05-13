import { clienteService } from "../service/cliente-service.js";

const criarNovaLinha = (nome, email) => {
    const linhaNovoCliente = document.createElement("tr");
    const conteudo = `<td class="td" data-td>${nome}</td>
      <td>${email}</td>
      <td>
          <ul class="tabela__botoes-controle">
              <li><a href="../telas/edita_cliente.html" class="botao-simples botao-simples--editar">Editar</a></li>
              <li><button class="botao-simples botao-simples--excluir" type="button">Excluir</button></li>
          </ul>
      </td>`;
  
    linhaNovoCliente.innerHTML = conteudo;
    return linhaNovoCliente;
  };
const tabela = document.querySelector("[data-tabela]");

// Recebe dados da api e retorna
clienteService.listaClientes()
.then(data => {
  data.forEach(element => {
    tabela.appendChild(criarNovaLinha(element.nome, element.email));
    
  });
});