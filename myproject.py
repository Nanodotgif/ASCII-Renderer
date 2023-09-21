import asciirenderer as ar
import keyboard as kb
import os
import time


# ASCII Renderer Options
ar.CANVAS_SIZE = (os.get_terminal_size().columns, os.get_terminal_size().lines -1)
ar.BACKGROUND_CHAR = " "
ar.FRAME_RATE = 30
debug_info = ""
options_open = False

# Creating renderables
top_bar = ar.create_renderable((0,0), [''])
rhombus = ar.create_renderable((3,1), ['   *   ', ' *```* ', '*`````*', ' *```* ', '   *   '])
card = ar.create_renderable((2,2), ['┌─────────┐', '│         │', '│         │', '│         │', '│         │', '│         │', '└─────────┘'])
text = ar.create_renderable((5,5), ["\u28FF"])
wow = ar.create_renderable((5,5), ['⠀⠀⢠⣶⣦⡀⠀⠀⠰⣿⣿⡄⠀⠀⢠⣿⣿⠆⠀⠀⢠⣶⣦⠀⠀⠀', '⠀⠀⠈⢿⣿⣷⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⣾⣿⡟⠀⠀⠀', '⠀⠀⠀⠀⠉⠉⠀⠀⠀⠈⠉⠁⠀⠀⠈⠉⠁⠀⠀⠀⠉⠉⠀⠀⠀⠀', '⣴⣄⠀⠀⠀⠀⢀⣴⡄⠀⢀⣤⣴⣦⣤⡀⠀⢠⣦⡀⠀⠀⠀⠀⣠⣦', '⣿⣿⠀⠀⠀⠀⢸⣿⠇⢠⣿⡟⠋⠙⢻⣿⡄⠸⣿⡇⠀⠀⠀⠀⣿⣿', '⢸⣿⣄⣴⣶⡄⣾⣿⠀⢾⣿⡁⠀⠀⢈⣿⡷⠀⣿⣷⢠⣶⣦⣠⣿⡇', '⠈⣿⣿⡿⠻⣿⣿⡿⠀⠘⣿⣧⣄⣠⣼⣿⠃⠀⢿⣿⣿⠟⢿⣿⣿⠁', '⠀⠻⠛⠁⠀⠘⠻⠃⠀⠀⠈⠛⠻⠟⠛⠁⠀⠀⠘⠟⠃⠀⠈⠛⠟⠀', '⠀⠀⠀⠀⣀⣀⠀⠀⠀⢀⣀⡀⠀⠀⢀⣀⡀⠀⠀⠀⣀⣀⠀⠀⠀⠀', '⠀⠀⢀⣾⣿⡿⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⢿⣿⣧⠀⠀⠀', '⠀⠀⠘⠿⠟⠁⠀⠀⠰⣿⣿⠃⠀⠀⠘⣿⣿⠆⠀⠀⠘⠿⠟⠀⠀⠀'])
options_menu_renderable = ar.create_renderable((1,1), ['┌───────────────────────────────────┐',
                                                       '│ This is the options menu :)       │',
                                                       '│                                   │',
                                                       '│                                   │',
                                                       '│                                   │',
                                                       '│                                   │',
                                                       '└───────────────────────────────────┘'
                                                       ])
options_menu_renderable.set_visibility(False)
title = ar.create_renderable((1,1), ['                                                       WELCOME TO                                                        ', ' █████╗ ███████╗ ██████╗██╗██╗    ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ ███████╗██████╗      ██╗    ██████╗ ', '██╔══██╗██╔════╝██╔════╝██║██║    ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗    ███║   ██╔═████╗', '███████║███████╗██║     ██║██║    ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝█████╗  ██████╔╝    ╚██║   ██║██╔██║', '██╔══██║╚════██║██║     ██║██║    ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗     ██║   ████╔╝██║', '██║  ██║███████║╚██████╗██║██║    ██║  ██║███████╗██║ ╚████║██████╔╝███████╗██║  ██║███████╗██║  ██║     ██║██╗╚██████╔╝', '╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝╚═╝ ╚═════╝ '], visible=False)
title.change_position(((ar.get_center()[0]-int(title.width/2)), 1))
goodbye_renderable = ar.create_renderable((0,0), [' ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗         ', '██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝         ', '██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗           ', '██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝           ', '╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗██╗██╗', ' ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝╚═╝╚═╝'], visible=False)
goodbye_renderable.change_position(((ar.get_center()[0]-int(goodbye_renderable.width/2)),1))

# Define helpers here
def terminate(e):
    title.set_visibility(False)
    goodbye_renderable.set_visibility(True)
    time.sleep(1)
    os.system("cls")
    ar.stop()
    os._exit(1)
def toggle_options(e):
    global options_open
    options_open = not options_open

# Executed every frame update
def every_frame():

    global debug_info
    debug_info = f"Count: {int(ar.frame_id / ar.FRAME_RATE)} || Frame: {ar.frame_id} || Frame Delta: {ar.frame_delta}"
    top_bar.visual = [f'===[q: quit | o: options]{"".join(["=" for i in range(ar.CANVAS_SIZE[0] - (27+len(debug_info)))])}[{debug_info}]']
    if options_open:
        options_menu_renderable.set_visibility(True)
    else:
        options_menu_renderable.set_visibility(False)
    text.change_position((text.x + 1, text.y))
    wow.change_position((wow.x + int(10/ar.frame_id), wow.y + int(10/ar.frame_id)))
    # time.sleep(3)
    # if ar.frame_id %3 ==0:
    #     rhombus.set_visibility(not rhombus.visible)




# Green lol
try:
    os.system("color 2")
except:
    pass

# Keyboard input assignments
kb.on_press_key('q', terminate, suppress=False)
kb.on_press_key('o', toggle_options, suppress=False)


#Scripted events that happen on specific frames
ar.create_event(20, lambda:card.change_position((100,10)))
ar.create_event(40, lambda:card.change_position((1,10)))
ar.create_event(70, lambda:rhombus.change_position((100,10)))
ar.create_event(30, lambda:card.set_visibility(False))

title.set_visibility(True)
ar.start(every_frame) # Start

