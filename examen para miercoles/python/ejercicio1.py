#1️⃣ Calculadora de Propinas 💰
#    - Enunciado: Crea un programa que calcule el total de una cuenta más la propina.
#    - Requerimientos: Pedir costo y % de propina, calcular el total y mostrar todo desglosado.

print("Calculadora de propinas")

precio_deloqsea = float(input("ponga el dinero que gasto:"))

propina = float(input("ponga el % de propina que quiere dar:"))

propina_adar = precio_deloqsea * propina / 100

print(f"a partir del precio que me dio: {precio_deloqsea}. y el porcentaje usted tiene que dar: {propina_adar} (moneda local)")