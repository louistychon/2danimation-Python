from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 5
yVelocity = 7

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background = PhotoImage(file="space2.png")
my_image2 = canvas.create_image(0,0,image=background,anchor=NW)

spaceship = PhotoImage(file="spaceship.png")
my_image = canvas.create_image(0,0,image=spaceship,anchor=NW)

image_width = spaceship.width()
image_height = spaceship.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0] >= (WIDTH-image_width) or coordinates[0]<0):
        xVelocity =- xVelocity
    if(coordinates[1] >= (HEIGHT-image_height) or coordinates[0]<0):
        yVelocity =- yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()