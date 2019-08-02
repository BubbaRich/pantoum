import tkinter as tk
import pantoum as pt
from tkinter import StringVar

def copy_callback():
    pass

pant = pt.pantoum()

master = tk.Tk()
master.title('Pantoum Creation')
master.geometry('1000x800')

raw_frame = tk.Frame(master, width=400, height=800, padx=0)
final_frame = tk.Frame(master, width=600, height=800, padx=0)

master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)

raw_frame.grid(row=0, column=0)
final_frame.grid(row=0, column=1)

tk.Label(raw_frame, text="Raw Lines").grid(row=0, column=0)

raw_lines_offset = (1, 0)
raw_entry_l = []
copy_button_l = []
space_lines = (4, 6)
gui_line_num = 0
skip_offset = 0
for raw_line in range(8):
    if raw_line in space_lines:
        blank = tk.Label(raw_frame, text="   \n   ")
        blank.grid(row=raw_line+raw_lines_offset[0]+skip_offset)
        skip_offset+=1
    raw_entry_l.append(tk.Entry(raw_frame))
    raw_entry_l[raw_line].grid(row=raw_line+raw_lines_offset[0]+skip_offset, column=0+raw_lines_offset[1])
    copy_button_l.append(tk.Button(raw_frame, text="Copy", command=copy_callback))
    copy_button_l[raw_line].grid(row=raw_line+raw_lines_offset[0]+skip_offset, column=1+raw_lines_offset[1])
    gui_line_num += 1
    
    #tk.Label(master, text= f"Line {line_num + 1}").grid(row=gui_line_num+raw_lines_offset[1])
    #newline_sv = StringVar()
    #http://effbot.org/tkinterbook/variable.htm
    #newline = tk.Entry(master)
    #raw_line_l.append(newline)
    #raw_line_l[line_num].grid(row=gui_line_num+raw_lines_offset[1], column=1+raw_lines_offset[0])
    #line_num+=1

pantoum_offset = (4, 1)
tk.Label(final_frame, text="Pantoum").grid(row=0, column=0)

master.mainloop()
tk.mainloop()
