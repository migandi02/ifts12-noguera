#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Migue
#
# Created:     17/08/2023
# Copyright:   (c) Migue 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
print("Programa de evaluación de alumnos")
nota_alumno=input()

def evaluacion(xnota):
    valoracion="aprobado"
    if xnota<5:
        valoracion="reprobado"
    return valoracion

print(evaluacion(int(nota_alumno)))

