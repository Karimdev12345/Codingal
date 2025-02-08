from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename 

window= Tk()
window.title ("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    """Open a file for editing."""
    filepath= askopenfilename(
        filetypes= [("Text File", "*.txt"), ("All Files", "*.*")]

    )
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    with open(filepath, "r") as input_file:
        text= input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
        window.title(f"Codingal's Text Editor-{filepath}")

txt_edit= Text(window)
fr_button= Frame(window, releif= RAISED, bd=2)
btn_open= Button(fr_button,text= "Open", command= open_file)
window.mainloop()