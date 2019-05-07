import tkinter as tk
import tkinter.ttk as ttk
import random


class ListboxExample(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Listbox Example')

        try:
            with open('value_file.txt') as value_file:
                values = value_file.readlines()
        except OSError as err:
            print(err)

        menubar = tk.Menu()
        example_menu = tk.Menu(tearoff=0)
        self.config(menu=menubar)
        menubar.add_cascade(label='Example Menu', menu=example_menu)

        example_menu.add_command(label='Set Random Colors', command=self.set_random_colors)
        example_menu.add_command(label='Create List Variable Example', command=self.create_list_var_example)
        example_menu.add_command(label='Create Insert-Delete Example', command=self.create_insertion_example)
        example_menu.add_command(label='Quit', command=self.destroy)

        self.the_listbox = tk.Listbox(self, height=10)

        self.the_listbox.insert(tk.END, *values)

        self.the_listbox.pack(fill=tk.BOTH, expand=True)

    @staticmethod
    def get_random_color():
        R = format(random.randint(0, 255), '02x')
        G = format(random.randint(0, 255), '02x')
        B = format(random.randint(0, 255), '02x')
        return '#' + ''.join([R, G, B])

    def set_random_colors(self):
        self.the_listbox['background'] = self.get_random_color()
        self.the_listbox['foreground'] = self.get_random_color()
        self.the_listbox['selectbackground'] = self.get_random_color()
        self.the_listbox['selectforeground'] = self.get_random_color()
        self.the_listbox['highlightbackground'] = self.get_random_color()
        self.the_listbox['highlightcolor'] = self.get_random_color()

    def create_list_var_example(self):
        toplevel = tk.Toplevel(self)
        toplevel.geometry('500x500')
        toplevel.title('Insert Delete Example')

        list_var = tk.StringVar(self)

        tk.Entry(toplevel, textvariable=list_var).pack(side=tk.TOP, fill=tk.X, anchor=tk.N)
        my_listbox = tk.Listbox(toplevel, listvariable=list_var, selectmode=tk.EXTENDED, activestyle=tk.DOTBOX)

        x_scrollbar = tk.Scrollbar(toplevel, orient=tk.HORIZONTAL, command=my_listbox.xview)
        y_scrollbar = tk.Scrollbar(toplevel, orient=tk.VERTICAL, command=my_listbox.yview)
        my_listbox['xscrollcommand'] = x_scrollbar.set
        my_listbox['yscrollcommand'] = y_scrollbar.set

        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        my_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def id_example_delete_find(self, listbox, string_var):
        value = string_var.get()
        for i in range(listbox.size()):
            if listbox.get(i) == value:
                listbox.delete(i)
                break

        listbox.get(i)
        listbox.get(tk.ACTIVE)
        listbox.get(tk.END)
        listbox.get(0, tk.END)

    def create_insertion_example(self):
        toplevel = tk.Toplevel(self)
        toplevel.geometry('500x500')
        toplevel.title('Listvariable Example')

        insert_delete_string = tk.StringVar(toplevel)
        my_listbox = tk.Listbox(toplevel, selectmode=tk.EXTENDED, activestyle=tk.DOTBOX)

        bottom_bar = tk.Frame(toplevel)
        tk.Button(bottom_bar, text="Insert",
                  command=lambda: my_listbox.insert(tk.END, insert_delete_string.get())).pack(side=tk.LEFT)
        tk.Button(bottom_bar, text="Insert Over Selection",
                  command=lambda: my_listbox.insert(tk.ANCHOR, insert_delete_string.get())).pack(side=tk.LEFT)
        tk.Button(bottom_bar, text="Delete if in Listbox",
                  command=lambda: self.id_example_delete_find(my_listbox, insert_delete_string)).pack(side=tk.LEFT)
        tk.Button(bottom_bar, text="Delete Selection",
                  command=lambda: my_listbox.delete(tk.ACTIVE)).pack(side=tk.LEFT)
        tk.Button(bottom_bar, text="Clear All",
                  command=lambda: my_listbox.delete(0, tk.END)).pack(side=tk.LEFT)
        bottom_bar.pack(side=tk.BOTTOM, fill=tk.X)

        main_entry = tk.Entry(toplevel, textvariable=insert_delete_string)
        main_entry.pack(side=tk.TOP, fill=tk.X, anchor=tk.N)
        main_entry.bind('<Return>', lambda event: my_listbox.insert(tk.END, insert_delete_string.get()))

        my_listbox.bind('<<ListboxSelect>>', lambda event: print('you selected ' + my_listbox.get(tk.ACTIVE)))

        y_scrollbar = tk.Scrollbar(toplevel, orient=tk.VERTICAL, command=my_listbox.yview)
        my_listbox['yscrollcommand'] = y_scrollbar.set

        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class ComboboxExample(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('500x150')
        self.title('Combobox Example')

        left_frame = tk.Frame(self)
        middle_frame = tk.Frame(self)
        right_frame = tk.Frame(self)

        self.left_string_var = tk.StringVar(left_frame)
        self.middle_string_var = tk.StringVar(middle_frame)

        left_label = tk.Label(left_frame, text='Enter text here, \n Hit enter to insert.')
        left_combobox = ttk.Combobox(left_frame,
                                     textvariable=self.left_string_var,
                                     values=['North', 'South', 'East', 'West'])
        left_combobox.bind('<Return>',
                           lambda event: self.insert_into_combobox(left_combobox, self.left_string_var))
        left_label.pack(side=tk.TOP, fill=tk.X, expand=True, padx=5, pady=5)
        left_combobox.pack(side=tk.TOP, fill=tk.X, expand=True, padx=5, pady=5)

        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(middle_frame, text='You Shouldn\'t be able to enter anything here').pack(side=tk.TOP, fill=tk.X, expand=True, padx=5, pady=5)
        middle_combobox = ttk.Combobox(middle_frame, textvariable=self.middle_string_var, state='readonly',
                                       values=['Red', 'Green', 'Blue', 'Purple', 'Orange', 'Tomato2'])
        middle_combobox.current(0)

        middle_combobox.pack(side=tk.TOP, fill=tk.X, expand=True, padx=5, pady=5)

        middle_combobox.bind('<<ComboboxSelected>>', lambda event: self.change_selection())

        middle_frame.pack(side=tk.LEFT, fill=tk.Y)
        right_frame.pack(side=tk.LEFT, fill=tk.Y)

    def change_selection(self):
        print('The Selection has Changed', self.middle_string_var.get())

    @staticmethod
    def insert_into_combobox(combobox, stringvar):
        print('the values', combobox['values'])
        the_values = list(combobox['values'])
        the_values.append(stringvar.get())
        stringvar.set('')
        combobox['values'] = the_values


class MenuExample(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('500x150')
        self.title('Menu Example')

        menu_bar = tk.Menu()

        file_menu = tk.Menu(tearoff=0)
        file_menu.add_command(label="Option 1", command=lambda: self.menu_string.set('Option 1'))
        file_menu.add_command(label="Option 2", command=lambda: self.menu_string.set('Option 2'))
        file_menu.add_command(label="Option 3", command=lambda: self.menu_string.set('Option 3'))
        file_menu.add_command(label="Option 4", command=lambda: self.menu_string.set('Option 4'))
        file_menu.add_separator()

        sub_menu = tk.Menu(tearoff=0)
        sub_menu.add_command(label="Sub-Option 1", command=lambda: self.menu_string.set('Sub-Option 1'))
        sub_menu.add_command(label="Sub-Option 2", command=lambda: self.menu_string.set('Sub-Option 2'))
        sub_menu.add_command(label="Sub-Option 3", command=lambda: self.menu_string.set('Sub-Option 3'))

        file_menu.add_cascade(label="Option 5 Expands", menu=sub_menu)
        file_menu.add_command(label="Exit", command=self.destroy)

        radio_choice_menu = tk.Menu(tearoff=0)
        self.the_radio_value = tk.IntVar(self)
        for i in range(5):
            radio_choice_menu.add_radiobutton(label='Radio Option ' + str(1 + i), variable=self.the_radio_value,
                                              value=1 + i, command=self.the_radio_changed)

        check_choice_menu = tk.Menu(tearoff=0)
        self.boolean_vars = [tk.BooleanVar(self) for _ in range(5)]
        for i, b in enumerate(self.boolean_vars):
            check_choice_menu.add_checkbutton(label='Check Option ' + str(i + 1),
                                              variable=b, onvalue=True, offvalue=False,
                                              command=self.check_the_checks)

        menu_bar.add_cascade(label='File', menu=file_menu)
        menu_bar.add_cascade(label='Radio', menu=radio_choice_menu)
        menu_bar.add_cascade(label='Checks', menu=check_choice_menu)

        # the two are equivalent
        self['menu'] = menu_bar
        # self.config(menu=menu_bar)

        left_frame = tk.Frame()

        self.menu_string = tk.StringVar(self)
        self.radio_string = tk.StringVar(self)

        tk.Label(left_frame, textvariable=self.menu_string).pack(side=tk.TOP, fill=tk.X)
        tk.Label(left_frame, textvariable=self.radio_string).pack(side=tk.TOP, fill=tk.X)

        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.the_tree = ttk.Treeview(self, columns=['Value'])
        self.the_tree.heading('#0', text='Variable')
        self.the_tree.heading('Value', text='Value')

        self.tree_ids = []
        for i, b in enumerate(self.boolean_vars):
            self.tree_ids.append(self.the_tree.insert('', tk.END, text='Check ' + str(i + 1), values=(b.get(), )))
        self.the_tree.pack(side=tk.RIGHT, fill=tk.BOTH)

        # self.bind('<Button-3>', lambda *args: print('you right clicked'))
        self.bind('<Button-3>', self.popup_menu)

    @staticmethod
    def popup_menu(event):
        the_popup_menu = tk.Menu(tearoff=0)
        the_popup_menu.add_command(label='C1')
        the_popup_menu.add_command(label='C2')
        the_popup_menu.add_command(label='C3')
        the_popup_menu.add_command(label='C4')
        print(vars(event))
        the_popup_menu.tk_popup(event.x_root, event.y_root)

    def the_radio_changed(self):
        self.radio_string.set('Radio Menu Changed to ' + str(self.the_radio_value.get()))

    def check_the_checks(self):
        for i, b in enumerate(self.boolean_vars):
            self.the_tree.item(self.tree_ids[i], values=['True' if b.get() else 'False'])


class TreeviewExample(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Treeview Example')


class ProgressbarExample(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Progress Bar Example')


if __name__ == '__main__':
    # s = ttk.Treeview(None)['style']
    # ComboboxExample().mainloop()
    # ListboxExample().mainloop()
    MenuExample().mainloop()

    print(ttk.Style().element_names())
    print(ttk.Style().theme_names())
