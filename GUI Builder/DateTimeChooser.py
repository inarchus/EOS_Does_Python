from ctypes import *
import tkinter as tk
# import tkinter.ttk as ttk

kernel32 = windll.kernel32
user32 = windll.user32
gdi32 = windll.gdi32


class DateTimeChooser(tk.Widget):
    WS_VISIBLE = 0x10000000
    WS_BORDER = 0x00800000
    WS_CHILD = 0x40000000

    def __init__(self, master, **kwargs):
        super().__init__(master, widgetName='Button')
        # self.CreateWindow = user32.CreateWindowA

        self.CreateWindowEx = user32.CreateWindowExA
        self.CreateWindowEx.argtypes = [c_int, c_char_p, c_char_p, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int]

        self.master = master
        self.hButton = 0
        self.hButton = self.CreateWindowEx(0, b'BUTTON', bytes(self.button_title), DateTimeChooser.WS_VISIBLE | DateTimeChooser.WS_CHILD,
                                                                                0, 0, 200, 200, self.master.w_info_id(), 0, 0, 0, 0)


    # def ui_handle_config(self):

    #def ui_handle_resize(self, width, height):
        # w, h = self.font.measure(self.text)
        # self.offset = (width - w) / 2, (height - h) / 2
        #pass

    #def ui_handle_repair(self, draw, x0, y0, x1, y1):
        # draw.text(self.offset, self.text, self.font)
        #pass