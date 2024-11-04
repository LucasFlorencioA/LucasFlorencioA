##Exemplo de kwargs
def mostrar_infos(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} - {v}')

mostrar_infos(lista=[1,2,3,4,5])


##Exemplo de args e kwargs:
def mostrar_infos(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(f'{k} - {v}')

mostrar_infos("Desenvolvedor","Backend",nome='Wilkson',idade=73)