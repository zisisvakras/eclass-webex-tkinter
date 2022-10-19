#!/usr/bin/python3
# Webex tkinter application
# author: r0thl3ss

from tkinter import *
import webbrowser
import pathlib
import os
import json

# All basic vars
current_folder = os.path.abspath(__file__).replace(__file__.split("\\")[-1], "")
with open(current_folder + "config.json", encoding="utf-8") as read_file:
    config = json.load(read_file)

book_color = config["book_color"]
webex_link = config["webex_link"]
books_folder = current_folder + config["books_folder"]
book_text = config["book_text"]

window = Tk()
window.title("Eclass")
window.geometry("677x307")

# Labels for days
row_days = 1
for i in config["days"]:
  Label(window, text=i).grid(column=0, row=row_days)
  row_days += 2

# Labels for time
column_time = 1
for i in config["time_table"]:
  Label(window, text=i).grid(column=column_time, row=0)
  column_time += 1

# Lessons labels & buttons loop
for i in config["lessons"]:
  lesson = i.split(",")
  Button(window, text=lesson[0],
      command=lambda lesson=lesson: webbrowser.open(webex_link + lesson[1]),
      height=1, width=11).grid(column=lesson[4], row=2*int(lesson[3])-1)
  if lesson[2]=="none":
    Button(window, text="---",height=1, width=11, fg=book_color).grid(column=lesson[4], row=2*int(lesson[3]))
  else:
    Button(window, text=book_text,
      command=lambda lesson=lesson: webbrowser.open(books_folder + "\\" + lesson[2]),
      height=1, width=11, fg=book_color).grid(column=lesson[4], row=2*int(lesson[3]))
    
# Extra loop
extra_count = 1
for i in config["extra"]:
  if extra_count > 8 : 
    break
  extra_i = i.split(",")
  Button(window, text=extra_i[0],
      command=lambda extra_i=extra_i: webbrowser.open(extra_i[1]),
      height=1, width=11, fg=extra_i[2]).grid(column=extra_count, row=11)
  extra_count += 1

# Initiating
window.mainloop()
