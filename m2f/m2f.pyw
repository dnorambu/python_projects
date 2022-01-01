from tkinter import Tk, Button, Label, DoubleVar, Entry
# TK app class basic, DoubleVar is a type of float

window = Tk()
window.title("Feet to meter")
window.configure(background="light green")
window.geometry("320x220")
window.resizable(width=False,height=False)

#functions
def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set("%.4f" % meter)

def clear():
    ft_value.set("")
    mt_value.set("")

#Add labels to the app
#Feet label
#padx,pady creates horizontal/vertical space to the margins of the app
ft_lbl= Label(window,text="Feet",bg="purple",fg="white",width=14)
ft_lbl.grid(column=0,row=0,padx=15,pady=15)

ft_value = DoubleVar() #Tkinter datatype to input numbers
ft_entry = Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end') #there is no value when the app launchs

#Meter labels
mt_lbl= Label(window,text="Meter",bg="purple",fg="white",width=14)
mt_lbl.grid(column=0,row=1,padx=15,pady=15)

mt_value = DoubleVar() #Tkinter datatype to input numbers
mt_entry = Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1)
mt_entry.delete(0,'end') #there is no value when the app launchs

#Buttons to make conversion
#command is the function call
convert_btn = Button(window,text="Convert",bg="purple",fg="white",width=14,command=convert)
convert_btn.grid(column=0,row=3,padx=15)

clear_btn = Button(window,text="Clear",bg="purple",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)
window.mainloop()
