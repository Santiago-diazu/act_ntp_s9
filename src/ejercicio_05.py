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

empleados_it_30_60000 = df[(df['departamento'] == 'IT') & (df['edad'] > 30) & (df['salario'] > 60000)]
print("Los empleados del departamento de IT que tienen más de 30 años y con salario mayor a 60000 son:\n", empleados_it_30_60000, "\n")

empleados_l_rrhh = df[(df['nombre'].str.startswith('L')) | (df['departamento'] == 'RRHH')]
print("Los empleados cuyos nombres comienzan con la letra L o que pertenecen al departamento de RRHH son:\n", empleados_l_rrhh)
