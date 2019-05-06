import tkinter as tk
import tkinter.ttk as ttk


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

        example_menu.add_command(label='Create List Variable Example', command=self.create_list_var_example)
        example_menu.add_command(label='Quit', command=self.destroy)

        self.the_listbox = tk.Listbox(self, height=10)

        self.the_listbox.insert(tk.END, *values)

        self.the_listbox.pack(fill=tk.BOTH, expand=True)

    def create_list_var_example(self):
        toplevel = tk.Toplevel(self)
        toplevel.geometry('500x500')
        toplevel.title('Listvariable Example')

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


if __name__ == '__main__':
    ListboxExample().mainloop()
