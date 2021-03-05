import pyautogui

import tkinter as tk

from tkinter import filedialog

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()


def takeScreenshot():
    myScreenshot = pyautogui.screenshot()

    file_path = filedialog.asksaveasfilename(defaultextension='.png')

    myScreenshot.save(file_path)


myButton = tk.Button(text="Take Screenshot", command=takeScreenshot, bg='green', fg='white', font=10)
close_button = tk.Button(text="QUIT", command=quit, bg='red', fg='white', font=10)

myButton.pack(side=tk.LEFT)
close_button.pack()
root.mainloop()
