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
ws.title('Room Locations')
ws.attributes("-fullscreen", True)
ws.config(bg='white')
# IMAGE TAKEN FROM:
# https://www.istockphoto.com/photo/september-2021-calendar-on-yellow-background-gm1298563635-391399204
img = PhotoImage(file="calendar.png")
f = ("Times bold", 10)
m = ("Times", 12)

mylabel = Label(ws, text='', font="0")
mylabel.pack()
myscroll = Scrollbar(ws)
myscroll.pack(side=RIGHT, fill=Y)
mylist = Listbox(ws, yscrollcommand=myscroll.set)

for appointment in appointments:

    for line in range(1, 100):
        mylist.insert(END, str(appointment.Subject))
mylist.pack(side = BOTTOM, fill = BOTH, padx=500, pady=100 )


def nextPage():
    ws.destroy()
    import page2

def prevPage():
    ws.destroy()
    import page3

def weatherPage():
    ws.destroy()
    import weatherAPI

Label(
    ws,
    image=img,
    padx=0,
    pady=0,
    bg='#bd580b',
    font=f
).pack(expand=True, fill=BOTH)

Label(
    ws,
    font=m,
    text=myscroll.config(command = mylist.yview) ,
    height=2,
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

Button(
    ws,
    text="Text Editor",
    font=f,
    command=weatherPage
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
