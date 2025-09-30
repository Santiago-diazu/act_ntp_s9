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

empleados_it_ventas = df[(df['departamento'] == 'IT') | (df['departamento'] == 'Ventas')]
print("Los empleados que pertenecen a los departamentos de IT o ventas son:\n", empleados_it_ventas, "\n")

empleados_28_35_42 = df[df['edad'].isin([28, 35, 42])]
print("Los empleados con edades de 28, 35 o 42 son:\n", empleados_28_35_42)
