from tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import Toplevel

def form(geometry="500x300",is_center=True):
    f=Tk()
    f.geometry(geometry)
    if is_center: tkcenter(f)
    return f

def button(form,text="Button",command=None):
     btn = ttk.Button(form,text=text)
     if command != None:
        btn.config(command =command)  
     return btn
def label(form,text="Label"):
    return ttk.Label(form,text=text)

def entry(form):
    txt=ttk.Entry(form)
    return txt

def stringVar():
    return StringVar()

def intVar():
    return IntVar()

def booeanVar():
    return BooleanVar()


def textbox(form,variable=None,isnum = False):
    
    def numberonly(text):
        if str.isdigit(text):
            return True
        elif text == "":
            return True
        else:
            return False
        
    reg_fun =form.register(numberonly)
    txt=ttk.Entry(form)
    if isnum : 
        txt.config(validate="key",validatecommand=(reg_fun,"%P"))
    if variable!=None:
        txt.config(textvariable=variable)
    return txt

def radio(form,text="radio",value=0,variable=None):
    rdo=ttk.Radiobutton(form,text=text,value=value)
    if variable !=None:
        rdo.config(variable=variable)
    return rdo

def checkbox(form,text="CheckBox",variable =None):
    cbx =ttk.Checkbutton(form ,text =text)
    if variable != None:
        cbx.config(variable = variable)
    return cbx

def tkcenter(form):
    form.update()
    fw = form.winfo_width()
    fh =form.winfo_height()
    sw =form.winfo_screenwidth()
    sh =form.winfo_screenheight()
    x =(sw-fw) / 2
    y =(sh - fh) / 2 
    form.geometry("%dx%d+%d+%d" %(fw,fh,x,y))

def bgall(form,bg):
    form.update()
    ctrls = form.winfo_children()
    form.config(bg=bg)
    for c in ctrls:
        ci = c.winfo_class()
        if ci =="Label" or ci =="Button" or ci =="Entry" or ci =="Radiobutton":
            c["bg"]=bg 
        if ci =="TLabel" or ci =="TButton" or ci =="TEntry" or ci =="TRadiobutton":
            my = ttk.Style()
            my.configure("TLabel",background =bg)
            my.configure("TButton",background =bg)
            my.configure("TEntry",background =bg)
            my.configure("TRadiobutton",background =bg)
def fontall(form, font):
    form.update()
    ctrls = form.winfo_children()
    for c in ctrls:
        ci = c.winfo_class()
        
        if ci =="Label" or ci =="Button" or ci =="Entry" or ci =="Radiobutton":
            c["font"] = font
        if ci =="TLabel" or ci =="TButton" or ci =="TEntry" or ci =="TRadiobutton":
             my =ttk.Style()
             
             my.configure("TLabel",font =font)
             
             my.configure("TButton",font =font)
             
             my.configure("TEntry",font =font)
             
             my.configure("TRadiobutton",font =font)

def fgall(form,fg):
    form.update()
    ctrls=form.winfo_children()
    for c in ctrls:
        ci =c.winfo_class()
        if ci =="Label" or ci =="Button" or ci =="Entry" or ci =="Radiobutton":
            c["fg"]=fg
        if ci =="TLabel" or ci =="TButton" or ci =="TEntry" or ci =="TRadiobutton":
            my =ttk.Style()
            my.configure("TLabel",foreground =fg)
            my.configure("TEntry",foreground =fg)
            my.configure("TButton",foreground =fg)
            my.configure("",foreground =fg)
def msgbox(text):
    messagebox.showinfo("TRadiobutton",text)
    
def msgask(text):
    return messagebox.askyesno("",text)
def inbox(text):
    f =Toplevel()
    f.title(text)
    f.geometry("400x200")
    f.resizable(False,False)
    tkcenter(f)
    ttk.Label(f,text =text,font ="None 15").pack(pady=10)
    sv =StringVar()
    txt=ttk.Entry(f,font="None 15",width=35,textvariable =sv)
    txt.pack(pady=10 )
    txt.bind("<Return>",lambda my: f.destroy())
    ttk.Style().configure("inbox.TButton",font="None 15")
    ttk.Button(f,text="ok",command =lambda:f.destroy(),style ="inbox.TButton").pack(pady=10)
    txt.focus()
    f.grab_set()
    f.wait_window()
 
    return sv.get()

def inboxnum(text,numberonly=False):
   
    
    #fm=Tk()
    fm=Toplevel()
    fm.geometry("500x300")
    fm.title("ines")
    fm.resizable(False,False)
    tkcenter(fm)
    ttk.Label(fm,text="text",font ="None 15").pack(pady=10)
    sv=StringVar()
    def numberonly(text):
        if str.isdigit(text):
            return True
        elif text == "":
            return True
        else:
            return False
    reg_fun =fm.register(numberonly)
    txt=ttk.Entry(fm,font ="None 15",textvariable=sv)
    if numberonly: 
        txt.config(validate="key",validatecommand=(reg_fun,"%P"))
    txt.pack(pady=10)
    txt.bind("<Return>",lambda my:f.destroy())
    ttk.Style().configure("inboxTButton",font ="None 15")
    ttk.Button(fm,text="ok",command=lambda:fm.destroy(),style="inbox.TButton").pack()
    
    fm.grab_set()
    txt.focus()
    fm.wait_window()
    return sv.get()


    
    
    
    
          
    
    

    
