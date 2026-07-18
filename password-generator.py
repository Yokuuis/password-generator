import random 
import string 

#Variables (arrays, cadenas de caracteres)
# Alfabeto

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#para guardar tiempo, utilizamos lowercase and uppercase

#Letras minusculas:
lmin = list(string.ascii_lowercase)

#Letras mayusculas:
lmay = list(string.ascii_uppercase)

caracteres_especiales = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ":", ";", "'", "\"", "<", ">", ".", "?", "/"]

# Opciones al usuario:
numeros = input("¿Deseas incluir números? (s/n): ")
#letras = input("Deseas incluir caracteres especiales? (s/n): ")

# Longitud de la contraseña
length = int(input("Ingresa la longitud de la contraseña: "))