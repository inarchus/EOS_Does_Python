import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class ExampleDisplay(tk.Tk):
    def __init__(self, name):
        super().__init__()
        self.geometry('500x500')
        self.title(name)
        self.example_functions = {}
    
    def register_example(self, example_name, example_func):
        
        self.example_functions[example_name] = example_func
        
        tk.Button(self, text=example_name, command=example_func).pack(side=tk.TOP)
