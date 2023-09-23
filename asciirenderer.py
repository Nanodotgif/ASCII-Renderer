class Renderable:
    def __init__(self, anchor_x, anchor_y, visual, visible=True, style=0, color=7):
        self.x = anchor_x # Top left
        self.y = anchor_y # Top left
        self.visual = visual
        self.width = len(max(visual))
        self.height = len(visual)
        self.visible = visible
        self.style = style
        self.color = color
    def set_position(self, x, y):
        self.x = x
        self.y = y
    def set_visibility(self, visibile):
        self.visible = visibile
    def set_color(self, color):
        self.color = color


import time
import os
import curses
FRAME_RATE = 20
DELTA_TIME = lambda : 1/FRAME_RATE
HEIGHT = 0
WIDTH = 0
objects = []
frame_id = 0
events = {}
frame_delta = 0


def render(stdscr):
    global frame
    global frame_id
    stdscr.clear()
    for renderable in objects:
        if renderable.visible == True:
            for r in range(len(renderable.visual)):
                for c in range(len(renderable.visual[r])):
                    current_char = chr(stdscr.inch(renderable.y+r, renderable.x+c) & 0xFF) # Get character where we are currently working
                    if renderable.visual[r][c] == "`": # If the character we want to write is "`", this means put a space regardless
                        stdscr.addch(renderable.y + r, renderable.x + c, "\uFEFF")
                    elif current_char != ' ' and current_char != "": # If there is not a space or nothing
                        continue # Don't overrite it, this allows for transparency
                    else: # Write intended character
                        try:
                            stdscr.addch(renderable.y + r, renderable.x + c, renderable.visual[r][c], curses.color_pair(renderable.color) | renderable.style)
                        except:
                            pass
    stdscr.refresh()
    

def create_renderable(x, y, visual, visible=True, style=0, color=1):
    r = Renderable(x, y, visual, visible, style, color)
    objects.append(r)
    return r

def init_colors(): # Add custom color combinations here!
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        
def main_loop(stdscr, callback):
    global frame_id
    global frame_delta
    global HEIGHT
    global WIDTH
    HEIGHT, WIDTH = stdscr.getmaxyx()

    curses.curs_set(0)
    init_colors()

    while True:
        start_of_frame_time = time.time()
        frame_id += 1
        
        # Trigger event callbacks to fire
        if frame_id in events:
            events[frame_id]()
            events.pop(frame_id)

        callback() # Call update function

        render(stdscr)

        frame_delta = (time.time()-start_of_frame_time)
        if frame_delta > (60/(FRAME_RATE*60)):
            continue
        time.sleep((60/(FRAME_RATE*60)) - frame_delta)

def start(callback):
    curses.wrapper(main_loop, callback)


def stop():
    os._exit(1)


def create_event(frame_to_execute, callback):
    global events
    events[frame_to_execute] = callback


def get_center():
    return(int(WIDTH/2),int(HEIGHT/2))