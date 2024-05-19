import pygame
import pygame_menu

pygame.init()
font1 = pygame_menu.font.FONT_MUNRO
window = pygame.display.set_mode((600, 400))

def set_difficulty(value, difficulty):
    # Do the job here!
    pass

def start_the_game():
    # Do the job here!
    pass

mytheme = pygame_menu.Theme(widget_font=font1, background_color=(0, 0, 0),
                            title_background_color=(153, 0, 153),
                            widget_font_color=(153, 0, 153))

start_settings_menu = pygame_menu.Menu(800, 830, theme=my_theme)
start_settings_menu.add_button('Back', pygame_menu.events.BACK)

start_menu = pygame_menu.Menu(800, 830, theme=my_theme)
start_menu.add_button('Play', start)
start_menu.add_button('Settings', start_settings_menu)
start_menu.add_button('Quit', pygame_menu.events.EXIT)
start_menu.mainloop(win)

start_menu.mainloop(window)
