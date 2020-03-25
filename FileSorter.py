import conda
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
from tkinter import *

Window = Tk()
Window.title("FileSorter")

fromtext = Entry(Window)
totext = Entry(Window)

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = str(fromtext.get())
folder_destination = str(totext.get())
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

def onclick():
    observer.start()

button = Button(Window, text="Sort Files", command=onclick)

fromtext.pack()
totext.pack()
button.pack()

Window.resizable(False, False)

Window.mainloop()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

