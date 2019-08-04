import tkinter as tk
import pantoum as pt
from tkinter import StringVar
from io import StringIO

def copy_callback():
    pass

def copy_title():
    pass

pant = pt.pantoum()

master = tk.Tk()
master.title('Pantoum Creation')
master.geometry('1000x800')


raw_frame = tk.Frame(master, width=400, height=800, padx=0)
raw_lines_frame = tk.LabelFrame(raw_frame, text="Raw Lines", relief=tk.SUNKEN)
final_frame = tk.Frame(master, width=600, height=800, padx=0)
pantoum_frame = tk.LabelFrame(final_frame, text=pant.title, relief=tk.SUNKEN)
pantoum_text = tk.Text(pantoum_frame)
pantoum_text.insert(tk.END, "TESTTEXT")

master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)

raw_frame.grid(row=0, column=0)
raw_lines_frame.grid(row=2, column=0, columnspan=3)
final_frame.grid(row=0, column=1)
pantoum_frame.grid(row=0, column=0)
pantoum_text.grid(row=0, column=0)

#tk.Label(raw_frame, text="Raw Lines").grid(row=0, column=0)
firstLineLast=True
firstlinelast_cb = tk.Checkbutton(raw_frame, text="Copy first line to last line", variable=firstLineLast)
title_label = tk.Label(raw_frame, text="Title")
title_entry = tk.Entry(raw_frame)
title_button = tk.Button(raw_frame, text="Copy", command=copy_title)

firstlinelast_cb.grid(row=0, column=0, columnspan=3)
title_label.grid(row=1, column=0)
title_entry.grid(row=1, column=1)
title_button.grid(row=1, column=2)

raw_lines_offset = (1, 0)
raw_entry_l = []
copy_button_l = []
space_lines = (4, 6)
gui_line_num = 0
skip_offset = 0
for raw_line in range(8):
    if raw_line in space_lines:
        blank = tk.Label(raw_lines_frame, text="   \n   ")
        blank.grid(row=raw_line+raw_lines_offset[0]+skip_offset)
        skip_offset+=1
    raw_entry_l.append(tk.Entry(raw_lines_frame))
    raw_entry_l[raw_line].grid(row=raw_line+raw_lines_offset[0]+skip_offset, column=0+raw_lines_offset[1])
    copy_button_l.append(tk.Button(raw_lines_frame, text="Copy", command=copy_callback))
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
#tk.Label(final_frame, text="Pantoum").grid(row=0, column=0)

master.mainloop()
tk.mainloop()
