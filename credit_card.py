from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("500x500")
root.title("PoKeMaN")
root.configure(background="yellow")

enter_pin_input=Entry(root)
enter_pin_input.place(relx=0.5,rely=0.2,anchor=CENTER)


label_card_image=Label(root)
label_card_image.place(relx=0.5,rely=0.5,anchor=CENTER)

def authentication():
    value=get(enter_pin_input)
    value_int=int(value)
    try:
        print(value)
    except ValueError:
        messagebox.showinfo("Error","CREDIT CARD SCANNED!,")    
        
btn = Button(text="CLICK TO SCAN CARD",command=authentication)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()