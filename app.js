const btnAbrir = document.getElementById('btn-abrir-menu')
const btnsair = document.getElementById('sair')
const foraDaTela = document.getElementById('mobile')

btnAbrir.addEventListener('click', (A)=>{
    A.preventDefault()
    foraDaTela.classList.add('active')
})

btnsair.addEventListener('click', (A)=>{
    A.preventDefault()
    foraDaTela.classList.remove('active')
})