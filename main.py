import tkinter as tk
import random
import pygame 

COLOR_WHITE = 'white'

WINDOW_WIDTH = 1254
WINDOW_HEIGHT = 627
CANVAS_MAX_WIDTH = 5000
CANVAS_MAX_HEIGHT = 5000

ENTER_X = 150
ENTER_Y = 250
TEXT_X = 150
TEXT_Y = 300
BUTTON_KEY_X = 150
BUTTON_KEY_Y = 350
BUTTON_ANIM_X = 150
BUTTON_ANIM_Y = 400

ANIMATION_CENTER_X = WINDOW_WIDTH // 2
ANIMATION_CENTER_Y = WINDOW_HEIGHT // 2
ANIMATION_FRAME_COUNT = 12
ANIMATION_DELAY_MS = 100

KEY_LENGTH = 6
SAMPLE_BLOCK_SIZE = 3

BACKGROUND_IMAGE = "photo.png"
ANIMATION_GIF = "animationcat.gif"
AUDIO = "Granny.mp3"


def create_key(word):
    if len(word) != KEY_LENGTH:
        key = "incorrect length"
        return key
    
    block1 = "".join(random.sample(word, SAMPLE_BLOCK_SIZE))
    block2 = "".join([str((ord(c)-64)%10) for c in word])
    block3 = "".join(random.sample(word, SAMPLE_BLOCK_SIZE))

    key = f"{block1}-{block2}-{block3}"

    return key


def click_button():
    created_key=create_key(enter.get().upper())
    canvas.itemconfig(text_id, text='generation key:  ' + created_key)
    enter.delete(0, tk.END)


def show_animation():
    frame_count =  ANIMATION_FRAME_COUNT         
    frames = [tk.PhotoImage(file=ANIMATION_GIF, format = f'gif -index {i}')
               for i in range(frame_count)]


    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frame_count:
            ind = 0
        canvas.create_image((ANIMATION_CENTER_X, ANIMATION_CENTER_Y),image=frame)
        window.after(ANIMATION_DELAY_MS, update, ind)
        

    label = tk.Label(window)
    label.pack()
    window.after(0, update, 0)


window = tk.Tk()
window.title('lab3')
window.geometry(F'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

canvas = tk.Canvas(bg=COLOR_WHITE, width=CANVAS_MAX_WIDTH, height=CANVAS_MAX_HEIGHT)
canvas.pack(anchor="center", expand=1)

bg_image = tk.PhotoImage(file=BACKGROUND_IMAGE)
canvas.create_image(0, 0,anchor="nw", image=bg_image)

enter = tk.Entry()
canvas.create_window((ENTER_X, ENTER_Y), anchor='nw', window=enter)

text_id = canvas.create_text((TEXT_X, TEXT_Y), anchor='nw', text='', fill=COLOR_WHITE)

button_show_key = tk.Button(window, text='Ganerate key', command=click_button)
canvas.create_window((BUTTON_KEY_X, BUTTON_KEY_Y), anchor='nw', window=button_show_key)

button_show_anim = tk.Button(window, text='Show Animation', command=show_animation)
canvas.create_window((BUTTON_ANIM_X, BUTTON_ANIM_Y), anchor='nw', window=button_show_anim)

pygame.mixer.init()
pygame.mixer.music.load(AUDIO)
pygame.mixer.music.play(-1)

if __name__ == '__main__':
    window.mainloop() 
