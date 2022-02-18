from tkinter import *
from tkinter import ttk
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
calendar = outlook.GetDefaultFolder(9)
appointments = calendar.Items

new_lst = []

for appointment in appointments:
    new_lst.append(appointment.Location)

x = ('\n'.join(new_lst))

ws = Tk()
ws.title('Room Locations')
ws.attributes("-fullscreen", True)
ws.config(bg='yellow')
# IMAGE TAKEN FROM:
# https://www.pinterest.ie/pin/288934132345151288/visual-search/?x=16&y=16&w=538&h=537&cropSource=6&imageSignature=3e6e0fe48f1e97ad27c496f4b8100024
img = PhotoImage(file="room_number.PNG")
f = ("Times bold", 10)
m = ("Times", 12)

def nextPage():
    ws.destroy()
    import page3


def prevPage():
    ws.destroy()
    import page1

Label(
    ws,
    image=img,
    padx=0,
    pady=0,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Label(
    ws,
    font=m,
    text="Room Locations\n\n" + x,
    height=27,
    width=53
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Previous Page",
    font=f,
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
