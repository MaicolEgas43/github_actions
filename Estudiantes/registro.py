import csv
from typing import List, Dict, Union
from pathlib import Path

# Definir tipos personalizados para mejorar legibilidad
EstudianteDict = Dict[str, Union[str, float]]
ListaEstudiantes = List[EstudianteDict]

def cargar_estudiantes(ruta_archivo: str) -> ListaEstudiantes:
    """
    Carga estudiantes desde un archivo CSV y valida que sus notas estén en el rango válido (0.0 a 5.0).
    
    Args:
        ruta_archivo: Ruta al archivo CSV con los datos de estudiantes
        
    Returns:
        Lista de diccionarios con los estudiantes válidos
    
    Raises:
        FileNotFoundError: Si no se encuentra el archivo
        Exception: Para otros errores durante la lectura
    """
    NOTA_MINIMA = 0.0
    NOTA_MAXIMA = 5.0
    
    estudiantes_validos = []
    ruta = Path(ruta_archivo)
    
    try:
        with ruta.open('r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            
            for fila in lector_csv:
                estudiante = _procesar_fila_estudiante(fila, NOTA_MINIMA, NOTA_MAXIMA)
                if estudiante:
                    estudiantes_validos.append(estudiante)
                    
        return estudiantes_validos
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")
        return []

def _procesar_fila_estudiante(fila: Dict[str, str], nota_min: float, nota_max: float) -> EstudianteDict:
    """
    Procesa una fila del CSV y valida los datos del estudiante.
    
    Args:
        fila: Diccionario con los datos de la fila
        nota_min: Nota mínima permitida
        nota_max: Nota máxima permitida
        
    Returns:
        Diccionario con los datos del estudiante si son válidos, None en caso contrario
    """
    try:
        nombre = fila['Nombre']
        nota = float(fila['Nota'])
        
        if nota_min <= nota <= nota_max:
            return {
                'nombre': nombre,
                'nota': nota
            }
        print(f"Nota inválida para {nombre}: {nota}")
        return None
        
    except (ValueError, KeyError):
        return None

def imprimir_estudiantes_ordenados(estudiantes: ListaEstudiantes) -> None:
    """
    Ordena a los estudiantes alfabéticamente por nombre y los imprime en formato tabular.
    
    Args:
        estudiantes: Lista de diccionarios con los datos de los estudiantes
    """
    if not estudiantes:
        print("No hay estudiantes para mostrar.")
        return
    
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['nombre'])
    _imprimir_tabla_estudiantes(estudiantes_ordenados)

def _imprimir_tabla_estudiantes(estudiantes: ListaEstudiantes) -> None:
    """
    Imprime la tabla formateada de estudiantes.
    
    Args:
        estudiantes: Lista ordenada de estudiantes
    """
    max_longitud_nombre = max(len(estudiante['nombre']) for estudiante in estudiantes)
    padding = 4
    ancho_nombre = max_longitud_nombre + padding
    
    print(f"\n{'NOMBRE':<{ancho_nombre}}{'NOTA':<10}")
    print("-" * (ancho_nombre + 10))
    
    for estudiante in estudiantes:
        print(f"{estudiante['nombre']:<{ancho_nombre}}{estudiante['nota']:<10.2f}")
    
    print("\nTotal de estudiantes:", len(estudiantes))

def calcular_promedio_notas(estudiantes: ListaEstudiantes) -> None:
    """
    Calcula la media de las notas de los estudiantes válidos y muestra el resultado.
    
    Args:
        estudiantes: Lista de diccionarios con los datos de los estudiantes
    """
    if not estudiantes:
        print("No hay estudiantes para calcular el promedio.")
        return
    
    notas = [estudiante['nota'] for estudiante in estudiantes]
    promedio = sum(notas) / len(notas)
    
    print(f"\nPromedio de notas: {promedio:.2f}")