import pygame as pg

#inicializar los modulos de pygame, pantallas, objetos, sonidos, teclas, ect.
pg.init()
    

#Crear pantalla o surface
pantalla = pg.display.set_mode( (800,600) ) #Definicion de tamaño de pantallas.
pg.display.set_caption("KILL KILL PUSSYCAT!") #Agregar un titulo a la ventana.

game_over = True
x = 0
y = 300
vx = 1
while  game_over:

    for eventos in pg.event.get(): #Capturo todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill( (70, 255, 0) ) # Asignar un color a la pantalla
    x = x+vx

    if x == 800 or x == 0:
        vx = vx*-1

    y = y + vx

    if y == 600 or y == 0:
        vx = vx*-1

    #la pantalla , color rgb, posiciones (posicionx,y), tamaño(x,y))
    pg.draw.rect(pantalla,( 240, 65, 14), (x,y,20,20))

    pg.display.flip() # Funcion para cargar toda la configuracion que va dentro de la pantalla







pg.quit()


