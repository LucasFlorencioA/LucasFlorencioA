const formElemet = document.querySelector('.form-login')
const btnLogin = document.querySelector('.form-login button')


function setLoading(isLoading) {
    if (isLoading) {
        btnLogin.innerHTML = "Carregando..."
        btnLogin.setAttribute('desabled', true)
        return
    }
    btnLogin.innerHTML = "Efetuar cadastro"
    btnLogin.removeAttribute('desabled')
}


formElemet.addEventListener('submit', async (event) => {
    event.preventDefault()

    const formData = new FormData(formElemet)

    if (formData.get('password') != formData.get('repeatPassword')) {
        alert('Oops! Senhas não conferem')
        return;
    }

    const usuarios = {
        name: formData.get('name'),
        email: formData.get('email'),
        password: formData.get('password'),
        avatar: formData.get('avatar')
    }

    const values = Object.values(usuarios)
    const camposVazios = values.includes('')

    try{
        setLoading(true)
        const response =await fetch('https://api.escuelajs.co/api/v1/users/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(usuarios)
    })
    
    const json = await response.json()

        if(!response.ok) {
            const { message } = json

            const erroMessage = message.reduce((acc, curr) => 
                    acc + `<li>${curr}</li>`, '')

            listErros.innerHTML = erroMessage
            return
        }

        alert("Cadastro efetuado com sucesso!!")
        formElement.reset()
        listErros = ""
    } catch (error) {
        alert("Ops! Ocorreu um erro interno. Tente novamente mais tarde")
    } finally {
        setLoading(false)
    }
    })