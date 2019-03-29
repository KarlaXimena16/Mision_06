#Autor: Karla Ximena Rueda Ruiz
#Este programa dibuja una curva definida con ecuaciones paramétricas generada un el espirógrafo

import pygame   # Librería de pygame
import math

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente


        # Proces    a los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        radio=100
        k=r/R
        for angulo in range (0,360*(r//math.gcd(r,R))):
            a=math.radians(angulo)
            for periodo in range (0,int(r//math.gcd(r,R))+1):
                a = math.radians(angulo)
                x = int(R*((1-k)*math.cos(a)+l*k* math.cos((1-k)/k*a)))
                y = int(R*((1-k)*math.sin(a)-l * k * math.sin((1 - k) / k * a)))
                pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main(r,R,l):
    r = int(input("Radio menor: "))
    R = int(input("Radio mayor: "))
    l = float(input("Valor de l: "))
    dibujar(r,R,l)   # Por ahora, solo dibuja




# Llamas a la función principal
main(65,220,0.8)