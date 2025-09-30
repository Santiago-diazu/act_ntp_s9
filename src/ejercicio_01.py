import pandas as pd

# Crear DataFrame simple de empleados
data = {
    'nombre': ['Ana', 'Luis', 'Carmen', 'José', 'María', 'Pedro', 'Laura', 'Miguel'],
    'departamento': ['Ventas', 'IT', 'RRHH', 'Ventas', 'IT', 'Marketing', 'RRHH', 'IT'],
    'salario': [45000, 65000, 50000, 48000, 70000, 55000, 52000, 68000],
    'edad': [28, 35, 42, 31, 29, 38, 45, 33]
}

df = pd.DataFrame(data)
print("Base de datos de empleados:")
print(df, "\n")

empleados_sup_50000 = df[df['salario'] > 50000]
print("Los empleados con salario mayor a 50000:\n", empleados_sup_50000, "\n")

empleados_men_35 = df[df['edad'] < 35]
print("\nLos empleados menores de 35 años:\n", empleados_men_35, "\n")

empleados_dep_it = df[df['departamento'] == 'IT']
print("\nLos empleados del departamento de IT son:\n", empleados_dep_it)
