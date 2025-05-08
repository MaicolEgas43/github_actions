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