#Valentina Moncada Morales
#Maicol Estiben Egas
import Estudiantes.registro as registro

def main():
    # Cargar estudiantes desde el archivo CSV
    print("Cargando datos de estudiantes...")
    dataEstudiantes = registro.cargar_estudiantes("estudiantes_notas.csv")
    print(f'Notas estudiantes cargadas: {len(dataEstudiantes)}')
    
    # Mostrar tabla de estudiantes ordenados alfabéticamentes
    registro.imprimir_estudiantes_ordenados(dataEstudiantes)
    
    # Calcular y mostrar el promedio de notas
    registro.calcular_promedio_notas(dataEstudiantes)

if __name__ == "__main__":
    main()
