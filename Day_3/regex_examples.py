import tkinter as tk
import tkinter.ttk as ttk
import re
import json


class RegexTutorial(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.title('Regex Tutorial')
        self.geometry('1200x500')

        top_frame = tk.Frame(self)

        self.tutorial_pattern = tk.StringVar(self)
        self.tutorial_test = tk.StringVar(self)
        self.prompt_variable = tk.StringVar(self)

        tk.Label(top_frame, textvariable=self.prompt_variable).pack(side=tk.TOP)
        tk.Label(top_frame, text='Enter the test pattern here').pack(side=tk.TOP)
        ttk.Entry(top_frame, width=50, textvariable=self.tutorial_pattern).pack(side=tk.TOP)

        # tk.Label(top_frame, text='Enter the test string here').pack(side=tk.TOP)
        # tk.Entry(top_frame, width=50, textvariable=self.tutorial_test).pack(side=tk.TOP)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        middle_frame = tk.Frame(self)
        # self.test_button = tk.Button(middle_frame, text='Test Matching')
        # self.test_button.pack(side=tk.LEFT, padx=5, pady=5)
        # self.submit_button = tk.Button(middle_frame, text='Submit')
        # self.submit_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.next_button = tk.Button(middle_frame, text='Next', command=self.step)
        self.next_button.pack(side=tk.LEFT, padx=5, pady=5)
        middle_frame.pack(side=tk.TOP, anchor= tk.S)

        self.bottom_frame = tk.Frame(self)
        self.treeview = ttk.Treeview(self.bottom_frame, columns=['Expected', 'Your Result'])
        self.treeview.heading('#0', text='Test Case')
        self.treeview.heading('Expected', text='Expected')
        self.treeview.heading('Your Result', text='Your Result')
        self.treeview.tag_configure('correct', background='green')
        self.treeview.tag_configure('wrong', background='tomato2')
        self.treeview.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.bottom_frame.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.step = 0
        self.sub_step = 0

        try:
            with open('regex_tests.json', 'r') as self.test_cases:
                json_block = ''.join(self.test_cases.readlines())
                self.tests = self.import_tests(json.loads(json_block))
        except IOError as err:
            print(err)

    def import_tests(self, json_block):
        tests = []
        if json_block:
            for test_name in sorted(json_block):
                print(test_name, json_block[test_name])
                tests.append(json_block[test_name])
        return tests

    def step(self):
        if self.step < len(self.tests):
            if self.sub_step == 0:
                print('step 1')
                self.sub_step += 1
                self.prompt_variable.set(self.tests[self.step]['prompt'])
            elif self.sub_step == 1:
                print('step 2')
                if self.test():
                    self.sub_step += 1
            else:
                self.prompt_variable.set(self.tests[self.step]['completion'])
                self.step += 1
                self.sub_step = 0

    def test(self):
        self.treeview.delete(*self.treeview.get_children())
        passed = True
        for test_case in self.tests[self.step]['tests']:
            user_input_match = True if re.match(self.tutorial_pattern.get(), test_case) else False
            tutorial_match = True if re.match(self.tests[self.step]['pattern'], test_case) else False
            if (user_input_match and tutorial_match) or (not tutorial_match and not user_input_match):
                self.treeview.insert('', tk.END, text=test_case, values=[tutorial_match, user_input_match], tags=('correct',))
            else:
                self.treeview.insert('', tk.END, text=test_case, values=[tutorial_match, user_input_match], tags=('wrong',))
                passed = False
        return passed


class RegexExamples(tk.Tk):

    pattern_values = [r'\d{3}[.,\-/ ]\d{3}[.,\-/ ]\d{4}',   # phone numbers
                      r'[a-z]*',                            # lowercase strings without space
                      r'[A-Z]*',                            # uppercase strings
                      r'[a-zA-Z0-9]*',                      # all alphanumerics
                      r'[a-zA-Z ]*'                         # letters with space
                      r'\w+'
                      ]

    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Regex Examples')

        self.test = tk.StringVar(self)
        self.pattern = tk.StringVar(self)

        main_menu = tk.Menu()
        file_menu = tk.Menu(tearoff=0)

        file_menu.add_command(label='Begin Tutorial', command=lambda: RegexTutorial(self))
        file_menu.add_command(label='Exit', command=self.destroy)
        main_menu.add_cascade(menu=file_menu, label='File')

        self.config(menu=main_menu)

        tk.Label(self, text='Enter the test string here').pack(side=tk.TOP)
        tk.Entry(self, width=50, textvariable=self.test).pack(side=tk.TOP)
        tk.Label(self, text='Enter the test pattern here').pack(side=tk.TOP)
        ttk.Combobox(self, width=50, textvariable=self.pattern, values=self.pattern_values).pack(side=tk.TOP)
        tk.Button(self, text='Match from Beginning of String', command=self.match).pack(side=tk.TOP)
        tk.Button(self, text='Search for Match Anywhere', command=self.search).pack(side=tk.TOP)
        tk.Button(self, text='Find All Matches', command=self.findall).pack(side=tk.TOP)
        self.result_box = tk.Text(self)
        self.result_box.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def match(self):
        self.result_box.delete(1.0, tk.END)
        p = self.pattern.get()
        s = self.test.get()
        try:
            m = re.match(p, s)
            if m:
                result_string = s + ' contains a match to pattern ' + p + '\n' + m.group(0)
                self.result_box.insert(tk.END, result_string)
            else:
                self.result_box.insert(tk.END, 'No Match Found')
        except re.error as err:
            print(err)

    def search(self):
        self.result_box.delete(1.0, tk.END)
        p = self.pattern.get()
        s = self.test.get()
        try:
            m = re.search(p, s)
            if m:
                print(type(m.groups()), m.groups())
                result_string = s + ' contains a match to pattern ' + p + '\n' + m.group(0)
                self.result_box.insert(tk.END, result_string)
            else:
                self.result_box.insert(tk.END, 'No Match Found')
        except re.error as err:
            print(err)

    def findall(self):
        self.result_box.delete(1.0, tk.END)
        p = self.pattern.get()
        s = self.test.get()
        m = re.findall(p, s)
        if m:
            for g in m:
                if g.strip():
                    self.result_box.insert(tk.END, str(g) + '\n')
        else:
            self.result_box.insert(tk.END, 'No Match Found\n')


if __name__ == '__main__':
    # m = re.findall(r'(?P<area_code>\d{3})\-(?P<phone_number>\d{3}\-\d{4})', '111-222-3344, 142-123-1414, 12-12-12, 14, 16, 467-443-1222')

    RegexExamples().mainloop()
