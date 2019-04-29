import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, font, colorchooser
import os


class Toolbar(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['relief'] = 'ridge'
        self.buttons = {}
        self.images = []

    def addButton(self, name, image, command):
        self.buttons[name] = tk.Button(self, image=image, command=command, relief='groove')
        self.buttons[name].pack(side=tk.LEFT, padx=2, pady=2)

    def addImage(self, image):
        self.images.append(image)

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



def create_frame(window):
    frame = tk.Frame(window, background='blue')
    label_in_frame = tk.Label(frame, text='This label will be in the frame, above the button',
                              background='tomato2')
    button_in_frame = tk.Button(frame, text='This button is in the Frame', command=frame_click)

    label_in_frame.pack()
    button_in_frame.pack()
    frame.pack()


def create_frame_layout(parent):
    top = tk.Toplevel(parent)
    top.title('Hello World')
    top.geometry('300x75')

    left_frame = tk.Frame(top, background='blue')
    right_frame = tk.Frame(top, background='LightGoldenrod1')

    b1 = tk.Button(left_frame, text='Button 1')
    b2 = tk.Button(left_frame, text='Button 2')
    b3 = tk.Button(left_frame, text='Button 3')
    for b in [b1, b2, b3]:
        b.pack(side=tk.LEFT)

    e1 = tk.Entry(right_frame, width=15)
    e2 = tk.Entry(right_frame, width=15)
    e3 = tk.Entry(right_frame, width=15)
    for e in [e1, e2, e3]:
        e.pack(side=tk.TOP)

    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


def create_grid_layout(parent):

    top = tk.Toplevel(parent)
    top.title('Edit Grid Window')
    top.geometry('360x150')

    e = []
    for row in range(3):
        e.append([])
        for col in range(3):
            e[row].append(tk.Entry(top))
            e[row][col].grid(row=row, column=col)

    second = tk.Toplevel(parent)
    second.title('Edit Grid Window')
    second.geometry('500x500')

    second.columnconfigure(1, minsize=100)
    second.rowconfigure(2, minsize=25)

    label_0 = tk.Label(second, background='red', text='Hello there, too')
    label_0.grid(row=0, column=0)

    label_1 = tk.Label(second, background='yellow', text='Hello there')
    label_1.grid(row=0, column=17)

    label_2 = tk.Label(second, background='lightcyan2', text='Hello there, also')
    label_2.grid(row=15, column=19)


def forgetting_stuff(parent):
    top = tk.Toplevel(parent)
    top.title('Forgetting Window')
    top.geometry('500x500')

    pack_frame = tk.Frame(top, background='DarkOrchid1', padx=10, pady=10)

    left_button = tk.Button(pack_frame, text='Click Me!', command=pack_frame.pack_forget)
    top_right = tk.Button(pack_frame, text='Click Me!', command=pack_frame.pack_forget)
    bottom_right = tk.Button(pack_frame, text='Click Me!', command=pack_frame.pack_forget)
    left_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    top_right.pack(side=tk.TOP, fill=tk.Y, expand=True)
    bottom_right.pack(side=tk.BOTTOM, fill=tk.Y, expand=True)

    grid_frame = tk.Frame(top, background='DarkSeaGreen1')
    button_grid = []
    for row in range(3):
        button_grid.append([])
        for col in range(3):
            button_grid[row].append(tk.Button(grid_frame, text='Click Me!'))
            button_grid[row][col]['command'] = button_grid[row][col].grid_forget
            button_grid[row][col].grid(row=row, column=col)

    button_bad = tk.Button(grid_frame, text='Click Me!')
    button_bad.pack(side=tk.LEFT)

    place_frame = tk.Frame(top, background='slategray1')

    button_x = tk.Button(place_frame, text='Button X!')
    button_x['command'] = button_x.place_forget
    button_x.place(in_=place_frame, x=5, y=121)

    button_y = tk.Button(place_frame, text='Deorbit!')
    button_y['command'] = button_y.place_forget
    button_y.place(in_=place_frame, x=50, y=250)

    pack_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    grid_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    place_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def grid_forgetting(parent):
    top = tk.Toplevel(parent)
    top.title('Forgetting Window')
    top.geometry('360x150')

    button1 = tk.Button(top, text='Wait Dont Delete Me!')
    button2 = tk.Button(top, text='Click Me!', command=button1.grid)

    button1.grid(row=1, column=1)
    button2.grid(row=1, column=2)

    button1.grid_forget()


def absolute_placing(parent):

    top = tk.Toplevel(parent)
    top.title('Absolute Placement')
    top.geometry('360x150')

    lab1 = tk.Label(top, text='Yes this is a label')
    but1 = tk.Button(top, text='Press the Button')

    lab2 = tk.Label(top, text='Text is often made to be read')
    but2 = tk.Button(top, text='Here\'s another Button')

    lab1.place(in_=top, x=30, y=42)
    but1.place(in_=top, x=30, y=62)
    # lab2.place(in_=top, x=45, y=71)
    lab2.place(in_=top, x=45, y=90)
    but2.place(in_=top, x=100, y=120)


def relative_placing(parent):

    top = tk.Toplevel(parent)
    top.title('Relative Placement')
    top.geometry('360x500')

    lab1 = tk.Label(top, text='Yes this is a label')
    but1 = tk.Button(top, text='Press the Button')

    lab2 = tk.Label(top, text='Text is often made to be read')
    but2 = tk.Button(top, text='Here\'s another Button')

    lab1.place(in_=top, relx=.2, rely=.1, relwidth=.25, relheight=.1)
    but1.place(in_=top, relx=.35, rely=.35, relwidth=.25, relheight=.1)
    lab2.place(in_=top, relx=.35, rely=.55, relwidth=.25, relheight=.1)
    but2.place(in_=top, relx=.15, rely=.75, relwidth=.75, relheight=.1)

def var_examples(parent):

    top = tk.Toplevel(parent)
    top.title('Variable Example Window')
    top.geometry('320x160')

    boolean_var = tk.BooleanVar(top)
    integer_var = tk.IntVar(top)
    double_var = tk.DoubleVar(top)
    string_var = tk.StringVar(top)

    boolean_var.get()
    integer_var.get()
    double_var.get()
    string_var.get()

    boolean_var.set(False)
    integer_var.set(1729)
    double_var.set(3.141592653589793238)
    string_var.set('Hello Everybody')
    # integer_var.set('blah blah')
    # print(integer_var.get())


def entry_example(parent):

    top = tk.Toplevel(parent)
    top.title('Variable Window')
    top.geometry('320x120')

    tv = tk.StringVar(top, value='hello')

    the_entry = tk.Entry(top, textvariable=tv, width=20)
    the_entry.pack(side=tk.TOP, anchor=tk.N, padx=5, pady=5)

    the_button = tk.Button(top, text='I am Button', width=20, command=lambda: messagebox.showinfo('Entry Example', tv.get()))
    the_button.pack(side=tk.BOTTOM, anchor=tk.S, padx=5, pady=5)


def font_examples(parent):
    top = tk.Toplevel(parent)
    top.title('Font Example Window')
    top.geometry('320x350')

    def create_font_tuple(label, font_var, style_var, size_var, text_var):
        label['font'] = (font_var.get(), size_var.get(), style_var.get())

    def change_color(the_label, fg_or_bg, var):
        try:
            the_label[fg_or_bg] = var.get()
        except tk.TclError:
            pass

    font_var = tk.StringVar(top, value='Helvetica')
    style_var = tk.StringVar(top, value='')
    size_var = tk.StringVar(top, value='16')
    text_var = tk.StringVar(top, value='Wherefore art thou Romeo?')
    text_color_var = tk.StringVar(top, value='black')
    color_var = tk.StringVar(top, value='white')

    left_frame = tk.Frame(top)

    the_font_box = ttk.Combobox(left_frame, values=list(font.families()), state='readonly', textvariable=font_var)
    the_font_box.pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)
    tk.Label(left_frame, text='What is the size?', width=20).pack(side=tk.TOP, anchor=tk.N, padx=5, pady=5)
    tk.Entry(left_frame, textvariable=size_var).pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)
    tk.Label(left_frame, text='What is the style?', width=20).pack(side=tk.TOP, anchor=tk.N, padx=5, pady=5)
    tk.Entry(left_frame, textvariable=style_var).pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)
    tk.Label(left_frame, text='What is the text?', width=20).pack(side=tk.TOP, anchor=tk.N, padx=5, pady=5)
    tk.Entry(left_frame, textvariable=text_var).pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)
    tk.Label(left_frame, text='What is the foreground color?', width=20).pack(side=tk.TOP, anchor=tk.N, padx=5, pady=5)
    tk.Entry(left_frame, textvariable=text_color_var).pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)
    tk.Label(left_frame, text='What is the background color?', width=20).pack(side=tk.TOP, anchor=tk.N, padx=5, pady=5)
    tk.Entry(left_frame, textvariable=color_var).pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)

    the_button = tk.Button(left_frame, text='Change Settings')
    the_button.pack(side=tk.TOP, anchor=tk.W, padx=5, pady=5)
    left_frame.pack(side=tk.LEFT)

    the_label = tk.Label(top, textvariable=text_var, width=20)
    the_label.pack(side=tk.RIGHT, anchor=tk.E, padx=5, pady=5)
    the_button['command'] = lambda: create_font_tuple(the_label, font_var, style_var, size_var, text_var)
    color_var.trace('w', lambda *args: change_color(the_label, 'background', color_var))
    text_color_var.trace('w', lambda *args: change_color(the_label, 'foreground', text_color_var))


def simple_var(parent):
    top = tk.Toplevel(parent)
    top.title('Simple Entry')
    top.geometry('200x100')

    def test_passcode(my_string):
        nonlocal top
        # print(name, var, mode, my_string, my_string.get())
        if my_string.get() == 'abcd1234':
            if messagebox.askyesno('Simple Entry Example', 'How did you guess? You\'re a genius.'):
                top.destroy()

    my_string = tk.StringVar(top, name='password variable')
    tk.Entry(top, textvariable=my_string, width=20).pack(side=tk.TOP)

    # my_string.trace('w', lambda name, var, mode: test_passcode(my_string, name, var, mode))

    my_string.trace('w', lambda *args: test_passcode(my_string))


def simple_bind(parent):

    top = tk.Toplevel(parent)
    top.title('Simple Bind')
    top.geometry('200x100')
    top.bind('<Return>',
             lambda event: messagebox.showinfo('Binding', 'You Hit Enter'))
    top.bind('<Double-Button-1>',
             lambda event: messagebox.showinfo('Binding, That Tickles', 'You Double Clicked'))
    top.bind('<bracketleft>',
             lambda event: messagebox.showinfo('Binding, That Tickles', 'You Did Something'))

    # top.bind('<MouseWheel>',lambda event: print(vars(event)))


def radio_star(parent):

    top = tk.Toplevel(parent)
    top.title('Select Your Favorite SciFi')
    top.geometry('400x100')

    upper_frame = tk.Frame(top)
    bottom_frame = tk.Frame(top)

    scifi_var = tk.IntVar(top, value=1)

    tk.Radiobutton(upper_frame, text='Star Wars', value=1, variable=scifi_var).pack(side=tk.LEFT)
    tk.Radiobutton(upper_frame, text='Star Trek', value=2, variable=scifi_var).pack(side=tk.LEFT)
    tk.Radiobutton(upper_frame, text='Babylon 5', value=3, variable=scifi_var).pack(side=tk.LEFT)
    tk.Radiobutton(upper_frame, text='Battlestar', value=4, variable=scifi_var).pack(side=tk.LEFT)
    tk.Radiobutton(upper_frame, text='Firefly', value=5, variable=scifi_var).pack(side=tk.LEFT)

    scifi_list = ['Star Wars', 'Star Trek', 'Babylon 5', 'Battlestar', 'Firefly']
    favorite_var = tk.StringVar()
    scifi_var.trace('w',
                    lambda *args: favorite_var.set('You Selected ' + scifi_list[scifi_var.get() - 1]))
    tk.Label(bottom_frame, textvariable=favorite_var).pack(side=tk.BOTTOM)
    upper_frame.pack(side=tk.TOP, fill=tk.X, expand=True)
    bottom_frame.pack(side=tk.TOP, fill=tk.X, expand=True)


def checkbutton_example(parent):

    def set_toppings(topping_vars, total_toppings):
        top_list = [v.get() for v in topping_vars if v.get()]
        total_toppings.set(', '.join(top_list))

    top = tk.Toplevel(parent)
    top.title('Select Your Pizza toppings')
    top.geometry('600x100')

    upper_frame = tk.Frame(top)
    bottom_frame = tk.Frame(top)

    toppings = ['Pepperoni', 'Mushrooms', 'Green Peppers', 'Olives', 'Pineapple', 'Ham',
                'Tomato', 'Extra Cheese', 'Onions', 'Spinach']
    topping_vars = [tk.StringVar(top) for _ in toppings]
    total_toppings = tk.StringVar(top)

    for i, t in enumerate(toppings):
        tk.Checkbutton(upper_frame, text=t, variable=topping_vars[i],
                       onvalue=t, offvalue='').grid(row=1 + i // 5, column=(i % 5))
        topping_vars[i].trace('w', lambda *args: set_toppings(topping_vars, total_toppings))

    tk.Label(bottom_frame, textvariable=total_toppings).pack(side=tk.BOTTOM)
    upper_frame.pack(side=tk.TOP, fill=tk.X, expand=True)
    bottom_frame.pack(side=tk.TOP, fill=tk.X, expand=True)


def checkbutton_boolean_example(parent):
    def set_toppings_boolean(names, topping_vars, total_toppings):
        top_list = [names[i] for i, v in enumerate(topping_vars) if v.get()]
        total_toppings.set(', '.join(top_list))

    top = tk.Toplevel(parent)
    top.title('Select Your Pizza toppings')
    top.geometry('600x100')

    upper_frame = tk.Frame(top)
    bottom_frame = tk.Frame(top)

    toppings = ['Pepperoni', 'Mushrooms', 'Green Peppers', 'Olives', 'Pineapple', 'Ham',
                'Tomato', 'Extra Cheese', 'Onions', 'Spinach']
    topping_vars = [tk.BooleanVar(top) for _ in toppings]
    total_toppings = tk.StringVar(top)

    for i, t in enumerate(toppings):
        tk.Checkbutton(upper_frame, text=t, variable=topping_vars[i],
                       onvalue=True, offvalue=False).grid(row=1 + i // 5, column=(i % 5))
        topping_vars[i].trace('w', lambda *args: set_toppings_boolean(toppings, topping_vars, total_toppings))

    tk.Label(bottom_frame, textvariable=total_toppings).pack(side=tk.BOTTOM)
    upper_frame.pack(side=tk.TOP, fill=tk.X, expand=True)
    bottom_frame.pack(side=tk.TOP, fill=tk.X, expand=True)


def canvas_example(parent):

    top = tk.Toplevel(parent)
    top.title('We are going to make art now')
    top.geometry('800x800')

    toolbar = Toolbar(top)
    for file in ['line.gif', 'rect.gif', 'circle.gif', 'arc.gif', 'poly.gif']:
        the_image = tk.PhotoImage(file=os.path.join('ToolbarImages', file))
        toolbar.addImage(the_image)
        toolbar.addButton(file.split('.')[0], the_image, 0)

    toolbar.pack(side=tk.TOP, fill=tk.X)

    the_canvas = tk.Canvas(top, background='white')
    the_canvas.pack(expand=True, fill=tk.BOTH)
    the_canvas.create_line(0, 0, 200, 200)


main_window = tk.Tk()
main_window.title('This is the Title String')
main_window.geometry('800x500')
create_labels(main_window)
create_buttons(main_window)
create_image(main_window)
create_frame(main_window)

# create_frame_layout(main_window)
# create_grid_layout(main_window)
# forgetting_stuff(main_window)
# grid_forgetting(main_window)
# absolute_placing(main_window)
# relative_placing(main_window)
# entry_example(main_window)
# var_examples(main_window)
# font_examples(main_window)
# the_color = colorchooser.askcolor()
# print(the_color)
# simple_var(main_window)
# simple_bind(main_window)
# radio_star(main_window)
# checkbutton_example(main_window)
# checkbutton_boolean_example(main_window)
canvas_example(main_window)
main_window.mainloop()
