from tkinter import *
from tkinter import ttk
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
calendar = outlook.GetDefaultFolder(9)
appointments = calendar.Items

new_lst = []

for appointment in appointments:
    new_lst.append(appointment.Subject)

x = ('\n'.join(new_lst))

ws = Tk()
ws.title('Calendar')
ws.attributes("-fullscreen", True)
ws.config(bg='yellow')
# IMAGE TAKEN FROM:
# https://www.istockphoto.com/photo/september-2021-calendar-on-yellow-background-gm1298563635-391399204
img = PhotoImage(file="calendar.png")
f = ("Times bold", 20)
m = ("Times", 15)

def nextPage():
    ws.destroy()
    import page2


def prevPage():
    ws.destroy()
    import page3

Label(
    ws,
    image=img,
    padx=10,
    pady=10,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)

Label(
    ws,
    font=m,
    text="CALENDAR:\n\n" + x,
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
