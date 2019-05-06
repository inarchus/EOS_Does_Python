import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, colorchooser
# from tkinter import simpledialog
import json


class NumberEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        
        master = args[0] if args else None
        self.variable = None
        if 'textvariable' in kwargs:
            self.variable = kwargs['textvariable']
        elif 'variable' in kwargs:
            self.variable = kwargs.pop('variable', None)
        else:
            self.variable = tk.StringVar(master)

        super().__init__(*args, **kwargs)

        validate_command = (self.register(self.ensure_numerical), '%P')
        self['validate'] = 'all'
        self['validatecommand'] = validate_command

    def ensure_numerical(self, new_value):
        try:
            if new_value != '':
                self.variable.set(int(new_value))
        except ValueError:
            return False
        return True


class ComponentFrame(tk.Frame):
    def __init__(self, master, parameters={}):
        '''
            the format should be:
            self.parameters[name] = {'name': widget_name, 'type': widget_type, 'label_text': prompt, 'variable_type': variable_type,
                    'values': list_of_values, 'variable_value': starting_value}
        '''
        super().__init__(master)
        self.parameters = parameters
        self.variables = {}
        self.components = {}
        self.construct_components(self.parameters, self.components)

    def construct_components(self, parameters, components=None):
        if not components:
            components = self.components

        for i, parameter_title in enumerate(parameters):

            parameter = parameters[parameter_title]

            if 'variable_type' in parameter and parameter['name'] not in self.variables:
                if 'variable_value' in parameter:
                    self.variables[parameter['name']] = parameter['variable_type'](self, value=parameter['variable_value'])
                else:
                    self.variables[parameter['name']] = parameter['variable_type'](self)

            components[parameter['name'] + '_label'] = tk.Label(self, text=parameter['label_text'] if 'label_text' in parameter else parameter['name'])
            if 'variable_type' in parameter:

                self.variables[parameter['name']] = parameter['variable_type'](self)
                if parameter['variable_type'] == tk.StringVar:
                    components[parameter['name']] = parameter['type'](self, textvariable=self.variables[parameter['name']])
                elif parameter['variable_type'] == tk.IntVar:
                    components[parameter['name']] = parameter['type'](self, variable=self.variables[parameter['name']])
                else:
                    print(parameter['name'], 'is not attached to a variable')
                    components[parameter['name']] = parameter['type'](self)

            else:
                components[parameter['name']] = parameter['type'](self)

            for x in parameter:
                if x not in ['name', 'type', 'variable_type', 'label_text']:
                    try:
                        components[parameter['name']][x] = parameter[x]
                    except tk.TclError as err:
                        print(err)

            components[parameter['name'] + '_label'].grid(row=i, column=0)
            components[parameter['name']].grid(row=i, column=1)

    def get_variable_instant(self):
        return {v: self.variables[v].get() for v in self.variables if self.variables[v].get()}

    def load_components(self, load_file):
        self.file_name = load_file
        try:
            with open(load_file, 'r') as json_file:
                json_data = json.loads(''.join(json_file.readlines()))
                print(json_data)
        except OSError as e:
            print(e)

    def save_component(self):
        try:
            with open(self.file_name, 'w') as write_json:
                write_json.write(json.dumps(self.json_data))
        except OSError as e:
            print(e)


class PlaceChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.x_place_string = tk.StringVar(self)
        self.y_place_string = tk.StringVar(self)

        tk.Label(self, text='X Position').grid(row=0, column=1)
        tk.Label(self, text='Y Position').grid(row=0, column=3)
        NumberEntry(self, textvariable=self.x_place_string).grid(row=1, column=1)
        NumberEntry(self, textvariable=self.y_place_string).grid(row=1, column=3)

    def get_layout_arguments(self):
        return {'x': int(self.x_place_string.get()), 'y': int(self.y_place_string.get())}


class GridChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.row_string = tk.StringVar(self)
        self.col_string = tk.StringVar(self)
        tk.Label(self, text='Grid Row').grid(row=0, column=1)
        tk.Label(self, text='Grid Column').grid(row=0, column=3)
        NumberEntry(self, textvariable=self.row_string).grid(row=1, column=1)
        NumberEntry(self, textvariable=self.col_string).grid(row=1, column=3)

    def get_layout_arguments(self):
        return {'row': int(self.row_string.get()), 'column': int(self.col_string.get())}


class PackChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.anchor_var = tk.StringVar(self, value='tk.NW')
        self.side_var = tk.StringVar(self, value='tk.LEFT')
        self.expand_var = tk.IntVar(self, value=0)
        self.fill_var = tk.StringVar(self, value=0)

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

    def get_layout_arguments(self):
        arguments = {}
        anchor_dict = {'tk.NW': 'nw', 'tk.N': 'n', 'tk.NE': 'ne', 'tk.W': 'w', 'tk.CENTER': 'center', 'tk.E': 'e', 'tk.SE': 'se', 'tk.S': 's', 'tk.SW': 'sw'}
        if self.anchor_var.get() in anchor_dict:
            arguments['anchor'] = anchor_dict[self.anchor_var.get()]
        arguments['expand'] = True if self.expand_var.get() else False
        fill_dict = {'tk.X': tk.X, 'tk.Y': tk.Y, 'tk.BOTH': tk.BOTH}

        if self.fill_var.get() in fill_dict:
            arguments['fill'] = fill_dict[self.fill_var.get()]
        side_dict = {'tk.LEFT': tk.LEFT, 'tk.RIGHT': tk.RIGHT, 'tk.TOP': tk.TOP, 'tk.BOTTOM': tk.BOTTOM}
        if self.side_var.get() in side_dict:
            arguments['side'] = side_dict[self.side_var.get()]

        return arguments


class TkBuilder(tk.Tk):
    """
            the format should be:
            self.parameters[name] = {'name': widget_name, 'type': widget_type, 'label_text': prompt, 'variable_type': variable_type,
                    'values': list_of_values, 'variable_value': starting_value}

    """
    x = {'test_button': {'name': 'Test Button', 'type': tk.Button, 'label_text': 'click me', 'state': tk.DISABLED, 'text': 'Button Title'},
     'test_edit': {'name': 'Test Edit', 'type': tk.Entry, 'label_text': 'edit me', 'variable_type': tk.StringVar}}

    component_types = {'Label': tk.Label, 'Canvas': tk.Canvas, 'Button': tk.Button, 'Entry': tk.Entry,
                       'Radiobutton': tk.Radiobutton, 'Checkbutton': tk.Checkbutton, 'Frame': tk.Frame,
                       'Listbox': tk.Listbox, 'ttk.Combobox': ttk.Combobox, 'ttk.Notebook': ttk.Notebook,
                       'ttk.Treeview': ttk.Treeview, 'ttk.Menubutton': ttk.Menubutton, 'ttk.Progressbar': ttk.Progressbar}
    
    TkDefault = {
        'text': {'name': 'text', 'type': tk.Entry, 'variable_type': tk.StringVar},
        'justify': {'name': 'justify', 'type': ttk.Combobox, 'values': ['None', tk.LEFT, tk.RIGHT, tk.CENTER],
                    'state': 'readonly', 'variable_type': tk.StringVar},
        'state': {'name': 'state', 'type': ttk.Combobox, 'values': ['None', tk.NORMAL, tk.ACTIVE, tk.DISABLED],
                  'state': 'readonly', 'variable_type': tk.StringVar},
        'relief': {'name': 'relief', 'type': ttk.Combobox,
                   'values': ['None', tk.FLAT, tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE], 'state': 'readonly',
                   'variable_type': tk.StringVar},
        'background': {'name': 'background', 'type': tk.Entry, 'variable_type': tk.StringVar},
        'padx': {'name': 'padx', 'type': NumberEntry, 'variable_type': tk.IntVar},
        'pady': {'name': 'pady', 'type': NumberEntry, 'variable_type': tk.IntVar},
        'ipadx': {'name': 'ipadx', 'type': NumberEntry, 'variable_type': tk.IntVar},
        'ipady': {'name': 'ipady', 'type': NumberEntry, 'variable_type': tk.IntVar},
        'width': {'name': 'width', 'type': NumberEntry, 'variable_type': tk.IntVar}
    }
    
    ComponentMap = {
        'Label': {
            },
        'Button': {
            },
        'Radiobutton': {
                'variable': {'name': 'variable', 'type': tk.Entry},
                'value': {'name': 'value', 'type': tk.Entry}
            },
        'Checkbutton': {
                'textvariable': {'name': 'textvariable', 'type': tk.Entry}
            },
        'Canvas': {
            },
        'Entry': {
            },
        'Frame': {
            },
        'Listbox': {
            },
        'ttk.Combobox': {
            },
        'ttk.Notebook': {
            },
        'ttk.Treeview': {
            },
        'ttk.Menubutton': {
            },
        'ttk.Progressbar': {
                'length': {'name': 'length', 'type': NumberEntry, 'variable_type': tk.IntVar},
                'mode': {'name': 'mode', 'type': ttk.Combobox, 'values': ['None','determinate', 'indeterminate'], 'state': 'readonly', 'variable_type': tk.StringVar},
                'value': {'name': 'value', 'type': NumberEntry, 'variable_type': tk.IntVar},
            },
    }

    def __init__(self):
        super().__init__()
        self.geometry('1500x800')
        self.title('TkBuilder')

        self.widget_tree_map = {}
        self.variable_map = {}
        self.component_map = {}
        self.draw_window = None
        self.draw_window_id = None
        
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

            # VARIABLE CHOICE FRAME
            variable_choice_frame = tk.Frame(self.variable_frame)
            self.select_variable_type = tk.IntVar(self, value=0)
            self.select_variable_type.trace('w', lambda *args: self.change_variable_type)
            self.select_label = tk.StringVar(self.variable_frame)
            self.variable_value = tk.StringVar(self.variable_frame)
            self.boolean_value = tk.BooleanVar(self.variable_frame)

            left_var_frame = tk.Frame(variable_choice_frame)

            tk.Radiobutton(left_var_frame, text='Boolean Variable', value=0, variable=self.select_variable_type, command=self.change_variable_type).pack(side=tk.TOP, anchor=tk.W)
            tk.Radiobutton(left_var_frame, text='Integer Variable', value=1, variable=self.select_variable_type, command=self.change_variable_type).pack(side=tk.TOP, anchor=tk.W)
            tk.Radiobutton(left_var_frame, text='String Variable', value=2, variable=self.select_variable_type, command=self.change_variable_type).pack(side=tk.TOP, anchor=tk.W)
            tk.Radiobutton(left_var_frame, text='Float Variable', value=3, variable=self.select_variable_type, command=self.change_variable_type).pack(side=tk.TOP, anchor=tk.W)
            tk.Button(left_var_frame, text='Create Variable', command=self.create_variable).pack(side=tk.TOP, anchor=tk.W)
            left_var_frame.pack(side=tk.LEFT)

            right_var_frame = tk.Frame(variable_choice_frame)
            self.variable_radio_frame = tk.Frame(right_var_frame)
            self.variable_name = tk.StringVar(self)
            tk.Label(right_var_frame, text='Variable Name').pack(side=tk.TOP)
            tk.Entry(right_var_frame, textvariable=self.variable_name).pack(side=tk.TOP)

            tk.Radiobutton(self.variable_radio_frame, text="False", value=False, variable=self.boolean_value).pack(side=tk.LEFT)
            tk.Radiobutton(self.variable_radio_frame, text="True", value=True, variable=self.boolean_value).pack(side=tk.LEFT)

            tk.Label(right_var_frame, text='Variable Value').pack(side=tk.TOP)
            self.variable_entry = tk.Entry(right_var_frame, textvariable=self.variable_value, width=20)

            right_var_frame.pack(side=tk.RIGHT)

            variable_choice_frame.pack(side=tk.BOTTOM)

            self.select_layout_type.trace('w', self.change_layout_frame)
            self.widget_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)
            self.variable_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)

            choice_box = ttk.Combobox(layout_choice_frame, values=list(TkBuilder.component_types.keys()), state='readonly', textvariable=self.widget_choice)
            choice_box.pack(side=tk.TOP)

            self.new_widget_name = tk.StringVar(self, value='')
            name_of_widget = tk.Entry(layout_choice_frame, width=12, textvariable=self.new_widget_name)
            name_of_widget.pack(side=tk.TOP)
            self.create_button = tk.Button(layout_choice_frame, text='Create Widget', command=self.create_new_widget, state=tk.DISABLED)
            self.create_button.pack(side=tk.TOP)
            top_block_frame.pack(side=tk.TOP, fill=tk.X, expand=True)
            self.block_frame.pack(side=tk.RIGHT, fill=tk.Y)

            choice_box.bind("<<ComboboxSelected>>", self.draw_component_frame)

        create_layout_manager(self)
        build_main_menu(self)
        self.change_layout_frame()
        self.component_frames = self.create_component_frames()
        if self.component_frames:
            self.component_frames[list(self.component_frames.keys())[0]].pack(side=tk.LEFT, fill=tk.Y, expand=True)

    def change_variable_type(self):
        if self.select_variable_type.get():
            self.variable_radio_frame.pack_forget()
            self.variable_entry.pack()
        else:
            self.variable_entry.pack_forget()
            self.variable_radio_frame.pack()

    def create_variable(self):
        name = self.variable_name.get()
        
        types = [tk.BooleanVar, tk.IntVar, tk.DoubleVar, tk.StringVar]
        if name not in self.variable_map:
            if not self.select_variable_type.get():
                value = self.boolean_value.get()
            else:
                value = self.variable_value.get()
            
            self.variable_map[name] = types[self.select_variable_type.get()](self.draw_window, value=value)
            self.variable_tree.insert('', tk.END, text=name, values=[self.variable_map[name]])

    def create_component_frames(self):

        the_frames = {}
        for component in TkBuilder.ComponentMap:
            component_parts = dict(TkBuilder.TkDefault)
            for x in TkBuilder.TkDefault:
                if 'name' not in TkBuilder.TkDefault[x]:
                    component_parts[x]['name'] = x
                if 'label_text' not in TkBuilder.TkDefault:
                    name = TkBuilder.TkDefault[x]['name']
                    component_parts[x]['label_text'] = name[0:1].upper() + name[1:].lower()

            for x in TkBuilder.ComponentMap[component]:
                component_parts[x] = TkBuilder.ComponentMap[component][x]
                if 'name' not in TkBuilder.ComponentMap[component][x]:
                    component_parts[x]['name'] = x
                if 'label_text' not in TkBuilder.ComponentMap[component]:
                    name = TkBuilder.ComponentMap[component][x]['name']
                    component_parts[x]['label_text'] = name[0:1].upper() + name[1:].lower()

            the_frames[component] = ComponentFrame(self, component_parts)

        return the_frames

    def draw_component_frame(self, *args):
        widget_type = self.widget_choice.get()
        if widget_type in self.component_frames:
            for frame_name in self.component_frames:
                self.component_frames[frame_name].pack_forget()
            self.component_frames[widget_type].pack(side=tk.LEFT, fill=tk.Y, expand=True)

    def create_new_widget(self):
        print('creating new widget', self.widget_choice.get(), 'named', self.new_widget_name.get())

        widget_type = self.widget_choice.get()
        widget_name = self.new_widget_name.get()

        if widget_type in TkBuilder.component_types:
            if widget_name not in self.component_map:
                arguments = self.get_widget_arguments(widget_name, widget_type)
                selection = self.widget_tree.selection()
                if selection:
                    self.component_map[widget_name] = TkBuilder.component_types[widget_type](self.widget_tree_map[selection[0]], **arguments)
                else:
                    self.component_map[widget_name] = TkBuilder.component_types[widget_type](self.draw_window, **arguments)
                
                if self.select_layout_type.get() == 0:
                    print(self.pack_layout_frame.get_layout_arguments())
                    self.component_map[widget_name].pack(**self.pack_layout_frame.get_layout_arguments())
                elif self.select_layout_type.get() == 1:
                    self.component_map[widget_name].grid(**self.grid_layout_frame.get_layout_arguments())
                elif self.select_layout_type.get() == 2:
                    self.component_map[widget_name].place(**self.place_layout_frame.get_layout_arguments())
                if selection:
                    new_id = self.widget_tree.insert(selection[0], tk.END, text=widget_name, values=[widget_type, ''])
                else:
                    new_id = self.widget_tree.insert(self.draw_window_id, tk.END, text=widget_name, values=[widget_type, ''])
                    
                self.widget_tree_map[new_id] = self.component_map[widget_name]
            else:
                messagebox.showinfo('TkBuilder', 'component with that name already exists')

    def get_widget_arguments(self, widget_name, widget_type):
        if widget_type in TkBuilder.ComponentMap:
            # print(self.component_frames[widget_type].get_variable_instant())
            return self.component_frames[widget_type].get_variable_instant()

        return {'text': widget_name}

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
            
            widget_id = self.widget_tree.insert('', tk.END, text='Main Window', values=['tk.Toplevel', ''], open=True)
            self.draw_window_id = widget_id
            self.widget_tree_map[widget_id] = self.draw_window


if __name__ == '__main__':
    main_window = TkBuilder()
    main_window.mainloop()
