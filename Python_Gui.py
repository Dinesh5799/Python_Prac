import tkinter
from tkinter import Menu
from tkinter import ttk   #themed tk


def _quit():
    top.quit()
    top.destroy()
    exit()


top = tkinter.Tk()
top.title('Weather App')
top.minsize(width=300,height=400)
top.resizable(0,0)
menuBar = Menu()
top.config(menu = menuBar)
fMenu = Menu(menuBar,tearoff=0)
fMenu.add_command(label = 'New')
fMenu.add_separator()
fMenu.add_command(label='Exit',command = _quit)
menuBar.add_cascade(label = 'File',menu = fMenu)

tabControl = ttk.Notebook(top)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1,text = 'Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text = 'Tab 2')

tabControl.pack(expand = 1,fill='both')
weather_condition = ttk.LabelFrame(tab1,text = 'Current Weather Conditions')
weather_condition.grid(column=0,row=0,pady=4)
ttk.Label(weather_condition,text='Location:').grid(column=0,row=0,sticky='W')
top.mainloop()


