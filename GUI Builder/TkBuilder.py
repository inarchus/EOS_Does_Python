import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser
# from tkinter import simpledialog

class PlaceChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


class GridChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


class PackChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack_example()

    def pack_example(self):
        self.anchor_var = tk.IntVar(self, value=0)
        self.side_var = tk.IntVar(self, value=0)
        self.expand_var = tk.IntVar(self, value=0)
        self.fill_var = tk.IntVar(self, value=0)

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


class TkBuilder(tk.Tk):

    component_types = ['Label', 'Canvas', 'Button', 'Radiobutton', 'Checkbutton', 'Combobox', 'ttk.Notebook', 'ttk.Treeview', 'Frame', 'Listbox', 'ttk.Menubutton', 'ttk.Progressbar']

    def __init__(self):
        super().__init__()
        self.geometry('1200x800')
        self.title('TkBuilder')

        def create_layout_manager(self):
            component_frame = tk.Frame(self)
            block_frame = tk.Frame(self, width=800)
            top_block_frame = tk.Frame(block_frame)

            self.widget_tree = ttk.Treeview(component_frame, selectmode='extended', columns=('Type', 'Parameters'))
            self.variable_tree = ttk.Treeview(component_frame, selectmode='extended', columns=('Type', 'Value'))

            self.widget_tree.heading('#0', text='Widget')
            self.widget_tree.heading('Type', text='Type')
            self.widget_tree.heading('Parameters', text='Parameters')

            self.variable_tree.heading('#0', text='Variable')
            self.variable_tree.heading('Type', text='Type')
            self.variable_tree.heading('Value', text='Value')

            self.widget_tree.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
            self.variable_tree.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT)
            component_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.widget_choice = tk.StringVar(self, value='')
            self.select_layout_type = tk.IntVar(self, value=0)

            layout_choice_frame = tk.Frame(top_block_frame)
            tk.Radiobutton(layout_choice_frame, text='Pack Layout', value=0, variable=self.select_layout_type).pack(side=tk.TOP, anchor=tk.W)
            tk.Radiobutton(layout_choice_frame, text='Grid Layout', value=1, variable=self.select_layout_type).pack(side=tk.TOP, anchor=tk.W)
            tk.Radiobutton(layout_choice_frame, text='Place Layout', value=2, variable=self.select_layout_type).pack(side=tk.TOP, anchor=tk.W)
            layout_choice_frame.pack(side=tk.BOTTOM)

            self.select_layout_type.trace('w', self.change_layout_frame)

            choice_box = ttk.Combobox(top_block_frame, values=TkBuilder.component_types, textvariable=self.widget_choice)
            choice_box.pack(side=tk.TOP, fill=tk.X, expand=True)
            top_block_frame.pack(side=tk.TOP, fill=tk.X, expand=True)
            block_frame.pack(side=tk.RIGHT, fill=tk.Y)

        def build_main_menu(self):
            menubar = tk.Menu(self)
            self.config(menu=menubar)
            file_menu = tk.Menu(self, tearoff=0)

            menubar.add_cascade(label='File', menu=file_menu)
            file_menu.add_command(label='Create New Layout', command=self.create_new_layout)
            file_menu.add_command(label='Exit', command=self.destroy)
            component_menu = tk.Menu(self, tearoff=0)
            menubar.add_cascade(label='Widgets', menu=component_menu)
            component_menu.add_command(label='Add Widget', command=0)

        create_layout_manager(self)
        build_main_menu(self)

    def change_layout_frame(self, *args):
        print('changing layout frame', self.select_layout_type, args)

        if self.select_layout_type.get() == 0:
            print('pack layout')
        elif self.select_layout_type.get() == 1:
            print('grid layout')
        elif self.select_layout_type.get() == 2:
            print('place layout')


    def create_new_layout(self):
        print('creating new layout')


if __name__ == '__main__':
    main_window = TkBuilder()
    main_window.mainloop()
