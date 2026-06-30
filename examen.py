# ============================================================================
# COLEGIO TÉCNICO PROFESIONAL DE OREAMUNO
# DEPARTAMENTO DE CIBERSEGURIDAD
# ============================================================================
#
# ESTUDIANTE: [Saray Solano Vargas]
# SECCIÓN: 10-_1_
# FECHA DE CREACIÓN: [30/6/2026]
#
# ============================================================================
# ARCHIVO: [examen.py]
# DESCRIPCIÓN: [Breve explicación de qué hace el programa y sus funciones]
# ============================================================================
#

# El código del programa inicia a partir de aquí...
import random 
import time
import os
# Paso 2: Diccionario con el arte de ASCII para las caras de los dados
CARAS_DADO = {
    1: [" ----- ", "|     |", "|  *  |", "|     |", " ----- "],
    2: [" ----- ", "|*    |", "|     |", "|    *|", " ----- "],
    3: [" ----- ", "|*    |", "|  *  |", "|    *|", " ----- "],
    4: [" ----- ", "|*   *|", "|     |", "|*   *|", " ----- "],
    5: [" ----- ", "|*   *|", "|  *  |", "|*   *|", " ----- "],
    6: [" ----- ", "|*   *|", "|*   *|", "|*   *|", " ----- "]
}
def mostrar_dados(cara_usuario, cara_pc):
   lineas_usuario = CARAS_DADO[cara_usuario]
   lineas_pc = CARAS_DADO[cara_pc]

   print("\n        Usuario:          COMPUTADORA:")
   for i in range(5):
         print(f"        {lineas_usuario[i]}          {lineas_pc[i]}")
   print("----------------------------------------------------------------------") 

def animarDado ():
    # Paso 4: Simulación  de la aniamción de los dados girando
    print("\nLanzando dados...")
    for i in range(15):
        # Limpia la pantalla según el sistema operativo para el efecto visual estable 
        os.system('cls' if os.name ==  'nt' else 'clear')

    dado_temporal_usuario = random.randint(1, 6)
    dado_temporal_pc = random.randint(1, 6)
     
    mostrar_dados(dado_temporal_usuario, dado_temporal_pc)
    time.sleep(0.1) # Pausa de 100 milisegundos para simular velocidad de giro

def ejecutar_juego():
    print("=== BIENVENIDO AL JUEGO DE DADOS ===\n")
    input("Presiona Enter para lanzar los dados:::")

    animarDado()
     # Limpieza final antes del resultado definitivo
    os.system('cls' if os.name =='nt' else 'clear')
    
    # Paso 5: Valores reales definitivos
    dado_usuario = random.randint(1,6)
    dado_pc = random.randint(1,6)

    print("============= RESULTADO FINAL ===============")
    mostrar_dados(dado_usuario, dado_pc)

    print(f"Resultado: Usuario sacó {dado_usuario} | Computadora sacó {dado_pc}\n")
    if dado_usuario > dado_pc:
        print ("felizidades has ganado")
    elif dado_usuario < dado_pc:
        print ("Ganó la pc")
    else: 
        print ("Empate")
     
    # Evaluacióm del ganador
    # Ejecución del programa
if __name__ == "__main__": 
    ejecutar_juego()
