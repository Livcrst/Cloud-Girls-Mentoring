

const listaClientes = () => {
  // const promise = new Promise((resolve, reject) => {
  //   const http = new XMLHttpRequest(); // Oferece os requests que serão usados no curso.

  //   http.open("GET", "http://localhost:3000/profile"); // Abre a conexão com o servidor.

    

  //   http.onload = () => {

  //       if (http.status >= 400){
  //           reject(JSON.parse(http.response));
  //       }
  //       else{
  //           resolve(JSON.parse(http.response));
  //       }

  //   };
  //   http.send(); // Envia a requisição.
  // });
  // console.log(promise);
  // return promise;

  return fetch("http://localhost:3000/profile")
  // Fetch é uma função global que por padrão retorna uma promisse.
 .then(response => response.json())
};

// Recebe dados da api e retorna
listaClientes()
.then(data => {
  data.forEach(element => {
    tabela.appendChild(criarNovaLinha(element.nome, element.email));
    
  });
})