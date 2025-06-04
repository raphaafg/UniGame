import pygame as pyg # Import the pygame library as 'pyg'

print('Setup start')
pyg.init() # Initialize the pygame library
window = pyg.display.set_mode (size=(800,600)) # Create a window with a size of 800x600 pixels -> size deve ser criada em tupla
print('Setup end')

print('Window loop start')
while True: # Start an infinite loop
    # Check for all events
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit() #if the event is a quit event, exit the loop == close the window
            print('Window loop end')
            quit() #End PYGAME

