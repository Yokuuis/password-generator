import random 
import string 

#Variables (arrays, cadenas de caracteres)

# Alfabeto (Obligatorias)
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Numeros (Opcionales)
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Letras minusculas:
lmin = list(string.ascii_lowercase)

#Letras mayusculas:
lmay = list(string.ascii_uppercase)

#Caracteres especiales (Opcionales)
caracteres_especiales = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ":", ";", "'", "\"", "<", ">", ".", "?", "/"]

# Opciones al usuario:
incluir_num = input("¿Deseas incluir números? (s/n): ")
incluir_especiales = input("Deseas incluir caracteres especiales? (s/n): ")


#Minimo caracteres:
minimo = 4

# Longitud de la contraseña
longitud = int(input("Ingresa la longitud de la contraseña: "))

# Ciclo while para cumplir la condicion del minimo de longitud
while longitud < minimo:
    print(f"La longitud minima es {minimo}. Intenta denuevo ingresando denuevo la longitud")
    longitud = int(input("Ingresa la longitud de la contraseña: "))

# Creamos una caja para guardar el texto (la cadena de texto es obligatoria esta)
pool = []

pool += lmin #Se guarda letras minusculas
pool += lmay #Se guarda letras mayusculas


# En caso de querer incluir las opciones para el usuario se agrega en el pool:

# Si quiere agregar numeros debio escoger si (s)
if incluir_num.lower() == "s" == "si":
    pool += numeros #Se guarda en la caja

# Si quiere agregar caracteres especiales debio escoger (s), en todo caso se vuelve en minuscula
if incluir_especiales.lower() == "s" == "si":
    pool += caracteres_especiales #Se guarda en la caja

# Guardar en variable vacia la password para que se pueda guardar en el texto lo aleatorio:
password = "" 

# Ciclo de la longitud segun escogida por el usuario, se guarda en password, 
# y el random.choice se utiliza en la caja que utilizamos (determinado puras alfabeto)

for i in range(longitud):
    password += random.choice(pool)
    
print(password)