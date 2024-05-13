
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

const criaCliente = ( nome, email) => {

  return fetch("http://localhost:3000/profile", {
    method: "POST",
    body: JSON.stringify({
      nome: nome,
      email: email,
      // senha: "123"
    }),
    headers: {
      "Content-Type": "application/json"
    }
  })
 .then(response => response.json())
}

const removeCliente = (id) => {
  return fetch(`http://localhost:3000/profile/${id}`, {
    method: "DELETE"
  })
 .then(response => response.json())
}
const detalhaCliente = (id) => {

  return fetch(`http://localhost:3000/profile/${id}`)
  
 .then(response => response.json())

}
// Export deixa visivel para outros arquivos que queiram acessar a função
export const clienteService ={
  listaClientes,
  criaCliente,
  removeCliente
};