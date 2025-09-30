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

empleados_M = df[df['nombre'].str.startswith('M')]
print("Los empleados cuyos nombres comienzan con la letra M son:\n", empleados_M, "\n")

departamentos_R = df[df['departamento'].str.contains('R')]
print("Los empleados que pertenecen a departamentos que contienen la letra R son:\n", departamentos_R)  
