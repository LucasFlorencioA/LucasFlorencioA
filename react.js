const precos = [
    "Credito",
    "R$ 200",
    "R$ 400",
    "Contas a pagar",
    "R$ 300",
    "R$ 400",
    "Meus dados",
]
// Retorna somente os numeros
const precosFiltro = precos.filter((preco) => preco.includes("R$"))
console.log(precosFiltro)

