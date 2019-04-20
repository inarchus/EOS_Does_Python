import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser
# from tkinter import simpledialog
import json


class NumberEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        kwargs.update({'validate': 'key', 'validatecommand': self.ensure_numerical})
        super().__init__(*args, **kwargs)

    def ensure_numerical(self):
        '''        try:
            print(self.get())
            int(self.get())
            return True
        except ValueError:
            return False
        '''
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
        print(parameters)
        for i, parameter_title in enumerate(parameters):

            parameter = parameters[parameter_title]
            if 'variable_type' in parameter and parameter['name'] not in self.variables:
                if 'variable_value' in parameter:
                    self.variables[parameter['name']] = parameter['variable_type'](self, value=parameter['variable_value'])
                else:
                    self.variables[parameter['name']] = parameter['variable_type'](self)

            components[parameter['name'] + '_label'] = tk.Label(self, text=parameter['label_text'] if 'label_text' in parameter else parameter['name'])
            if 'variable_type' in parameter:
                if isinstance(parameter['variable_type'], tk.StringVar):
                    components[parameter['name']] = parameter['type'](self, textvariable=self.variables[parameter['name']])
                else:
                    components[parameter['name']] = parameter['type'](self, variable=self.variables[parameter['name']])
            else:
                components[parameter['name']] = parameter['type'](self)

            for x in ['background', 'command', 'font', 'ipadx', 'ipady', 'padx', 'pady', 'relief', 'state', 'text', 'values']:
                if x in parameter:
                    components[parameter['name']][x] = parameter[x]

            components[parameter['name'] + '_label'].grid(row=i, column=0)
            components[parameter['name']].grid(row=i, column=1)

    def get_variable_instant(self):
        return {v: v.get() for v in self.variables}

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
        tk.Entry(self, textvariable=self.x_place_string).grid(row=1, column=1)
        tk.Entry(self, textvariable=self.y_place_string).grid(row=1, column=3)

    def get_layout_arguments(self):
        return {}


class GridChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.row_string = tk.StringVar(self)
        self.col_string = tk.StringVar(self)
        tk.Label(self, text='Grid Row').grid(row=0, column=1)
        tk.Label(self, text='Grid Column').grid(row=0, column=3)
        tk.Entry(self, textvariable=self.row_string).grid(row=1, column=1)
        tk.Entry(self, textvariable=self.col_string).grid(row=1, column=3)

    def get_layout_arguments(self):
        return {}


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
        print(self.fill_var.get())
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

    component_types = {'Label': tk.Label, 'Canvas': tk.Canvas, 'Button': tk.Button, 'Radiobutton': tk.Radiobutton, 'Checkbutton': tk.Checkbutton, 'Frame': tk.Frame,
                       'Listbox': tk.Listbox, 'ttk.Combobox': ttk.Combobox, 'ttk.Notebook': ttk.Notebook, 'ttk.Treeview': ttk.Treeview,
                       'ttk.Menubutton': ttk.Menubutton, 'ttk.Progressbar': ttk.Progressbar}
    ComponentMap = {
        'Label': {
                'text': {'name': 'text', 'type': tk.Entry},
                'justify': {'name': 'justify', 'type': ttk.Combobox, 'values': ['None', tk.LEFT, tk.RIGHT, tk.CENTER], 'state': 'readonly'},
                'state': {'name': 'state', 'type': ttk.Combobox, 'values': ['None', tk.NORMAL, tk.ACTIVE, tk.DISABLED], 'state': 'readonly'},
                'relief': {'name': 'relief', 'type': ttk.Combobox, 'values': ['None', tk.FLAT, tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE], 'state': 'readonly'},
                'background': {'name': 'background', 'type': tk.Entry},
                'padx': {'name': 'padx', 'type': NumberEntry},
                'pady': {'name': 'pady', 'type': NumberEntry},
                'ipadx': {'name': 'ipadx', 'type': tk.Entry},
                'ipady': {'name': 'ipady', 'type': tk.Entry},
                'width': {'name': 'width', 'type': tk.Entry},
            },
        'Button': {},
        'Radiobutton': {},
        'Checkbutton': {},
        'Canvas': {},
        'Frame': {},
        'Listbox': {},
        'ttk.Combobox': {},
        'ttk.Notebook': {},
        'ttk.Treeview': {},
        'ttk.Menubutton': {},
        'ttk.Progressbar': {}
    }

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


    def create_component_frames(self):

        the_frames = {}
        for component in TkBuilder.ComponentMap:
            if 'name' not in component:
                TkBuilder.ComponentMap[component]['name'] = component
            if 'label_text' not in component:
                name = TkBuilder.ComponentMap[component]['name']
                TkBuilder.ComponentMap[component]['label_text'] = name[0:1].upper() + name[1:].lower()

            the_frames[component] = ComponentFrame(self, TkBuilder.ComponentMap[component])

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
                self.component_map[widget_name] = TkBuilder.component_types[widget_type](self.draw_window, **arguments)
                if self.select_layout_type.get() == 0:
                    self.component_map[widget_name].pack(**self.pack_layout_frame.get_layout_arguments())
                elif self.select_layout_type.get() == 1:
                    self.component_map[widget_name].grid(**self.grid_layout_frame.get_layout_arguments())
                elif self.select_layout_type.get() == 2:
                    self.component_map[widget_name].place(**self.place_layout_frame.get_layout_arguments())

            else:
                print('component with that name already exists')

    def get_widget_arguments(self, widget_name, widget_type):
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

            self.widget_tree.insert('', tk.END, text='Main Window', values=['tk.Toplevel', ''], open=True)


def build_test_rig():
    """
            the format should be:
            self.parameters[name] = {'name': widget_name, 'type': widget_type, 'label_text': prompt, 'variable_type': variable_type,
                    'values': list_of_values, 'variable_value': starting_value}

        {'test_button': {'name': 'Test Button', 'type': tk.Button, 'label_text': 'click me', 'state': tk.DISABLED, 'text': 'Button Title'},
            'test_edit': {'name': 'Test Edit', 'type': tk.Entry, 'label_text': 'edit me', 'variable_type': tk.StringVar} }
    """
    return {'test_button': {'name': 'Test Button', 'type': tk.Button, 'label_text': 'click me', 'state': tk.DISABLED, 'text': 'Button Title'},
            'test_edit': {'name': 'Test Edit', 'type': tk.Entry, 'label_text': 'edit me', 'variable_type': tk.StringVar} }


if __name__ == '__main__':
    main_window = TkBuilder()
    main_window.mainloop()
