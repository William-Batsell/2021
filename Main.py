import tkinter
from tkinter import *
from PIL import ImageTk,Image
from playsound import playsound
App = tkinter.Tk()
App.iconbitmap('C:/Connor/Bac Mono.ico')
App.title('Time Manager')
App.geometry('337x450')
activity = Label(App, text='Activity')
activity.grid(row=0, column=2)
App.wm_attributes('-transparentcolor', '#60b26c')
bg = ImageTk.PhotoImage(file="C:/Users/wbats/Downloads/drui2.jpg")
bj = Label(App, image=bg)
bj.place(x=0, y=0, relwidth=1, relheight=1)
def clear():
    ricky.delete(0, END)
    ricky2.delete(0, END)
    ricky3.delete(0, END)
    ricky4.delete(0, END)
    ricky5.delete(0, END)
    ricky6.delete(0, END)
    ricky7.delete(0, END)
    ricky8.delete(0, END)
    ricky9.delete(0, END)
    ricky10.delete(0, END)
    ricky11.delete(0, END)
    ricky12.delete(0, END)
    ricky13.delete(0, END)
    ricky14.delete(0, END)
    ricky15.delete(0, END)
    ricky16.delete(0, END)
    ricky17.delete(0, END)
    ricky18.delete(0, END)
    ricky19.delete(0, END)
    ricky20.delete(0, END)
kichy = Label(App, text='8:00', bg="#60b26c", font='Helvetica')
kichy.grid(row=1, column=1)
kichy2 = Label(App, text='8:30', bg="#60b26c", font='Helvetica')
kichy2.grid(row=2, column=1)
kichy3 = Label(App, text='9:00', bg="#60b26c", font='Helvetica')
kichy3.grid(row=3, column=1)
kichy4 = Label(App, text='9:30', bg="#60b26c", font='Helvetica')
kichy4.grid(row=4, column=1)
kichy5 = Label(App, text='10:00', bg="#60b26c", font='Helvetica')
kichy5.grid(row=5, column=1)
kichy6 = Label(App, text='10:30', bg="#60b26c", font='Helvetica')
kichy6.grid(row=6, column=1)
kichy7 = Label(App, text='11:00', bg="#60b26c", font='Helvetica')
kichy7.grid(row=7, column=1)
kichy8 = Label(App, text='11:30', bg="#60b26c", font='Helvetica')
kichy8.grid(row=8, column=1)
kichy9 = Label(App, text='12:00', bg="#60b26c", font='Helvetica')
kichy9.grid(row=9, column=1)
kichy10 = Label(App, text='12:30', bg="#60b26c", font='Helvetica')
kichy10.grid(row=10, column=1)
kichy11 = Label(App, text='1:00', bg="#60b26c", font='Helvetica')
kichy11.grid(row=11, column=1)
kichy12 = Label(App, text='1:30', bg="#60b26c", font='Helvetica')
kichy12.grid(row=12, column=1)
kichy13 = Label(App, text='2:00', bg="#60b26c", font='Helvetica')
kichy13.grid(row=13, column=1)
kichy14 = Label(App, text='2:30', bg="#60b26c", font='Helvetica')
kichy14.grid(row=14, column=1)
kichy15 = Label(App, text='2:30', bg="#60b26c", font='Helvetica')
kichy15.grid(row=15, column=1)
kichy16 = Label(App, text='3:00', bg="#60b26c", font='Helvetica')
kichy16.grid(row=16, column=1)
kichy17 = Label(App, text='3:30', bg="#60b26c", font='Helvetica')
kichy17.grid(row=17, column=1)
kichy18 = Label(App, text='4:00', bg="#60b26c", font='Helvetica')
kichy18.grid(row=18, column=1)
kichy19 = Label(App, text='4:30', bg="#60b26c", font='Helvetica')
kichy19.grid(row=19, column=1)
kichy20 = Label(App, text='5:00', bg="#60b26c", font='Helvetica')
kichy20.grid(row=20, column=1)
ricky = Entry(App, width=35)
ricky.grid(row=1, column=2)
ricky2 = Entry(App, width=35)
ricky2.grid(row=2, column=2)
ricky3 = Entry(App, width=35)
ricky3.grid(row=3, column=2)
ricky4 = Entry(App, width=35)
ricky4.grid(row=4, column=2)
ricky5 = Entry(App, width=35)
ricky5.grid(row=5, column=2)
ricky6 = Entry(App, width=35)
ricky6.grid(row=6, column=2)
ricky7 = Entry(App, width=35)
ricky7.grid(row=7, column=2)
ricky8 = Entry(App, width=35)
ricky8.grid(row=8, column=2)
ricky9 = Entry(App, width=35)
ricky9.grid(row=9, column=2)
ricky10 = Entry(App, width=35)
ricky10.grid(row=10, column=2)
ricky11 = Entry(App, width=35)
ricky11.grid(row=11, column=2)
ricky12 = Entry(App, width=35)
ricky12.grid(row=12, column=2)
ricky13 = Entry(App, width=35)
ricky13.grid(row=13, column=2)
ricky14 = Entry(App, width=35)
ricky14.grid(row=14, column=2)
ricky15 = Entry(App, width=35)
ricky15.grid(row=15, column=2)
ricky16 = Entry(App, width=35)
ricky16.grid(row=16, column=2)
ricky17 = Entry(App, width=35)
ricky17.grid(row=17, column=2)
ricky18 = Entry(App, width=35)
ricky18.grid(row=18, column=2)
ricky19 = Entry(App, width=35,)
ricky19.grid(row=19, column=2)
ricky20 = Entry(App, width=35)
ricky20.grid(row=20, column=2)
button = Button(App, text="Clear", command=clear)
button.grid(row=15, column="3")


App.mainloop()
