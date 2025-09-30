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

empleados_it_60000 = df[(df['departamento'] == 'IT') & (df['salario'] > 60000)]
print("Los empleados del departamento de IT con salario mayor a 60000 son:\n", empleados_it_60000, "\n")

empleados_ventas_40 = df[(df['departamento'] == 'Ventas') | (df['edad'] > 40)]
print("Los empleados del departamento de ventas mayores de 40 años son:\n", empleados_ventas_40, "\n")

empleados_no_marketing = df[~(df['departamento'] == 'Marketing')]
print("Los empleados que no pertenecen al departamento de marketing son:\n", empleados_no_marketing)
