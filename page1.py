from tkinter import *
from tkinter import ttk
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
calendar = outlook.GetDefaultFolder(9)
appointments = calendar.Items

new_lst = []

for appointment in appointments:
    # print(appointment.ResponseStatus)
    # print(appointment.Location)
    # print(appointment.Duration)
    # print(appointment.Body)
    # print(appointment.ConversationTopic)
    # print("\n")
    new_lst.append(appointment.Subject)  # + ", TOPIC - " + appointment.Body)

x = ('\n'.join(new_lst))

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg'] = '#ffbf00'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import page2


def prevPage():
    ws.destroy()
    import page3


Label(
    ws,
    text="CALENDAR:\n\n" + x,
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
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