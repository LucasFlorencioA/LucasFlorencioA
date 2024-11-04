def hour():
    hr = input("Digite um horário(HH:MM):")

    #Separar variável em horas e minutos
    horas, minutos = hr.split(':')

    horas = int(horas)
    minutos = int(minutos)

    if 5 <= horas <= 12:
        return f'são {horas}hrs e {minutos} minutos! Bom dia!'
    elif 12 <= horas <= 18:
        return f'são {horas}hrs e {minutos} minutos! Boa tarde!'
    else:
        return f'são {horas}hrs e {minutos} minutos! Boa noite!'

print(hour())