from datetime import date
import os
import re
from typing import final
from itertools import cycle
import sys

regexName = r'^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$'

def dateToInt(birthDate):
    date = birthDate.split('/')
    dateInt = [int (i) for i in date]
    return dateInt

def checkName(name):
    resultado = re.match(regexName, name)
    is_match = bool(resultado)
    if is_match == True:
        return name
    else:
        print('Nombre no válido')
        return None

def checkSex(sex):
    finalSex = sex.lower()
    if finalSex == 'f' or finalSex == 'femenino':
        return finalSex
    elif finalSex == 'm' or finalSex == 'masculino':
        return finalSex
    else:
        print('Sexo no válido')
        return None

def checkPersonType(personType):
    personTypeFinal = personType.lower()
    if personTypeFinal == 'si':
        return 'atleta'
    elif personTypeFinal == 'no':
        return 'normal'
    else:
        return None   
    

def validarRut(rut):
	rut = rut.upper();
	rut = rut.replace("-","")
	rut = rut.replace(".","")

	aux = rut[:-1]
	dv = rut[-1:]
	revertido = map(int, reversed(str(aux)))
	factors = cycle(range(2,8))
	s = sum(d * f for d, f in zip(revertido,factors))
	res = (-s)%11

	if str(res) == dv:
		return rut
	elif dv=="K" and res==10:
		return rut
	else:
		return None

def ingresarPersona(name, sex, birthDate, personType, rut):
    pass

def calculateImc():
    pass

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


if __name__ == "__main__":
    print('--------------------------------------------------------------------------------')
    name = input('Ingresa tu nombre\n')
    # Valida que el nombre sea correcto
    name = checkName(name)

    sex = input('Ingresa tu sexo\n1. Femenino - F\n2. Masculino - M\n')
    # Valida que el sexo sea correcto
    sex = checkSex(sex)

    birthDate = input('Fecha de nacimiento? i.e AAAA/MM/DD\n')
    dateInt = dateToInt(birthDate)
    age = calculateAge(date(dateInt[0], dateInt[1], dateInt[2]))

    personType = input('¿Eres un atleta? Responder Si o No\n')
    # Valida que el tipo de persona sea correcto
    personType = checkPersonType(personType)

    rut = input('Ingresa tu rut\n')
    # Valida que el rut exista
    rut = validarRut(rut)
    
    print('--------------------------------------------------------------------------------')