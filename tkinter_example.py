# tkinter_example.py
import tkinter as tk
from PIL import Image, ImageTk
import threading
root = tk.Tk()

root.geometry('300x500')
root.title('Tkinter Hub')
gif_frames = []

frame_delay = 0




def ready_gif():
    global frame_delay
    print('Started')
    gif_file =Image.open('giphy.gif')
    
    for r in range(0, gif_file.n_frames):
        gif_file.seek(r)
        gif_frames.append(gif_file.copy())
    
    frame_delay = gif_file.info['duration']
    print('Complete')
    play_gif()

frame_count = -1

def play_gif():
    global frame_count, current_frame
    
    if frame_count >= len(gif_frames) - 1:
        frame_count = -1
        play_gif()
        
        
    else:    
        frame_count += 1
    
        current_frame = ImageTk.PhotoImage(gif_frames[frame_count])
        gif_lb.config(image=current_frame)
    
    
        root.after(frame_delay, play_gif)   
    
gif_lb = tk.Label(root)
gif_lb.pack(fill=tk.BOTH)
            
threading.Thread(target=ready_gif).start()

root.mainloop()
