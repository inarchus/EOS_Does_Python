import math
import tkinter as tk
from threading import Thread


class FindPrimesWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        scrollbar = tk.Scrollbar(self)
        self.the_primes_box = tk.Listbox(self, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.the_primes_box.pack(fill=tk.BOTH, expand=True)

        self.current = 0
        self.primes = [2, 3, 5]

        self.after(100, self.insert_into_listbox)

        self.terminate = False

        self.the_thread = Thread(target=self.find_primes)
        self.the_thread.start()

        self.wm_protocol('WM_DELETE_WINDOW', self.__del__)

    def insert_into_listbox(self):
        if self.current < len(self.primes):
            new_current = min(len(self.primes), self.current + 10)
            while self.current < new_current:
                self.the_primes_box.insert(tk.END, str(self.primes[self.current]))
                self.current += 1
        if not self.terminate:
            self.after(100, self.insert_into_listbox)

    def find_primes(self):
        n = 7
        while not self.terminate:
            if self.is_prime(n):
                self.primes.append(n)
            n += 1

    def __del__(self):
        self.terminate = True
        self.quit()

    def is_prime(self, n):
        if n == 1:
            return False

        upper_bound = math.ceil(math.sqrt(n))
        for p in self.primes:
            if n % p == 0:
                return False
            if p > upper_bound:
                return True

        return True


if __name__ == '__main__':
    main_window = FindPrimesWindow()
    main_window.title('Listing Primes')
    main_window.geometry('250x800')
    main_window.mainloop()
