class Renderable:
    def __init__(self, anchor_pos, visual, visible=True):
        self.x = anchor_pos[0] # Top left
        self.y = anchor_pos[1] # Top left
        self.visual = visual
        self.width = len(max(visual))
        self.height = len(visual)
        self.visible = visible
    def change_position(self, new_position):
        self.x = new_position[0]
        self.y = new_position[1]
    def set_visibility(self, visibile):
        self.visible = visibile



import time
import os
CANVAS_SIZE = (100, 30)
BACKGROUND_CHAR = " "
FRAME_RATE = 20
DELTA_TIME = 1/FRAME_RATE
frame = []
objects = []
frame_id = 0
events = {}

def clear_frame_data():
    global frame
    frame = [[BACKGROUND_CHAR for r in range(CANVAS_SIZE[0])] for c in range(CANVAS_SIZE[1])]

def render():
    global frame
    global frame_id
    if frame_id in events:
        events[frame_id]()
        events.pop(frame_id)
    clear_frame_data()
    for renderable in objects:
        if renderable.visible == True:
            render_object(renderable)
    # frame[0][len(frame[0])-1] = str(frame_id)
    frame_string = ''
    for r in frame:
        for c in r:
            frame_string += c
        frame_string += '\n'
    print(frame_string, end="\r")
    

def render_object(obj):
    global frame
    if obj.width > CANVAS_SIZE[0] or obj.height > CANVAS_SIZE[1]:
        return
    for r in range(len(obj.visual)):
        for c in range(len(obj.visual[r])):
            try:
                if obj.visual[r][c] == ' ':
                    frame[obj.y + r][obj.x + c] = BACKGROUND_CHAR
                else:
                    frame[obj.y + r][obj.x + c] = obj.visual[r][c] if obj.visual[r][c] != '`' else " "
            except Exception as e:
                # frame[0][0] = f"\n\nERROR: Could not render object of id {objects.index(obj)}: {e}"
                pass

def create_renderable(anchor_pos, visual, visible=True):
    r = Renderable(anchor_pos, visual, visible)
    objects.append(r)
    return r


# hollow_square = create_renderable((20,4), ['#####', '#```#', '#```#', '#####'])
# circle = create_renderable((10,1), [' @@@@ ', '@    @', '@    @', ' @@@@ '])
# square = create_renderable((1,3), ["  #  "," ### ","#####"])
        
def main_loop(callback):
    global frame_id
    global FRAME_RATE
    while True:
        start_of_frame_time = time.time()
        frame_id += 1

        callback()
        clear_frame_data()
        render()
        frame_delta = (60/(FRAME_RATE*60)) - (time.time()-start_of_frame_time)
        if frame_delta < 0:
            continue
        time.sleep(frame_delta)

def start(callback):
    main_loop(callback)


def stop():
    os._exit(1)
# TODO: Prevent sprites from overlapping 
# TODO: Colors

def create_event(frame_to_execute, callback):
    global frame_id
    global events
    events[frame_to_execute] = callback


def get_center():
    global CANVAS_SIZE
    return(int(CANVAS_SIZE[0]/2),int(CANVAS_SIZE[1]/2))