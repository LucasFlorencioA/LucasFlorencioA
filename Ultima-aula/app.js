const formElemet = document.querySelector('.form-login')
const btn = document.querySelector('.form-login button')

formElemet.addEventListener('submit', async(event) =>{
    event.preventDefault()
    
    const formData = new FormData(formElemet)

    if(formData.get('password')!=formData.get('repeatPassword')){
        alert('Oops! Senhas não conferem')
        return;
    }

    const usuarios ={
        name: formData.get('name'),
        email: formData.get('email'),
        password: formData.get('password'),
        avatar:formData.get('avatar')
    }
    
    const values = Object.values(usuarios)
    const camposVazios = values.includes('')

    if (camposVazios){
        alert('Oops! Todos os campos devem estar preenchidos!')
        return;
    }
    await fetch('https://api.escuelajs.co/api/v1/users/',{
        method: "POST",
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify(usuarios)
    })

    btn.innerHTML = "Carregando..."
    btn.setAttribute('desabled', true)
    await new Promise((resolve)=> setTimeout(resolve, 4000))
   
    btn.innerHTML = "Efetuar cadastro"
    btn.removeAttribute('desabled')

})