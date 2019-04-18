import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser
# from tkinter import simpledialog


class PlaceChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.x_place_string = tk.StringVar(self)
        self.y_place_string = tk.StringVar(self)

        tk.Label(self, text='X Position').grid(row=0, column=1)
        tk.Label(self, text='Y Position').grid(row=0, column=3)
        tk.Entry(self, textvariable=self.x_place_string).grid(row=1, column=1)
        tk.Entry(self, textvariable=self.y_place_string).grid(row=1, column=3)


class GridChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.row_string = tk.StringVar(self)
        self.col_string = tk.StringVar(self)
        tk.Label(self, text='Grid Row').grid(row=0, column=1)
        tk.Label(self, text='Grid Column').grid(row=0, column=3)
        tk.Entry(self, textvariable=self.row_string).grid(row=1, column=1)
        tk.Entry(self, textvariable=self.col_string).grid(row=1, column=3)


class PackChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.anchor_var = tk.StringVar(self, value='tk.NW')
        self.side_var = tk.StringVar(self, value='tk.LEFT')
        self.expand_var = tk.IntVar(self, value=0)
        self.fill_var = tk.IntVar(self, value=0)

        internal_frame = tk.Frame(self, background='white')
        button_frame = tk.Frame(self)

        anchor_frame = tk.Frame(button_frame)
        anchor_text = ['None', 'tk.NW', 'tk.N', 'tk.NE', 'tk.W', 'tk.CENTER', 'tk.E', 'tk.SE', 'tk.S', 'tk.SE']
        tk.Label(anchor_frame, text='Anchor').pack(side=tk.TOP)
        ttk.Combobox(anchor_frame, values=anchor_text, textvariable=self.anchor_var).pack(side=tk.BOTTOM)

        side_frame = tk.Frame(button_frame)
        tk.Label(side_frame, text='Side').pack(side=tk.TOP)
        side_text = ['None', 'tk.LEFT', 'tk.RIGHT', 'tk.TOP', 'tk.BOTTOM']
        ttk.Combobox(side_frame, values=side_text, textvariable=self.side_var).pack(side=tk.BOTTOM)

        expand_frame = tk.Frame(button_frame)
        expand_label = tk.Label(expand_frame, text='Expand')
        expand_text = ['False', 'True']
        expand_buttons = [tk.Radiobutton(expand_frame, text=expand_text[i], variable=self.expand_var, value=i, width=7) for i in range(2)]

        fill_frame = tk.Frame(button_frame)
        tk.Label(fill_frame, text='Fill').pack(side=tk.TOP)
        fill_text = ['None', 'tk.X', 'tk.Y', 'tk.BOTH']
        ttk.Combobox(fill_frame, values=fill_text, textvariable=self.fill_var).pack(side=tk.BOTTOM)

        for button in [expand_label, *expand_buttons]:
            button.pack(side=tk.LEFT)

        anchor_frame.pack(fill=tk.X)
        side_frame.pack(fill=tk.X)
        fill_frame.pack(fill=tk.X)
        expand_frame.pack(fill=tk.X)

        internal_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)


class TkBuilder(tk.Tk):

    component_types = {'Label': tk.Label, 'Canvas': tk.Canvas, 'Button': tk.Button, 'Radiobutton': tk.Radiobutton, 'Checkbutton': tk.Checkbutton, 'Frame': tk.Frame,
                       'Listbox': tk.Listbox, 'ttk.Combobox': ttk.Combobox, 'ttk.Notebook': ttk.Notebook, 'ttk.Treeview': ttk.Treeview,
                       'ttk.Menubutton': ttk.Menubutton, 'ttk.Progressbar': ttk.Progressbar}

    def __init__(self):
        super().__init__()
        self.geometry('1200x800')
        self.title('TkBuilder')

        self.variable_map = {}
        self.component_map = {}
        self.draw_window = None


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

        def create_layout_manager(self):
            self.component_frame = tk.Frame(self)
            self.block_frame = tk.Frame(self, width=800)
            top_block_frame = tk.Frame(self.block_frame)

            self.widget_frame = tk.Frame(self.component_frame)
            self.variable_frame = tk.Frame(self.component_frame)

            self.widget_tree = ttk.Treeview(self.widget_frame, selectmode='extended', columns=('Type', 'Parameters'))
            self.variable_tree = ttk.Treeview(self.variable_frame, selectmode='extended', columns=('Type', 'Value'))

            self.pack_layout_frame = PackChoiceFrame(self.widget_frame)
            self.grid_layout_frame = GridChoiceFrame(self.widget_frame)
            self.place_layout_frame = PlaceChoiceFrame(self.widget_frame)

            self.widget_tree.heading('#0', text='Widget')
            self.widget_tree.heading('Type', text='Type')
            self.widget_tree.heading('Parameters', text='Parameters')

            self.variable_tree.heading('#0', text='Variable')
            self.variable_tree.heading('Type', text='Type')
            self.variable_tree.heading('Value', text='Value')

            self.widget_tree.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            self.variable_tree.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            self.component_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.widget_choice = tk.StringVar(self, value='')
            self.select_layout_type = tk.IntVar(self, value=0)

            layout_choice_frame = tk.Frame(self.widget_frame)
            tk.Radiobutton(layout_choice_frame, text='Pack Layout', value=0, variable=self.select_layout_type).pack(side=tk.TOP, anchor=tk.W)
            tk.Radiobutton(layout_choice_frame, text='Grid Layout', value=1, variable=self.select_layout_type).pack(side=tk.TOP, anchor=tk.W)
            tk.Radiobutton(layout_choice_frame, text='Place Layout', value=2, variable=self.select_layout_type).pack(side=tk.TOP, anchor=tk.W)
            layout_choice_frame.pack(side=tk.LEFT)

            self.select_layout_type.trace('w', self.change_layout_frame)
            self.widget_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)
            self.variable_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)

            choice_box = ttk.Combobox(layout_choice_frame, values=list(TkBuilder.component_types.keys()), textvariable=self.widget_choice)
            choice_box.pack(side=tk.TOP)

            self.new_widget_name = tk.StringVar(self, value='')
            name_of_widget = tk.Entry(layout_choice_frame, width=12, textvariable=self.new_widget_name)
            name_of_widget.pack(side=tk.TOP)
            self.create_button = tk.Button(layout_choice_frame, text='Create Widget', command=self.create_new_widget, state=tk.DISABLED)
            self.create_button.pack(side=tk.TOP)
            top_block_frame.pack(side=tk.TOP, fill=tk.X, expand=True)
            self.block_frame.pack(side=tk.RIGHT, fill=tk.Y)

        create_layout_manager(self)
        build_main_menu(self)
        self.change_layout_frame()

    def create_new_widget(self):
        print('creating new widget', self.widget_choice.get(), 'named', self.new_widget_name.get())

        widget_type = self.widget_choice.get()
        widget_name = self.new_widget_name.get()

        if widget_type in TkBuilder.component_types:
            if widget_name not in self.component_map:
                arguments = self.get_widget_arguments()
                self.component_map[widget_name] = TkBuilder.component_types[widget_type](self.draw_window, **arguments)
                if self.select_layout_type.get() == 0:
                    self.component_map[widget_name].pack(**self.pack_layout_frame.get_layout_arguments())
                elif self.select_layout_type.get() == 1:
                    self.component_map[widget_name].grid(**self.grid_layout_frame.get_layout_arguments())
                elif self.select_layout_type.get() == 2:
                    self.component_map[widget_name].place(**self.place_layout_frame.get_layout_arguments())

            else:
                print('component with that name already exists')

    def get_widget_arguments(self):
        return {}

    def change_layout_frame(self, *args):

        if self.select_layout_type.get() == 0:
            self.place_layout_frame.pack_forget()
            self.grid_layout_frame.pack_forget()
            self.pack_layout_frame.pack(side=tk.BOTTOM, fill=tk.X)
        elif self.select_layout_type.get() == 1:
            self.pack_layout_frame.pack_forget()
            self.place_layout_frame.pack_forget()
            self.grid_layout_frame.pack(side=tk.BOTTOM, fill=tk.X)
        elif self.select_layout_type.get() == 2:
            self.pack_layout_frame.pack_forget()
            self.grid_layout_frame.pack_forget()
            self.place_layout_frame.pack(side=tk.BOTTOM, fill=tk.X)

    def create_new_layout(self):
        if not self.draw_window:
            self.create_button['state'] = tk.ACTIVE
            self.draw_window = tk.Toplevel(self)
            self.draw_window.geometry('800x800')
            self.draw_window.title('Layout Drawing Window')

            self.widget_tree.insert('', tk.END, text='Main Window', values=['tk.Toplevel', ''], open=True)


if __name__ == '__main__':
    main_window = TkBuilder()
    main_window.mainloop()
