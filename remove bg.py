from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog


APP = tk.Tk()
APP.title("REMOVE BG")
APP.minsize(500,200)
APP.maxsize(500,200)

def REMOVE_BG():
    input_image = filedialog.askopenfilename()
    output_image = filedialog.asksaveasfilename() + ".png"
    
    if output_image is None:
        return output_image

    if output_image == "":
        return 0

    
    inpuT = Image.open(input_image)
    output = remove(inpuT)
    output.save(output_image)

    APP_info["text"] = "THE PİCTURE SUCCESSFULLY SAVED"+"\n"+"-->"+"\n"+str(output_image)


APP_info = tk.Label(APP,text = " ",fg = "blue",bg = "white",font = "Arial 15")
APP_info.place(width = 500,height = 120,x = 0,y = 0)

command_button = tk.Button(APP,text = "REMOVE\nBACKGROUND",fg = "lime",bg = "black",activebackground = "lime",activeforeground = "black",font = "Arial 25",command = REMOVE_BG)
command_button.place(width = 500,height = 80,x = 0,y = 120)
    
APP.mainloop()
