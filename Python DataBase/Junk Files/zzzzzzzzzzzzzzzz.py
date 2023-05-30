from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
import pygame

pygame.init()

# Configurar la ventana de visualización
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Botón animado")

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Definir las dimensiones y la posición del botón
button_width = 200
button_height = 60
button_x = 100
button_y = 100

# Crear el objeto de botón
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Definir el texto del botón
font = pygame.font.SysFont(None, 36)
text = font.render("Presiona aquí", True, WHITE)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Detectar si el botón ha sido presionado
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                print("¡Botón presionado!")

    # Dibujar el botón
    pygame.draw.rect(screen, GREEN, button_rect)
    screen.blit(text, (button_x + 50, button_y + 10))

    # Cambiar el color del botón al hacer clic en él
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, WHITE, button_rect, 3)
    else:
        pygame.draw.rect(screen, BLACK, button_rect, 3)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()




























































































