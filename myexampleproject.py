import asciirenderer as ar
import keyboard as kb
import os
import time


# ASCII Renderer Options
ar.FRAME_RATE = 30


debug_info = ""
options_open = False
paused = False

# Creating renderables
top_bar = ar.create_renderable(0,0, [' '])
options_menu_renderable = ar.create_renderable(1,1, ['┌───────────────────────────────────┐',
                                                     '│`This`is`the`options`menu`:)```````│',
                                                     '│```````````````````````````````````│',
                                                     '│```````````````````````````````````│',
                                                     '│```````````````````````````````````│',
                                                     '│```````````````````````````````````│',
                                                     '└───────────────────────────────────┘'
                                                     ], color=3)
card = ar.create_renderable(2,2, ['┌─────────┐',
                                  '│  HELLO  │',
                                  '│         │',
                                  '│         │',
                                  '│         │',
                                  '│         │',
                                  '└─────────┘'])
goodbye_renderable = ar.create_renderable(0,0, [' ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗         ',
                                                '██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝         ',
                                                '██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗           ',
                                                '██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝           ',
                                                '╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗██╗██╗',
                                                ' ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝╚═╝╚═╝']
                                                , visible=False, color=3)
square = ar.create_renderable(3,3, [' .----------------. ',
                                    '| .--------------. |',
                                    '| |              | |',
                                    '| |              | |',
                                    '| |              | |',
                                    '| |              | |',
                                    '| |              | |',
                                    '| |              | |',
                                    '| |              | |',
                                    "| '--------------' |",
                                    " '----------------' "])
title = ar.create_renderable(0,0, [' █████╗ ███████╗ ██████╗██╗██╗    ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ ███████╗██████╗ ',
                                   '██╔══██╗██╔════╝██╔════╝██║██║    ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗',
                                   '███████║███████╗██║     ██║██║    ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝█████╗  ██████╔╝',
                                   '██╔══██║╚════██║██║     ██║██║    ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗',
                                   '██║  ██║███████║╚██████╗██║██║    ██║  ██║███████╗██║ ╚████║██████╔╝███████╗██║  ██║███████╗██║  ██║',
                                   '╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝',]
                                   , color=3)

# Key mapped functions
def terminate(e):
    global paused
    paused = True
    title.set_visibility(False)
    goodbye_renderable.set_visibility(True)
    time.sleep(1)
    ar.stop()
    os._exit(1)
def toggle_options(e):
    global options_open
    options_open = not options_open

# Executed every frame update, passed to asciirenderer.start()
def every_frame():
    if paused:
        return
    global debug_info
    debug_info = f"Seconds: {int(ar.frame_id / ar.FRAME_RATE)} || Frame: {ar.frame_id} || Center: {ar.get_center()} || Delta Time: {ar.DELTA_TIME():.2f} || Frame Time = {ar.frame_delta:.5f}"
    top_bar.visual = [f'===[q: quit | o: options]{"".join(["=" for _ in range(ar.WIDTH - (27+len(debug_info)))])}[{debug_info}]']
    if options_open:
        options_menu_renderable.set_visibility(True)
    else:
        options_menu_renderable.set_visibility(False)
    try:
        square.set_position(int(square.x + 50 * ar.DELTA_TIME()), square.y)
    except:
        pass
    if ar.frame_id %10 ==0:
        title.set_visibility(not title.visible)


# Keyboard input assignments
kb.on_press_key('q', terminate, suppress=False)
kb.on_press_key('o', toggle_options, suppress=False)


#Scripted events that happen on specific frames, limited to one event per frame.
ar.create_event(1, lambda: title.set_position((ar.get_center()[0]-int(title.width/2)), 2))
ar.create_event(2, lambda: goodbye_renderable.set_position((ar.get_center()[0]-int(goodbye_renderable.width/2)), 2))


ar.start(every_frame) # Start the application

