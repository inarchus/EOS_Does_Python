import tkinter as tk
from PIL import ImageTk
from PIL import Image


class ResizeImageExample(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('This is the Title String')
        self.geometry('800x500')

        self.the_image = Image.open('thing.jpg')
        print(self.the_image)
        self.the_tk_image = ImageTk.PhotoImage(self.the_image)
        self.fractal_label = tk.Label(self, image=self.the_tk_image)

        self.fractal_label.image = self.the_image
        self.fractal_label.pack(expand=True)
        self.bind('<Configure>', lambda event: self.reconfigure())

    def reconfigure(self):
        size_coordinate = self.winfo_geometry().split('+')[0]
        x, y = list(map(int, size_coordinate.split('x')))
        print(x, y)
        self.the_image = self.the_image.resize((x, y), Image.ANTIALIAS)
        print(self.the_image)
        # self.fractal_label['image'] = self.the_tk_image
        self.the_tk_image = ImageTk.PhotoImage(self.the_image)
        self.fractal_label.image = self.the_tk_image
        self.fractal_label['image'] = self.the_tk_image


example = ResizeImageExample()
example.mainloop()
