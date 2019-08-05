import tkinter as tk
from PIL import ImageTk, Image

def on_escape(event=None):
    print("escaped")
    root.destroy()

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# --- fullscreen ---
root.configure(background='black')

#root.overrideredirect(True)  # sometimes it is needed to toggle fullscreen
                              # but then window doesn't get events from system
#root.overrideredirect(False) # so you have to set it back

root.attributes("-fullscreen", True) # run fullscreen
root.wm_attributes("-topmost", True) # keep on top
root.focus_set() # set focus on window
# --- closing methods ---

# close window with key `ESC`
root.bind("<Escape>", on_escape)

canvas = tk.Canvas(root, width = screen_width, height = screen_height)
canvas.pack()
img = Image.open("cloud-texture.png")
pi = ImageTk.PhotoImage(img)

for i in range(0,10):
  offset = i * img.size[0]
  if offset > screen_width:
    break
  canvas.create_image(offset,0, anchor=tk.NW, image=pi)

root.mainloop()