const btnAbrir = document.getElementById('btn-abrir-menu')
const btnsair = document.getElementById('sair')
const foraDaTela = document.getElementById('mobile')

btnAbrir.addEventListener('click', (A) => {
    A.preventDefault()
    foraDaTela.classList.add('active')
})

btnsair.addEventListener('click', (A) => {
    A.preventDefault()
    foraDaTela.classList.remove('active')
})


const transform = new IntersectionObserver((arguments) => {
    arguments.forEach((e) => {
        if (e.isIntersecting) {
            e.target.classList.add("show")
        }
    })
})

const anime = document.querySelectorAll(".hidden")
anime.forEach((t) => transform.observe(t))


