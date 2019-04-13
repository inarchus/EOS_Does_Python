import tkinter as tk
from tkinter import messagebox


def click_me():
    messagebox.showinfo('Click Event', 'You have clicked, Good Work')


def create_labels(window):
    new_label = tk.Label(window, text='I am a Label, made of text. ')
    new_label.pack()
    next_label = tk.Label(window, text='I am also a label, what about me?')
    next_label.pack()


def create_buttons(window):
    the_button = tk.Button(window, text='This is our first Button', command=click_me)
    the_button.pack()


def create_image(window):
    the_image = tk.PhotoImage(file='fractal.gif')
    fractal_label = tk.Label(window, image=the_image)
    fractal_label.image = the_image
    fractal_label.pack()


def frame_click():
    if messagebox.askyesno('Click Event', 'You have clicked, Good Work') == tk.YES:
        messagebox.showinfo('Message Box', 'You have clicked yes!')


class AddWidgetDialog(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)


class PackExample(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x800')
        self.title('Packing Example')

        self.anchor_var = tk.IntVar(self)
        self.anchor_var.set(0)
        self.side_var = tk.IntVar(self)
        self.side_var.set(0)
        self.expand_var = tk.IntVar(self)
        self.expand_var.set(0)
        self.fill_var = tk.IntVar(self)
        self.fill_var.set(0)

        internal_frame = tk.Frame(self, background='white')
        button_frame = tk.Frame(self)

        anchor_frame = tk.Frame(button_frame)
        anchor_text = ['tk.NW', 'tk.N', 'tk.NE', 'tk.W', 'tk.CENTER', 'tk.E', 'tk.SE', 'tk.S', 'tk.SE']
        anchor_label = tk.Label(anchor_frame, text='Anchor')
        anchor_buttons = [tk.Radiobutton(anchor_frame, text=anchor_text[i], variable=self.anchor_var, value=i) for i in range(9)]

        side_frame = tk.Frame(button_frame)
        side_label = tk.Label(side_frame, text='Side')
        side_text = ['tk.LEFT', 'tk.RIGHT', 'tk.TOP', 'tk.BOTTOM']
        side_buttons = [tk.Radiobutton(side_frame, text=side_text[i], variable=self.side_var, value=i) for i in range(4)]

        expand_frame = tk.Frame(button_frame)
        expand_label = tk.Label(expand_frame, text='Expand')
        expand_text = ['False', 'True']
        expand_buttons = [tk.Radiobutton(expand_frame, text=expand_text[i], variable=self.expand_var, value=i) for i in range(2)]

        fill_frame = tk.Frame(button_frame)
        fill_label = tk.Label(fill_frame, text='Fill')
        fill_text = ['None', 'tk.X', 'tk.Y', 'tk.BOTH']
        fill_buttons = [tk.Radiobutton(fill_frame, text=fill_text[i], variable=self.fill_var, value=i) for i in range(4)]

        for button in [anchor_label, side_label, expand_label, fill_label] + anchor_buttons + side_buttons + expand_buttons + fill_buttons:
            button.pack(side=tk.LEFT)

        anchor_frame.pack(fill=tk.X)
        side_frame.pack(fill=tk.X)
        expand_frame.pack(fill=tk.X)
        fill_frame.pack(fill=tk.X)

        internal_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(self, tearoff=0)
        component_menu = tk.Menu(self, tearoff=0)

        menubar.add_cascade(label='File', menu=file_menu)
        menubar.add_cascade(label='Widgets', menu=component_menu)

        file_menu.add_command(label='Exit', command=self.destroy)
        component_menu.add_command(label='Add Widget', command=self.add_widget)

    def add_widget(self):
        AddWidgetDialog(self)


def create_frame(window):
    frame = tk.Frame(window, background='blue')
    label_in_frame = tk.Label(frame, text='This label will be in the frame, above the button',
                              background='tomato2')
    button_in_frame = tk.Button(frame, text='This button is in the Frame', command=frame_click)
    button_in_frame = tk.Button(frame, text='Open Pack Example', command=PackExample)

    label_in_frame.pack()
    button_in_frame.pack()
    frame.pack()


main_window = tk.Tk()
main_window.title('This is the Title String')
main_window.geometry('800x500')
create_labels(main_window)
create_buttons(main_window)
create_image(main_window)
create_frame(main_window)
main_window.mainloop()
