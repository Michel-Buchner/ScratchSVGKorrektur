from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showerror, showinfo
from ScratchSvgKorrektur_backend import correct_svg     

# defines exit function for quitting the program and window
def exit():
    master.destroy()

# defines function to be called by buttonclick, opens file selector, returns list of selected files and executes actual correct_svg function on this list
def callback():
    names = askopenfilenames() 
    try:
        number_of_svg_files, number_of_selected_files = correct_svg(names)

        #shows info dialog of how many of the selected files were .svg and exits the program
        showinfo("Info", str(number_of_svg_files) + " von " + str(number_of_selected_files) + " ausgewählten Dateien wurden korrigiert." )
        exit()
    except NameError:
        showerror("Fehler", "Bitte wähle eine oder mehrere SVG-Dateien aus.")

#create GUI with tk inter
master = Tk()

master.title('Korrekturskript')
Label(master, text="Hier kannst du SVG-Dateien von Scratchblöcken \n auswählen, die korrigiert werden müssen.").grid(row=0)

errmsg = 'Error!'
#Creates button to select files
Button(text='Dateien auswählen', command=callback).grid(row=3, column=0, sticky='w')
#Creates button to quit window
Button(text='Beenden', command=exit).grid(row=3, column=0, sticky='e')
mainloop()