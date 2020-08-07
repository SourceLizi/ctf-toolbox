#!/usr/bin/env python
import tkinter

WIN_WIDTH=60

UP_CHAR='w'
DOWN_CHAR='s'
LEFT_CHAR='a'
RIGHT_CHAR='d'

mwin = tkinter.Tk()
mwin.title("maze_runner")
mwin.width=WIN_WIDTH
mwin.height=80
move_log=tkinter.StringVar(mwin)

entry = tkinter.Entry(mwin,textvariable=move_log,width=WIN_WIDTH)
entry.pack()

def up_event(event_obj):
	global move_log
	move_log.set(move_log.get() + UP_CHAR)

def down_event(event_obj):
	global move_log
	move_log.set(move_log.get() + DOWN_CHAR)

def left_event(event_obj):
	global move_log
	move_log.set(move_log.get() + LEFT_CHAR)

def right_event(event_obj):
	global move_log
	move_log.set(move_log.get() + RIGHT_CHAR)

def clear_event(event_obj):
	global move_log
	move_log.set("")

text = tkinter.Text(mwin,width=WIN_WIDTH)
text.bind("<KeyPress-Up>",up_event)
text.bind("<KeyPress-Down>",down_event)
text.bind("<KeyPress-Left>",left_event)
text.bind("<KeyPress-Right>",right_event)
text.bind("<KeyPress-Escape>",clear_event)
text.pack()

mwin.mainloop()
