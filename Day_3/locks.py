import time
import random
from threading import Thread, Lock, Semaphore
import tkinter as tk
import tkinter.ttk as ttk


class NumberEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        self.variable = None
        if 'variable' in kwargs:
            self.variable = kwargs.pop('variable', None)

        super().__init__(*args, **kwargs)
        if self.variable:
            self['text'] = str(self.variable.get())

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


class CountClass:
    def __init__(self):
        self.x = 0
        self.lock = Lock()


class Incrementer(Thread):
    def __init__(self, n, cc):
        super().__init__()
        self.cc = cc
        self.n = n

    def run(self):
        x = self.cc.x
        # print(' '.join(['Thread', str(self.n), 'incrementing x =', str(x)]))
        x += 1
        time.sleep(random.uniform(0, 1) * .001)
        self.cc.x = x
        # print(' '.join(['Thread', str(self.n), 'setting x =', str(x)]))


class Incrementer(Thread):
    def __init__(self, n, cc, locking=False):
        super().__init__()
        self.cc = cc
        self.n = n
        self.locking = locking

    def run(self):
        print(' '.join(['Thread', str(self.n), 'acquiring']))
        self.cc.lock.acquire()
        x = self.cc.x
        x += 1
        time.sleep(random.uniform(0, 1) * .001)
        self.cc.x = x
        print(' '.join(['Thread', str(self.n), 'releasing']))
        self.cc.lock.release()

        # print(' '.join(['Thread', str(self.n), 'incrementing x =', str(x)]))
        # print(' '.join(['Thread', str(self.n), 'setting x =', str(x)]))


class DeadLocker(Thread):
    def __init__(self, n, lock_A, lock_B, t):
        super().__init__()
        self.n = n
        self.lock_A = lock_A
        self.lock_B = lock_B
        self.t = t

    def run(self):
        time.sleep(random.uniform(0, 1) * self.t)
        self.lock_A.acquire()
        print(self.n, 'I have acquired the first lock.  ')
        time.sleep(random.uniform(0, 1) * self.t)
        self.lock_B.acquire()
        print(self.n, 'I have acquired both locks')
        time.sleep(random.uniform(0, 1) * self.t)
        self.lock_B.release()
        self.lock_A.release()

def lock_example():
    i = int(input('What is the number of threads? '))
    for _ in range(5):
        threads = []
        cc = CountClass()

        for j in range(i):
            threads.append(Incrementer(j, cc))
            threads[j].start()

        time.sleep(.01)
        print(cc.x)


def deadlock_example():
    lock1 = Lock()
    lock2 = Lock()
    DeadLocker(1, lock1, lock2, .01).start()
    DeadLocker(2, lock2, lock1, .01).start()


class ResourceHog(Thread):
    def __init__(self, name, semaphore, minimum=10, maximum=100):
        super().__init__(daemon=True)
        self.name = name
        self.semaphore = semaphore
        self.minimum = minimum
        self.maximum = maximum
        self.tick = -1

    def run(self):
        self.semaphore.acquire()
        self.tick = random.randint(self.minimum, self.maximum)
        while self.tick > 0:
            time.sleep(1)
            self.tick -= 1
        self.semaphore.release()
        self.tick = 'Completed'


class SemaphoreExample(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x500')
        self.title('Semaphore Example')

        self.thread_count = tk.IntVar(self, value=5)
        self.concurrent_count = tk.IntVar(self, value=3)
        self.min_time = tk.IntVar(self, value=10)
        self.max_time = tk.IntVar(self, value=100)

        left_frame = tk.Frame(self)

        tk.Label(left_frame, text='How many threads should we create?').pack(side=tk.TOP)
        NumberEntry(left_frame, variable=self.thread_count).pack(side=tk.TOP)
        tk.Label(left_frame, text='How many threads should be concurrent?').pack(side=tk.TOP)
        NumberEntry(left_frame, variable=self.concurrent_count).pack(side=tk.TOP)
        tk.Label(left_frame, text='What is the minimum time for a Thread?').pack(side=tk.TOP)
        NumberEntry(left_frame, variable=self.min_time).pack(side=tk.TOP)
        tk.Label(left_frame, text='What is the maximum time for a Thread').pack(side=tk.TOP)
        NumberEntry(left_frame, variable=self.max_time).pack(side=tk.TOP)
        self.go_button = tk.Button(left_frame, text='Go', command=self.start_process)
        self.go_button.pack(side=tk.TOP)

        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.main_treeview = ttk.Treeview(self, columns=('Value',))
        scrolly = tk.Scrollbar(self, command=self.main_treeview.yview)
        self.main_treeview['yscrollcommand'] = scrolly.set
        self.main_treeview.heading('#0', text='Thread Name')
        self.main_treeview.heading('Value', text='Current Value')
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        self.main_treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.main_treeview.tag_configure('waiting', background='gold')
        self.main_treeview.tag_configure('active', background='springgreen2')
        self.main_treeview.tag_configure('complete', background='cyan')

        self.thread_vars = {}

    def start_process(self):
        self.go_button['state'] = tk.DISABLED
        self.main_treeview.delete(*self.main_treeview.get_children())
        self.thread_vars = {}
        sem = Semaphore(self.concurrent_count.get())
        for i in range(self.thread_count.get()):
            thread = ResourceHog(i + 1, sem, self.min_time.get(), self.max_time.get())
            item = self.main_treeview.insert('', tk.END, text='Thread ' + str(i + 1), values=('Started', ), tags=('waiting', ))
            thread.start()
            self.thread_vars[item] = thread

        self.after(100, self.update_treeview)

    def update_treeview(self):
        for t_name in self.thread_vars:
            if self.thread_vars[t_name].tick != -1 and self.thread_vars[t_name].tick != 'Completed':
                self.main_treeview.item(t_name, values=(self.thread_vars[t_name].tick, ), tags=('active', ))
            elif self.thread_vars[t_name].tick != -1:
                self.main_treeview.item(t_name, values=(self.thread_vars[t_name].tick,), tags=('complete',))

        if not any(self.thread_vars[t].is_alive() for t in self.thread_vars):
            self.go_button['state'] = tk.ACTIVE

        self.after(250, self.update_treeview)


# deadlock_example()
if __name__ == '__main__':
    SemaphoreExample().mainloop()
