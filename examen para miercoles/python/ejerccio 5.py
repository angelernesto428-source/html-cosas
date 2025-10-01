
#    - Enunciado: Cuenta cuántas vocales hay en un texto que ingrese el usuario.
#    - Requerimientos: Pedir texto, usar un for para recorrerlo y un if para contar las vocales (¡no olvides las mayúsculas!).

print("contador de vocales")

texto = input("ponga un palabra:")

vocales = 0

for letras in texto:
    if letras in "aieouAIUEO":
        vocales += 1
print(f"en la palabra hay {vocales} vocales")
