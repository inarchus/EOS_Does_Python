import tkinter as tk


class EditableTable(tk.Frame):
    def __init__(self, master, rows=0, cols=0):
        super().__init__(master)
        self.text_vars = [[tk.StringVar(master) for _ in range(cols)] for _ in range(rows)]
        self.labels = [[tk.Label(master, textvariable=self.text_vars[i][j], borderwidth=1, width=15, relief='solid', takefocus=True) for j in range(cols)] for i in range(rows)]
        self.edit_var = tk.StringVar(master)
        self.edit_box = tk.Entry(master, textvariable=self.edit_var, width=15)
        self.edit_box.bind('<Return>', self.exit_label)

        for i in range(rows):
            for j in range(cols):
                self.text_vars[i][j].set(str((i, j)))
                self.labels[i][j].grid(row=i, column=j, sticky='news')
                self.labels[i][j].bind('<Button-1>', lambda event, row=i,col=j: self.label_click(row, col))

        self.current = None

    def exit_label(self, event):
        if self.current:
            self.text_vars[self.current[0]][self.current[1]].set(self.edit_var.get())
            self.labels[self.current[0]][self.current[1]].grid(row=self.current[0], column=self.current[1], sticky='news')
            self.edit_box.grid_forget()

    def label_click(self, row, col):
        print(row, col)
        if self.current:
            self.text_vars[self.current[0]][self.current[1]].set(self.edit_var.get())
            self.labels[self.current[0]][self.current[1]].grid(row=self.current[0], column=self.current[1], sticky='news')

        self.labels[row][col].grid_forget()
        self.edit_box.grid(row=row, column=col, sticky='news')
        self.edit_var.set(self.text_vars[row][col].get())
        self.current = (row, col)


if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.geometry('500x500')
    main_window.title('test table')
    table = EditableTable(main_window, 10, 10)
    main_window.mainloop()
