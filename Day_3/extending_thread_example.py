import tkinter as tk
import tkinter.ttk as ttk
import urllib.request
import time
from threading import Thread


class WebThread(Thread):
    def __init__(self, url, retries):
        super().__init__()
        # super().__init__(daemon=True)
        self.url = url
        self.retries = retries
        self.data = ''
        self.error_message = ''

    def run(self):

        while self.retries and not self.data:
            try:
                url_object = urllib.request.urlopen(self.url)
                html = url_object.read()
                self.data = html
            except urllib.request.URLError as err:
                self.error_message = str(err)
            except ValueError as err:
                self.error_message = str(err)
            time.sleep(1)
            self.retries -= 1

        print('Thread Terminating', self.url)


class MainWindow(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry('800x800')

        top_frame = tk.Frame(self)
        bottom_frame = tk.Frame(self)

        self.current_url = tk.StringVar(self)
        self.notepad = {}
        self.threads = {}

        tk.Label(top_frame, text='Enter a URL').pack(side=tk.TOP, fill=tk.X)
        the_entry = tk.Entry(top_frame, textvariable=self.current_url, width=116)
        the_entry.pack(side=tk.LEFT)
        the_entry.bind('<Return>', self.load_url_to_tab)
        tk.Button(top_frame, text='Go', width=10, command=self.load_url_to_tab).pack(side=tk.RIGHT)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self.the_notebook = ttk.Notebook(bottom_frame)
        self.the_notebook.pack(fill=tk.BOTH, expand=True)
        self.the_notebook.bind('<Control-Key-c>', self.close_current_tab)

        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def close_current_tab(self, event=None):
        selection = self.the_notebook.select()
        if selection:
            the_index = self.the_notebook.index(selection)
            self.the_notebook.forget(the_index)

    def load_url_to_tab(self, event=None):
        the_url = self.current_url.get()
        new_frame = tk.Frame(self.the_notebook)

        scrollbar = tk.Scrollbar(new_frame)
        new_textbox = tk.Text(new_frame, yscrollcommand=scrollbar.set)
        new_textbox.bind('<Control-Key-c>', self.close_current_tab)
        scrollbar.config(command=new_textbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        new_textbox.insert(tk.END, 'Waiting for Response...')
        # pack this first, expand will cause weirdness
        new_textbox.pack(fill=tk.BOTH, expand=True)

        self.the_notebook.add(new_frame, text=the_url)

        self.notepad[the_url] = new_textbox
        self.threads[the_url] = WebThread(the_url, retries=10)
        self.threads[the_url].start()
        self.after(100, lambda *args: self.check_for_results(the_url))

    def check_for_results(self, the_url):
        if self.threads[the_url].data:
            self.notepad[the_url].delete(1.0, tk.END)
            self.notepad[the_url].insert(tk.END, self.threads[the_url].data)
        elif self.threads[the_url].error_message:
            self.notepad[the_url].delete(1.0, tk.END)
            self.notepad[the_url].insert(tk.END, self.threads[the_url].error_message)
            if self.threads[the_url].is_alive():
                self.after(100, lambda *args: self.check_for_results(the_url))
        elif self.threads[the_url].is_alive():
            self.after(100, lambda *args: self.check_for_results(the_url))


if __name__ == '__main__':
    mw = MainWindow('Random Web Reading Stuff')
    mw.mainloop()
