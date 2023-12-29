from tools import *

frm =form()
sv=stringVar()
textbox(frm,sv).pack()

def test():
    print(sv.get())
button(frm,"ok",test).pack()
frm.mainloop()
