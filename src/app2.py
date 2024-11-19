from tkinter import *
from dataHandler import *



def showAlerts(alerts):
    for i in alerts:
        print(i)

    count = 1
    for alert in alerts:
        Lb.insert(count, alert["title"])
        count += 1

    Lb.pack()

    top.mainloop()

def on_select(event):
    # Get the selected item(s) from the Listbox
    selected_items = Lb.curselection()

    # Display the selected item(s) in the label
    alert = alerts[selected_items[0]]
    label_str = ""
    for i in alert:
        label_str = label_str + "{}: {}\n".format(i, alert[i])
    var.set(label_str)
    label.pack()
    top.mainloop()


data = readData()
alerts = parseXML("weather_alerts.xml")

top = Tk()
Lb = Listbox(top, width=500, height=25)
var = StringVar()
label = Label(top, textvariable=var, relief=RAISED, width=500, height=25)
Lb.bind("<<ListboxSelect>>", on_select)


showAlerts(alerts)