import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_235=tk.Label(root)
        GLabel_235["bg"] = "#a1e2a1"
        ft = tkFont.Font(family='Times',size=17)
        GLabel_235["font"] = ft
        GLabel_235["fg"] = "#333333"
        GLabel_235["justify"] = "center"
        GLabel_235["text"] = "You Are Protected!"
        GLabel_235.place(x=60,y=100,width=422,height=107)

        GLabel_930=tk.Label(root)
        GLabel_930["bg"] = "#91a291"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_930["font"] = ft
        GLabel_930["fg"] = "#333333"
        GLabel_930["justify"] = "center"
        GLabel_930["text"] = "System secured"
        GLabel_930.place(x=300,y=210,width=182,height=30)

        GLabel_998=tk.Label(root)
        GLabel_998["activebackground"] = "#131111"
        GLabel_998["bg"] = "#8ededf"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_998["font"] = ft
        GLabel_998["fg"] = "#0b0e0e"
        GLabel_998["justify"] = "center"
        GLabel_998["text"] = "Scan"
        GLabel_998["relief"] = "groove"
        GLabel_998.place(x=500,y=130,width=84,height=101)

        GLabel_451=tk.Label(root)
        GLabel_451["bg"] = "#8bd7d8"
        GLabel_451["disabledforeground"] = "#e5dbdb"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_451["font"] = ft
        GLabel_451["fg"] = "#0f0f11"
        GLabel_451["justify"] = "center"
        GLabel_451["text"] = "Toolbox"
        GLabel_451.place(x=500,y=240,width=85,height=102)

        GLabel_888=tk.Label(root)
        GLabel_888["bg"] = "#6fc1c3"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_888["font"] = ft
        GLabel_888["fg"] = "#0f1011"
        GLabel_888["justify"] = "center"
        GLabel_888["text"] = "Update"
        GLabel_888.place(x=500,y=350,width=86,height=100)

        GLabel_450=tk.Label(root)
        GLabel_450["bg"] = "#080303"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_450["font"] = ft
        GLabel_450["fg"] = "#333333"
        GLabel_450["justify"] = "center"
        GLabel_450["text"] = "label"
        GLabel_450.place(x=30,y=310,width=145,height=119)

        GLabel_724=tk.Label(root)
        GLabel_724["bg"] = "#020306"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_724["font"] = ft
        GLabel_724["fg"] = "#333333"
        GLabel_724["justify"] = "center"
        GLabel_724["text"] = "label"
        GLabel_724.place(x=200,y=310,width=131,height=120)

        GLabel_193=tk.Label(root)
        GLabel_193["bg"] = "#0a0404"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_193["font"] = ft
        GLabel_193["fg"] = "#333333"
        GLabel_193["justify"] = "center"
        GLabel_193["text"] = "label"
        GLabel_193.place(x=350,y=310,width=137,height=118)

        GLabel_640=tk.Label(root)
        GLabel_640["bg"] = "#e19dc8"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_640["font"] = ft
        GLabel_640["fg"] = "#333333"
        GLabel_640["justify"] = "center"
        GLabel_640["text"] = "Privacy"
        GLabel_640.place(x=30,y=310,width=140,height=119)

        GLabel_198=tk.Label(root)
        GLabel_198["bg"] = "#b58ca6"
        ft = tkFont.Font(family='Times',size=15)
        GLabel_198["font"] = ft
        GLabel_198["fg"] = "#333333"
        GLabel_198["justify"] = "center"
        GLabel_198["text"] = "Backup"
        GLabel_198.place(x=200,y=310,width=125,height=120)

        GLabel_531=tk.Label(root)
        GLabel_531["bg"] = "#c693b3"
        GLabel_531["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=15)
        GLabel_531["font"] = ft
        GLabel_531["fg"] = "#333333"
        GLabel_531["justify"] = "center"
        GLabel_531["text"] = "Perfomance"
        GLabel_531["relief"] = "sunken"
        GLabel_531.place(x=350,y=310,width=131,height=119)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
