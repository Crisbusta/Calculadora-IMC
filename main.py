from datetime import date
import os
import re
from typing import final
from itertools import cycle
import sys
import json

people = {}
regexName = r'^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$'


def dateToInt(birthDate):
    date = birthDate.split('/')
    dateInt = [int(i) for i in date]
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
        print('Tipo de persona no valido')
        return None


def validarRut(rut):
    rut = rut.upper()
    rut = rut.replace("-", "")
    rut = rut.replace(".", "")
    aux = rut[:-1]
    dv = rut[-1:]
    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(revertido, factors))
    res = (-s) % 11
    if str(res) == dv:
        return rut
    elif dv == "K" and res == 10:
        return rut
    else:     
        return None


def appendPerson(dicty):
    global people
    if dicty['rut'] in people:
        print('Rut ya existe')
    else:
        people[dicty['rut']] = dicty




def calculateImc(rut):
    global people
    if rut in people:
        peso = float(input('Ingresa tu peso en KILOGRAMOS\n'))
        weighDate = input('Ingrese la fecha en que se pesó i.e AAAA/MM/DD\n')
        altura = float(input('Ingresa tu altura en METROS\n'))
        IMC = round((peso/(altura*altura)),1)
        people[rut]['IMC'] = IMC
        people[rut]['weighDate'] = weighDate

        if people[rut]['sex'] == 'm':
            if IMC < 20:
                people[rut]['indice'] = 'Bajo peso'
            elif IMC >= 20 and IMC <= 24.9:
                people[rut]['indice'] = 'Normal'
            elif IMC >= 25 and IMC <= 29.9:
                people[rut]['indice'] = 'Obesidad Leve'
            elif IMC >= 30 and IMC <= 40:
                people[rut]['indice'] = 'Obesidad Severa'
            elif IMC > 40:
                people[rut]['indice'] = 'Obesidad Muy Severa'
        else:
            if IMC < 20:
                people[rut]['indice'] = 'Bajo peso'
            elif IMC >= 20 and IMC <= 23.9:
                people[rut]['indice'] = 'Normal'
            elif IMC >= 24 and IMC <= 28.9:
                people[rut]['indice'] = 'Obesidad Leve'
            elif IMC >= 29 and IMC <= 37:
                people[rut]['indice'] = 'Obesidad Severa'
            elif IMC > 37:
                people[rut]['indice'] = 'Obesidad Muy Severa'
        print('Datos Personales\nNombre: '+ str(people[rut]['name']) +"\nSexo: "+ str(people[rut]['sex']) + '\nEdad: '+ str(people[rut]['age']) + '\nIMC: '+ str(people[rut]['IMC']) +'\nInterpretación IMC: '+ str(people[rut]['indice']) +'\n')
    else:
        print('Rut no existe')
        


def calculateAge(birthDate):
    today = date.today()
    global corre
    age = today.year - birthDate.year - \
        ((today.month, today.day) < (birthDate.month, birthDate.day))
    if age >= 15 and age <= 70:
        return age
    else:
        print('Edad no se encuentra en el rango')
        return None

def saveDicty(dicty):
    tf = open("myDictionary.json", "w")
    json.dump(dicty,tf)
    tf.close()


def readDicty():
    global people
    tf = open("myDictionary.json", "r")
    people = json.load(tf)


if __name__ == "__main__":
    print('--------------------------------------------------------------------------------')
    readDicty()
    ans = True
    while ans:
        print("""
        1. Ingresar Datos
        2. Calcular IMC
        3. Salir
        """)
        ans = input("¿Que quieres hacer?\n")
        if ans == "1":  
            name = input('Ingresa tu nombre\n')
            name = checkName(name)# Valida que el nombre sea correcto
            sex = input('Ingresa tu sexo\n1. Femenino - F\n2. Masculino - M\n')
            sex = checkSex(sex)# Valida que el sexo sea correcto
            birthDate = input('Fecha de nacimiento? i.e AAAA/MM/DD\n')
            dateInt = dateToInt(birthDate)
            age = calculateAge(date(dateInt[0], dateInt[1], dateInt[2]))
            personType = input('¿Eres un atleta? Responder Si o No\n')
            personType = checkPersonType(personType) # Valida que el tipo de persona sea correcto
            rut = input('Ingresa tu rut\n')
            rut = validarRut(rut) # Valida que el rut exista

            thisdict = {"name": name, "sex": sex, 'birthDate': birthDate, 'age': age, 'personType': personType, 'rut': rut}
            nones = not all(thisdict.values())
            
            if nones == True:
                print('Los datos que ingresaste son incorrectos')                
            else:
                appendPerson(thisdict)

        elif ans == "2":
          rut = input('Ingresa el rut de la persona\n')
          calculateImc(rut)
        elif ans == "3":
            saveDicty(people)
            print("\n Adiós")
            ans = None
        else:
            print("\n Opción no valida")

    print('--------------------------------------------------------------------------------')
